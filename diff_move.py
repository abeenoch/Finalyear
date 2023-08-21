import RPi.GPIO as GPIO
import time

# Set up GPIO
servo_pin1 = 27
servo_pin2 = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin1, GPIO.OUT)
GPIO.setup(servo_pin2, GPIO.OUT)

# Create PWM instances
p = GPIO.PWM(servo_pin1, 50)  # 50 Hz (20 ms period)
q = GPIO.PWM(servo_pin2, 50)

p_down = 9
p_up = 12.5
q_down = 6
q_up = 2.5

# Calculate time per cycle and steps for two cycles in 5 seconds
time_per_cycle = 5 / 2  # Two cycles in 5 seconds
steps = 50  # Number of steps

# Start PWM
p.start(p_up)
q.start(q_up)

def move_servo_up(servo, start_pos, end_pos, steps, time_per_step):
    duty_range = end_pos - start_pos
    duty_increment = duty_range / steps

    for _ in range(steps):
        start_pos += duty_increment
        servo.ChangeDutyCycle(start_pos)
        time.sleep(time_per_step)

def move_servo_down(servo, start_pos, end_pos, steps, time_per_step):
    duty_range = start_pos - end_pos
    duty_decrement = duty_range / steps

    for _ in range(steps):
        start_pos -= duty_decrement
        servo.ChangeDutyCycle(start_pos)
        time.sleep(time_per_step)

try:
    
    move_servo_up(p, p_down, p_up, steps, time_per_cycle / steps)
    move_servo_down(p, p_up, p_down, steps, time_per_cycle / steps)

    move_servo_up(q, q_down, q_up, steps, time_per_cycle / steps)
    move_servo_down(q, q_up, q_down, steps, time_per_cycle / steps)
        

except KeyboardInterrupt:
    p.stop()
    q.stop()
    GPIO.cleanup()
