# finding the latest time to catch a bus 

# buses = [10,20] -> departure time
# passengers = [2,17,18,19]  -> arrival time
# capacity = 2  -> capacity of the bus 

# you have to come there very late such that you catch the bus (latest -> most recent)

# my approach
# search first {capacity} smallest values in passengers
# run the first step for {buses} number of loops
# grab the time of the last passenger boarding
# result is last passengers time-1 (iff time-1 is not in passengers)

class Solution:

    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        buses.sort()
        passengers.sort()
        
        passenger_index = 0
        for bus in buses:
            count = 0
            while count < capacity and passenger_index < len(passengers) and passengers[passenger_index] < bus:
                passenger_index += 1
                count += 1
    
        latest_passenger = buses[-1] if passenger_index == 0 else passengers[passenger_index-1]
        
        while latest_passenger in passengers:
            if latest_passenger + 1 <= buses[-1] and latest_passenger + 1 not in passengers:
                latest_passenger += 1
                while latest_passenger < buses[-1] and latest_passenger not in passengers:
                    latest_passenger += 1
                return latest_passenger
            latest_passenger -= 1
        
        return latest_passenger

        
if __name__=="__main__":

    buses = [20,30,10]
    passengers = [19,13,26,4,25,11,21]
    # buses = [3]
    # passengers = [2,4]
    capacity = 2

    s = Solution()
    result = s.latestTimeCatchTheBus(buses, passengers, capacity)
    print(result)
