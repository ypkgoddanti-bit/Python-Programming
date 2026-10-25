#51.Bus Passenger Occupancy Simulation
passengers = 0

for stop in range(3):
    board = int(input("Passengers boarding: "))
    leave = int(input("Passengers leaving: "))

    passengers += board - leave
    print("Passengers:", passengers)
