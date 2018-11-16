class ANY:
    def __init__(self, dtype):
        self.dtype = dtype
    def __eq__(self, actual):
        return self.dtype == type(actual)
