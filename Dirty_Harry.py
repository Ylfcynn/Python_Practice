"""
PLaying with the random library and text formatting.
"""

import random


def run():
    prompt = '''
             Uh uh. I know what you\'re thinking. "Did he fire six shots or only five?" Well to tell you the truth in 
             all this excitement I kinda lost track myself. But being this is a .44 Magnum, the most powerful handgun 
             in the world and would blow your head clean off, you\'ve gotta ask yourself one question: "Do I feel lucky?" 
             Well, do ya, punk? 
             
             '''

    answer = input(prompt)

    affirmative = ['yes', 'Yes', 'yeah', 'Yeah', 'yea', 'Yea', 'uh huh', 'uh huh']

    if answer in affirmative:
        spin = (random.randrange(1, 6,))
        if spin in range(1, 5):
            print('<click>')

        else:
            print('<bang>')

    else:
        print('<bang>')

run()