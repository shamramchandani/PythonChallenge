import argparse

class ValidationProcessing:
    
    def __init__(self, args):
        for k, v in args.items():
            setattr(self, k, v)

    def is_positive(self):
        if self.number > 0:
            return True
        else:
            return False

class DivisionProcessing:
    
    def __init__(self):
        pass

    def check_num(self, number):
        while number > 9:
            digit_list = list(str(number))

            number = sum([int(d) for d in str(number)])
        if number in (3,6,9):
            return True
        else:
            return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--number', required=True, type=int, help="--number NUMBER")
    #parser.add_argument('--number2', required=True, type=int, help="--number2 NUMBER")
    args = parser.parse_args()
    vp = ValidationProcessing(vars(args))
    if not vp.is_positive():
        print("Number is not positive")
        exit()



# This is main
if __name__ == "__main__":
    main()