"""Perform actions on lists."""

import copy


def get_diff(first, second):
    """Diff two lists. Return list of x - y (everything in x that is not in y). Reverse order to get inverse diff.

    Args:
        first (list): List1
        second (list): List2

    Returns:
        List: The list of items in List1 that are not in List2.
    """
    second = set(second)
    return [item for item in first if item not in second]


def dedupe_array(data, col):
    """For a 2D array (list of lists), remove rows that have duplicate data in a given column. Provide index on which to match dupes.

    Args:
        data (list): 2-dimensional array
        col (int): index to match for duplicates

    Returns:
        list: Result array with duplicates removed.
    """
    new_data = []
    for row in data:
        if row[col] not in [r[col] for r in new_data]:
            new_data.append(row)
    return new_data


def trim_array(data, indices):
    """Trim columns from array.

    Provide column indexes as list to remove (starts with 0). Leaves original array
    intact (by deep copying)

    Args:
        data (list): 2-dimensional array (list of lists)
        indices (list): List of integer column indexes (starting with 0)

    Returns:
        list: New list with columns trimmed
    """
    new_data = copy.deepcopy(data)
    for row in new_data:
        for i in sorted(indices, reverse=True):
            del row[i]
    return new_data


def sort_array(data, match_key=0, ignore_heads=False):
    """Sort an array based on given column (1st one by default).

    Args:
        data (list): 2-dimensional array (list of lists)
        match_key (int, optional): Column to sort on. Defaults to 0.
        ignore_heads (bool, optional): Treat row 0 as heads and ignore. Defaults to False.

    Returns:
        list: New sorted list
    """
    data_sorted = copy.deepcopy(data)
    if ignore_heads:
        heads = data_sorted.pop(0)
    data_sorted.sort(key=lambda x: x[match_key])
    if ignore_heads:
        data_sorted.insert(0, heads)
    return data_sorted
