class BaseConverter():
    def __init__(self, deg, unit):
        self.deg = deg
        self.unit = unit
        
    def convert(self):
        if self.unit == 'k':
            self.new_deg = round(self.deg + 273.15, 2)
            self.unit = 'Kelvin'

        if self.unit == 'f':
            self.new_deg = round((self.deg * 9 / 5) + 32, 2)
            self.unit = 'Fahrenheit'

        print(f'{self.new_deg} {self.unit}')


def main():
    deg = float(input('Hello! How many degrees Celsius? :  '))
    unit = input('Where will we convert?\nKelvin (k) or Fahrenheit (f) : ')
    if unit == 'k' or unit == 'f':
        new_deg = BaseConverter(deg, unit)
        new_deg.convert()
    else : print('   ¯\_(ツ)_/¯   ')


if __name__ == "__main__":
    main()