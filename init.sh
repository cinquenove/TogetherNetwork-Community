#!/bin/bash
echo -n "This will destroy your work and restore the repository."
echo -n "Would you like to continue? [Y/n]"; read answer;
if [[ $answer == "N" || $answer == "n" ]]; then
        exit 0;
fi

echo ""
echo "If not installed, you should install those"
echo "dependencies manually first (use brew or apt-get):"
echo " - libjpeg"
echo " - optipng"
echo -n "Are those libraries available? [Y/n] "; read answer;
if [[ $answer == "N" || $answer == "n" ]]; then
        echo "Plz, install them!"
        exit 0;
fi

echo ""
echo "Running the installation..."
echo -n "- Cleaning & updating the local copy: "
git fetch --all &> /dev/null
git reset --hard origin/master  &> /dev/null
git pull &> /dev/null
echo "done"

echo -n "- Creating a virtual environment: "
virtualenv venv -v &> /dev/null
echo "done"

echo -n "- Installing dependencies inside the virtual environment: "
source venv/bin/activate
pip install -q -U -r togethernetwork/requirements.txt &> /dev/null
echo "done"
echo ""
echo "Installation done"
