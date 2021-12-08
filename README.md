# Description

New-World-Auto-Fishing is a fully automatic program to fish in New World, using mouse and keyboard inputs and image recognition.

This program violates [NW Code of Conduct](https://www.newworld.com/en-us/forward-link?id=code-of-conduct/) and **you shouldn't use it on live situations, so it's your own responsability to use it**.

<div>
  <kbd>
    <img src="https://i.imgur.com/hKSGdZr.png"
    width=800/>
  </kbd>
</div>

## Features ⚙
- Anti AFK disconnection
- Switch to the "fishing stance"
- Equip a bait when it's expired
- Cast to a custom distance
- Skip the "uncommon fish" animation
- Repair at custom number of casts
- Reel the most effective way possible
---

## Getting started
### Prerequisites 🔴
You'll need [Python3](https://www.python.org/downloads/) to run.  
You'll need [pyAutoGUI](https://pypi.org/project/PyAutoGUI/), [pyDirectInput](https://pypi.org/project/PyDirectInput/) and [pyGetWindow](https://pypi.org/project/PyGetWindow/) Python libraries.

The images have been taken with a 1920*1080 resolution, so you should use the same resolution to avoid any errors.

### Console LOG 🔴
The "console.bat" displays useful information like how many casts made so far, casts until next repair and successfully completion of steps.

I reccommend using [AutoHotkey](https://www.autohotkey.com/) or any of [these](https://www.howtogeek.com/196958/the-3-best-ways-to-make-a-window-always-on-top-on-windows/) methods.  

### Anti-AFK 🔴
The Anti-AFK function will move left and right, so beware not to be standing on a little spot from which you can fall.

### Bait Function 🔴
The bait function equips a bait everytime it expires, and always equips the first bait on the baits menu.  
It doesn't stops automatically whenever you have 0 baits, so be sure to get enough baits to fish for the time you need.

### Key Bindings 🔴
The key bindings in-game are set to default, but you can change them at "config.py" file.  
~~~
E       -> Interact  
A       -> Move left
D       -> Move right
R       -> Repair AND Equip Bait
TAB     -> Inventory  
leftALT -> Lock the camera (free look)  
F3      -> Switch to "fishing stance" (cannot be modified)  
~~~

### Set up 🚀
Configure the settings at :
<div>
  <kbd>
    <img src="https://i.imgur.com/UfPyIbw.png" />
  </kbd>
</div>