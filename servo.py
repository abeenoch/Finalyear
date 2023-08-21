import RPi.GPIO as GPIO
import time


# Set up GPIO
servo_pin1 = 18
servo_pin2 = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin1, GPIO.OUT)
GPIO.setup(servo_pin2, GPIO.OUT)

# Create PWM instance
p = GPIO.PWM(servo_pin1, 50)  # 50 Hz (20 ms period)
q = GPIO.PWM(servo_pin2, 50)

p_down = 2.5
p_up =  12.5
q_down = 12.5
q_up = 2.5

# Start PWM
p.start(p_up)  # Initial duty cycle (0 degrees)
q.start(q_up)


def move_joint1():
    turning = True

    try:
        while turning:
            # Rotate the servo motor to 180 degrees
            p.ChangeDutyCycle(p_up)# 180 degrees
            q.ChangeDutyCycle(q_up)
            print('turning')
            time.sleep(1)  # Wait for 1 second
        
        
            # Rotate the servo motor back to 0 degrees
            p.ChangeDutyCycle(7)# 0 degrees
            q.ChangeDutyCycle(8)
            print('return')
            time.sleep(1)# Wait for 1 second
            
            #turning = False

    except KeyboardInterrupt:
        pass
    
#
        
    
move_joint1()


# Clean up
p.stop()
GPIO.cleanup()
