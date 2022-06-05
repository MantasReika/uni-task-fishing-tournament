
from typing import List
from fish import Fish

from fisher import Fisher
from fisherCategory import FisherCategory


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
