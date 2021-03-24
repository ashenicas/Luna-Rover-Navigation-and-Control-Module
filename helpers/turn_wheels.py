from services.single_stepper_motor import TurnOneWheel


class Turn:
    def __init__(self):
        self.front_left = TurnOneWheel(motor_channel=(29, 31, 33, 35))
        self.front_right = TurnOneWheel(motor_channel=(29, 31, 33, 35))  # change pin numbers
        self.back_left = TurnOneWheel(motor_channel=(29, 31, 33, 35))  # change pin numbers
        self.back_right = TurnOneWheel(motor_channel=(29, 31, 33, 35))  # change pin numbers
        self.current_angle = 0
        self.current_direction = ''

    def left(self, speed, angle):
        self.current_angle = self.front_left.current_angle
        self.current_direction = 'l'
        front_motor_direction = 'c'
        back_motor_direction = 'a'
        self.front_left.runner(motor_direction=front_motor_direction, speed=speed, angle=angle)
        self.front_right.runner(motor_direction=front_motor_direction, speed=speed, angle=angle)

        self.back_left.runner(motor_direction=back_motor_direction, speed=speed, angle=angle)
        self.back_right.runner(motor_direction=back_motor_direction, speed=speed, angle=angle)

    def right(self, speed, angle):
        self.current_angle = self.front_left.current_angle
        self.current_direction = 'r'
        front_motor_direction = 'a'
        back_motor_direction = 'c'
        self.front_left.runner(motor_direction=front_motor_direction, speed=speed, angle=angle)
        self.front_right.runner(motor_direction=front_motor_direction, speed=speed, angle=angle)

        self.back_left.runner(motor_direction=back_motor_direction, speed=speed, angle=angle)
        self.back_right.runner(motor_direction=back_motor_direction, speed=speed, angle=angle)

    def switch_direction(self, current_direction):
        if current_direction == 'a':
            new_direction = 'c'
        else:
            new_direction = 'a'

        return new_direction

    def home_position(self, speed):
        current_front_left_angle = self.front_left.current_angle
        current_front_right_angle = self.front_right.current_angle
        current_back_left_angle = self.back_left.current_angle
        current_back_right_angle = self.back_right.current_angle

        if current_front_left_angle != 0:
            motor_direction = self.switch_direction(self.front_left.current_direction)
            self.front_left.runner(motor_direction=motor_direction, speed=speed, angle=current_front_left_angle)

        if current_front_right_angle != 0:
            motor_direction = self.switch_direction(self.front_right.current_direction)
            self.front_right.runner(motor_direction=motor_direction, speed=speed, angle=current_front_right_angle)

        if current_back_left_angle != 0:
            motor_direction = self.switch_direction(self.back_left.current_direction)
            self.back_left.runner(motor_direction=motor_direction, speed=speed, angle=current_back_left_angle)

        if current_back_right_angle != 0:
            motor_direction = self.switch_direction(self.back_right.current_direction)
            self.back_right.runner(motor_direction=motor_direction, speed=speed, angle=current_back_right_angle)
