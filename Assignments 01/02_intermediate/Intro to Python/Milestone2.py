# Milestone #2: Calculate weight on any planet
def planetary_weight():
    # Gravitational constants for each planet
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ")

    if planet in gravity_factors:
        equivalent_weight = round(earth_weight * gravity_factors[planet], 2)
        print(f"The equivalent weight on {planet}: {equivalent_weight}")
    else:
        print("Invalid planet. Please enter a valid planet name (e.g., Mars, Jupiter).")

# Run the planetary weight calculator
planetary_weight()
