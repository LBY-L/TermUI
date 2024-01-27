#!/bin/bash

function Files {
echo "**/Test/windows.py**" >> README.md 
echo "\`\`\`python" >> README.md
cat Tests/windows.py >> README.md
echo "\`\`\`" >> README.md

echo "---" >> README.md
echo "**/Test/keysmove.py**" >> README.md 
echo "\`\`\`python" >> README.md
cat Tests/keysmove.py >> README.md
echo "\`\`\`" >> README.md
}

function run {
pip3 install .
rm -r build/ TermUI.egg-info/
python3 Tests/keysmove.py
python3 Tests/windows.py
}

echo "Want to put the files in README.md (y/n) "

read option 
if [[ $option == "y" ]]; then
	Files
	run
elif [[ $option == "n" ]]; then
	run
fi

echo "Test compeleted!"
