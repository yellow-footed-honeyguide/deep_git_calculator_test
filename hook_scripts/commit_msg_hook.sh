#!/bin/sh
# Commit-msg hook - enforces commit message format
# Place this file in .git/hooks/commit-msg
# Make it executable: chmod +x .git/hooks/commit-msg

# Read commit message
commit_regex='^(feat|fix|docs|style|refactor|test|chore): .{10,}'
commit_msg=$(cat $1)

echo "📝 Checking commit message format..."

# Check if message matches pattern
if ! echo "$commit_msg" | grep -qE "$commit_regex"; then
    echo "❌ Bad commit message!"
    echo "Format: <type>: <description>"
    echo "Types: feat, fix, docs, style, refactor, test, chore"
    echo "Description: at least 10 characters"
    echo ""
    echo "Example: feat: add division operation to calculator"
    exit 1
fi

echo "✅ Commit message looks good!"
exit 0
