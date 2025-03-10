# finding the latest time to catch a bus 

# buses = [10,20] -> departure time
# passengers = [2,17,18,19]  -> arrival time
# capacity = 2  -> capacity of the bus 

# you have to come there very late such that you catch the bus (latest -> most recent)

# my approach
# search first {capacity} smallest values in passengers
# run the first step for {buses} number of loops
# grab the time of the last passenger boarding
# result is last passengers time-1 (iff time-1 is not in passengers), here is a problem though what if time+1 is also available for boarding???

# this is the solution provided by grok

class Solution:
    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        # Sort both arrays
        buses.sort()  # Bus departure times
        passengers.sort()  # Passenger arrival times
        
        # Convert passengers to set for O(1) lookup
        passengers_set = set(passengers)
        p_idx = 0  # Passenger index
        n = len(passengers)
        
        # Simulate boarding for each bus
        for bus in buses:
            curr_capacity = 0
            # Board passengers until capacity or no more passengers before bus time
            while (curr_capacity < capacity and 
                   p_idx < n and 
                   passengers[p_idx] <= bus):
                curr_capacity += 1
                p_idx += 1
        
        # After simulation, determine the latest possible time
        # If no passengers or last bus wasn't full
        if p_idx == 0 or curr_capacity < capacity:
            latest = buses[-1]  # Can arrive at last bus departure time
        else:
            latest = passengers[p_idx - 1]  # Last boarded passenger's time
        
        # Find the latest possible time before or at last bus departure
        while latest in passengers_set or latest > buses[-1]:
            latest -= 1
            
        return latest

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([10, 20], [2, 17, 18, 19], 2),    # Your original example
        ([3], [2, 4], 2),                  # Your test case
        ([20, 30, 10], [19, 13, 26, 4, 25, 11, 21], 2)  # Additional test case
    ]
    
    s = Solution()
    for buses, passengers, capacity in test_cases:
        result = s.latestTimeCatchTheBus(buses.copy(), passengers.copy(), capacity)
        print(f"Buses: {buses}, Passengers: {passengers}, Capacity: {capacity}")
        print(f"Result: {result}\n")