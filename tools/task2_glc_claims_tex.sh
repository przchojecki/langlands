#!/usr/bin/env bash
set -euo pipefail

# Convenience wrapper to run TeX claim extraction assuming the five TeX files
# are in the repository root as:
#   gaits1.tex ... gaits5.tex
#
# Usage:
#   bash tools/task2_glc_claims_tex.sh
# or:
#   bash tools/task2_glc_claims_tex.sh /path/to/tex/dir

TEX_DIR="${1:-.}"
OUT_DIR="atlas/glc/claims"

python3 tools/extract_glc_claims_tex.py \
  --glc1 "${TEX_DIR}/gaits1.tex" \
  --glc2 "${TEX_DIR}/gaits2.tex" \
  --glc3 "${TEX_DIR}/gaits3.tex" \
  --glc4 "${TEX_DIR}/gaits4.tex" \
  --glc5 "${TEX_DIR}/gaits5.tex" \
  --out "${OUT_DIR}"
