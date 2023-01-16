def fuel_required(mass) :
   
       return mass // 3 - 2

def total_fuel_required(masses) :
     return sum(fuel_required(mass) for mass in masses)


if __name__ == '__main__':
 masses=[]
 with open("input_day_1part_1.txt")as file:
        for line in file:
            masses.append(int(line.strip()))

 print(f"result : {total_fuel_required(masses)}")

