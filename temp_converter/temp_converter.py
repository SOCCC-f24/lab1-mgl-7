#!/usr/bin/python3

# process
def c2f(c):
    return ((c*9)/5)+32 #PEMDAS

def main(cel):
    return c2f(cel)

if __name__ == "__main__":
    cel = input("What do you want Celsius to be? ")      # input and Chanes to interger
    dig= cel.isdigit() #checks if you include any letters
    while dig==False: #if letter is included repeat until user stops
        cel=input("Please Only include Numbers")
        dig=cel.isdigit()
        #If has a letter will repeat
    cel=int(cel) #turns string in interger
    print(main(cel))  # output

#Matthew Lee, 9/10/24, 
