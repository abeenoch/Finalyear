import RPi.GPIO as GPIO
import time

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

r_down = 5.5
r_up = 6
s_down = 7.5
s_up = 6

# Calculate time per cycle and steps for two cycles in 5 seconds
time_per_cycle = 5 / 2  # Two cycles in 5 seconds
steps = 50  # Number of steps

# Start PWM
p.start(p_up)
q.start(q_up)
r.start(p_up)
s.start(q_up)

joint = 'shoulder'


try:
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
        
        move_elbow_down(s, s_up, q_down, steps, time_per_cycle / steps)



    move_shoulder_up(p, p_down, p_up, steps, time_per_cycle / steps)      



except KeyboardInterrupt:
    p.stop()
    q.stop()
    r.stop()
    s.stop()
    GPIO.cleanup()


