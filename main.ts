let strip = neopixel.create(DigitalPin.P2, 12, NeoPixelMode.RGB)
strip.setBrightness(32)
strip.clear()
strip.showRainbow(1, 360)
basic.forever(function () {
    strip.rotate(1)
    strip.show()
    basic.pause(100)
})
