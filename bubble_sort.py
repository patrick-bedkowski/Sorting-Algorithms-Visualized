
def bubble_sort(data):
    if not data:
        return []
    else:
        list_length = len(data)
        # iterate through every element in the list
        for index in range(list_length):
            # iterate through elements that are placed on indecies less than data[index]:
            for less_index in range(0, list_length - index - 1):
                # compare these less deep elements
                if data[less_index] >= data[less_index + 1]: # if element with smaller index is greater
                    data[less_index], data[less_index + 1] = data[less_index + 1], data[less_index] # swap them together
        return data # return sorted list
