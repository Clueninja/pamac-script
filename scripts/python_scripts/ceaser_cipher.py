import enchant
#d= enchant.Dict("en_GB")


dictionary={"a":8.2,
"b":1.5,
"c":2.8,
"d":4.3,
"e":13,
"f":2.2,
"g":2,
"h":6.1,
"i":7,
"j":0.15,
"k":0.77,
"l":4,
"m":2.4,
"n":6.7,
"o":7.5,
"p":1.9,
"q":0.095,
"r":6,
"s":6.3,
"t":9.1,
"u":2.8,
"v":0.98,
"w":2.4,
"x":0.15,
"y":2,
"z":0.074}


def remove_spaces(text):
    new = ""
    for character in text:
        if character != " " or character not in [i for i in range (0,10)]:
            new+=character
    return new

def score_of_ciphertext(ciphertext):
    characters = []
    for character in ciphertext:
        #find fre of each char
        found = False
        for item in characters:
            if character == item[0]:
                item[1]+=1
                found = True
        if found == False:
            characters.append([character, 1])
    sumofpercentages = 0
    for item in characters:
        percentage = item[1]/len(ciphertext)
        #print(dictionary[item[0]])
        percentagediff = abs(dictionary[item[0]]-percentage)
        sumofpercentages +=percentagediff  
    print(sumofpercentages)
    return sumofpercentages


def brute_force_ceaser(ciphertext):
    scores = []
    for shift in range(26):
        maybeplaintext = decrypt(ciphertext, shift)
        scores.append(score_of_ciphertext(maybeplaintext))
    minimums = [[100.0,0], [100.0, 0], [100.0, 0], [100.0, 0],[100.0, 0],[100.0, 0],[100.0, 0]]
    for shift in range(len(scores)):
        score = scores[shift]
        for minimumind in range(len(minimums)):
            minimum = minimums[minimumind]
            #yes this is bad, does not move all the items down the list
            if score<minimum[0]:
                if minimumind<6:
                    minimums[minimumind+1][0]=minimum[0]
                    minimums[minimumind+1][1]=minimum[1]
                minimum[0]= score
                minimum[1] = shift
                break
    for minimum in minimums:
        print(minimum[0], minimum[1])
        print(decrypt(ciphertext, minimum[1]))
        print()
    return 0


def decrypt(ciphertext, shift):
    scores = []
    plaintext = ""
    print ("i am using vim XD")
    for character in ciphertext:
        plaintext+=chr(97+(ord(character)-97-shift)%26)
    return(plaintext)


def encrypt(plaintext, shift):
    plaintext.lower()
    plaintext=remove_spaces(plaintext)
    ciphertext = ""
    for character in plaintext:
        ciphertext+=chr(97+(ord(character)-97+shift)%26)
    return(ciphertext)


if __name__ == "__main__":
    print(decrypt("jgnnqyqtnf", 2))
    print(decrypt(remove_spaces("kwux akq zwksa"),8))


def remove_spaces(text):
    new = ""
    for character in text:
        if character != " " or character not in [i for i in range (0,10)]:
            new+=character
    return new


def remove_spaces(text):
    new = ""
    for character in text:
        if character != " " or character not in [i for i in range (0,10)]:
            new+=character
    return new


def remove_spaces(text):
    new = ""
    for character in text:
        if character != " " or character not in [i for i in range (0,10)]:
            new+=character
    return new


def remove_spaces(text):
    new = ""
    for character in text:
        if character != " " or character not in [i for i in range (0,10)]:
            new+=character
    return new


def remove_spaces(text):
    new = ""
    for character in text:
        if character != " " or character not in [i for i in range (0,10)]:
            new+=character
    return new


