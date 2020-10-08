import random as rnd


def generate_array_or_random_ints (ArraySize, MinInt, MaxInt):
    Pointer, Array = 0, []
    while Pointer < ArraySize:
        Array.append(rnd.randrange(MinInt, MaxInt))
        Pointer += 1

    return Array

def bouble_sort_an_array (UnsortedArray):
    Sorted = False

    while Sorted == False:
        Pointer, Sorted = 1, True

        while Pointer  < len(UnsortedArray):       
            if UnsortedArray[Pointer-1] > UnsortedArray[Pointer]:
                UnsortedArray[Pointer-1], UnsortedArray[Pointer] = UnsortedArray[Pointer], UnsortedArray[Pointer-1]
                Sorted = False
            Pointer += 1

    return UnSortedArray


UnSortedArray = generate_array_or_random_ints (100,0,100)
print (UnSortedArray)
print (bouble_sort_an_array (UnSortedArray))