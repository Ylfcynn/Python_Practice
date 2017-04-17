"""
Write a function that returns the meal for any given hour of the day.

Breakfast: 7AM - 9AM
Lunch: 12PM - 2PM
Dinner: 7PM - 9PM
Hammer: 10PM - 4AM

>>> meal(7)
'Breakfast time.'
>>> meal(13)
'Lunch time.'
>>> meal(20)
'Dinner time.'
>>> meal(21)
'No meal scheduled at this time.'
>>> meal(0)
'Hammer time.'
>>> meal(3)
'Hammer time.'
>>> meal(9999)
'Not a valid time.'
>>> meal(99767676766799)
'Not a valid time.'

"""

#Hard coded solution

# def meal(hour):
#     if hour in [5, 6]:
#         result = 'No meal scheduled at this time.'
#     elif hour in [7, 8, 9]:
#         result = 'Breakfast time.'
#     elif hour in [10, 11]:
#         result = 'No meal scheduled at this time.'
#     elif hour in [12, 13, 14]:
#         result = 'Lunch time.'
#     elif hour in [15, 16, 17, 18, 21]:
#         result = 'No meal scheduled at this time.'
#     elif hour in [19, 20]:
#         result = 'Dinner time.'
#     elif hour in [22, 23, 24, 0, 1, 2, 3, 4]:
#         result = 'Hammer time.'
#     else:
#         result = 'Not a valid time.'
#
#     return result
#

def meal(hour):
    if hour >= 5 :
        result = 'No meal scheduled at this time.'
    elif hour in [7, 8, 9]:
        result = 'Breakfast time.'
    elif hour in [10, 11]:
        result = 'No meal scheduled at this time.'
    elif hour in [12, 13, 14]:
        result = 'Lunch time.'
    elif hour in [15, 16, 17, 18, 21]:
        result = 'No meal scheduled at this time.'
    elif hour in [19, 20]:
        result = 'Dinner time.'
    elif hour in [22, 23, 24, 0, 1, 2, 3, 4]:
        result = 'Hammer time.'
    else:
        result = 'Not a valid time.'

    return result

