# Milestone #1: Calculate Mars weight
def mars_weight():
    earth_weight = float(input("Enter a weight on Earth: "))
    mars_weight = round(earth_weight * 0.378, 2)  # 37.8% of Earth weight
    print(f"The equivalent on Mars: {mars_weight}")

# Run the Mars weight calculator
mars_weight()
