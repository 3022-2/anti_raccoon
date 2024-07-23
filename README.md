# anti raccoon clipper
A script written in python to detect if the malware [raccoon clipper](https://github.com/3022-2/raccoon_clipper) (written by me) is installed on your computer
---
# what is raccoon clipper?
raccoon clipper is crypto clipping malware designed to steal crypto currency of a target by replaceing the crypto address they intend to send crypto to with the attackers address
---
![image](https://github.com/user-attachments/assets/457966e9-9a69-4dc4-bc21-f3c1d187b619)

# install
```console
git clone https://github.com/3022-2/anti_raccoon.git

cd anti_raccoon

pip install -r requirements.txt

python anti_clipper.py
```
future features:
- more in depth checking (files within the CLPPTH and Storage0 to verify 100% they come from [raccoon clipper](https://github.com/3022-2/raccoon_clipper))

warning:  
notification can stack but these will clear. to avoid this you can kill the code by killing the python process/s within task manager then restart the installed file in roaming folder
