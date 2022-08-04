led.toggle(1, 0)
led.toggle(2, 0)
led.toggle(3, 0)
led.toggle(4, 0)
led.toggle(0, 1)
led.toggle(1, 1)
led.toggle(2, 1)
led.toggle(3, 1)
led.toggle(4, 1)
led.toggle(0, 2)
led.toggle(1, 2)
led.toggle(2, 2)
led.toggle(3, 2)
led.toggle(4, 2)
led.toggle(1, 3)
led.toggle(2, 3)
led.toggle(3, 3)
led.toggle(1, 4)
led.toggle(2, 4)
led.toggle(3, 4)

def on_button_pressed_a():
    basic.show_leds("""
    . . . . .
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    basic.show_leds("""
    . # . # .
    # . # . #
    # . # . #
    . . # . .
    . . # . .
    """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

seconds = 0

def on_gesture_shake():
    global seconds
    while seconds > 0:
        basic.show_number(seconds)
        basic.pause(1000)
        seconds -= 1
    basic.show_number(17)
    basic.show_leds("""
    . . # # #
    . . . # #
    # # # . #
    # . # . .
    # # # . .
    """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
