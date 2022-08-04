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
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showLeds(`
    . . . . .
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    `)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        `)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showLeds(`
    . # . # .
    # . # . #
    # . # . #
    . . # . .
    . . # . .
    `)
})
let seconds = 0
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    while (seconds > 0) {
        basic.showNumber(seconds)
        basic.pause(1000)
        seconds -= 1
    }
    basic.showNumber(17)
    basic.showLeds(`
    . . # # #
    . . . # #
    # # # . #
    # . # . .
    # # # . .
    `)
})
