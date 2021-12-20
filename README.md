<div>
    <p align="center">
    <img src="https://i.imgur.com/BMMIgXm.png"
    width=700 />
    </p>
</div>

---


New-World-Auto-Fishing is a fully automatic program to fish in New World, using image recognition and mouse/keyboard inputs.

This program is strictly developed for *educational purposes and own research*; it violates [New World ToU / Code of Conduct](https://www.newworld.com/en-us/legal) and **you shouldn't use it on AGS New World live servers**.

<div>
  <kbd>
    <img src="https://i.imgur.com/hKSGdZr.png"
    width=800/>
  </kbd>
</div>

## Features
- Bait setter
- Reconnection
- Custom cast distance
- Anti AFK disconnection
- Skip the "uncommon fish" animation
- Repair at custom number of casts
- Reject group invites
- Treasure Chests counter
- Reel the most effective way possible

## Prerequisites
You'll need [Python3](https://www.python.org/downloads/) to run.  
You'll need [pyAutoGUI](https://pypi.org/project/PyAutoGUI/), [pyDirectInput](https://pypi.org/project/PyDirectInput/) and [pyGetWindow](https://pypi.org/project/PyGetWindow/) Python libraries.

The images have been taken on 1920*1080, so you should use the same resolution to avoid any errors.

## How does it work?

### 🚀 Get Started
Get your fishing rod, baits and enough repair parts and head to your favorite fishing spot.  
Set up your settings in config.py and run the program!

### 🔴 Console LOG
Launching the program executing "console.py" is highly recommended, as it displays useful information like timestamp, how many loops made so far, casts until next repair and successfully completion or error of steps.
The console will stay always on top of everything else.

### 🔴 Anti-AFK
Will move left and right, back to original position, so beware not to be standing on a little spot from which you can fall.

### 🔴 Bait Usage
Equips a bait everytime it expires, and always equips the first one on the baits menu.  
It stops automatically whenever you run out of baits.

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