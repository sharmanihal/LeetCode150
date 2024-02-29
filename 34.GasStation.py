"""
Let's break down the provided solution step by step:

Part 1: Initial check for feasibility
The first part of the solution checks whether the total amount of gas available across all stations is sufficient to cover the total cost of the journey. If the sum of available gas is less than the sum of the costs, it implies that there isn't enough fuel to complete the circuit regardless of the starting point. In such cases, the function immediately returns -1, indicating that it's not possible to complete the journey.

Part 2: Determining the optimal starting point
As we iterate through the stations and update the total gas surplus/deficit, we keep track of the potential starting point (stored in the variable res).
Consider the scenario this way: if we run out of fuel at gas station n, then to reach gas station n, all preceding stations must have either added some fuel or none at all. This implies that if we started at any of these gas stations before n, upon reaching n again, we would encounter a fuel deficit once more. Therefore, it makes more sense to start at the next gas station after n.

Part 3: Conclusion and optimization
Once we've identified the optimal starting point, we return its index as the solution. Since the problem guarantees a unique solution if it exists, we don't need to continue traversing the circuit once we find the optimal starting point. This optimization ensures that the function terminates efficiently, making it run in linear time complexity (O(n)), as required by the problem constraints.

Summary:

    Part 1 ensures the feasibility of the journey based on fuel availability.
    Part 2 determines the optimal starting point by analyzing the gas surplus/deficit.
    Part 3 concludes the process and returns the solution index.
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        total=0
        res=0
        for i in range(len(gas)):
            total+= gas[i]-cost[i]
            if total<0:
                total=0
                res=i+1
        return res
