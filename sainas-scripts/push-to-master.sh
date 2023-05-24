
#!/bin/bash

filename=$(git status -s | grep "^A " )

if [[ $(grep -c "^A " <<< $filename) -ne 1 ]]; then
    echo "More than one file added"
    exit 1
fi

if [[ $(grep -c "sainas.md" <<< $filename) -ne 1 ]]; then
    echo "Wrong file added"
    exit 1
fi

echo "Will push $filename to main"
gcmsg "Create sainas.md"
git checkout main && git push
echo "Pushed to main"
git checkout sainas-scripts


