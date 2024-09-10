#!/usr/bin/python3

# process
#def c2f(c):
    #return ((c*9)/5)+32 #PEMDAS
def f2c_op(f):
    return (f-32)*5/9 #Fahrenheit to Celsius

def main():
    f=input("What Fahrenheit Temp do you want?") #input
    dig=f.isdigit() 
    while dig==False: #If it includes any letters it will repeat until only Numbers
        f=input("Please ONLY Include Numbers")
        dig=f.isdigit()
    f=int(f)
    c=f2c_op(f)
    print(f"{f}F is {c} C")
if __name__ == "__main__":
    main() # output
