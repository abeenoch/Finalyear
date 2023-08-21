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

p_down = 7
p_up = 12.5
q_down = 8
q_up = 2.5

# Calculate time per cycle and steps for two cycles in 5 seconds
time_per_cycle = 5 / 2  # Two cycles in 5 seconds
steps = 50  # Number of steps

# Start PWM
p.start(p_up)
q.start(q_up)

try:
    while True:
        for step in range(steps):
            # Calculate intermediate duty cycle values for smooth motion
            p_duty = p_up + (p_down - p_up) * (step) / steps
            q_duty = q_up + (q_down - q_up) * (step) / steps
            print(p_duty)
            print(q_duty)
            
            # Set the duty cycle for both servos
            p.ChangeDutyCycle(p_duty)
            q.ChangeDutyCycle(q_duty)
            
        
            timee = time.sleep(time_per_cycle / steps)
        
        # Swap the up and down positions for the servos
        lemp = p_up
        p_up = p_down
        p_down = lemp
        
        
        lemp = q_up
        q_up = q_down
        q_down = lemp

except KeyboardInterrupt:
    pass

# Clean up
p.stop()
q.stop()
GPIO.cleanup()
