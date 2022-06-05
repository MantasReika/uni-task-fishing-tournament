from typing import List
from fish import Fish
from fisherCategory import FisherCategory


class Fisher():
    name: str
    category: FisherCategory
    caughtFish: List[Fish]

    def __init__(self, name: str, category: FisherCategory) -> None:
        self.name = name
        self.category = category
        self.caughtFish = []

    def addFish(self, fish: Fish) -> None:
        self.caughtFish.append(fish)

    def getFishCount(self) -> int:
        return len(self.caughtFish)

    def getAverageWeight(self) -> float:
        count = self.getFishCount()
        if count < 1:
            return 0

        weights = self._getWeights()
        return sum(weights) / count

    def getMaxWeight(self) -> float:
        return max(self._getWeights())

    def getScore(self) -> float:
        # score = (fish_biggest_weight*0.3 + fish_average_weight*0.3 + n*0.3)
        return self.getMaxWeight() * 0.3 + self.getAverageWeight() * 0.3 + self.getFishCount() * 0.3

    def printStats(self) -> None:
        print(f'Fisher: {self.name} - {self.category.name}')
        print(f'Caught fish: {self.getFishCount()}')
        print(f'Average weight: {self.getAverageWeight():.2f}kg.')
        largestFish = self._getLargestFish()
        print(
            f'Largest fish: {largestFish.name} - {largestFish.weight:.2f}kg.')
        print(f'Score: {self.getScore():.2f}')
        print('======================')
        for i in range(self.getFishCount()):
            print(
                f'{i + 1 }. {self.caughtFish[i].name} - {self.caughtFish[i].weight:.2f}kg.')
        print('======================\n')

    def _getWeights(self) -> List[float]:
        return [i.weight for i in self.caughtFish]

    def _getLargestFish(self) -> Fish:
        idx = self._getWeights().index(self.getMaxWeight())
        return self.caughtFish[idx]
