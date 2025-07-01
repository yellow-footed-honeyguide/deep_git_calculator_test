#!/bin/sh
# Pre-push hook - runs tests before pushing
# Place this file in .git/hooks/pre-push
# Make it executable: chmod +x .git/hooks/pre-push

echo "🚀 Running pre-push hook..."

# Run Python tests
echo "Running calculator tests..."
python -m pytest test_calculator.py -v

if [ $? -ne 0 ]; then
    echo "❌ Tests failed!"
    echo "Fix the tests before pushing!"
    exit 1
fi

echo "✅ All tests passed! Pushing..."
exit 0
