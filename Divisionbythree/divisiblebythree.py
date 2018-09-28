import argparse

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