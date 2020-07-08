#This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.
#Please credit me at this URL: https://github.com/CaydendW/

import winsound
import time
import pyttsx3

print("welcome to morse")
print("Made by Cayden de Wit")
print("The formating for this is -, . and .")
mode2 = input("Press m for text to morse and leave blank for morse to text: ")
string = input("Input the string you want to be translated: ")

mode = mode2.lower()

engine = pyttsx3.init()
engine.setProperty('rate', 140)

counter = 0

A	=".-"
B	="-..."
C	="-.-."
D	="-.."
E	="."
F	="..-."
G	="--."
H	="...."
I	=".."
J	=".---"
K	="-.-"
L	=".-.."
M	="--"
N	="-."
O	="---"
P	=".--."
Q	="--.-"
R	=".-."
S	="..."
T	="-"
U	="..-"
V	="...-"
W	=".--"
X	="-..-"
Y	="-.--"
Z	="--.."
one	=".----"
two	="..---"
three	="...--"
four	="....-"
five	="....."
six     ="-...."
seven	="--..."
eight	="---.."
nine	="----."
zero	="-----"
Period	=".-.-.-"
Comma	="--..--"
ex = "-.-.--"
ques = "..--.."
apos = ".----."
col = "---..."
fsla = "-..-."

x = string.lower()

l = []

if mode == "m":
    for index, letter in enumerate(x):
        if letter == "a":
            l.append(A + " ")
        elif letter == "b":
            l.append(B + " ")
        elif letter == "c":
            l.append(C + " ")
        elif letter == "d":
            l.append(D + " ")
        elif letter == "e":
            l.append(E + " ")
        elif letter == "f":
            l.append(F + " ")
        elif letter == "g":
            l.append(G + " ")
        elif letter == "h":
            l.append(H + " ")
        elif letter == "i":
            l.append(I + " ")
        elif letter == "j":
            l.append(J + " ")
        elif letter == "k":
            l.append(K + " ")
        elif letter == "l":
            l.append(L + " ")
        elif letter == "m":
            l.append(M + " ")
        elif letter == "n":
            l.append(N + " ")
        elif letter == "o":
            l.append(O + " ")
        elif letter == "p":
            l.append(P + " ")
        elif letter == "q":
            l.append(Q + " ")
        elif letter == "r":
            l.append(R + " ")
        elif letter == "s":
            l.append(S + " ")
        elif letter == "t":
            l.append(T + " ")
        elif letter == "u":
            l.append(U + " ")
        elif letter == "v":
            l.append(V + " ")
        elif letter == "w":
            l.append(W + " ")
        elif letter == "x":
            l.append(X + " ")
        elif letter == "y":
            l.append(Y + " ")
        elif letter == "z":
            l.append(Z + " ")
        elif letter == "1":
            l.append(one + " ")
        elif letter == "2":
            l.append(two + " ")
        elif letter == "3":
            l.append(three + " ")
        elif letter == "4":
            l.append(four + " ")
        elif letter == "5":
            l.append(five + " ")
        elif letter == "6":
            l.append(six + " ")
        elif letter == "7":
            l.append(seven + " ")
        elif letter == "8":
            l.append(eight + " ")
        elif letter == "9":
            l.append(nine + " ")
        elif letter == "0":
            l.append(zero + " ")
        elif letter == ",":
            l.append(Comma + " ")
        elif letter == ".":
            l.append(Period + " ")
        elif letter == " ":
            l.append('/' + " ")
        elif letter == "?":
            l.append(ques + " ")
        elif letter == "!":
            l.append(ex + " ")
        elif letter == "'":
            l.append(apos + " ")
        elif letter == ":":
            l.append(col + " ")
        elif letter == "/":
            l.append(fsla + " ")
        else:
            print(letter + " is not a recognized character.")
            exit()

    s = ''.join(l)
    print(s)
    playsound = input("Would you like it to be played y/n: ")
    playsound = playsound.lower()
    if playsound == "y":
        for index, letter in enumerate(s):
            if letter == "-":
                winsound.Beep(750, 300)
                time.sleep(0.1)
            elif letter == ".":
                winsound.Beep(750, 100)
                time.sleep(0.1)
            elif letter == " ":
                time.sleep(0.200)
            elif letter == "/":
                time.sleep(0.6)
    else:
        pass

elif mode != "m":
    y = string.split(" ")
    length = len(y)

    for loop in range(length):
        if y[counter] == A:
            l.append("a")
            counter += 1
        elif y[counter] == B:
            l.append("b")
            counter += 1
        elif y[counter] == C:
            l.append("c")
            counter += 1
        elif y[counter] == D:
            l.append("d")
            counter += 1
        elif y[counter] == E:
            l.append("e")
            counter += 1
        elif y[counter] == F:
            l.append("f")
            counter += 1
        elif y[counter] == G:
            l.append("g")
            counter += 1
        elif y[counter] == H:
            l.append("h")
            counter += 1
        elif y[counter] == I:
            l.append("i")
            counter += 1
        elif y[counter] == J:
            l.append("j")
            counter += 1
        elif y[counter] == K:
            l.append("k")
            counter += 1
        elif y[counter] == L:
            l.append("l")
            counter += 1
        elif y[counter] == M:
            l.append("m")
            counter += 1
        elif y[counter] == N:
            l.append("n")
            counter += 1
        elif y[counter] == O:
            l.append("o")
            counter += 1
        elif y[counter] == P:
            l.append("p")
            counter += 1
        elif y[counter] == Q:
            l.append("q")
            counter += 1
        elif y[counter] == R:
            l.append("r")
            counter += 1
        elif y[counter] == S:
            l.append("s")
            counter += 1
        elif y[counter] == T:
            l.append("t")
            counter += 1
        elif y[counter] == U:
            l.append("u")
            counter += 1
        elif y[counter] == V:
            l.append("v")
            counter += 1
        elif y[counter] == W:
            l.append("w")
            counter += 1
        elif y[counter] == X:
            l.append("x")
            counter += 1
        elif y[counter] == Y:
            l.append("y")
            counter += 1
        elif y[counter] == Z:
            l.append("z")
            counter += 1
        elif y[counter] == one:
            l.append("1")
            counter += 1
        elif y[counter] == two:
            l.append("2")
            counter += 1
        elif y[counter] == three:
            l.append("3")
            counter += 1
        elif y[counter] == four:
            l.append("4")
            counter += 1
        elif y[counter] == five:
            l.append("5")
            counter += 1
        elif y[counter] == six:
            l.append("6")
            counter += 1
        elif y[counter] == seven:
            l.append("7")
            counter += 1
        elif y[counter] == eight:
            l.append("8")
            counter += 1
        elif y[counter] == nine:
            l.append("9")
            counter += 1
        elif y[counter] == zero:
            l.append("0")
            counter += 1
        elif y[counter] == Period:
            l.append(".")
            counter += 1
        elif y[counter] == Comma:
            l.append(",")
            counter += 1
        elif y[counter] == ex:
            l.append("!")
            counter += 1
        elif y[counter] == ques:
            l.append("?")
            counter += 1
        elif y[counter] == apos:
            l.append("'")
            counter += 1
        elif y[counter] == col:
            l.append(":")
            counter += 1
        elif y[counter] == fsla:
            l.append("/")
            counter += 1
        elif y[counter] == "/":
            l.append(" ")
            counter += 1
        else:
            print(y[counter] + " is not a recognized character.")
            exit()
            
    s = ''.join(l)
    print(s)
    say = input("Would you like it to be said y/n: ")
    say = say.lower()
    if say == "y":
        engine.say(s)
        engine.runAndWait()
    else:
        pass
