#!/usr/bin/env python3

import argparse
from printprintbaby import print_baby

def main():
    parser = argparse.ArgumentParser(
        description="PrintPrintBaby – prints text to the terminal"
    )
    parser.add_argument(
        "text",
        help="Text to print"
    )

    args = parser.parse_args()
    print_baby(args.text)


if __name__ == "__main__":
    main()
