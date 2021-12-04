# Description

New-World-Auto-Fishing is a fully automatic program to fish in New World, using mouse and keyboard inputs and image recognition.
<div>
  <kbd>
    <img src="https://i.imgur.com/hKSGdZr.png"
    width=800/>
  </kbd>
</div>

## Features ⚙
- Anti AFK disconnection
- Switch to the "fishing stance"
- Equip a bait if desired and when it's expired
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
If you have a second monitor you should drag it there, if not, I reccommend using [AutoHotkey](https://www.autohotkey.com/) but any of [these](https://www.howtogeek.com/196958/the-3-best-ways-to-make-a-window-always-on-top-on-windows/) methods will work.  

### Anti-AFK 🔴
The Anti-AFK function will write the /sit command and then jump, so keep in mind that **if you're too deep into water its not possible to jump and you may die due running out of air.**

### Key Bindings 🔴
The key bindings in-game are set to default, but you can change them at "config.py" file.  
By default are the following :
~~~
E       -> Use  
Space   -> Jump  
R       -> Repair  
TAB     -> Inventory  
Enter   -> Opens the chat
F3      -> Switch to "fishing stance"  
leftALT -> Lock the camera (free look)  
~~~

### Set up 🚀
Configure the settings at :
<div>
  <kbd>
    <img src="https://i.imgur.com/UfPyIbw.png" />
  </kbd>
</div>