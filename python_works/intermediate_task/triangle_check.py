# the sum of two side lengths of a triangle is always greater than the third side

# Equilateral triangle. The Equilateral triangle shown on the left has three congruent sides and three congruent angles. Each angle is 60°.
# Isosceles triangle. The Isosceles triangle shown on the left has two equal sides and two equal angles.
# Scalene Triangle. The Scalene Triangle has no congruent sides. In other words, each side must have a different length.


side_1 = int(input("Enter the first side value")) 

side_2 = int(input("Enter the second side value"))

side_3 = int(input("Enter the third side value"))

if ((side_1+side_2)>side_3) or ((side_2+side_3)>side_1) or ((side_1+side_3)>side_2):

    if side_1 == side_2 == side_3:

        print("It is an  Equilateral triangle")

    elif side_1 != side_2 != side_3:

        print("It is an Scalene Triangle")

    elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:

        print("It is an Isosceles triangle")

else:
    
    print("Given value can't create a Triangle")