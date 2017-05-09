"""
This is Doby's attempt to make a genuinely useful tool for extracting and manipulating data from a webpage.

This program must accomplish the following operations:

- Slice out the header lines from all the lines you read. 
- Split a string by whitespace into a list of strings using .split(). 
- Extract the date string from the date columns.
- If there are any days with missing data ('-'), explicitly drop them from your dataset. 
- Avoid using un-named "pairs" outside of dictionaries. 
- Use tuples to group together individual instances of a date and a rainfall amount. (Or namedtuple form collections.) 
- Print out a summary of the data: date with the most rain, year with the most rain.
"""


import os
import re


BASE_DIR = '/Users/ylf/Git/Python_Practice/rain'


#def reckon_year(diced_data: str) -> str:


    #rainiest_year =


def reckon_day(diced_data: dict) -> str:
    """                                            
    This will extract and return meaningful data from diced_data.
    :return:                                     
    """
    rainiest = max(diced_data.items(), key=lambda t: t[1][0])  # Returns value of the first element of the tuple
    print(rainiest)
    rainiest_day = rainiest[0]
    rainiest_total = rainiest[1][0]
    print(f'Rainiest day: {rainiest_day}', f'Total precipitation: {rainiest_total}', sep='\n')


def slice_n_dice(raw_text: str) -> dict:
    """                                            
    This converts raw text into a searchable 3-d data structure (dictionary).
    :return: dict                                    
    """
    tranches = raw_text.splitlines()
    decapitated = tranches[11::]
    sliced_data = (tranche.split() for tranche in decapitated)
    diced_data = {daily_rain[0]: (daily_rain[1], daily_rain[2:]) for daily_rain in sliced_data}   # Suggested by Kieran
    reckon_day(diced_data)


def file_handler(filesystem_path: str) -> str:
    """
    This loads a user-selected file and outputs a string
    :param filesystem_path: User selectable path to a file
    :return: 
    """
    with open(filesystem_path, 'r') as file:                     # This is a context manager.
        raw_text = file.read()                                   # returns entire file contents as a single string
        return raw_text


def run():
    filesystem_path = os.path.join(BASE_DIR, 'sample.rain')
    raw_text = file_handler(filesystem_path)
    slice_n_dice(raw_text)


run()


# def menu():
#     """
#
#     :return:
#     """
#     print('Blah blah blah...')
#
#     menu_opts = {str(num): path for num, path in enumerate(file_paths, start=1)}      # Menu display generator
#     menu_length = len(menu_opts)
#     menu_opts.update({str(menu_length+1):'Load file', str(menu_length+2): 'Quit'})    # Adds options to load file and quit
#     user_opt = os.listdir(BASE_DIR)
#     fullpath = BASE_DIR + user_opts[selection]
#     data = file_handler(user_opts_[path)
#     raw_rain_data = file_handler(os.path.join(BASE_DIR, 'sample.rain'))
#
#     for key, value in menu_opts.items():                                          # Prints menu
#         print(key, '⟹ ', value)
#     selection = input('>>>>> ')