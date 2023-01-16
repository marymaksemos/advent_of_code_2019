def fuel_required(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + fuel_required(fuel)
