from robot_control_class import RobotControl

def main():
    # Create an instance of the RobotControl class
    robot = RobotControl()

    # Set a threshold distance for detecting obstacles (less than 1 meter)
    obstacle_threshold = 1.0

    # Start moving the robot forwards
    robot.move_straight()

    # Continuously capture and check laser readings
    while True:
        # Get the current laser readings
        laser_readings = robot.get_laser_full()

        # Check if an obstacle is closer than the threshold distance
        if min(laser_readings) < obstacle_threshold:
            # Stop the robot when an obstacle is detected
            robot.stop_robot()
            break

    # Turn 90 degrees to the right to face the opening corner
    robot.rotate(-90)

    # Clean up and exit
    robot.stop_robot()

if __name__ == "__main__":
    main()
