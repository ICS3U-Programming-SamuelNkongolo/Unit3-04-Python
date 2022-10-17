#!/usr/bin/env python3
# Created By: Samuel Nkongolo
# Date: Oct. 5, 2022
# This program asks the user to enter an integer and tells them if it is positive, negative or zero


def main():

    integer = int(input("enter an integer:"))

    if integer > 0:
        print("this number is positive")
    if integer < 0:
        print("this number is negative")
    if integer == 0:
        print("this number is zero")


if __name__ == "__main__":
    main()
