class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.ratings = {}
        self.cuisines = {}
        for i in range(len(foods)):
            self.ratings[foods[i]] = ratings[i]
            self.cuisines[foods[i]] = cuisines[i]

        # max heap per cuisine
        self.max_ratings = {}
        for i in range(len(cuisines)):
            if cuisines[i] not in self.max_ratings:
                self.max_ratings[cuisines[i]] = []
            heappush(self.max_ratings[cuisines[i]], (-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        self.ratings[food] = newRating

        # update max heap
        cuisine = self.cuisines[food]
        heappush(self.max_ratings[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        max_rating, food = self.max_ratings[cuisine][0]

        # ignore stale ratings
        while -max_rating != self.ratings[food]:
            heappop(self.max_ratings[cuisine])
            max_rating, food = self.max_ratings[cuisine][0]

        return food

"""
initial thoughts:
- modify a value efficiently -> hashmap
- access max item efficiently -> heap


"""

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)