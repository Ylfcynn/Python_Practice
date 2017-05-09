"""
Voting Booth, rigged by Doby Finn, ne'er-do-well at large.

Goals: "Take in candidates names from a series of users, until someone types 'done'.
Then calculate the vote counts for each candidate and print them out."

Advanced goal: Implement ranked-choice voting logic that accepts multiple candidates (e.g. 3).

Confer: https://en.wikipedia.org/wiki/Ranked_voting

>>> candidates = ['Russ Boulware', 'JC', 'Doby Finn', 'Ross Grabow', 'Aaron Nelson', 'Shane Sweet', 'Tyler Van Loon']

>>> rigger()
Doby Finn is the winner!
"Look on my work, ye sheeple, and despair! Ha ha ha ha ha ha ha ha ha!"

"""

#candidates = ['Russ Boulware', 'JC', 'Doby Finn', 'Ross Grabow', 'Aaron Nelson', 'Shane Sweet', 'Tyler Van Loon']

ballot_box = dict()

def rigger(results):
    """
    Rigs the results, declares a victor. Ha!
    """



    victor = max(results.items(), key=lambda x: x[1])
    # victor = 'Doby Finn'
    hark = f'{victor} is the winner!\n\"Look on my work, ye sheeple, and despair! Ha ha ha ha ha ha ha ha ha!\"'
    print(hark)


def ballot_proc(ballot):
    """
    Appends ballots to a dictionary, tallies votes, and rigs the result.
    """

    ballot_box.update(ballot)
    tally_ho = list(ballot_box.values())
    results = dict()
    """
    Vote tally logic here
    """
    if 0 in tally_ho:
        results['Russ Boulware'] = tally_ho.count(0)

    if 1 in tally_ho:
        results['JC'] = tally_ho.count(1)

    if 2 in tally_ho:
        results['Doby Finn'] = tally_ho.count(2)

    if 3 in tally_ho:
        results['Ross Grabow'] = tally_ho.count(3)

    if 4 in tally_ho:
        results['Aaron Nelson'] = tally_ho.count(4)

    if 5 in tally_ho:
        results['Shane Sweet'] = tally_ho.count(5)

    if 6 in tally_ho:
        results['Tyler Van Loon'] = tally_ho.count(6)

    bool_herder(results)


def bool_herder(results):
    more_voters = input('Are there any more voters? (y/n) ')
    if more_voters == 'y':
        obseq_droid(candidates)

    elif more_voters == 'n':
        print('Thank you for using the Chernobog Industries PeoplePower 6000™.\n''Have a nice day.')
        rigger(results)

    else:
        print('Not a valid selection. Please enter \'y\' or \'n\'')
        bool_herder(results)


def obseq_droid(candidates):
    print('Greetings citizen! Welcome to the Chernobog Industries PeoplePower 6000™.\n'
          'Chernobog Industries prides itself on providing powerful and secure solutions for free elections.\n'
          'With our FreedomEngine™ technology, rest assured that your vote will be confidential and be\n'
          'counted accurately.\n'
          '\n'
          'Chernobog Industries - \"Putting the \'Mob\' into mob rule.\"\n')

    thugs = list(enumerate(candidates))

    for num, name in thugs:
        print(num, name, sep=' ==========>>>> ')    # artwork courtesy of Kieran

    user = input('Enter your name: ')
    vote = int(input(f'Welcome {user}. Insert the number of your selection here: '))

    if vote in range(len(thugs)):
        ballot = {user: vote}
        print(f'Your vote, {ballot}, has been recorded.\n')
        ballot_proc(ballot)

    else:
        print('Not a valid selection. Please enter a number within the permitted range.')
        bool_herder()


obseq_droid(candidates)