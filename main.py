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


from tournament import Tournament


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
