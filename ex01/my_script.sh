#!/bin/sh
pip -v
mkdir local_lib
cd local_lib
if [ -d path.py ]
then
  rm -rf path.py
fi
git clone https://github.com/jaraco/path.py.git &>logs.log
cd ../
cp ./local_lib/path.py/path.py ./
python3 ./my_program.py
