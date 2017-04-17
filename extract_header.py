"""
Write a function named extract_domain that will print the first matching domain name in a given string.

>>> extract_domain("kieran@pdxcodeguild.com")
'pdxcodeguild.com'

>>> extract_domain("domain of jwackman@hvc.rr.com designates 2a00:1450:400c:c09::22d as permitted sender")
'hvc.rr.com'
"""



def extract_domain(email):
    # email =  input('Enter e-mail address: ')
    at_is_where = email.index('@') + 1
    tld_is_where = email.index('.com') + 4
    extract = email[at_is_where:tld_is_where]
    return extract

# extract_domain()



'''
def extract_domain(email):
    # email =  input('Enter e-mail address: ')
    spaced_email = email + " "
    at_is_where = spaced_email.index('@')
    space_is_where = spaced_email.index(' ')
    backwards_extract = spaced_email[space_is_where:at_is_where:-1]
    forwards_extract = backwards_extract[::-1]

    return forwards_extract

# extract_domain()

'''