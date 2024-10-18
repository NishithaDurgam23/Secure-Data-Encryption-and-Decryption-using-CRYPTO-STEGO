def convert(txt):
    if (txt == "A"):
        k = 1
    elif (txt == "B"):
        k = 2
    elif (txt == "C"):
        k = 3
    elif (txt == "D"):
        k = 4
    elif (txt == "E"):
        k = 5
    elif (txt == "+"):
        k = 74
    elif (txt == "/"):
        k = 75
    elif (txt == "!"):
        k = 63
    elif (txt == "@"):
        k = 64
    elif (txt == "#"):
        k = 65
    elif (txt == "$"):
        k = 66
    elif (txt == "%"):
        k = 67
    elif (txt == "^"):
        k = 68
    elif (txt == "&"):
        k = 69
    elif (txt == "*"):
        k = 70
    elif (txt == "("):
        k = 71
    elif (txt == ")"):
        k = 72
    elif (txt == "-"):
        k = 73
    else:
        k = "ERROR"
    return k

def revconvert(num):
    if (num == 1):
        k = "A"
    elif (num == 2):
        k = "B"
    elif (num == 3):
        k = "C"
    elif (num == 4):
        k = "D"
    elif (num == 5):
        k = "E"
    elif (num == 6):
        k = "F"
    elif (num == 63):
        k = "!"
    elif (num == 64):
        k = "@"
    elif (num == 65):
        k = "#"
    elif (num == 66):
        k = "$"
    elif (num == 67):
        k = "%"
    elif (num == 68):
        k = "^"
    elif (num == 69):
        k = "&"
    elif (num == 70):
        k = "*"
    elif (num == 71):
        k = "("
    elif (num == 72):
        k = ")"
    elif (num == 73):
        k = "-"
    elif (num == 74):
        k = "+"
    elif (num == 75):
        k = "/"
    else:
        k = "Error"
    return k

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == "__main__":
    p = int(input('Enter the value of p = '))
    q = int(input('Enter the value of q = '))
    file = open(r'C:\Users\Renuka\OneDrive\Desktop\hel.txt', "r")
    text = file.read()
    file.close()
    #text = input('Enter the value of text = ')
    l1 = len(text)
    k10 = ""
    k20 = ""
    for i in range(0, l1):
        no = convert(text[i])
        n = p * q
        if (no > n):
            print("Please enter correct text.........")
        else:
            t = (p - 1) * (q - 1)
            for e in range(2, t):
                if gcd(e, t) == 1:
                    break

