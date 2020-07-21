from ChromaPython import ChromaApp, ChromaAppInfo, ChromaColor, Colors, ChromaGrid
from rtmidi.midiutil import open_midiinput
from time import sleep
import sys

#infos
Info = ChromaAppInfo()
Info.DeveloperName = "RaddedMC"
Info.DeveloperContact = "reddit.com/u/raddedmc"
Info.Category = "application"
Info.SupportedDevices = ['mousepad']
Info.Description = "RaddedMC's MIDI light-show plugin for Razer Chroma. Designed for use with a Razer Firefly and Ableton Live. Source code at github.com/raddedmc/ChromaMidi ."
Info.Title = "ChromaMidi"

#some other assignments
App = ChromaApp(Info)
MousepadGrid = ChromaGrid('Mousepad')
App.Mousepad.setStatic(Colors.BLUE)

#Welcome
print("---------------------------------------")
print("Thanks for checking out RaddedMC's ChromaMidi program! Let's get started:")
print("Note: This version of ChromaMidi currently only supports Chroma-enabled mousepads. Other devices can be added on request. Open the Chroma Connect app or PM u/RaddedMC if you're interested in support for other devices.")
print("---------------------------------------")

#light test
print("The mousepad has " + str(len(MousepadGrid)) + " lights.")

#to change colour:
#   DeviceGrid[light].set("HEX CODE")
#   App.[DEVICE].setCustomGrid(DeviceGrid)
#   App.[DEVICE].applyGrid()

print("Testing lights...")

for i in range(0, len(MousepadGrid)):

    # RED
    print("Light " + str(i) + ": ON")
    MousepadGrid[i].set(red=255,green=0,blue=0)
    App.Mousepad.setCustomGrid(MousepadGrid)
    App.Mousepad.applyGrid()
    sleep(0.1)
    
    # GREEN
    MousepadGrid[i].set(red=0,green=255,blue=0)
    App.Mousepad.setCustomGrid(MousepadGrid)
    App.Mousepad.applyGrid()
    sleep(0.1)
    
    # BLUE
    MousepadGrid[i].set(red=0,green=0,blue=255)
    App.Mousepad.setCustomGrid(MousepadGrid)
    App.Mousepad.applyGrid()
    sleep(0.1)
    
    # OFF
    MousepadGrid[i].set(red=0,green=0,blue=0)
    App.Mousepad.setCustomGrid(MousepadGrid)
    App.Mousepad.applyGrid()
    print("Light " + str(i) + ": OFF")
    
print("---------------------------------------")
print("Test complete. Initializing midi.")
print("Note: If your device's LEDs did not light up, make sure that Chroma Connect is enabled and that your device is visible to Razer Synapse.")
print("---------------------------------------")
print("Please select your virtual midi port below:")

def setALight(lightToSet, lightR, lightG, lightB):
    try:
        MousepadGrid[lightToSet].set(red=lightR, green=lightG, blue=lightB)
        App.Mousepad.setCustomGrid(MousepadGrid)
        App.Mousepad.applyGrid()
    except IndexError:
        print("Index out of range!")
    # 0 is Razer logo, goes around downwards

def interpretVelColor(vel):
    red = 0
    green = 0
    blue = 0
    if vel == 0:
        pass
    elif vel == 1:
        red = 85
        green = 85
        blue = 85
    elif vel == 2:
        red = 170
        green = 170
        blue = 170
    elif vel == 3:
        red = 255
        green = 255
        blue = 255
    elif vel == 4: # Needs more red
        red = 255
        green = 50
        blue = 50
    elif vel == 5:
        red = 255
    elif vel == 6:
        red = 170
    elif vel == 7:
        red = 85
    elif vel == 8:
        red = 255
        green = 240
        blue = 142
    elif vel == 9:
        red = 255
        green = 80
    elif vel == 10:
        red = 170
        green = 40
    elif vel == 11:
        red = 85
        green = 20
    elif vel == 12:
        red = 255
        green = 226
        blue = 36
    elif vel == 13:
        red = 255
        green = 255
    elif vel == 14:
        red = 170
        green = 170
    elif vel == 15:
        red = 85
        green = 85
    elif vel == 16:
        red = 113
        green = 255
        blue = 36
    elif vel == 17:
        red = 75
        green = 255
    elif vel == 18:
        red = 50
        green = 170
    elif vel == 19:
        red = 25
        green = 85
    elif vel == 20:
        red = 65
        green = 255
        blue = 55
    elif vel == 21:
        green = 255
    elif vel == 22:
        green = 170
    elif vel == 23:
        green = 85
    elif vel == 24:
        red = 95
        green = 255
        blue = 85
    elif vel == 25:
        green = 255
        blue = 30
    elif vel == 26:
        green = 170
        blue = 20
    elif vel == 27:
        green = 85
        blue = 10
    elif vel == 28:
        red = 80
        green = 255
        blue = 40
    elif vel == 29:
        red = 60
        green = 255
        blue = 30
    elif vel == 30:
        red = 50
        green = 235
        blue = 20
    elif vel == 31:
        red = 40
        green = 255
        blue = 10
    elif vel == 32:
        red = 160
        green = 255
        blue = 110
    elif vel == 33:
        red = 112
        green = 179
        blue = 77
    elif vel == 34:
        red = 87
        green = 139
        blue = 60
    elif vel == 35:
        red = 55
        green = 87
        blue = 38
    elif vel == 36:
        red = 118
        green = 255
        blue = 255
    elif vel == 37:
        green = 200
        blue = 255
    elif vel == 38:
        green = 133
        blue = 170
    elif vel == 39:
        green = 66
        blue = 85
    elif vel == 40:
        red = 105
        green = 182
        blue = 255
    elif vel == 41:
        green = 152
        blue = 255
    elif vel == 42:
        green = 103
        blue = 170
    elif vel == 43:
        green = 51
        blue = 85
    elif vel == 44:
        red = 107
        green = 144
        blue = 255
    elif vel == 45:
        blue = 255
    elif vel == 46:
        blue = 170
    elif vel == 47:
        blue = 85
    elif vel == 48:
        red = 211
        green = 143
        blue = 255
    elif vel == 49:
        red = 164
        blue = 244
    elif vel == 50:
        red = 142
        green = 66
        blue = 255
    elif vel == 51:
        red = 94
        green = 44
        blue = 169
    elif vel == 52:
        red = 82
        green = 39
        blue = 170
    elif vel == 53:
        red = 255
        blue = 255
    elif vel == 54:
        red = 200
        blue = 200
    elif vel == 55:
        red = 150
        blue = 150
    elif vel == 56:
        red = 255
        green = 88
        blue = 85
    elif vel == 57:
        red = 255
        blue = 102
    elif vel == 58:
        red = 209
        blue = 108
    elif vel == 59:
        red = 158
        blue = 82
    elif vel == 60:
        red = 255
        green = 30
    elif vel == 61:
        red = 255
        green = 150
    elif vel == 62:
        red = 255
        green = 216
    elif vel == 63:
        red = 110
        green = 204
    elif vel == 64:
        green = 255
    elif vel == 65:
        green = 187
        blue = 60
    elif vel == 66:
        green = 102
        blue = 255
    elif vel == 67:
        red = 47
        green = 86
        blue = 255
    elif vel == 68:
        red = 45
        green = 184
        blue = 196
    elif vel == 69:
        red = 100
        green = 59
        blue = 255
    elif vel == 70:
        red = 255
        green = 251
        blue = 216
    elif vel == 71:
        red = 135
        green = 133
        blue = 114
    elif vel == 72:
        red = 194
        green = 191
        blue = 164
    elif vel == 73:
        red = 255
        green = 243
        blue = 20
    elif vel == 74:
        red = 234
        green = 255
    elif vel == 75:
        red = 132
        green = 255
    elif vel == 76:
        red = 18
        green = 225
    elif vel == 77:
        green = 255
        blue = 50
    elif vel == 78:
        green = 212
        blue = 255
    elif vel == 79:
        green = 162
        blue = 255
    elif vel == 80:
        red = 175
        green = 92
        blue = 255
    elif vel == 81:
        red = 222
        green = 92
        blue = 255
    elif vel == 82:
        red = 255
        green = 95
        blue = 205
    elif vel == 83:
        red = 187
        green = 114
    elif vel == 84:
        red = 255
        green = 92
    elif vel == 85:
        red = 198
        green = 255
    elif vel == 86:
        red = 128
        green = 255
        blue = 37
    elif vel == 87:
        red = 91
        green = 241
    elif vel == 88:
        red = 22
        green = 255
        blue = 34
    elif vel == 89:
        red = 72
        green = 255
        blue = 72
    elif vel == 90:
        red = 55
        green = 255
        blue = 190
    elif vel == 91: 
        red = 165
        green = 255
        blue = 255
    elif vel == 92:
        red = 104
        green = 211
        blue = 255
    elif vel == 93:
        red = 205
        green = 192
        blue = 255
    elif vel == 94:
        red = 235
        green = 105
        blue = 255
    elif vel == 95:
        red = 255
        blue = 134
    elif vel == 96:
        red = 255
        green = 102
    elif vel == 97:
        red = 255
        green = 155
    elif vel == 98: 
        red = 150
        green = 255
    elif vel == 99:
        red = 205
        green = 174
    elif vel == 100:
        red = 163
        green = 138
    elif vel == 101:
        red = 68
        green = 212
        blue = 40
    elif vel == 102:
        green = 255
        blue = 80
    elif vel == 103: 
        red = 82
        green = 90
        blue = 107
    elif vel == 104:
        red = 73
        green = 79
        blue = 95
    elif vel == 105:
        red = 255
        green = 200
        blue = 30
    elif vel == 106:
        red = 255
        green = 35
    elif vel == 107:
        red = 255
        green = 140
        blue = 80
    elif vel == 108:
        red = 255
        green = 166
        blue = 30
    elif vel == 109:
        red = 255
        green = 255
        blue = 20
    elif vel == 110:
        red = 171
        green = 255
        blue = 50
    elif vel == 111:
        red = 157
        green = 230
    elif vel == 112: 
        red = 89
        green = 92
        blue = 97
    elif vel == 113:
        red = 255
        green = 246
        blue = 80
    elif vel == 114:
        red = 139
        green = 255
        blue = 100
    elif vel == 115: 
        red = 205
        green = 207
        blue = 255
    elif vel == 116:
        red = 166
        green = 170
        blue = 255
    elif vel == 117:
        red = 191
        green = 193
        blue = 155
    elif vel == 118:
        red = 228
        green = 231
        blue = 186
    elif vel == 119:
        red = 238
        green = 255
        blue = 205
    elif vel == 120: # Untested
        red = 255
        green = 22
    elif vel == 121: # Untested
        red = 235
    elif vel == 122: 
        red = 90
        green = 255
    elif vel == 123:
        red = 59
        green = 167
    elif vel == 124:
        red = 224
        green = 227
    elif vel == 125:
        red = 181
        green = 183
    elif vel == 126:
        red = 255
        green = 170
    elif vel == 127:
        red = 255
        green = 90
    
    colors = (int(red), int(green), int(blue))
    return colors


#--LETS GET STARTED!--
port = sys.argv[1] if len(sys.argv) > 1 else None # Prompts user for MIDI input port, unless a valid port number or name
                                                  # is given as the first argument on the command line.
                                                  # API backend defaults to ALSA on Linux.
midiin, port_name = open_midiinput(port)
print("Midi opened on device " + str(port_name) + ".")
print("---------------------------------------")

while True:
    msg = midiin.get_message()
    
    if msg:
        led_num = msg[0][1]-48
        colors = (0,0,0)
        if msg[0][0] == 144:
            # ON
            colors = interpretVelColor(msg[0][2])
            print("%r: Light %i set to (%s,%s,%s)" % (msg, led_num, colors[0], colors[1], colors[2]))
            setALight(abs(led_num), colors[0], colors[1], colors[2])
        elif msg[0][0] == 128:
            # OFF
            print("%r: Turning off light %i" % (msg, led_num))
            setALight(abs(led_num), colors[0], colors[1], colors[2])
    
    
# [noteon/off, note value, velocity]
# [144 = ON, 128 = OFF (off vel is 64)]
# [Note 48 is C2]