"""Example of a Network module"""


class Network:
    def __init__(self):
        print("Network ctor")

    def __del__(self):
        print("Network dtor")

    def has_value(self):
        return True