import RPi.GPIO as GPIO
import time
import threading

# Set up GPIO
servo_pin1 = 27
servo_pin2 = 23
servo_pin3 = 17
servo_pin4 = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin1, GPIO.OUT)
GPIO.setup(servo_pin2, GPIO.OUT)
GPIO.setup(servo_pin3, GPIO.OUT)
GPIO.setup(servo_pin4, GPIO.OUT)

# Create PWM instances
p = GPIO.PWM(servo_pin1, 50)  # 50 Hz (20 ms period)
q = GPIO.PWM(servo_pin2, 50)
r = GPIO.PWM(servo_pin3, 50)
s = GPIO.PWM(servo_pin4, 50)

p_down = 9
p_up = 10.5
q_down = 6
q_up = 4.5

r_down = 12.5
r_up = 12.5
s_down = 2.5
s_up = 2.5

# Calculate time per cycle and steps for two cycles in 5 seconds
time_per_cycle = 5 / 2  # Two cycles in 5 seconds
steps = 50  # Number of steps

# Start PWM
p.start(p_up)
q.start(q_up)
r.start(p_up)
s.start(q_up)

def move_elbow_down(servo, start_pos, end_pos, steps, time_per_step):
    duty_range = start_pos - end_pos
    duty_decrement = duty_range / steps

    for _ in range(steps):
        start_pos -= duty_decrement
        servo.ChangeDutyCycle(start_pos)
        time.sleep(time_per_step)

def move_shoulder_up(servo, start_pos, end_pos, steps, time_per_step):
    duty_range = end_pos - start_pos
    duty_increment = duty_range / steps

    for _ in range(steps):
        start_pos += duty_increment
        servo.ChangeDutyCycle(start_pos)
        time.sleep(time_per_step)

def move_elbow_shoulder(servo1, servo2, start_pos1, start_pos2, end_pos1, end_pos2, steps, time_per_step):
    duty_range1 = start_pos1 - end_pos1
    duty_decrement1 = duty_range1 / steps

    duty_range2 = start_pos2 - end_pos2
    duty_decrement2 = duty_range2 / steps

    for _ in range(steps):
        start_pos1 -= duty_decrement1
        start_pos2 -= duty_decrement2

        servo1.ChangeDutyCycle(start_pos1)
        servo2.ChangeDutyCycle(start_pos2)

        time.sleep(time_per_step)

try:
    #shoulder_thread = threading.Thread(target=move_shoulder_up, args=(p, p_down, p_up, steps, time_per_cycle / steps))
    elbow_thread = threading.Thread(target=move_elbow_down, args=(s, s_up, s_down, steps, time_per_cycle / steps))

    #shoulder_thread.start()
    #time.sleep(1)  # Wait for a moment before starting the elbow thread
    elbow_thread.start()

    #shoulder_thread.join()
    elbow_thread.join()

except KeyboardInterrupt:
    p.stop()
    q.stop()
    r.stop()
    s.stop()
    GPIO.cleanup()
  