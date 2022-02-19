import webbrowser
print("'In 1874 Georg Cantor, a German mathematician, published a paper that")
print("launched a new branch of mathematics called \"Set Theory.\"")
print()
print("I want to challenge that theory, so I wrote a program that will nullify the statement:")
print("'Are there more natural numbers or more real numbers between 0 and 1?'")
print()
print("Cantor hypothesized that if you wrote a list of natural numbers and then threw some ridiculously long real")
print("number on the other side, that the list of real numbers would definitely make the list of natural numbers")
print("pale in comparison.")
print()
print("This program will show you why this is VERY WRONG.")
print("Type 'open' to open the video for more information!")
print("Please enter a number greater than zero. No decimals!")
num = 0
while num != 'quit':
    print("Enter a number to be converted to decimal form: or type 'quit'")
    num = input().lower()
    if num.isdigit():
        revNum = str(num)
        print("{} is the true equality of    0.{}".format(num, revNum[::-1]))
        print("{} is the inverse equality of 0.{}".format(revNum[::-1], num))
    elif num == 'quit':
        print("There are definitely more if you continue beyond zero, though we could just then wonder about the")
        print("difference between 1 and 2. But he pitted the two against each other in an arbitrary way. I believe")
        print("WHOLEHEARTEDLY that there are an equal amount of real and natural numbers between 0 and 1.")
    elif num == 'open':
        print("Opening Video: Math Has a Fatal Flaw")
        print("Video Created By: Veritasium")
        webbrowser.open("https://youtu.be/HeQX2HjkcNo?t=225")
    else:
        print("That isn't a number, or it isn't a compatible number.")
