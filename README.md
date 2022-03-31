# ParadoxFileComparer

## What is this?

A Tool to find probably conflicting Game Files from Paradox' Crusader Kings 3 and open them in VS Code.  
Despite the name, it doesn't actually compare any files for you.

### Features

* Allows you to find all Files of a specified type (e.g. window_character.gui or descriptor.mod) inside the Steam Workshop Folder
* Opens those Files in VS Code for you to compare them and find Conflicts

### How it Works

The Program will ask the User, which File They want to find, and then crawl through the Mods Folder with a simple .bat Program.

Every time a file matches, its path is attached to the back of a string. When no more matches are found,
the String is returned back to the main program.  

Then, it uses Regular Expressions to find out wether or not the found file is inside a mod that is currently active. it uses the dlc_load.json file for this.  
If it isnt, the part of the string containing the path in question is discarded.  

Finally, the String containing the filtered Paths is passed to VS Code to open.  

You can find the source code in `openfiles.py` and `findvalidfiles.bat`

### Currently Supported Games

* Crusader Kings 3

## How to use

First, ParadoxFileComparer will ask you wether or not it should open a new VS Code Instance or 'recycle' the one last used, where the files will just open right behind your last used files.  
Then it will ask you for the name of the file you are searching. Please enter the file name together with the extension here.  
Now wait until the Program redirects you to VS Code, where your desired files are opened!

ParadoxFileComparer currently only opens all Files in your current CK3 Launcher Playset, so I recommend that you create a new Playset with all installed Workshop Mods inside.  
to change the current Playset, just change the Playset in the Launcher and press the Play Button. It doesn't matter wether or not the Game crashes,but from my observations, the dlc_load.json,  
where your "current Playset" is stored, only gets updated when you press said Start Button.

## Installation Guide

   1. Navigate to your CK3 Steam Workshop folder.  
   You can usually find it inside your Steam Library Folder "SteamLibrary",  
   which is usually located in the root folder of your Hard Drive, C:\ for example.  
   The Path of CK3s Workshop Folder usually looks like this:
   `.\SteamLibrary\steamapps\workshop\content\1158310\`  
   where `\1158310\` is the Steam ID of CK3.  
   You can check the ID of different Games on sites like
   Steamdb.info. (i wont link there, dont want to be held responsible for any icky stuff that may happen)

   2. Create a new Folder inside the Workshop Folder, you can call it "Script", "ParadoxFileFinder" or "ULMISALMIGHTY!!!", for example

   3. Copy `openfiles.exe` as well as `findvalidfiles.bat` to the newly created folder:  
   [Image goes Here]

   4. Done!

## Future Plans

### Short Term Goals

* integrate the `findvalidfiles.bat` into the main program
  * use paths in mod descriptor files as reference
* specify multiple files at once to open
* allow User to switch between "only open mods in current Profile" and "Open every Valid file"

### Mid Term Goals

* find a way to speed the program up, its currently too slow for my taste
* add support for local mods
* move everything out of the Steam Workshop Folder into another location
* create a command line quick access method, ie `openfiles /n window_character.gui`

### Long Term Goals

none, for now

### Late Long Term Goals

* add Support for more Paradox Games in the following Priority:
  1. Stellaris
  2. Victoria 3
  3. Hearts of Iron 4
  4. Europa Universalis 4
* localize the Program into different Languages

### What i dont plan to do

* Automate the Conflict Finding Process. Its just waay too much out of scope for a little, i dont plan to create PDXEdit (yet)

### Changelog

30/03/2022: Version 1: Release

---

#### Disclaimer

 i am neither associated with, nor own any of the Following:

* Paradox Interactive or its associates
* Europa Universalis 4
* Stellaris
* Victoria 3
* Hearts of Iron 4
* Crusader Kings 3
