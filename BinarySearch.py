from random import randint

def BinarySearch(sortedList, item):
    low = 0
    high = len(sortedList) - 1
    numberOfTry = 0
    guess = 0


    while guess != item:
        mid = (low + high) // 2
        guess = mid
        numberOfTry += 1

        if guess < item:
            low = guess + 1
            print (f"{guess} is too low")
        elif guess > item:
            high = guess - 1
            print (f"{guess} is too high")
    
    return numberOfTry


# listLenght = randint(100,500001)
listLenght = 1000
numberToGuess = randint(0,listLenght)
mySortedList = [a for a in range(0, listLenght)]
result = BinarySearch(mySortedList, numberToGuess)

print(f"You found the mysterious number ({numberToGuess}) in {result} try")
print(f"The sorted list was {listLenght} tall")
        