import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define motor pins
motor1A = 17
motor1B = 18
motor2A = 22
motor2B = 23

# Additional GPIO pin for activation/deactivation
activationPin = 24

# Set motor pins and activation pin as output
GPIO.setup(motor1A, GPIO.OUT)
GPIO.setup(motor1B, GPIO.OUT)
GPIO.setup(motor2A, GPIO.OUT)
GPIO.setup(motor2B, GPIO.OUT)
GPIO.setup(activationPin, GPIO.OUT)

# Function to activate the robot motions
def activate_motion():
    GPIO.output(activationPin, GPIO.LOW)

# Function to deactivate the robot motions
def deactivate_motion():
    GPIO.output(activationPin, GPIO.HIGH)

# Function to move the robot forward
def move_forward():
    GPIO.output(motor1A, GPIO.LOW)
    GPIO.output(motor1B, GPIO.HIGH)
    GPIO.output(motor2A, GPIO.LOW)
    GPIO.output(motor2B, GPIO.HIGH)

# Function to move the robot backward
def move_backward():
    GPIO.output(motor1A, GPIO.HIGH)
    GPIO.output(motor1B, GPIO.LOW)
    GPIO.output(motor2A, GPIO.HIGH)
    GPIO.output(motor2B, GPIO.LOW)

# Function to turn the robot left
def turn_left():
    GPIO.output(motor1A, GPIO.HIGH)
    GPIO.output(motor1B, GPIO.LOW)
    GPIO.output(motor2A, GPIO.LOW)
    GPIO.output(motor2B, GPIO.HIGH)

# Function to turn the robot right
def turn_right():
    GPIO.output(motor1A, GPIO.LOW)
    GPIO.output(motor1B, GPIO.HIGH)
    GPIO.output(motor2A, GPIO.HIGH)
    GPIO.output(motor2B, GPIO.LOW)

# Function to stop the robot
def stop_robot():
    GPIO.output(motor1A, GPIO.HIGH)
    GPIO.output(motor1B, GPIO.HIGH)
    GPIO.output(motor2A, GPIO.HIGH)
    GPIO.output(motor2B, GPIO.HIGH)

try:
    while True:
        activate_motion()
        move_forward()
        time.sleep(2)
        
        stop_robot()
        time.sleep(1)
        
        move_backward()
        time.sleep(2)
        
        stop_robot()
        time.sleep(1)
        
        turn_left()
        time.sleep(1)
        
        stop_robot()
        time.sleep(1)
        
        turn_right()
        time.sleep(1)
        
        stop_robot()
        time.sleep(1)
        
        deactivate_motion()
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
