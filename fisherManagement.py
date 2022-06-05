
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

    def registerFish(self, fisherId: int, name: str, weight: float) -> None:
        try:
            self.fishers[fisherId].addFish(Fish(name, weight))
        except:
            print('Could not add a fish, check data and try again...')

    def findWinner(self) -> Fisher:
        return

    def findTopFishers(self) -> List[Fisher]:
        return

    def findMostFrequentFish(self) -> List[Fish]:
        return
