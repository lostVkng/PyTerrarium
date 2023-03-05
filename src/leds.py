#!/usr/bin/env python3

"""
    leds.py
    
    Control LED Strip
    flags to set value
    -on
    -off
    
    Controlled via crontab
"""
import argparse
import neopixel
import board

# set dtparam=spi=on in boot/config/txt

#set GPIO Pins
pixel_pin = board.D10 # gpio 10 = pin 19


# Set the LEDs
def set_leds(status: bool):

    # The number of NeoPixels
    num_pixels = 60

    # The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
    # For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
    ORDER = neopixel.GRB

    pixels = neopixel.NeoPixel(
        pixel_pin, num_pixels, brightness=0.25, auto_write=False, pixel_order=ORDER
    )

    if status == True:
        # Color Pattern
        pattern = [(156, 255, 227)]
        
        # match pattern to length of LED strip (60 leds)
        led_colors = pattern * 60

        # set pixels
        for i, color in enumerate(led_colors):
            pixels[i] = color
    else:
        # turn off all LEDS
        pixels.fill((0,0,0))

    # Set the LEDS
    pixels.show()



if __name__ == "__main__":

    # setup arg parse
    parser = argparse.ArgumentParser()
    parser.add_argument('-on', action='store_true', help='Turn LEDS on')

    # parse the args
    args = parser.parse_args()

    # set the LEDS
    set_leds(args.on)