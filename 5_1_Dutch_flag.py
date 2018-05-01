RED, WHITE, BLUE = range(3)

def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    # 1st: group elemetns smaller than pivot.
    smaller = 0
    for i in  range(len(A)):
        # Search for smaller elements
        if A[j] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    # 2nd: group elements larger than pivotself.
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] =  A[larger], A[i]
            larger -= 1
