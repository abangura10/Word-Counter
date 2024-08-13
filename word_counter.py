import string

#Word Count - Counts the frequency of each word in a textfile.

def printOut(data):
    #Prints each word in data the amount of time it appears sorted.
    for x in sorted(data.keys()):
        print(f"{x} :: {data[x]}")
    return

def wordFreq(fptr):
    #Creates empty data type for a list.
    freq = {}

    #Reading first line
    line = fptr.readline()

    #Creates tuple of punctuation characters to eliminate.
    punctChars = tuple(string.punctuation)

    while line:
        for c in punctChars:
            # Replaces punctuation characted with space.
            line = line.replace(c, "")
        #List of separate words that make up the line.
        words = line.split()

        for word in words:
            #Creates a temporary word converted to lowercase using the lower()
            temporary = word.lower()

            #Temporary words get added to the dictionary
            freq[temporary] = freq.get(temporary, 0) + 1

        #Read another line
        line = fptr.readline()

    return freq

def main():
    #Asking user for filename to read
    filename = input("Enter filename to read: ")

    try:
        #Opening file
        with open(filename, 'r') as fptr:
            #Count and prints the word frequencies of each word in file
            print(printOut(wordFreq(fptr)))
    except FileNotFoundError:
        #If file isn't present error shows.
        print("ERROR: The file was not found.")

if __name__ == "__main__":
    main()
        
            
            
        
