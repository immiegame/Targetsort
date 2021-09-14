"""
This is a python implementation of the quick sort algorithm,
for use in video games.

Specifically, this implementation will be used to sort an array
into order of closest to furthest to the inputted number value.
"""


def prepareArray(array, targetValue, low, high):
    pivot = array[high]
    item = low - 1

    for i in range(low, high):

        # this checks if the difference between the current index to the target is less than the difference from pivot to the target
        if abs(array[i] - targetValue) <= abs(pivot - targetValue):
            item += 1
            (array[item], array[i]) = (array[i], array[item])

    (array[item + 1], array[high]) = (array[high], array[item + 1])
    print(array)
    return item + 1


def TargetSort(targetValue, arrayToSort, low, high):
    if low < high:
        pivot = prepareArray(arrayToSort, targetValue, low, high)

        TargetSort(targetValue, arrayToSort, low, pivot - 1)
        TargetSort(targetValue, arrayToSort, pivot + 1, high)


if __name__ == '__main__':
    targetValue = 1
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    TargetSort(4, arr, 0, len(arr) - 1)
    print(arr)

    
