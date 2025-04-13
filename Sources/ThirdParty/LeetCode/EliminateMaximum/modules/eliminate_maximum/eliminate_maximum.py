from typing import List
from math import ceil


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        arrivals = sorted([(dist[i] / speed[i]) for i in range(n)])
        ans = 0
        for i in range(n):
            if arrivals[i] <= i:
                break

            ans += 1

        return ans


class MemorySolution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        time = [dist[i] / speed[i] for i in range(n)]
        time.sort()
        for i in range(n):
            if time[i] <= i:
                return i
        return n


class FastestSolution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        monsters = [0] * n

        for d, s in zip(dist, speed):
            arrival = ceil(d / s)

            if arrival < n:
                monsters[arrival] += 1

        killed = 0
        for i in range(len(monsters)):
            if killed + monsters[i] > i:
                return i
            killed += monsters[i]

        return n


class GptSolution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # Calculate arrival times as integers using ceiling to avoid float precision issues
        arrival_times = sorted(ceil(d / s) for d, s in zip(dist, speed))

        for minute, arrival in enumerate(arrival_times):
            if arrival <= minute:
                return minute  # A monster reaches the city before we can eliminate it

        return len(dist)  # All monsters can be eliminated in time
