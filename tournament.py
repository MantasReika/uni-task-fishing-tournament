from fisherCategory import FisherCategory
from fisherManagement import FisherManagement
from dataLoader import DataLoader


class Tournament(FisherManagement, DataLoader):

    def __init__(self) -> None:
        super().__init__()

    def loadData(self) -> None:
        self.fishers = self.loadDataFile()

    def statistics(self) -> None:
        for fisher in self.fishers:
            fisher.printStats()

    def results(self) -> None:
        print('''\n\n
============================
--------  Results  ---------
============================
''')
        winner = self.findWinner()
        if (winner != None):
            print(
                f'Winner: {winner.name}({winner.category.name}) - {winner.getScore():.2f}')

        top = self.findTopFishers()
        print('Top fishers:')
        for i in range(len(top)):
            print(
                f'{i+1}. {top[i].name}({top[i].category.name}) - {top[i].getScore():.2f}')
        freq = self.findMostFrequentFish()
        print('')

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
