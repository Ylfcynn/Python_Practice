"""
We're going to have some fun with REST and JSON.
"""


import requests


RESPONSE = requests.get('https://api.randomuser.me/?results=5')

USERS = RESPONSE.json().get('results')


def pretty_print(name: str, email: str, username: str, reg_date: str, dob: str, ) -> str:
    '''

    :return: 
    '''
    bio_data = f"""
    Name: {name}
    E-mail: {email}
    Username: {username}
    Registration date: {reg_date}
    Birth date: {dob}
    """

    print(bio_data)


def fetch() -> None:
    '''
    
    :return: 
    '''
    for user in USERS:
        name_data = user['name']
        title = name_data['title']
        first = name_data['first']
        last = name_data['last']

        name = f'{title} {first} {last}'

        email = user['email']

        username = user['login']['username']

        reg_date = user['registered']

        dob = user['dob']

        pretty_print(name, email, username, reg_date, dob)


fetch()





