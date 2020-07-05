def findSmallest(arr):
    smallest = arr[0]
    smallestIndex = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallestIndex = i
    
    return smallestIndex


music = [15, 85, 74, 3, 13, 75, 96, 5, 45]

def selectionSort(arr):
    sorted_music = []
    for i in range(len(music)):
        smal_music = findSmallest(music)
        sorted_music.append(music.pop(smal_music))
    return sorted_music


print(selectionSort(music))