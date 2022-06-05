
from typing import List
from fish import Fish

from fisher import Fisher
from fisherCategory import FisherCategory


class FisherManagement():
    fishers: List[Fisher]

    def __init__(self) -> None:
        self.fishers = []
        pass

    def registerFisher(self, name: str, category: str) -> None:
        fisher = Fisher(name, FisherCategory[category])
        self.fishers.append(fisher)
        print('Fisher registered!\n')

    def registerFish(self, fisherId: int, name: str, weight: float) -> None:
        try:
            self.fishers[fisherId].addFish(Fish(name, weight))
        except:
            print('Could not add a fish, check data and try again...')
            return
        print('Fish added!\n')

    def findWinner(self) -> Fisher:
        return max(self.fishers, key=lambda x: x.getScore())

    def findTopFishers(self) -> List[Fisher]:
        return sorted(self.fishers, key=lambda x: x.getScore(), reverse=True)

    def findMostFrequentFish(self) -> str:
        fishes = sorted([
            fish.name for fisher in self.fishers for fish in fisher.caughtFish])
        return max(set(fishes), key=fishes.count)
