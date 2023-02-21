class InputError(Exception):
    def __init__(self, massage):
        super().__init__()
        self.massage = massage

    def __str__(self):
        return self.massage