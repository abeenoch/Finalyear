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
p_up = 12.5
q_down = 12.5
q_up = 2.5

# Calculate time per cycle and steps for two cycles in 5 seconds
time_per_cycle = 5 / 2  # Two cycles in 5 seconds
steps = 100  # Number of steps

# Start PWM
p.start(p_up)
q.start(q_up)

def move_servo_slowly(start, end, delta):
    incMove = (end - start) / 100.0
    incTime = delta / 100.0
    for x in range(100):
        p.ChangeDutyCycle(int(start + x * incMove))
        q.ChangeDutyCycle(int(start + x * incMove))
        time.sleep(incTime)

def move_joint1():
    turning = True

    try:
        while turning:
            # Rotate the servo motor to initial position slowly
            move_servo_slowly(p_up, p_down, 2)  # Move servo 1
            move_servo_slowly(q_up, q_down, 2)  # Move servo 2
            print('Going to initial position')

            # Continue the remaining motion slowly
            for step in range(steps):
                # Calculate intermediate duty cycle values for smooth motion
                p_duty = p_down + (p_up - p_down) * step / steps
                q_duty = q_down + (q_up - q_down) * step / steps
                print(p_duty)
                print(q_duty)

                # Set the duty cycle for both servos
                p.ChangeDutyCycle(p_duty)
                q.ChangeDutyCycle(q_duty)

                time.sleep(time_per_cycle / steps)

            # Swap the up and down positions for the servos
            temp = p_up
            p_up = p_down
            p_down = temp

            temp = q_up
            q_up = q_down
            q_down = temp

            print('Cycle completed')

    except KeyboardInterrupt:
        pass

move_joint1()

# Clean up
p.stop()
q.stop()
GPIO.cleanup()
