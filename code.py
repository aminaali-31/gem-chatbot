"""
To calculate the distance of an airplane from the ground (altitude), the most common method is 
using trigonometry based on the **angle of elevation** and the **horizontal distance** from an 
observer.
Here is a clean, easy-to-understand Python program to solve this.
"""
import math

def calculate_airplane_altitude():
    """
    Calculates the altitude of an airplane using the horizontal distance 
    from an observer and the angle of elevation.
    """
    print("--- Airplane Altitude Calculator ---")

    try:
        # Step 1: Get user input for horizontal distance
        horizontal_dist = float(input("Enter the horizontal distance from you to the plane (in meters/feet): "))

        # Step 2: Get user input for the angle of elevation
        angle_elevation = float(input("Enter the angle of elevation from the ground (in degrees): "))

        # Step 3: Convert the angle from degrees to radians 
        # (The math.tan function requires radians)
        angle_radians = math.radians(angle_elevation)

        # Step 4: Calculate the altitude (Height)
        # Formula: Height = Horizontal Distance * tan(Angle)
        altitude = horizontal_dist * math.tan(angle_radians)

        # Step 5: Display the result
        if altitude < 0:
            print("\nError: The calculated altitude is negative. Please check your inputs.")
        else:
            print(f"\nResult: The airplane is approximately {altitude:.2f} units above the ground.")

    except ValueError:
        print("\nInvalid input. Please enter numeric values for distance and angle.")

if __name__ == "__main__":
    calculate_airplane_altitude()


""" How the logic works:
1.  **Inputs**: We take the **horizontal distance** (the distance from you to the point directly under the plane) and the **angle of elevation** (the angle at which you are looking up at the plane).
2.  **Trigonometry**: In a right-angled triangle, the Tangent of an angle ($\tan \theta$) is the ratio of the Opposite side (Altitude) to the Adjacent side (Horizontal Distance).
    *   $\tan(\text{angle}) = \frac{\text{Altitude}}{\text{Horizontal Distance}}$
3.  **Conversion**: Since Python's `math.tan()` function expects the angle in **radians**, we use `math.radians()` to convert the user's input from degrees.
4.  **Formatting**: The result is rounded to 2 decimal places using `:.2f` for better readability."""