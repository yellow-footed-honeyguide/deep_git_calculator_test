#!/bin/sh
# Pre-commit hook - checks Python syntax before commit
# Place this file in .git/hooks/pre-commit
# Make it executable: chmod +x .git/hooks/pre-commit

echo "🔍 Running pre-commit hook..."

# Check all Python files for syntax errors
for file in $(git diff --cached --name-only | grep '\.py$'); do
    echo "Checking $file..."
    python -m py_compile "$file"
    if [ $? -ne 0 ]; then
        echo "Syntax error in $file!"
        echo "Fix it before committing!"
        exit 1
    fi
done

echo "All Python files passed syntax check!"
exit 0
