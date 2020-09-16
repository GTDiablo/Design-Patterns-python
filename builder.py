class RobotHead:
    def __init__(self, *args, **kwargs):
        self.is_up = False

    def look_up(self) -> None:
        print('Looking up')
        self.is_up = True

class RobotArm:
    def __init__(self, *args, **kwargs):
        self.is_up = False

    def up(self) -> None:
        print('Raising arm')
        self.is_up = True

    def down(self) -> None:
        self.is_up = False

class Robot:
    def __inti__(self, *args, **kwargs):
        self.head = None
        self.left_arm = None
        self.right_arm = None

    def set_head(self, head: RobotHead) -> None:
        self.head = head

    def set_right_arm(self, arm: RobotArm) -> None:
        self.right_arm = arm

    def set_left_arm(self, arm: RobotArm) -> None:
        self.left_arm = arm


if __name__ == '__main__':
    class MyRobot(Robot):
        def __init__(self, name):
            super().__init__()
            self.name = name
            print(f'Robot named "{name}" is booting...')

        def prase_the_sun(self):
            if all([self.left_arm, self.right_arm, self.head]):
                print('PRASE THE SUN!')
                self.left_arm.up()
                self.right_arm.up()
                self.head.look_up()

    
    robot = MyRobot('T-5000')
    
    head = RobotHead()
    left_arm = RobotArm()
    right_arm = RobotArm()

    robot.set_head(head)
    robot.set_left_arm(left_arm)
    robot.set_right_arm(right_arm)

    robot.prase_the_sun()
