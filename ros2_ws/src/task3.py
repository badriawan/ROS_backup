from robot_control_class import RobotControl


class ExamControl:
    def __init__(self):
        self.robot = RobotControl()
    def get_laser_readings(self):
        # Simulate the laser readings (replace this with actual robot code)
        left_reading = self.robot.get_laser(719)
        right_reading = self.robot.get_laser(0)
        return left_reading, right_reading

    def main(self):
        # Start moving forward
        print("Robot is moving forward...")
        self.robot.move_straight()
        # Continuously check laser readings while moving forward
        while True:
            left_reading, right_reading = self.get_laser_readings()
            print("left",left_reading)
            print("right",right_reading)

            # If there are no obstacles detected at the left or right side, stop the robot
            if left_reading > 10 and right_reading > 10:
                print("No obstacles detected on the left or right. Stopping the robot.")
                self.robot.stop_robot()
                break

if __name__ == "__main__":
    # Test the ExamControl class
    control = ExamControl()
    control.main()
