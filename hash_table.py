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

    def add_to_hash(self, key, value):
        """
        Add "value" based on given get_hash(key)
        :param key:
        :param value:
        :return:
        """
        k1 = self.get_hash(key)
        self.hash_arr[k1] = value

    def get_from_hash(self, key):
        """
        Retrieve value from Hash-table based on given "key"
        :param key:
        :return:
        """
        k1 = self.get_hash(key)
        return self.hash_arr[k1]


if __name__ == "__main__":
    # --- Examples to calculate hash value ---
    # print(get_hash("Rehan"))
    # print(get_hash("Shareka"))

    # --- Hash-map or Hash-table ---
    hm = HashMap()
    # print(hm.get_hash("Afsha"))  # 83

    hm.add_to_hash("Rehan", 33)
    print(hm.get_from_hash("Rehan"))
    print(hm.get_from_hash("Rizwan"))
