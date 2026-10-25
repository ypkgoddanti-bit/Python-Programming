#59.Campus Transport Allocation
students = int(input("Number of students: "))
capacity = int(input("Bus capacity: "))

buses = students // capacity

if students % capacity != 0:
    buses += 1

print("Required buses:", buses)
