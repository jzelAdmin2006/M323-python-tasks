def min2(lst):
    """Returns the smallest element in a list."""
    return min(lst)

def simple_sort(lst):
    """Sorts a list of numbers in ascending order using min2 and filter."""
    sorted_list = []
    while lst:
        smallest = min2(lst)
        sorted_list.append(smallest)
        lst = list(filter(lambda x: x != smallest, lst))
    return sorted_list

example_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_example = simple_sort(example_list)
sorted_example
