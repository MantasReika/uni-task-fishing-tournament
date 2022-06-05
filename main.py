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


class FisherCategory(enum.Enum):
    Newbie = 1
    Amateur = 2
    Professional = 3

    def getCategories() -> List[str]:
        return [e.name for e in FisherCategory]


class Fish():
    name: str
    weight: float

    def __init__(self, name: str, weight: int) -> None:
        self.name = name
        self.weight = weight


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
        print('======================')
        for i in range(len(self.caughtFish)):
            print(
                f'{i + 1 }. {self.caughtFish[i].name} - {self.caughtFish[i].weight}kg.')
        print('======================\n')

    def _getWeights(self) -> List[float]:
        return [i.weight for i in self.caughtFish]


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
            category = FisherCategory[data[2]]
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
        super().__init__()

    def loadData(self) -> None:
        self.fishers = self.loadDataFile()

    def statistics(self) -> None:
        for fisher in self.fishers:
            fisher.printStats()

    def results(self) -> None:
        for fisher in self.fishers:
            pass

    def start(self) -> None:
        while (True):
            self.menu()

    def menu(self) -> None:
        MENU_OPTIONS = ['Add participant',
                        'Enter fish data',
                        'Print statistics',
                        'Print results']

        print('Select option:')
        formattedOptions = [
            f'{i+1}. {MENU_OPTIONS[i]}' for i in range(len(MENU_OPTIONS))]
        print('\n'.join(formattedOptions))

        try:
            option = int(input(':> '))
        except:
            print('Please enter a number...')
            return

        if (option == 1):
            name = input('Enter name: ')

            print('Available categories:')
            allCategories = FisherCategory.getCategories()
            print(
                '\n'.join([f'{i+1}. {allCategories[i]}' for i in range(len(allCategories))]))
            try:
                categoryId = int(input('Enter category: '))
                if (categoryId < 1 or categoryId > len(allCategories)):
                    raise ''
            except:
                print('Incorrect data entered, please try again...')
                return

            self.registerFisher(name, allCategories[categoryId - 1])

        elif (option == 2):
            print('Available fishers:')
            print(
                '\n'.join([f'{i+1}. {self.fishers[i].name}' for i in range(len(self.fishers))]))
            try:
                fisherId = int(input('Enter fishers number: '))
                if (fisherId < 1 or fisherId > len(self.fishers)):
                    raise ''
            except:
                print('Incorrect data entered, please try again...')
                return

            name = input('Enter fish name: ')
            weight = input('Enter fish weight: ')
            self.registerFish(fisherId - 1, name, weight)
            pass
        elif (option == 3):
            self.statistics()

        elif (option == 4):
            self.results()
        else:
            pass


def main() -> None:
    print('''
###############################
###### Fishing tournament #####
###############################
''')

    tournament = Tournament()
    tournament.loadData()
    tournament.start()

    print('Done')


if __name__ == '__main__':
    main()
