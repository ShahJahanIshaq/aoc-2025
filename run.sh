#!/usr/bin/env bash

set -euo pipefail

usage() {
  cat <<EOF
Usage:
  $0 [python|cpp] <day> <part>

If <language> is omitted, python is assumed.
EOF
  exit 1
}

lang=python
if   [[ $# -eq 3 ]]; then
  lang=$1; shift
elif [[ $# -ne 2 ]]; then
  usage
fi

day=$1
part=$2

day_dir="day${day}"
input="${day_dir}/input.txt"
output="${day_dir}/output.txt"


case "$lang" in
  python)
    source venv/bin/activate
    python "${day_dir}/part${part}.py"  < "$input" > "$output"
    ;;
  cpp)
    src="${day_dir}/main.cpp"
    bin="${day_dir}/main"
    g++-14 -std=c++20 -pedantic-errors -Wall -Werror "$src" -o "$bin"
    "$bin" < "$input" > "$output"
    ;;
  *)
    echo "[!] Unknown language: $lang"
    usage
    ;;
esac