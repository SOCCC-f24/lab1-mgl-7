#!/usr/bin/python3

# process
def c2f(c):
    return ((c*9)/5)+32 #PEMDAS

def main(cel):
    return c2f(cel)

if __name__ == "__main__":
    cel = int(input("What do you want Celsius to be? "))        # input and Chanes to interger
    print(main(cel))  # output
