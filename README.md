Python software program for an iterative search algorithm to find maxima and minima of analytically intractable functions- Car Fuel Consumption based on MPH 

My Real-World Physics & Use Case: Plug and Play in any scenario you find deemable. 

Car Fuel Consumption:
Lets Think: When you drive a car down the highway, fuel economy (MPG) does not form a straight line; it follows an inverted parabola with a distinct sweet spot (usually between 55 and 65 mph). The code simulates this behavior through three primary real-world constraints:

1. Too Slow (Below Lower Limit): If you crawl in heavy stop-and-go city traffic, your engine spends too much time running inefficiently in low gears on the transmission, resulting in high fuel consumption. The code applies a penalty multiplier (0.4) for every mph below the target band.

2. The Sweet Spot (Optimal Speed): At moderate cruising speeds (e.g., ~55–65 mph), the engine operates near its peak thermal and mechanical efficiency in top gear.

3. Too Fast (Above Upper Limit): Aerodynamic drag (wind resistance) increases with the square of your velocity, while the engine power required to punch through that air scales with the cube of your velocity. Example: If you push a 2007 Lexus IS 250 up to 75 or 80 mph, drag spikes dramatically. The code models this steeper penalty (0.5 per mph) because high-speed wind resistance tanks fuel economy.   

Sciencing
+ 1
Acceleration Penalties: Stomping on the gas pedal forces the engine to dump extra fuel into the cylinders to build kinetic energy rapidly. The code simulates this via acceleration_penalty = 1 + (acceleration * 0.3), which scales down your overall MPG.

How the Algorithm Solves It
Because real-world fuel curves can be analytically intractable (meaning you can't easily solve them with a simple high school algebra formula due to shifting gear ratios, drag coefficients, and engine maps), the script uses numerical optimization:

Gradient Descent (find_extrema with find_max=False): Steps through speeds incrementally to find the exact bottom of the fuel consumption curve—the optimal cruising speed where your fuel consumption is minimized (and your MPG is maximized).

Gradient Ascent / Boundary Checks: Scans the outer boundaries (e.g., bumper-to-bumper crawl vs. max highway speed) to find where efficiency collapses entirely (maximum fuel consumption).

By plugging in your vehicle parameters after running the code it will punch or spit out the value for you (base_mpg, optimal_speed, lower_limit, upper_limit), the algorithm numerically maps out the exact economic tipping points for that specific machine.
