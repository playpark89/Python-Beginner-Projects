bottles_of_beer = list(range(1, 100))
j = 98
k = 97
singular = " bottle "
plural = " bottles "

for x in bottles_of_beer:
    if j > 0:
        print((str(bottles_of_beer[j])) + plural + "of beer on the wall, " + (str(bottles_of_beer[j])) + plural + "of beer.")
        j -= 1
        if k > 0:
            print("Take one down and pass it around, " + (str(bottles_of_beer[k])) + plural + "of beer on the wall\n")
            k -= 1
        else:
            print("Take one down and pass it around, " + (str(bottles_of_beer[k])) + singular + "of beer on the wall\n")

    if j == 0:
        print((str(bottles_of_beer[j])) + singular + "of beer on the wall, " + (str(bottles_of_beer[j])) + singular + "of beer.")
        j -= 1
        print("Take one down and pass it around, no more bottles of beer on the wall\n")
    else:
        print("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall")












"""
lyrics1 = str(bottles_of_beer[0]) + " bottles of beer on the wall, " + str(bottles_of_beer) + " bottles of beer.\n"

lyrics2 = "Take one down and pass it around, " + str(bottles_of_beer) + " bottles of beer on the wall."
print(lyrics1 + lyrics2)
"""