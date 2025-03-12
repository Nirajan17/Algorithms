# latest time to catch a bus

# buses = [10,20], passengers = [2,17,18,19], capacity = 2

def latestTimeCatchBus(buses, passengers, capacity):
    buses.sort()
    passengers.sort()

    passenger_idx = 0
    bus_idx = 0

    # simulation of passenger boarding bus
    while bus_idx < len(buses) and passenger_idx < len(passengers):
        current_capacity = 0
        while passengers[passenger_idx]<=buses[bus_idx] and current_capacity<capacity and passenger_idx<len(passengers):
            passenger_idx += 1
            current_capacity += 1
        bus_idx += 1

    # now let's calculate the latest time
    if passenger_idx<len(passengers):   # not all boarded
        if current_capacity == capacity and passenger_idx>=0:  # there is no space in last bus
            last_boarded = passengers[passenger_idx]
            time = last_boarded-1
            while time in passengers and time >= 0:
                time -= 1
            return time if time >= 0 else -1   # if valid time is not found, return -1
    
        else:   # there is space in bus so arrive unit time before the bus leaves
            time = buses[bus_idx-1]
            while time in passengers and time>=0:
                time -= 1
            return time if time>=0 else -1 
    # all boarded
    else:
        if passenger_idx <= (len(buses) * capacity):
            time = buses[-1]
            while time in passengers and time >= 0:
                time -= 1
            return time if time >= 0 else -1
    return buses[-1]

print(latestTimeCatchBus([10, 20], [2, 17, 18, 19], 2))