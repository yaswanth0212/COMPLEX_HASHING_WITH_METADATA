@echo off
echo "Please Add the path of this directory in Windows "PATH" system variable"
echo --------------------------
echo --------------------------
python -m pip install --upgrade pip
pip install Pillow
set /p input= "Enter Your File Path To Calculate the New_Hash :"
"exiftool(-k).exe" %input% > %input%.txt
python MD5IMAGE.py %input%
python MD.py %input%.txt
python MD5MDATA.py %input%.txt
start notepad CH
pause