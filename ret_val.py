import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Parsing arguments")
    parser.add_argument('-i', action='store_true')
    args = parser.parse_args()
    if args.i:
        return -1
    return 0


if __name__ == '__main__':
    x = main()
    sys.exit(x)
