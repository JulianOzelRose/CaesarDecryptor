"""
Program: CaesarDecryptor.py
Author: Julian Rose

The purpose of this program is to decrypt a single line of Caesar cipher-encrypted
text using a two-pronged approach; brute force and simple heuristics. The program
produces 15 decryption results, then makes its best "guess" which one is the correct
key based on whether or not a result contains keywords. User must manually enter the
input and output filenames.
"""

def DecryptText(text, distance):
    plainTxt = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            plainTxt += chr((ord(char) - distance - 65) % 26 + 65)
        else:
            plainTxt += chr((ord(char) - distance - 97) % 26 + 97)
    return(plainTxt)

def GetNumHits(filename, text):
    keywordsFile = open(filename, 'r')
    numHits = 0
    for line in keywordsFile:
        words = line.split()
        for word in words:
            if word in text:
                numHits = numHits + 1
    keywordsFile.close()
    return numHits

def GetText(filename):
    cipherTxt = ""
    inputFile = open(filename, 'r')
    for line in inputFile:
        words = line.split()
        line.lstrip
        for word in words:
            cipherTxt += word
    inputFile.close()
    return cipherTxt

def WriteToFile(filename, text):
    outputFile = open(filename, 'w')
    outputFile.seek(0)
    outputFile.truncate(0)
    outputFile.write(text)
    outputFile.close()

def main():
    print("*** Caesar Cipher Brute Force Decryptor ***")

    # Filenames
    inputFilename = str(input("Enter input filename: "))
    outputFilename = "./output_file.txt"
    keywordsFilename = "./keywords.txt"

    # Decryption variables
    maxDistVal = 14
    numHits = 0
    cipherTxt = GetText(inputFilename)
    plainTxt = ""
    keysWithHits = []

    # Print all decryption results
    print("\nALL results:")
    for key in range(maxDistVal):
        text = DecryptText(cipherTxt, key)
        numHits = GetNumHits(keywordsFilename, text)
        print("key =",key,"\t",text,"\t\thits:",numHits)
        if numHits > 0:
            keysWithHits.append(key)

    # Print likely decryption results
    print("\nLIKELY results:")
    if len(keysWithHits) > 0:
        for key in keysWithHits:
            text = DecryptText(cipherTxt, key)
            numHits = GetNumHits(keywordsFilename, text)
            print("key =",key,"\t",text,"\t\thits:",numHits)
    else:
        print("None")

    # Get correct decryption key
    correctKey = int(input("\nEnter the key that produces the best result, or 0 to exit: "))
    plainTxt = DecryptText(cipherTxt, correctKey)

    # Write to file or exit program
    if correctKey != 0:
        outputFilename = input("Enter filename to write result to: ")
        try:
            WriteToFile(outputFilename, plainTxt)
            print("SUCCESS: Decrypted result written to",outputFilename)
        except:
            print("ERROR: Unable to write to file.")
    else:
        print("Exiting program...")
        exit()

if __name__ == "__main__":
    main()
