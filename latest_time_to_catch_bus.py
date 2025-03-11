# latest time to catch a bus

# buses = [10,20], passengers = [2,17,18,19], capacity = 2

def latestTimeCatchBus(buses, passengers, capacity):
    buses.sort()
    passengers.sort()
    passengers_copy = passengers.copy()

    for bus in buses:
        for passenger in passengers:
            if passenger < bus and passenger in passengers_copy:
                for _ in range(capacity):
                    current_passenger = passengers_copy.remove(passenger)
            
    # here we have current passenger in current_passenger variable, now we need to check both ways whether there is a time that we can reach to catch the bus

    if buses[-1] > current_passenger:
        while current_passenger+1 not in passengers:
            current_passenger += 1
        return current_passenger
    else:
        while current_passenger-1 not in passengers:
            current_passenger -= 1
        return current_passenger

buses = [10,20]
passengers = [2,17,18,19]
capacity = 2
print(latestTimeCatchBus(buses, passengers, capacity))