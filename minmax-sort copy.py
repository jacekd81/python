import random as rnd


def generate_array_or_random_ints (ArraySize, MinInt, MaxInt):
    Pointer, Array = 0, []
    while Pointer < ArraySize:
        Array.append(rnd.randrange(MinInt, MaxInt))
        Pointer += 1

    return Array


def generate_steps_for_sort(Length):
    Step, Steps = 0, [] 
    while Step < Length/2:
        Steps.append ([Step, Length-Step])
        Step += 1
    
    return Steps

def minmax_sort_an_array (UnsortedArray):
   
    WholeArrayMin = min(UnSortedArray)
    WholeArrayMax = max(UnsortedArray)

    for StartStop in (generate_steps_for_sort (len (UnsortedArray) - 1)):
        Pointer, Min, MinIndex, Max, MaxIndex = StartStop[0], WholeArrayMax, StartStop[0], WholeArrayMin, StartStop[1]

        while Pointer < StartStop[1]:
            if UnsortedArray[Pointer] <= Min:
                Min, MinIndex = UnsortedArray[Pointer], Pointer
            if UnsortedArray[Pointer] >= Max:
                Max, MaxIndex = UnsortedArray[Pointer], Pointer
            Pointer += 1

        UnSortedArray[StartStop[0]], UnsortedArray[MinIndex] = UnsortedArray[MinIndex], UnSortedArray[StartStop[0]]
        UnSortedArray[StartStop[1]], UnsortedArray[MaxIndex] = UnsortedArray[MaxIndex], UnsortedArray[StartStop[1]]
        print (UnsortedArray)
    
    return UnSortedArray


UnSortedArray = generate_array_or_random_ints (10,0,100)
print (UnSortedArray)
print (minmax_sort_an_array (UnSortedArray))