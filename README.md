# Car Fuel Optimization Search Algorithm

A Python software program that implements an **iterative numerical optimization search algorithm** (gradient ascent/descent) to find the optimal cruising speed for maximizing vehicle fuel efficiency (MPG) and identifying efficiency extremes.

---

## Real-World Physics & Use Case

When driving a car, fuel economy does not follow a linear path—it forms an **inverted parabola** with a distinct "sweet spot" (typically between 55 and 65 mph). This script models real-world driving constraints:

Term to know: Drag coefficient: measures an object's resistance to moving through a fluid- in this case the fuel in the car
1. **Stop-and-Go Traffic (Too Slow):** Operating below the efficient lower speed limit keeps the engine in inefficient low transmission gears, increasing fuel consumption (modeled with a `0.4` penalty per mph).
2. **The Sweet Spot (Optimal Speed):** Moderate cruising speeds (e.g., ~55–65 mph) allow the engine to operate near peak thermal and mechanical efficiency in top gear.
3. **Aerodynamic Drag (Too Fast):** Wind resistance increases with the square of velocity, and power requirements scale with the cube of velocity. Pushing past the upper speed limit spikes drag dramatically (modeled with a steeper `0.5` penalty per mph).
4. **Acceleration Penalties:** Rapid acceleration forces the engine to dump extra fuel into the cylinders (`acceleration_penalty = 1 + (acceleration * 0.3)`), scaling down overall MPG.

---

## How the Algorithm Solves It

Because real-world fuel curves are analytically intractable (meaning they cannot be solved with simple high school algebra due to shifting gear ratios and drag coefficients), the script uses **numerical optimization**:
* **Finite Differences (`approximate_slope`):** Calculates the local slope/derivative of the fuel consumption curve at any given speed.
* **Gradient Ascent/Descent (`find_extrema`):** Iteratively steps through speeds to locate the exact peak efficiency point.
* **Epsilon Stopping Condition (`epsilon`):** Halts the loop when further iterations yield negligible functional improvements ($< \epsilon$).

Note: Without epsilon, the algorithm would take an infinite number of steps trying to reach the exact dead center of the peak
---

## Code Structure

- `approximate_slope()`: Estimates the derivative of the performance function using small finite differences ($h$).
- `find_extrema()`: Core optimization loop implementing step-by-step gradient movement and bounding.
- `fuel_consumption()`: Simulates real-world MPG penalties based on speed limits, drag, and acceleration.

---

## Getting Started

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/car-fuel-optimizer.git](https://github.com/your-username/car-fuel-optimizer.git)
   cd car-fuel-optimizer
