

def key_in_dict_with_max_value(dictionary):
    """
    Gives the key in dictionary whose value is the highest.
    Args:
        dictionary (dict): Dictonary only containing values of int type.

    Returns:
        str: Key with highest value in dictionary.
    """
    return str([k for k, v in dictionary.items() if v == max(dictionary.values())][0])


def invert_dict_keyvalues(dictionary):
    """
    Inverts the positions of keyvalues in dictionary.
    Args:
        dictionary (dict): A valid dictionary.

    Returns:
        dict: Inputed dictionary with inverted keyvalues.
    """
    return {v: k for k, v in dictionary.items()}

