import random 
l = sorted([random.randint(1, 100) for _ in range(465784)])

def bin_search(l, item ):
    low = 0
    high = len(l)-1
    while low <= high:
        mid = (low+ high)//2
        if l[mid] == item:
            return mid
        elif l[mid]> item:
            high = mid - 1
        else:
            low = mid + 1

print(bin_search(l, 56))