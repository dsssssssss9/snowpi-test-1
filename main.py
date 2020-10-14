strip = neopixel.create(DigitalPin.P2, 12, NeoPixelMode.RGB)
strip.set_brightness(32)
strip.clear()
strip.show_rainbow(1, 360)

def on_forever():
    strip.rotate(1)
    strip.show()
    basic.pause(100)
basic.forever(on_forever)
