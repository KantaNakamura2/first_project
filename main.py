from random import randint


symbols = ['*', '#', '@', '$']


# create symbols.txt file with four symbols.
fd = open("symbols.txt", "w")
for i in range(20):
    for j in range(randint(1, 30)):
        fd.write(symbols[randint(0, len(symbols)-1)])
    fd.write("\n")
fd.close()


# input symbols alternative number.
print('Input:', end=' ')
get_alternative_number = input().split(',')
# create a list for storing alternative numbers
symbols_number = []
for _ in range(len(get_alternative_number)):
    symbols_number.append(get_alternative_number[_][2])
symbols_dictionary = dict(zip(symbols, symbols_number))
print(symbols_dictionary)


# output each symbols to its corresponding number.
with open('symbols.txt', 'r') as f:
    while True:
        line = f.readline()
        for symbol in line:
            if symbol in symbols_dictionary:
                print(symbols_dictionary[symbol], end='')
            else:
                print(symbol, end='')
        if not line:
            break