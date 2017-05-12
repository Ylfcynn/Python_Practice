"""
ARI Calculator, or: How I Learned to Stop Writing Monolithic Scripts and Distribute Logic Across Multiple Files,
by Doby Finn.

Output will look like this:
--------------------------------------------------------

The ARI for the file gettysburg-address.txt is 12.
This corresponds to a 11th Grade level of difficulty,
which is suitable for an average Anglophone 16 to 17 years of age.

--------------------------------------------------------
"""

import os
import re

CODEX_ROOT = '/Users/ylf/Git/Python_Practice/ari/codices/'  # Global variables are all in caps!


def ari_proc(codex: str) -> str:
    """
    
    """
    whitey_b_gone = codex.replace(' ', '')
    文章 = re.split('[.|?|!]', whitey_b_gone)
    pattern = re.compile(r'[!\"\#$%&'() * +,\-./:; <= > ?@\[\\\] ^ _`{ |}~]')
    no_punc = pattern.sub(' ', codex)
    wee_no_punc = no_punc.lower()
    leixis = split(wee_no_punc)
    mega_string = ''.lexis.join()
    score = (((len(mega_string) / len(leixis)) * 4.17) + .5) + ((len(leixis) / len(文章)) - 21.43)

    print('The A.R.I for the selected text is: {score}')


def menu():
    """
    This is a programmatic alternative to hard coding options into a menu and is much more performant.
    Thanks Kieran!

    """

    print("""
    Welcome to D.A.R.I.U.S. (D-Force Automated Readability Index UtilitieS).
    Please make a selection from the menu below.
    """)

    paths = os.listdir(CODEX_ROOT)  # Creates a list of directories
    codex_paths = (path for path in paths if '.txt' in path)  # Filters out all but ,.txt files

    #     pretty_opts = '①②③④'
    #     load_opt, quit_opts = '🄻', '🅀'

    menu_opts = {str(num): path for num, path in enumerate(codex_paths, start=1)}  # Menu display generator
    menu_length = len(menu_opts)
    menu_opts.update(
        {str(menu_length + 1): 'Load file', str(menu_length + 2): 'Quit'})  # Adds options to load file and quit
    print(list(menu_opts))
    for key, value in menu_opts.items():  # Prints menu
        print(key, '⟹ ', value)

    selection = input('>>>>> ')
    menu_assoc = menu_opts[selection]

    full_path = CODEX_ROOT + menu_assoc

    if int(selection) in range(len(menu_opts) - 1):
        with open(full_path, 'r') as file:
            codex = file.read()
            ari_proc(codex)

    elif int(selection) == menu_length + 1:
        try:
            path = input('Path to codex to analyze: ')  # Ex. '/Users/ylf/Git/Python_Practice/Bēowulf.txt'
            with open(path, 'r') as file:
                codex = file.read()
                ari_proc(codex)
        except FileNotFoundError:
            print('No such file or directory.')
            menu()

    elif int(selection) == menu_length + 2:
        print('Buh bye.')

    else:
        print('Invalid. Please select an option from the menu.')
        menu()


menu()