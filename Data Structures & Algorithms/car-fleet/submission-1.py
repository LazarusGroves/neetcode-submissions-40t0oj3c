class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_cars = sorted(zip(position, speed))
        fleets = 0
        turns = 0
        while len(sorted_cars) > 0:
            car = sorted_cars.pop()
            # target < position + turns(speed)
            turns_needed = (target - car[0])/car[1]
            if turns_needed > turns:
                turns = turns_needed
                fleets += 1
            
        return fleets

