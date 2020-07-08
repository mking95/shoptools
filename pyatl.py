

# Exercise 1: Write code that can compress a string of letters as showed above.
# Part2: Strings with numbers 
from collections import Counter


def parse(string):
    c=Counter(string)
    return(c)

def output(c):
    r=''
    for key in c.keys():
        r += key+str(c[key])
    return r

def main():
    from collections import Counter
    string=input("STRING: ")
    return output(parse(string))

if __name__ == "__main__":
    main()
