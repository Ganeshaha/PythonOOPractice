"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """initializes the object with start and new as start-1 as the generate function increments by 1
        """
        self.start = start
        self.new = int(start)-1

    def generate(self):
        """generate serial, then increments 'new' variable by 1
        """
        self.new+=1
        return self.new
    def reset(self):
        """resets new back to start-1 int() is to change the reference
        """
        self.new = int(self.start)-1

serial = SerialGenerator(start=100)
print(serial.generate())
print(serial.generate())
print(serial.generate())
serial.reset()
print(serial.generate())
print(serial.generate())
print(serial.generate())