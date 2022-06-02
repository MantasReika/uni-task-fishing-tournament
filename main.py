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
    name:str
    category: FisherCategory
    caughtFish: List[Fish]

    def __init__(self, name: str, category: FisherCategory) -> None:
        self.name = name
        self.category = category
    
    def getFishCount(self)->int:
        return len(self.caughtFish)

    def getAverageWeight(self)->float:
        count = self.getFishCount()
        if count < 1:
            return 0

        weights = self._getWeights()
        return sum(weights) / count

    def getMaxWeight(self)->float:
        return max(self._getWeights())

    def getScore(self)->float:
        # score = (fish_biggest_weight*0.3 + fish_average_weight*0.3 + n*0.3)
        return self.getMaxWeight() * 0.3 + self.getAverageWeight() * 0.3 + self.getFishCount() * 0.3

    def printStats(self)->None:
        print(f'Fisher: {self.name} - {self.category.name}')
        print(f'Caught fish: {self.getFishCount()}')
        print('======================')
        for i in len(self.caughtFish):
            print(f'{i + 1 }. {self.caughtFish[i].name} - {self.caughtFish[i].weight}kg.')
        print('======================\n')

    def _getWeights(self)->List[float]:
        return [i.weight for i in self.caughtFish]

class FisherManagement():
    fishers: List[Fisher]

    def __init__(self) -> None:
        pass

    def registerFisher(self, name: str, category: str)->Fisher:
        fisher = Fisher(name, FisherCategory[category])
        self.fishers.append(fisher)

    def findWinner(self)->Fisher:
        return

    def findTopFishers(self)->List[Fisher]:
        return

    def findMostFrequentFish(self)->List[Fish]:
        return

class DataLoader():
    def __init__(self) -> None:
        pass

    def loadDataFile(self) -> List[Fisher]:
        with open('data.csv') as f:
            return self.parseData(f.readlines())

    def parseData(self, data: List[str])->List[Fisher]:
        fisher: Fisher = None
        fishers: List[Fisher] = []
        fish: Fish = None

        for row in data:
            rowItems = row.split('|')
            if (len(rowItems) == 0 and fisher != None):
                fishers.append(fisher)
                fisher = None
                continue

            if (len(rowItems) != 3):
                # Incorrect amount of data
                continue

            if (rowItems[0] == 'FISHER'):
                fisher = self.createFisher(rowItems)
            elif (rowItems[0] == 'FISH'):
                if (fisher == None):
                    return
                fish = self.createFish(rowItems)
                fisher.caughtFish.append(fish)
 
        return fishers
    
    def createFisher(self, data: List[str])->Fisher:
        pass

    def createFish(self, data: List[str])->Fish:
        pass


class Tournament(FisherManagement, DataLoader):
    
    def __init__(self) -> None:
        super()




def main() -> None:
    print('''
###############################
###### Fishing tournament #####
###############################
''')
    # fisher = Fisher('Artur', FisherCategory.Amateur)
    # print(f'fisher.category: ', fisher.category)
    data = DataLoader().loadDataFile()
    print('Done')

if __name__ == '__main__':
    main()