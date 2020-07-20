You have not seen anything like this before...

This is the ChromaMidi plugin! With this simple Python program, you can use the RGB lights on your Razer Chroma enabled devices (currently only supported on mousepads) to create a full light show using a DAW like Ableton Live.
This program is designed to be used in conjunction with a midi controller like a Launchpad to bring your light show game to its fullest.
It uses the exact same color pallete that you're already used to with your Launchpad, and works in any version of Live, or any program that can send a midi signal!

Examples of this in action:
	Working on a cover!

Prerequisites:
	1. chroma-python (github.com/chroma-sdk/chroma-python)
	2. rtmidi (pip install python-rtmidi
	3. Some MIDI virtual device plugin like LoopBe
	4. Something that can send midi signals
	5. Obviously, a Razer device and Razer Synapse
	6. This has only been tested on Windows 10 and Python 3.8 with Ableton Live 10 Lite.

Installation & Usage:
	1. Make sure you've installed the prerequisites above.
	2. Make sure that 3rd-party apps are enabled in the Chroma Connect module.
	3. Run the program!
	4. Every LED on your mousepad will illuminate once as a test to make sure it has control. The remaining lights should be OFF during this test, and the red, green, and blue channels should all illuminate.
	5. Each LED's cooresponding number will also show up on the console output.
	6. Pick a device to monitor for note data
	7. Get playing! LED 0 is mapped to C2 and each LED is one note higher than the rest. Colors are controlled via velocity values on the same scale that the Launchpad MK2 uses. (http://www.launchpadfun.com/en/downloads_en/velocity-colors/)