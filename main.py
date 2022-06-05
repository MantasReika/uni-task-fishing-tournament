'''
Task for you:

There's a fishing tournament taking place in the city. In the tournament, there will be a total of (m) fishers. 
Each fisher has a name (fisher_name), and is one of the three categories (fisher_category) : newbie, amateur, professional.

After the tournament has concluded, each fisher announces the amount of fish he has caught No, the names of each fish (fish_name), 
and their respective weight (fish_weight).

The system must find the average weight of the fishes (fish_average_weight) for each of the fishermen, 
and also determine the biggest fish each fisherman has caught by weight (fish_biggest_weight).

Lastly the system must determine the winner by following this score formula: score = (fish_biggest_weight*0.3 + fish_average_weight*0.3 + n*0.3).

(Make input from .txt file to avoid having to input data each time)

*Determine what kind of fish was caught the most times (by name)
*Make a list of top 3 fishermen (by score)

'''

import enum
from typing import List
from unicodedata import category
import copy


class FisherCategory(enum.Enum):
    Newbie = 1
    Amateur = 2
    Professional = 3


class Fish():
    name: str
    weight: float

    def __init__(self, name: str, weight: int) -> None:
        self.name = name
        self.weight = weight


class Fisher():
    name: str
    category: FisherCategory
    caughtFish: List[Fish] = []

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
        print('======================')
        for i in len(self.caughtFish):
            print(
                f'{i + 1 }. {self.caughtFish[i].name} - {self.caughtFish[i].weight}kg.')
        print('======================\n')

    def _getWeights(self) -> List[float]:
        return [i.weight for i in self.caughtFish]


class FisherManagement():
    fishers: List[Fisher]

    def __init__(self) -> None:
        pass

    def registerFisher(self, name: str, category: str) -> Fisher:
        fisher = Fisher(name, FisherCategory[category])
        self.fishers.append(fisher)

    def findWinner(self) -> Fisher:
        return

    def findTopFishers(self) -> List[Fisher]:
        return

    def findMostFrequentFish(self) -> List[Fish]:
        return


class DataLoader():
    def __init__(self) -> None:
        pass

    def loadDataFile(self) -> List[Fisher]:
        with open('data.csv') as f:
            return self.parseData(f.readlines())

    def parseData(self, data: List[str]) -> List[Fisher]:
        fishers: List[Fisher] = []
        fisherCount = -1

        for row in data:
            rowItems = row.strip('\n').split('|')

            if (len(rowItems) != 3):
                # Incorrect amount of data
                continue

            if (rowItems[0] == 'FISHER'):
                fisherCount += 1
                fishers.append(self.createFisher(rowItems))
            elif (rowItems[0] == 'FISH'):
                fishers[fisherCount].addFish(self.createFish(rowItems))

        return fishers

    def createFisher(self, data: List[str]) -> Fisher:
        try:
            name = data[1]
            category = data[2]
        except:
            raise f'Error: Incorrect fish data: {data}'

        return Fisher(name, category)

    def createFish(self, data: List[str]) -> Fish:
        try:
            name = data[1]
            weight = float(data[2])
        except:
            raise f'Error: Incorrect fish data: {data}'
        return Fish(name, weight)


class Tournament(FisherManagement, DataLoader):

    def __init__(self) -> None:
        super()


def main() -> None:
    print('''
###############################
###### Fishing tournament #####
###############################
''')

    tournament = Tournament()
    t = tournament.loadDataFile()

    print('Done')


if __name__ == '__main__':
    main()
