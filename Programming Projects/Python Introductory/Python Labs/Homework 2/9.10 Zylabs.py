# Andy Luong 1525166
# 9.10 Zylabs

import csv

def frequency(line):
    line = line.split() #turns line into individual words
    store = [] #make storage
    for i in line: #goes through each word
        if i not in store: #if word is unique
            store.append(i) #puts word in list
    for i in range(0, len(store)): #counts up to how many unique words there are
        x = line.count(store[i]) #adds each recurring word
        print(store[i] + " " + str(x)) #prints word & number it occurs

def main():
    filename = input() #read file
    with open(filename, "r") as file: # opens file as read
        word = csv.reader(file) #reads file as csv through word variable
        for row in word: #goes through each column in row
            sentence = (' '.join(row)) #puts everything in one line
            frequency(sentence) #performs frequency function

if __name__=="__main__":
    main()