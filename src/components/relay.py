from machine import Pin


class Relay(Pin):

    def __init__(self, pin_number: int):
        super().__init__(pin_number, Pin.OUT)
