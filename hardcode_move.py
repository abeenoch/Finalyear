# import RPi.GPIO as GPIO
import time

# Set up GPIO mode
# GPIO.setmode(GPIO.BCM)

# Define motor pins
motor1A = 17
motor1B = 18
motor2A = 22
motor2B = 23

# arm commands
pick_motor = 25
drop_motor = 5


# Set motor pins as output
# GPIO.setup(motor1A, GPIO.OUT)
# GPIO.setup(motor1B, GPIO.OUT)
# GPIO.setup(motor2A, GPIO.OUT)
# GPIO.setup(motor2B, GPIO.OUT)
# GPIO.setup(pick_motor, GPIO.OUT)
# GPIO.setup(drop_motor, GPIO.OUT)


# Function to pick an object
def pick_object():
    print('Picking object')
    # GPIO.setup(pick_motor, GPIO.LOW)


def drop_object():
    print('Dropping object')
    # GPIO.setup(drop_motor, GPIO.LOW)


# Function to move the robot forward
def move_forward():
    # comment out the return statement and uncomment the rest
    print('Moving forward')
    # GPIO.output(motor1A, GPIO.LOW)
    # GPIO.output(motor1B, GPIO.HIGH)
    # GPIO.output(motor2A, GPIO.LOW)
    # GPIO.output(motor2B, GPIO.HIGH)


# Function to move the robot backward
def move_backward():
    # comment out the return statement and uncomment the rest
    print('Moving backward')

    # GPIO.output(motor1A, GPIO.HIGH)
    # GPIO.output(motor1B, GPIO.LOW)
    # GPIO.output(motor2A, GPIO.HIGH)
    # GPIO.output(motor2B, GPIO.LOW)


# Function to turn the robot left
def turn_left():
    # comment out the return statement and uncomment the rest
    print('Turning left')

    # GPIO.output(motor1A, GPIO.HIGH)
    # GPIO.output(motor1B, GPIO.LOW)
    # GPIO.output(motor2A, GPIO.LOW)
    # GPIO.output(motor2B, GPIO.HIGH)


# Function to turn the robot right
def turn_right():
    # comment out the return statement and uncomment the rest
    print('turning right')

    # GPIO.output(motor1A, GPIO.LOW)
    # GPIO.output(motor1B, GPIO.HIGH)
    # GPIO.output(motor2A, GPIO.HIGH)
    # GPIO.output(motor2B, GPIO.LOW)


# Function to stop the robot
def stop_robot():
    # comment out the return statement and uncomment the rest
    print('Stopping')

    # GPIO.output(motor1A, GPIO.HIGH)
    # GPIO.output(motor1B, GPIO.HIGH)
    # GPIO.output(motor2A, GPIO.HIGH)
    # GPIO.output(motor2B, GPIO.HIGH)


try:
    while True:
        command = input('Give a command: ')
        if command == 'forward':
            move_forward()
            time.sleep(2)
        elif command == 'stop':
            stop_robot()
            time.sleep(1)
        elif command == 'backward':
            move_backward()
            time.sleep(2)
        elif command == 'turn left':
            turn_left()
            time.sleep(1)
        elif command == 'turn right':
            turn_right()
            time.sleep(1)
        elif command == 'pick':
            pick_object()
        elif command == 'drop':
            drop_object()

except KeyboardInterrupt:
    print('omo')
    # GPIO.cleanup()
