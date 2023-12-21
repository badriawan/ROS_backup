from robot_control_class import RobotControl

def get_highest_lowest():
    # Create an instance of the RobotControl class
    robot = RobotControl()

    # Get all the laser readings and store them in a list
    laser_readings = robot.get_laser_full()

    # Initialize variables to keep track of the highest and lowest values and their positions
    highest_value = None
    lowest_value = None
    highest_position = None
    lowest_position = None

    # Iterate through the laser readings
    for i, value in enumerate(laser_readings):
        # Ignore 'inf' values
        if value == float('inf'):
            continue

        # Check for the highest value
        if highest_value is None or value > highest_value:
            highest_value = value
            highest_position = i

        # Check for the lowest value
        if lowest_value is None or value < lowest_value:
            lowest_value = value
            lowest_position = i

    # Return the positions of the highest and lowest values
    return highest_position, lowest_position

# The following code is for testing the function
if __name__ == "__main__":
    highest, lowest = get_highest_lowest()
    print("Position of the highest value:", highest)
    print("Position of the lowest value:", lowest)
