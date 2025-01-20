from math import sqrt, atan2, pi, degrees, isnan
from controller import Robot, GPS, Motor, InertialUnit
import time

# Constants
FRONT_WHEEL_RADIUS = 0.38
REAR_WHEEL_RADIUS = 0.6
STOP_THRESHOLD = 0.5  # Distance threshold for stopping
ANGLE_THRESHOLD = 0.005  # Precise threshold for alignment
MAX_SPEED = 10.0
STEERING_GAIN = 0.5
PAUSE_DURATION = 5  # Pause duration at each target in seconds
LIDAR_MIN_DISTANCE = 0.01  # Minimum range for obstacle detection
LIDAR_MAX_DISTANCE = 5.0  # Maximum range for obstacle detection
OBSTACLE_AVOID_SPEED = 1.0  # Speed while avoiding obstacles
OBSTACLE_TURN_ANGLE = 0.94  # Fixed steering angle to avoid obstacles

# Initialize robot and devices
robot = Robot()
time_step = int(robot.getBasicTimeStep())
gps = robot.getDevice("gps")
gps.enable(time_step)
imu = robot.getDevice("inertial unit")
imu.enable(time_step)
lidar = robot.getDevice("lidar")
lidar1 = robot.getDevice("lidar1")

lidar.enable(time_step)
lidar1.enable(time_step)

lidar1.enablePointCloud()
lidar.enablePointCloud()

#final point decider
def get_valid_gps_coordinates():
    coords = gps.getValues()
    # Check if GPS coordinates are valid (not NaN)
    while any(isnan(c) for c in coords):
        robot.step(time_step)  # Wait for the next simulation step
        coords = gps.getValues()
    return coords

# Define target points
final_point = get_valid_gps_coordinates()
# print(final_point(0), final_point(0))
targets = [(80.0, -10.0), (100.0, -80.0), (70.0, -120.0), (final_point[0],final_point[1])]
current_target_index = 0

left_front_wheel = robot.getDevice("left_front_wheel")
right_front_wheel = robot.getDevice("right_front_wheel")
left_rear_wheel = robot.getDevice("left_rear_wheel")
right_rear_wheel = robot.getDevice("right_rear_wheel")
left_steer = robot.getDevice("left_steer")
right_steer = robot.getDevice("right_steer")

# Set wheels to rotate freely
left_front_wheel.setPosition(float('inf'))
right_front_wheel.setPosition(float('inf'))
left_rear_wheel.setPosition(float('inf'))
right_rear_wheel.setPosition(float('inf'))

# Function to set speed of the tractor
def set_speed(kmh):
    if kmh > MAX_SPEED:
        kmh = MAX_SPEED
    front_ang_vel = kmh * 1000.0 / 3600.0 / FRONT_WHEEL_RADIUS
    rear_ang_vel = kmh * 1000.0 / 3600.0 / REAR_WHEEL_RADIUS
    
    left_front_wheel.setVelocity(front_ang_vel)
    right_front_wheel.setVelocity(front_ang_vel)
    left_rear_wheel.setVelocity(rear_ang_vel)
    right_rear_wheel.setVelocity(rear_ang_vel)

# Function to set steering angle
def set_steering_angle(angle):
    min_steer_angle = -0.94
    max_steer_angle = 0.94
    steer_angle = max(min_steer_angle, min(angle, max_steer_angle))
    
    left_steer.setPosition(steer_angle)
    right_steer.setPosition(steer_angle)

# Normalizes angle to the range [-pi, pi]
def normalize_angle(angle):
    while angle > pi:
        angle -= 2 * pi
    while angle < -pi:
        angle += 2 * pi
    return angle

# Function to move tractor towards the target coordinates
def go_to_target(x, y):
    coords = gps.getValues()
    current_x = coords[0]
    current_y = coords[1]
    distance = sqrt((x - current_x)**2 + (y - current_y)**2)

    target_angle = atan2(y - current_y, x - current_x)
    current_yaw = imu.getRollPitchYaw()[2]
    
    # Calculate normalized angle difference
    angle_diff = normalize_angle(target_angle - current_yaw)
    
    # Adjust steering angle to always turn towards reducing `angle_diff`
    if distance <= STOP_THRESHOLD:
        set_speed(0.0)  # Stop the tractor when close to the target
        return 1  # Indicates arrival
    elif abs(angle_diff) > ANGLE_THRESHOLD:
        steering_angle = angle_diff * STEERING_GAIN
        set_steering_angle(-steering_angle)
        set_speed(5)  # Slow speed while aligning
    else:
        # Proceed straight towards target
        set_steering_angle(0)
        set_speed(MAX_SPEED)
    return 0

# Function to check for obstacles and avoid them
def avoid_obstacles():
    lidar_data_right = lidar.getRangeImage()  # Get range data from right lidar
    lidar_data_left = lidar1.getRangeImage()  # Get range data from left lidar

    # Check for obstacles within the specified range for both sensors
    right_obstacle = any(LIDAR_MIN_DISTANCE <= dist <= LIDAR_MAX_DISTANCE for dist in lidar_data_right)
    left_obstacle = any(LIDAR_MIN_DISTANCE <= dist <= LIDAR_MAX_DISTANCE for dist in lidar_data_left)

    if right_obstacle and left_obstacle:
        # Both sensors detect obstacles, turn right by default
        set_steering_angle(-OBSTACLE_TURN_ANGLE)  # Turn right
        set_speed(OBSTACLE_AVOID_SPEED)
        return True
    else:
        if right_obstacle:
            # Right sensor detects obstacle, turn left
            set_steering_angle(-OBSTACLE_TURN_ANGLE)  # Turn left
            set_speed(OBSTACLE_AVOID_SPEED)
            return True
        elif left_obstacle:
            # Left sensor detects obstacle, turn right
            set_steering_angle(OBSTACLE_TURN_ANGLE)  # Turn right
            set_speed(OBSTACLE_AVOID_SPEED)
            return True

    return False


# Main loop
while robot.step(time_step) != -1:
    # Check for obstacles
    if avoid_obstacles():
        continue  # Skip target navigation if avoiding an obstacle

    # Get current target
    target_x, target_y = targets[current_target_index]
    
    # Navigate to target
    if go_to_target(target_x, target_y) == 1:
        print(f"Arrived at target {current_target_index + 1} (x={target_x:.2f}, y={target_y:.2f})")
        time.sleep(PAUSE_DURATION)  # Pause for 5 seconds
        
        # Move to the next target if available
        current_target_index += 1
        if current_target_index >= len(targets):
            print("All targets reached.")
            break
