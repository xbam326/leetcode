#!/bin/bash

# Usage: ./organize_problem.sh <problem_number>
# Example: ./organize_problem.sh 141

if [ -z "$1" ]; then
    echo "Usage: $0 <problem_number>"
    echo "Example: $0 141"
    exit 1
fi

PROBLEM_NUM=$1

# 元のファイルを探す（problems/ディレクトリ内）
ORIGINAL_FILE=$(find problems -maxdepth 1 -type f -name "${PROBLEM_NUM}-*" -o -name "${PROBLEM_NUM}.*" | grep -v ".md" | head -n 1)

if [ -z "$ORIGINAL_FILE" ]; then
    echo "Error: No file found for problem ${PROBLEM_NUM}"
    echo "Looking for: problems/${PROBLEM_NUM}-* or problems/${PROBLEM_NUM}.*"
    exit 1
fi

# ファイル名から拡張子を取得
EXT="${ORIGINAL_FILE##*.}"

# ファイル名（拡張子なし）を取得してディレクトリ名とする
BASENAME=$(basename "$ORIGINAL_FILE")
PROBLEM_NAME="${BASENAME%.*}"

# ディレクトリを作成
PROBLEM_DIR="problems/${PROBLEM_NAME}"
mkdir -p "$PROBLEM_DIR"

# step1, step2, step3にコピー
cp "$ORIGINAL_FILE" "$PROBLEM_DIR/step1.$EXT"
cp "$ORIGINAL_FILE" "$PROBLEM_DIR/step2.$EXT"
cp "$ORIGINAL_FILE" "$PROBLEM_DIR/step3.$EXT"

# 空のmemo.mdを作成
touch "$PROBLEM_DIR/memo.md"

# 元のファイルを削除（オプション）
rm "$ORIGINAL_FILE"

echo "✓ Created directory structure for problem ${PROBLEM_NUM}:"
echo "  $PROBLEM_DIR/"
echo "    ├── step1.$EXT"
echo "    ├── step2.$EXT"
echo "    ├── step3.$EXT"
echo "    └── memo.md"
echo ""
echo "Original file: $ORIGINAL_FILE"
echo "Note: Original file is kept. Uncomment the 'rm' line in the script to auto-delete."
