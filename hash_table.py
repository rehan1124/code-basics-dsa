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
    # return h % 100, h
    return h % 100


class HashMap:
    def __init__(self):
        self.MAX = 100
        self.hash_arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        """
        Method to calculate hash value for any given "key"
        :param key:
        :return:
        """
        h = 0
        for chars in key:
            h += ord(chars)
        return h % self.MAX

    def __setitem__(self, key, value):
        """
        Add "value" based on given get_hash(key)
        :param key:
        :param value:
        :return:
        """
        k1 = self.get_hash(key)
        self.hash_arr[k1] = value

    def __getitem__(self, key):
        """
        Retrieve value from Hash-table based on given "key"
        :param key:
        :return:
        """
        k1 = self.get_hash(key)
        return self.hash_arr[k1]

    def __delitem__(self, key):
        k1 = self.get_hash(key)
        self.hash_arr[k1] = None


if __name__ == "__main__":
    # --- Examples to calculate hash value ---
    # print(get_hash("Rehan"))
    # print(get_hash("Shareka"))

    # --- Hash-map or Hash-table ---
    hm = HashMap()
    # print(hm.get_hash("Afsha"))  # 83

    hm["Rehan"] = 33  # Calls __setitem__ method
    print(hm["Rehan"])  # 33. Calls __getitem__ method
    hm["Shareka"] = 32  # Calls __setitem__ method
    hm["Rizwan"] = 31
    hm["Afsha"] = 22
    del hm["Rehan"]  # Calls __delitem__
    print(hm["Rehan"])  # None
    print(hm.hash_arr)
