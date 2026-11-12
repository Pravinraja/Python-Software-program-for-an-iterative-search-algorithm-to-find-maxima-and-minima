#Wrote and implemented a software program in Python for an iterative search algorithm
# to find maxima and minima of analytically intractable functions

#Use Case by Pravin Raja

#1 implement an iterative search algorithm to find the speed at which a car achieves minimum and maximum fuel.
#2 consumption based on user-defined parameters like optimal speed, fuel efficiency limits, and acceleration penalties.
#3 It calculates the extrema (minima or maxima) by using gradient-based ascent or descent and stops (epsilon) when the change in fuel
#efficiency is smaller
#than a defined threshold.
#4 To calculate this program in the end, we need to input the
#car's details, including make, model, and year, to your personal car preference choices EX. 2007 Lexus IS 250.

import math
#Import Python Math Modules
#Ex: result = math.sqrt(16) would be 4

# Key Steps
# 1. Iterative Search:
#    - Uses a loop to gradually improve the solution by updating positions based on the slope (gradient) of the function.
#    - This is an optimization technique where the solution improves step by step.

# 2. Gradient Ascent/Descent:
#    - The gradient (or slope) at each step is used to determine the direction of movement.
#    - If we are finding a maximum (gradient ascent), we move in the direction where the slope is positive.
#    - If we are finding a minimum (gradient descent), we move in the direction where the slope is negative.

# 3. Epsilon Stopping Condition:
#    - The search continues until the change in function value between iterations is below a small threshold epsilon (ϵ).
#    - This ensures that the solution converges to an optimal or near-optimal value.
#    - The function stops if the value change becomes small enough (i.e., if the slope is close to zero or the improvement is negligible).
#    - Very Finite Differences (Small)

def approximate_slope(f, x, h):
    """
    Approximates the slope (derivative) of the function f at a given point x using finite differences.
    h is a small increment used to calculate the slope approximation.
    """
    return (f(x + h) - f(x)) / h  # Calculate the slope using finite differences

def find_extrema(f, x_start, step, h, epsilon, min_speed, max_speed, find_max=True):
    """
    Finds the extrema (maximum or minimum) of the function f starting from x_start.
    Uses iterative gradient ascent or descent to find the optimal point, ensuring convergence when
    the change in function value is smaller than epsilon.

    Parameters:
    - f: The function to minimize or maximize (fuel consumption in our case).
    - x_start: Starting point for the search (initial speed).
    - step: The step size used for adjusting the position based on the gradient.
    - h: A small increment used to approximate the slope of the function.
    - epsilon: A threshold for stopping the search when the change in function value is smaller than epsilon.
    - min_speed: Lower bound for the speed range (speed cannot go below this value).
    - max_speed: Upper bound for the speed range (speed cannot exceed this value).
    - find_max: Whether to find the maximum (True) or minimum (False) of the function.

    Returns:
    - The optimal speed where the fuel consumption is minimized or maximized.
    """
    x = x_start
    while True:
        slope = approximate_slope(f, x, h)  # Calculate the slope of the function at the current x

        # Gradient ascent/descent: Move towards the maximum (ascent) or minimum (descent)
        if find_max:
            x_new = x + step * slope  # Move in the direction of the maximum (ascent)
        else:
            x_new = x - step * slope  # Move in the direction of the minimum (descent)

        # Ensure that the new speed value stays within the specified bounds
        x_new = max(min_speed, min(x_new, max_speed))

        # Epsilon stopping condition: Stop if the change in the function value is below epsilon
        if abs(f(x_new) - f(x)) < epsilon or x_new == x:
            break  # Stop the search if the change is sufficiently small

        x = x_new

    return x_new

def fuel_consumption(speed, optimal_speed, lower_limit, upper_limit, base_mpg, acceleration=0):
    """
    Calculates the fuel consumption (MPG) based on the car's speed, acceleration, and other parameters.
    The function penalizes for speeds outside the optimal range and applies a penalty for acceleration.
    """
    if speed < lower_limit:
        mpg = base_mpg - (lower_limit - speed) * 0.4  # Penalty for speeds below the lower limit
    elif speed > upper_limit:
        mpg = base_mpg - (speed - upper_limit) * 0.5  # Penalty for speeds above the upper limit
    else:
        mpg = base_mpg - (abs(speed - optimal_speed) * 0.2)  # Penalty for deviation from optimal speed

    # Apply a penalty for acceleration (higher acceleration leads to lower MPG)
    acceleration_penalty = 1 + (acceleration * 0.3)
    mpg /= acceleration_penalty

    # Ensure that the fuel efficiency doesn't go below 12 MPG
    return max(mpg, 12)

def get_car_details():
    """
    input car's details, such as model year, make, and model.
    """
    print("Please enter the details of your car:")
    year = input("Enter the model year of your car: ")
    make = input("Enter the make of your car (e.g., Toyota, Ford): ")
    model = input("Enter the model of your car (e.g., Camry, Mustang): ")
    return year, make, model

if __name__ == "__main__":
    # enter their car's parameters
    print("Enter your car's Details:")
    optimal_speed = float(input("Optimal speed for fuel efficiency (mph): "))  # Optimal speed for good fuel efficiency
    lower_limit = float(input("Lower speed limit for good fuel efficiency (mph): "))  # Lower speed limit for good fuel efficiency
    upper_limit = float(input("Upper speed limit for good fuel efficiency (mph): "))  # Upper speed limit for good fuel efficiency
    base_mpg = float(input("Base fuel efficiency (mpg): "))  # Base fuel efficiency without any penalties

    # Get the car model details from the user
    year, make, model = get_car_details()
    print(f"Car details: Year: {year}, Make: {make}, Model: {model}")  # Display the car model details

    # Constants for optimization
    step = 0.1  # Step size for the iterative search
    h = 0.001  # Small increment for slope approximation
    epsilon = 0.0001  # Stopping condition threshold

    # Speed boundaries
    min_speed = lower_limit - 10  # Allow a buffer below the lower limit for exploration
    max_speed = upper_limit + 10  # Allow a buffer above the upper limit for exploration

    # Define the fuel consumption function to pass to the optimization method
    def user_defined_fuel_consumption(speed):
        return fuel_consumption(speed, optimal_speed, lower_limit, upper_limit, base_mpg)

    # Find the optimal speed for minimum fuel consumption (gradient descent)
    optimal_speed_result = find_extrema(user_defined_fuel_consumption, optimal_speed, step, h, epsilon, min_speed, max_speed, find_max=False)
    print(f"Optimal speed for maximum fuel efficiency (minimum fuel consumption) found at x = {optimal_speed_result:.2f} mph, "
          f"f(x) = {user_defined_fuel_consumption(optimal_speed_result):.2f} mpg")

    # Check for the speed that results in the maximum fuel consumption (gradient ascent)
    lower_extreme_mpg = user_defined_fuel_consumption(min_speed)  # Calculate the fuel consumption for the lower extreme
    upper_extreme_mpg = user_defined_fuel_consumption(max_speed)  # Calculate the fuel consumption for the upper extreme

    if lower_extreme_mpg < upper_extreme_mpg:
        max_consumption_speed = min_speed
        max_consumption_value = lower_extreme_mpg
    else:
        max_consumption_speed = max_speed
        max_consumption_value = upper_extreme_mpg

    print(f"Speed for minimum fuel efficiency (maximum fuel consumption) found at x = {max_consumption_speed:.2f} mph, "
          f"f(x) = {max_consumption_value:.2f} mpg")
