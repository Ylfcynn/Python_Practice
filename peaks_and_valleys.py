"""

>>> data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

>>> peaks(data)
[6, 14]

>>> valleys(data)
[9, 17]

>>> peaks_and_valleys(data)
[6, 9, 14, 17]

>>> points_of_interest = peaks_and_valleys(data)

>>> chop(data, points_of_interest)
[[1, 2, 3, 4, 5, 6, 7], [6, 5, 4], [5, 6, 7, 8, 9], [8, 7, 6], [7, 8, 9]]

"""


"""
My first solution for peaks.
"""

def peaks(data):
    
    maxima = list()

    counter = 0
    
    for datum in data:
        if datum == data[0]:
            counter += 1

        elif datum == data[len(data)-1]:
            break
            
        elif data[counter] - data[counter - 1] > 0 and data[counter] - data[counter + 1] > 0:
            maxima.append(data.index(data[counter]))
        counter += 1
    
    return maxima


def valleys(data):

    minima = list()

    counter = 0
    
    for datum in data:
        if datum == data[0]:
            counter += 1

        elif datum == data[len(data)-1]:
            break
            
        elif data[counter] - data[counter - 1] < 0 and data[counter] - data[counter + 1] < 0:
            minima.append(data.index(data[counter]))
        counter += 1
    
    return minima


"""
def peaks(data):

    maxima = list()

    for index, datum in enumerate(data):

        this_one = datum  # Here
        next = data[index+1]    # Ahead


        if index == 0 or index == (len(data) - 1):
            continue

        else:
            datum > datum index + 1 and datum > datum index - 1
            spew.append(datum)

    return maxima


def valleys(data):
    pass


def peaks_and_valleys(data):


def chop(data, points_of_interest):
    pass
"""
