# Raspberry Pi Coding 101

Instructions and presentation for a Raspberry Pi Coding 101 class for Python and button, LED and more!

To view the slides for the presentation, see the [Github Pages site](https://synshop.ch4lox.com/RaspberryPiCoding101/).

## Students

### Getting Started

This assumes your educator has prepared your Pi for you and you're getting started with the class.

Your educator should have the slides up to help you get familiar with the parts and help you assemble your Pi.

After that, follow along with your educator by opening the browser on your Pi and the Mu editor. Double click the "mu" icon 
and the "Chromium Web Browser":

![](images/launcher.icons.jpg)  

On the slides, you can use the arrow keys to 
go forward and backward in the slides.  

Set up your desktop to look like this so the editor and browser are side by side:

![](images/side.by.side.jpg)  

## Lessons

* 0: Parts and Patience</a> - Only lecture of the day - let's get to hacking ASAP!</li>
* 1: Hello World
* 2: Light
* 3: Button
* 4: Light Button
* 5: Light Button Game

## Educators

This class assumes the educator knows how to program and provision Raspberry Pi's.  The class is assumed to be
3 hours and targets middle schoolers, but likely older elementary and high schoolers would be fine as well. 

### BOM

Bill of Materials for this class is:

* \>$14 - Raspberry Pi - Pi 4 was used in screen shots, but any should work. This base price is 
for a Pi Zero W with headers.
* $9 - Squid Combo Pack - two buttons and an RGB LED
* $10 - 16 GB Micro SD card
* $10 - Pi power supply with cable
* $5 - HDMI cable
* \>$0 - Keyboard and Mouse (ideally donated or purchased at a used shop for cheap)

We've had great luck purchasing from [Chicago Electronic Distributors](https://chicagodist.com/). As we're a 
tax exempt non-profit, they didn't charge us tax, gave us educational discounts and generally were a
joy to work with.  That said, they don't sell the Pi Zero, so the $14 base price above isn't attainable through them.
As mentioned above, we used a Pi4. 

### Prep

1. Order all the equipment
1. Write 
[Raspbian with desktop and recommended software](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/2) 
to an SD card
1. Connect to the WiFI you'll use for the class
1. [Enable VNC](https://www.raspberrypi.org/documentation/remote-access/vnc/) (optional)
1. [Ensure Mu is installed](https://projects.raspberrypi.org/en/projects/getting-started-with-mu)
1. Clone the `squid` repo and run setup: `git clone https://github.com/simonmonk/squid.git;cd squid;sudo python3 setup.py install`
1. Clone this repo to docs `cd ~/Documents;git clone https://github.com/synshop/RaspberryPiCoding101.git`
1. Open `RaspberryPiCoding101/index.html` in the browser. Make this the default start page.
1. Create two icons on the desktop as shown in the "Getting started" section above. You can 
just drag the icons you need from the Pi application menu in the upper left
1. [Clone this first SD card onto all the others](https://beebom.com/how-clone-raspberry-pi-sd-card-windows-linux-macos/) 
so all Pi's are set up identically for the class.

todo - add steps to [shrink image](https://github.com/Drewsif/PiShrink)? 

### Sources

* [reveal.js](https://github.com/hakimel/reveal.js) for slides
* [LED & button contols via gpiozero](https://gpiozero.readthedocs.io/en/stable/api_output.html)
* [Getting Started with MU Eidtor](https://projects.raspberrypi.org/en/projects/getting-started-with-mu)
* [Getting Started with Raspberry Pi](https://projects.raspberrypi.org/en/projects/raspberry-pi-getting-started)
* [Chicago Electronic Distributors](https://chicagodist.com/)

## Wait, why did you do this!?  

With so much great material online, this repository likely is redundant, agreed!  However,
we wanted to have all our materials in one place where we could refine it over time.  Please
do use the sources above if you find it easier than this repo. 

## Contributions

Pull Requests and Issues are Welcome! 