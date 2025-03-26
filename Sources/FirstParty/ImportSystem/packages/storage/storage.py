"""Example of a Storage module"""


class Storage:
    def __init__(self):
        print("Storage ctor")

    def __del__(self):
        print("Storage dtor")

    def has_value(self):
        return False