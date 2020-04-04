# Raspberry Pi Coding 101

Instructions and presentation for a Raspberry Pi Coding 101 class for Python and button, LED and more!

To view the slides for the presentation, see the [Github Pages site](https://synshop.ch4lox.com/RaspberryPiCoding101/)
or clone this repo and open `index.html` in a browser. 

## Students

### Getting Started

This assumes your educator has prepared your Pi for you and your educator also should have the slides up an central
screen/projector to help you get familiar with the parts and help you assemble your Pi so you can follow
these slides yourself.

After you have your Pi assumbled and booted up, follow along with your educator by opening the browser on your 
Pi and the Mu editor. Double click the "mu" icon 
and the "Chromium Web Browser":

![](./images/launcher.icons.png)  

On the slides, you can use the arrow keys to go forward and backward in the slides. Be sure to be
patient while you learn to code. As well, if you get done early, help out other classmates who might need
a hand!  

## Lessons

* 0: Parts and Patience - Learn how to assemble your hardware and what all the parts are.
* 1: Hello World - Your first line of code!  "Hello World" is often 
[the first line of code you write](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program) when learning a new language.
Concepts covered are the [`print()`](https://docs.python.org/3.5/library/functions.html#print) function. The second version of the app introduces 
[variables](https://www.tutorialspoint.com/python/python_variable_types.htm) and 
a [`while:`](https://docs.python.org/3.5/reference/compound_stmts.html#while) loop; 
* 2: Light - We'll upgrade from 1 line to 6 lines of code and control a light you'll attach to your Pi. Concepts
covered are [objects](https://www.tutorialspoint.com/python/python_classes_objects.htm) and the concept
of [importing](https://docs.python.org/3/reference/import.html)
* 3: Button - Now we'll go up to 9 lines of code so you can code a button interacting with your Pi. Concepts covered
are [functions](https://www.tutorialspoint.com/python/python_functions.htm)
* 4: Light Button Game - While almost 30 lines of code, this game will use all the concepts we've learned above to
write a game. Concepts covered are mixing and matching all the of the above concepts.

## Educators

This class assumes the educator knows how to program and provision Raspberry Pi's.  The class is assumed to be
3 hours and targets late elementary kids at the youngest (4th grade and up). However, motivated younger kids
could do it! I tested this class on my 2nd grader ;)  Otherwise, any one older than a 4th grade can be a student
in this class. Teach away!! 

### BOM

Bill of Materials for this class is:

* \>$14 - Raspberry Pi*
* $9 - Squid Combo Pack - two buttons and an RGB LED
* $10 - 16 GB Micro SD card
* $10 - Pi power supply with cable
* $5 - HDMI cable
* \>$0 - Keyboard and Mouse (ideally donated or purchased at a used shop for cheap)
* $0 - Monitor - It's assumed students will use either a monitor they have at home or use their TV so won't need
one to take home. We used shop monitors or brought in personal ones from shop members to borrow for the day. 

* - While a Pi Zero W with headers ($10 for board + $4 soldered on headers) will work, it might be painfully slow, bordering
on an unusable UI.  If you 
can spring for it a 3 or 4 would be better.

We've had great luck purchasing from [Chicago Electronic Distributors](https://chicagodist.com/). As we're a 
tax exempt non-profit, they didn't charge us tax, gave us educational discounts and generally were a
joy to work with.  That said, they don't sell the Pi Zero, so the $14 base price above isn't attainable through them.
As mentioned above, we used a Pi4. 

### Prep

If you have any issues doing this prep, please reach out to us, we'd be happy to help!  We're working to create a disk 
image with all this work done. You could then just download the image and write it to your SD cards.  Until then, 
follow these steps:

1. Order all the equipment
1. Write 
[Raspbian with desktop and recommended software](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/2) 
to an SD card. Optionally enable SSH via writing file to disk ([option 3 here](https://www.raspberrypi.org/documentation/remote-access/ssh/))
1. Assemble a complete kit of one of your Pi setups including keyboard and monitor from the class. We'll prep everything 
here just once and the clone to the SD cards.
1. Go through the first run wizard. Consider changing the `pi` user password to something simple, but not the `raspberry` default. 
You will share this password with the students so they know it.
1. Update all software from the console with `sudo apt update&&sudo apt dist-upgrade`
1. Connect to the WiFI you'll use for the class - this way the Pi will auto connect during the class and you can finish prep.
Note - if you connect to other WiFi networks, the password is stored in cleartext in `/etc/wpa_supplicant/wpa_supplicant.conf`, so 
be aware!
1. [Enable VNC](https://www.raspberrypi.org/documentation/remote-access/vnc/) (optional - if you do do this and download
the [RealVNC client](https://www.realvnc.com/en/connect/download/viewer/) you can do the rest of the config remotely 
and with out the bulky monitor, keyboard and mouse)
1. [Enable SSH](https://www.raspberrypi.org/documentation/remote-access/ssh/) (optional - handy for copying files too
and from the device).
1. [Ensure Mu is installed](https://projects.raspberrypi.org/en/projects/getting-started-with-mu)
1. Clone this repo to `Documents` directory `cd ~/Documents;git clone https://github.com/synshop/RaspberryPiCoding101.git`
1. Open `RaspberryPiCoding101/index.html` in the browser. Make this the default start page.
1. Create two icons on the desktop as shown in the "Getting started" section above. You can 
just drag the icons you need from the Pi application menu in the upper left
1. [Clone this first SD card onto all the others](https://beebom.com/how-clone-raspberry-pi-sd-card-windows-linux-macos/) 
so all Pi's are set up identically for the class. Optionally, you may use  
[PiShrink](https://github.com/Drewsif/PiShrink) to reduce the .img size and time to write to subsequent SD cards. See also [Etcher](https://www.balena.io/etcher/) for a fancy UI way to do this.

### Sources

* [reveal.js](https://github.com/hakimel/reveal.js) for slides
* [LED & button contols via gpiozero](https://gpiozero.readthedocs.io/en/stable/api_output.html)
* [Getting Started with MU Eidtor](https://projects.raspberrypi.org/en/projects/getting-started-with-mu)
* [Getting Started with Raspberry Pi](https://projects.raspberrypi.org/en/projects/raspberry-pi-getting-started)
* [Chicago Electronic Distributors](https://chicagodist.com/)

## Q&A 

### Wait, why did you do this!?  

With so much great material online, this repository likely is redundant, agreed!  However,
we wanted to have all our materials in one place where we could refine it over time.  Please
do use the sources above if you find it easier than this repo. 

### I'm an educator, don't know how to program but want to lead this course - help!

Your best bet is to follow the awesome 
[getting Started with Raspberry Pi](https://projects.raspberrypi.org/en/projects/raspberry-pi-getting-started) guides.
Teach yourself first one of these beginning classes and then turn around and teach your students.  Or,
reach out to us, we'd be happy to do this class for grown ups if you can get to our location (or have
all kinds of fancy budget to fly one of out ;).

## Contributions

Pull Requests and Issues are Welcome! 
