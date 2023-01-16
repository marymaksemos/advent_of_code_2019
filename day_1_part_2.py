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
    
    
if __name__ == '__main__':
   masses=[]
   with open("input_day_1part_1.txt")as file:
        for line in file:
            masses.append(int(line.strip()))

            print(f"result : {total_fuel_required(masses)}")
