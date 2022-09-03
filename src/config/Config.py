'''
!Important!
Allways import the whole Config module using
import config.Config as Cfg
because otherwise overriding config-values wont take effect for your code
'''

# How many screen-pixels one poxel-pixel takes up on the pygame-renderer
LED_PIXEL_SCALE = 60

# Serial-Baud rate that the esp32 uses for the serial-userinput connection
ESP_BAUD = 9600

# General speed of all scenes. Default is normal 1
APP_SPEED = 1

# Amount of leds a cube consists of
CUBE_SIZE_X = 3
CUBE_SIZE_Y = 4

# Amount of cubes the wall consists of
WALL_SIZE_X = 6
WALL_SIZE_Y = 6