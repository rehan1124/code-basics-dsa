"""
Hash-table or Hash-map
"""


def get_hash(key):
    """
    Function to calculate hash value for any given "key"
    :param key:
    :return:
    """
    h = 0
    for chars in key:
        h += ord(chars)
    return h % 100, h


if __name__ == "__main__":
    # --- Examples to calculate hash value ---
    print(get_hash("Rehan"))
    print(get_hash("Shareka"))
