def fuel_required(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + fuel_required(fuel)
        
def total_fuel_required(masses):
    total_fuel = 0
    for mass in masses:
        total_fuel += fuel_required(mass)
    return total_fuel