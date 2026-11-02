class Newspaper:
    def __init__(self, name, year, month, day_of_month, is_finnish):
        self.__name = name
        self.year = year
        self.month = month
        self.day_of_month = day_of_month
        self.is_finnish = is_finnish
    def get_name(self):
        return self.__name
    def __str__(self):
        return f'{self.get_name()} ({self.year}-{self.month}-{self.day_of_month})'