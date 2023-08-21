import RPi.GPIO as GPIO
import time
import speech_recognition as sr

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define motor pins
motor1A = 17
motor1B = 18
motor2A = 22
motor2B = 23

# Set motor pins as output
GPIO.setup(motor1A, GPIO.OUT)
GPIO.setup(motor1B, GPIO.OUT)
GPIO.setup(motor2A, GPIO.OUT)
GPIO.setup(motor2B, GPIO.OUT)

# Initialize speech recognition
recognizer = sr.Recognizer()

# Function to move the robot forward
def move_forward():
    GPIO.output(motor1A, GPIO.HIGH)
    GPIO.output(motor1B, GPIO.LOW)
    GPIO.output(motor2A, GPIO.HIGH)
    GPIO.output(motor2B, GPIO.LOW)

# Function to move the robot backward
def move_backward():
    GPIO.output(motor1A, GPIO.LOW)
    GPIO.output(motor1B, GPIO.HIGH)
    GPIO.output(motor2A, GPIO.LOW)
    GPIO.output(motor2B, GPIO.HIGH)

# Function to turn the robot left
def turn_left():
    GPIO.output(motor1A, GPIO.LOW)
    GPIO.output(motor1B, GPIO.HIGH)
    GPIO.output(motor2A, GPIO.HIGH)
    GPIO.output(motor2B, GPIO.LOW)

# Function to turn the robot right
def turn_right():
    GPIO.output(motor1A, GPIO.HIGH)
    GPIO.output(motor1B, GPIO.LOW)
    GPIO.output(motor2A, GPIO.LOW)
    GPIO.output(motor2B, GPIO.HIGH)

# Function to stop the robot
def stop_robot():
    GPIO.output(motor1A, GPIO.LOW)
    GPIO.output(motor1B, GPIO.LOW)
    GPIO.output(motor2A, GPIO.LOW)
    GPIO.output(motor2B, GPIO.LOW)

try:
    while True:
        print("Listening for a command...")
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print("Command:", command)
            
            if "move forward" in command:
                move_forward()
            elif "move backward" in command:
                move_backward()
            elif "turn left" in command:
                turn_left()
            elif "turn right" in command:
                turn_right()
            elif "stop" in command:
                stop_robot()
            else:
                print("Unknown command")

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

except KeyboardInterrupt:
    GPIO.cleanup()
