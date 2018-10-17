class Calculator(object):

    def validate_input(self, x, y):
        number_types = (int, float, complex)
        return isinstance(x, number_types) and isinstance(y, number_types)

    def add(self, x, y):
        if self.validate_input(x,y) is True:
            return (x + y)
        
    def subtract(self, x, y):
        if self.validate_input(x,y) is True:
            return (x - y)

    def divide(self, x, y):
        if self.validate_input(x,y) is True:
            return (x / y)

    def multiply(self, x, y):
        if self.validate_input(x,y) is True:
            return (x * y)