<div>
    <p align="center">
    <img src="https://i.imgur.com/BMMIgXm.png"
    width=700 />
    </p>
</div>

---


New-World-Auto-Fishing is a fully automatic program to fish in New World, using image recognition and mouse/keyboard inputs.

This program is strictly developed for *educational purposes and own research*; it violates [NW GTU / Code of Conduct](https://www.newworld.com/en-us/legal) and **you shouldn't use it on AGS New World live servers**.

<div>
  <kbd>
    <img src="https://i.imgur.com/hKSGdZr.png"
    width=800/>
  </kbd>
</div>

## Features
- Anti AFK disconnection
- Cast to custom distance
- Equip a bait when it's expired
- Skip the "uncommon fish" animation
- Repair at custom number of casts
- Reject group invites
- Reel the most effective way possible

## Prerequisites
You'll need [Python3](https://www.python.org/downloads/) to run.  
You'll need [pyAutoGUI](https://pypi.org/project/PyAutoGUI/), [pyDirectInput](https://pypi.org/project/PyDirectInput/) and [pyGetWindow](https://pypi.org/project/PyGetWindow/) Python libraries.

The images have been taken on 1920*1080, so you should use the same resolution to avoid any errors.

## How does it work?

### 🔴 Get Started
Simply reach at your favorite fishing spot, with a fishing rod equipped, enough repair parts and run the program.

### 🔴 Console LOG
Launching the program executing "console.bat" is highly recommended, as it displays useful information like timestamp, how many loops made so far, casts until next repair and successfully completion or error of steps.

If you want the console to be on top, use [AutoHotkey](https://www.autohotkey.com/) or any of [these](https://www.howtogeek.com/196958/the-3-best-ways-to-make-a-window-always-on-top-on-windows/) methods. 

### 🔴 Anti-AFK
Will move left and right, back to original position, so beware not to be standing on a little spot from which you can fall.

### 🔴 Bait Function
Equips a bait everytime it expires, and always equips the first bait on the baits menu.  
It stops automatically whenever you don't have baits left.

### 🔴 Key Bindings
The key bindings in-game are set to default, you can change them at "config.py" file.  
~~~
E       -> Interact  
A       -> Move left
D       -> Move right
R       -> Repair AND Equip Bait
TAB     -> Inventory  
leftALT -> Free look (lock the POV)
F2      -> Reject group invite  (cannot be modified) 
F3      -> Switch to "fishing stance" (cannot be modified) 
~~~