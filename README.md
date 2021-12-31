<div>
    <p align="center">
    <img src="https://i.imgur.com/BMMIgXm.png"
    width=700 />
</div>

---


New-World-Auto-Fishing is a fully automatic program to fish in New World, using image recognition and mouse/keyboard inputs.

This program is strictly developed for *educational purposes and own research*; it violates [New World ToU / Code of Conduct](https://www.newworld.com/en-us/legal) and **you shouldn't use it on AGS New World live servers**.

<div>
  <kbd>
    <img src="https://i.imgur.com/XIP2Fgg.png"
    width=800/>
  </kbd>
</div>

## Features
- Bait setter
- Reconnection *(BETA)*
- Custom cast distance
- Anti AFK disconnection
- Skip the "uncommon fish" animation
- Repair at custom number of casts
- Hotkeys to pause/resume
- Reject group invites
- Treasure Chests counter
- Reel the most effective way possible

## Prerequisites
You'll need [Python3](https://www.python.org/downloads/) to run.  
You'll need [pyAutoGUI](https://pypi.org/project/PyAutoGUI/), [pyDirectInput](https://pypi.org/project/PyDirectInput/) and [pyGetWindow](https://pypi.org/project/PyGetWindow/) Python libraries.

The images have been taken on 1920*1080, so you should use the same resolution to avoid any errors.

## How does it work?

### 🟢 Getting Started
Get your fishing rod, baits and enough repair parts and head to your favorite fishing spot.  
Set up your settings in config.py and run the program.

Launching the program ***double clicking "console.py" is highly recommended***, as it displays useful information like timestamp, loops made so far, successfully completion or error of steps etc.
The console will stay always on top of everything else.

**The following points have to be considered in order to understand how all the features work.**

### 🟡 Reeling
As the program uses image recognition, keep the images on screen clear to be detected correctly and not trigger any errors.

<div>
  <p align="center">
  <kbd>
    <img src="https://i.imgur.com/NFh8Jtm.png"
    width=500>
  </kbd>
</div>

### 🟡 Bait
Equips a bait everytime it expires, and *always equips the first one on the baits menu*.  
It stops automatically when you run out of baits.

### 🟡 Anti-AFK
Will move left and right, back to original position, so beware not to be standing on a little spot from which you can fall.

### 🟡 Reconnection (BETA)
The reconnection will be checked at the start of the loop, if it's true, the program will recognize in which step it is and then begin to reconnect.

In order to get a succesful reconnection, the program looks for the backpack icon on screen  
<kbd>
  <img src="https://i.imgur.com/H2BftgY.png"
  width=55>
</kbd>

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


HOME    -> Resume
END     -> Pause
~~~


[<img alt='DonateButton' width='250px' src='https://i.imgur.com/8sr6feS.png'/>](https://www.paypal.com/donate/?hosted_button_id=6HDWEU7U7ZYNN)