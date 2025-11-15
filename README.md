```
    _____                      __        _______                         __                         
   |     \                    |  \      |       \                       |  \                        
    \$$$$$ __    __  _______  | $$   __ | $$$$$$$\ __    __   _______  _| $$_     ______    ______  
      | $$|  \  |  \|       \ | $$  /  \| $$__/ $$|  \  |  \ /       \|   $$ \   /      \  /      \ 
 __   | $$| $$  | $$| $$$$$$$\| $$_/  $$| $$    $$| $$  | $$|  $$$$$$$ \$$$$$$  |  $$$$$$\|  $$$$$$\
|  \  | $$| $$  | $$| $$  | $$| $$   $$ | $$$$$$$\| $$  | $$ \$$    \   | $$ __ | $$    $$| $$   \$$
| $$__| $$| $$__/ $$| $$  | $$| $$$$$$\ | $$__/ $$| $$__/ $$ _\$$$$$$\  | $$|  \| $$$$$$$$| $$      
 \$$    $$ \$$    $$| $$  | $$| $$  \$$\| $$    $$ \$$    $$|       $$   \$$  $$ \$$     \| $$      
  \$$$$$$   \$$$$$$  \$$   \$$ \$$   \$$ \$$$$$$$   \$$$$$$  \$$$$$$$     \$$$$   \$$$$$$$ \$$
                                                                                         
                  J U N K B U S T E R                         
```
# JunkBuster – Windows Temp Cleaner

JunkBuster is a small personal project I created to automate the cleanup of Windows temporary files and save some time during my daily use.  
Since it might be useful to others, I decided to share it here on GitHub.

The script shows the size of each folder before cleaning, asks for confirmation, and reports how much space was freed.

## Features
- Shows the size of all target folders on launch  
- Cleans only **safe** Windows folders  
- Deletes only the content inside the folders  
- Displays size before and after cleaning  
- Shows the total amount of space removed  
- Ignores locked files to avoid interruptions  

## Safe Folders Cleaned
- `%TEMP%` (User Temp)  
- `C:\Windows\Temp`  
- `C:\Windows\Logs\CBS`  
- `C:\Windows\Minidump`  

## Requirements
- Python 3.x  
- Windows OS

## How to Use
1. Download or clone the repository  
2. Run the script:

```bash
python main.py
```
3. Check folder sizes

4. Choose what you want to clean

Done!

## Windows Executable

A standalone Windows `.exe` version of JunkBuster is now included in the project.  
You can find it`(main.exe)` inside the `/dist` folder.  
This allows you to use the tool without having Python installed.

License
MIT License

yaml
Copy code

---
