
def selection_sort(data):
    if not data:
        return []
    # by default minimum value of the list is set to be the first one

    indecies_length = len(data) - 1 # number of indecies to iterate through is smaller by one

    # iterate through the rest of the values
    # and compare them with minimum
    for index in range(indecies_length): # iterathe through indecies
        minimum_index = index

        for greater_index in range(index + 1, len(data)): # all elements to the right of the current iterating one
            if data[greater_index] < data[minimum_index]:
                minimum_index = greater_index

        if minimum_index != index:
            data[minimum_index], data[index] = data[index], data[minimum_index]

    return data
