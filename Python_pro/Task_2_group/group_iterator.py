class GroupIterator:
    def __init__(self, __students):
        self.__students = __students
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.__students):
            raise StopIteration()
        temp_group = self.__students[self.index]
        self.index += 1
        return temp_group
