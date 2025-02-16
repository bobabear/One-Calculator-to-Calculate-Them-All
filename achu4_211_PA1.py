'''
---------------------------------------------------------------------------------
Name: Amanda Chu
Assignment: PA 1
Due Date: 09/11/2023
---------------------------------------------------------------------------------
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by professor and class syllabus.
---------------------------------------------------------------------------------
Comments and Assumptions: A note to the grader as to any problems or
uncompleted aspects of the assignment, as well as any assumptions.
You can write in N/A if you don’t have any comments/assumptions.
---------------------------------------------------------------------------------
NOTE: width of source code should be <=80 characters to be readable on-screen.
12345678901234567890123456789012345678901234567890123456789012345678901234567890
         1        2          3         4         5         6         7         8
---------------------------------------------------------------------------------
'''
#function to convert cm to mm
def cm_to_mm(cm_val):
    mm = cm_val * 10
    return mm
    

#START
print("One Calculator to Calculate Them All!\n")
#write code here
#asks the user for the diameter in cm and height in mm
#assign pi to 3.14
diameter = float(input("Diameter of a ring (in cm)? "))
height = float(input("Height of a ring (in mm)? "))
pi = 3.14
#called the function to convert the diameter from cm to mm
#equation for the total volume without the inner cutout removed
#display output in a full sentence
diameter = cm_to_mm(diameter)
full_volume = pi * (diameter/2)**2 * height
print("Volume of a ring without the inner cutout is: " + str(full_volume) + " mm^3")
#equation for the total volume with the inner cutout removed
#display output of the volume without the inner cutout in a full sentence
inner_cutout_diameter = float(input("Ratio of the inner cutout diameter (as a decimal)? "))
volume_of_inner_cutout = pi * ((0.5 * diameter * inner_cutout_diameter)**2 * height)
removed_inner_cutout = full_volume - volume_of_inner_cutout
print("Volume of the inner cutout is: " + str(round(volume_of_inner_cutout,2)) + " mm^3")
print("Volume of a ring with the inner cutout is: " + str(round(removed_inner_cutout,2)) + 
" mm^3\n")
#display title 
print("***Rings of Power***\n")
#asks the user for the number of rings, cost of material, and forging cost  
num_of_rings = int(input("Number of rings? "))
cost_of_material = int(input("Cost of the material (in cents per cubic inch)? "))
forging_cost = int(input("Forging cost (in cents per ring)? "))
#equation to calculate total material and displays output in a sentence
total_material = (full_volume - volume_of_inner_cutout) * num_of_rings 
print("Total material needed is: " + str(round(total_material,2)) + " mm^3")
#equation to calculate total material in inches
total_material_inches = total_material / (25.4**3)
#equation to calculate total number of cubes and displays output in a sentence
total_num_cubes = int(total_material_inches + 1) - int(int(total_material_inches + 1) - 
total_material_inches)
print("Total number of cubes to purchase is: " + str(total_num_cubes) + " cube(s)")
#equation to calculate total costs, forging cost, material cost, final dollar and cents
#displays output in a sentence
total_cost = forging_cost * total_num_cubes
forging_costs_all_rings = num_of_rings * forging_cost
material_cost_all_rings = cost_of_material * total_num_cubes
final_cost_cents = forging_costs_all_rings + material_cost_all_rings
final_dollar = final_cost_cents // 100
final_cents = final_cost_cents % 100
print("Cost for the Rings of Power is: " + str(final_dollar) + " dollar(s) and " + 
str(final_cents) + " cent(s)!\n")
#display title 
print("***The One Ring***\n")
#ask user for cost of material, equation to calculate the total material
#convert the total materials to inches
cost_of_material = int(input("Cost of the material (in cents per cubic inch)? "))
total_material = (full_volume - volume_of_inner_cutout)
total_material_inches = total_material / (25.4**3)
#equation to calculate the total number of cubes and display the output in a sentence
total_num_cubes = int(total_material_inches + 1) - int(int(total_material_inches + 1) - 
total_material_inches)
print("Number of cubes to purchase is: " + str(total_num_cubes) + " " + "cube(s)")
#equation to calculate the total cost, separating dollars from cents
#display the output in a sentence
total_cost = 3 * forging_cost + cost_of_material*total_num_cubes
dollars = int(total_cost // 100)
cents = int(total_cost % 100)
print("Cost for the One Ring is: " + str(dollars) + " dollar(s)" + " and " + str(cents) + 
" cent(s)!\n")
#display title 
print("This Shall Not Fail!")