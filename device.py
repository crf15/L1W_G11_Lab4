from sense_hat import SenseHat
from backend import Backend, logger
from mydbconfig import *

sense = SenseHat()

def init_screen(backend):
    if backend.is_device():
        colors=backend.get_led_status(backend._device_info['serial'])
        sense.set_pixels(colors)
    else:
        raise Exception("This is not a Raspberry pi. This file should be run from a RPi.")

def led_stream_handler(message):
    if message['event'] =='put':
        if message ['path'][1:].isnumeric():
            ledn = int(message ['path'][1:])
            color = message['data']
            sense.set_pixel(
                (ledn-1)%8,
                int((ledn-1)/8),
                message['data'][0],
                message['data'][1],
                message['data'][2],
                )
            logger.debug(f"Received update for led: {message}")

def main():
    #initialize the db with configuration and user data
    backend = Backend(config, email, firstname, lastname)

    #initialize the LED values from database
    init_screen(backend)

    #register a stream: whenever there is a change, execute the function led_stream_handler()
    led_stream = backend._db \
        .child('devices') \
        .child(backend._device_info['serial']) \
        .child('leds') \
        .stream(led_stream_handler)
       
    clear_leds(backend)

# to be implemented by students
def clear_leds(backend):
    # constantly check if SenseHat joystick was pressed
    # if joystick pressed, clear all leds
    while True:
        for event in sense.stick.get_events():
            # clear SenseHat leds if joystick is pressed (middle button)
            if event.direction == "middle":
                backend.clear_leds(backend.get_device_id())
    

if __name__ == '__main__':
    main()
    
