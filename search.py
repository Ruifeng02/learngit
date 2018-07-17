def search(lst, x):
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    return -1

def bi_search(lst, x):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid =(low+high)/2
        if lst[mid] == x:
            return mid
        elif lst[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def swap(lst, a, b):
    sp = lst[a]
    lst[a] = lst[b]
    lst[b] = sp
def selection_sort(lst):
    top = len(lst) - 1
    is_exchange = True
    while is_exchange:
        is_exchange = False
        for i in range(top):
            if lst[i] > lst[i+1]:
                is_exchange = True
                swap(lst, i, i+1)
        top -= 1

lst = [10, 5 , 8, 13]
selection_sort(lst)
print lst
