class UndergroundSystem:

    def __init__(self):
        self.customerLocations = {}
        self.averageTimes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customerLocations[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, tStart = self.customerLocations[id]
        travelTime = t - tStart

        # update average time from startStation to endStation
        trip = (startStation, stationName)
        if trip not in self.averageTimes:
            self.averageTimes[trip] = [1, travelTime]
        else:
            n, avgTime = self.averageTimes[trip]
            self.averageTimes[trip] = [n + 1, ((n * avgTime) + travelTime) / (n + 1)]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.averageTimes[(startStation, endStation)][1]

"""
initial thoughts:
- track customers (what station they are at)
- when checking out, update average time between stations
- rather than recalculating entire average everytime, use a rolling average
    - track number of data points and current average
    - update average by doing ((n * avg) + new_val) / (n + 1)

data structures:
- map of customers to location and time
- map of location pairs to number of trips and average time 
"""

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)