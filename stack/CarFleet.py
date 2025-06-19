# https://neetcode.io/problems/car-fleet?list=neetcode150


from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort()
        timestack = [(target - car[0]) / car[1] for car in cars]
        fleet_count = 0
        curr_time = timestack.pop()
        while len(timestack):
            if timestack[-1] > curr_time:
                fleet_count += 1
                curr_time = timestack.pop()
            else:
                while len(timestack) and timestack[-1] <= curr_time:
                    timestack.pop()

        fleet_count += 1
        return fleet_count
