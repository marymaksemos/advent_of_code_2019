def fuel_required(mass) :
   
       return mass // 3 - 2

def total_fuel_required(masses) :
     return sum(fuel_required(mass) for mass in masses)
  