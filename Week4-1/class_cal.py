class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def subtract (self):
        result = self.first - self.second
        return result

    def add (self):
        result = self.first + self.second
        return result

calculate = Calculator(5,9)
print(calculate.subtract())
print(calculate.add())