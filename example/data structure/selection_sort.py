data = [89,34,23,78,67,100,66,29,79,55,78,88,92,96,96,23]

def SelectionSort(data):
    n =len(data)
    for i in range(n):
        min_dix = i 
        for  j in range(i+1, n):
            if data[j] < data[min_dix]:
                min_dix = j
        if min_dix != i:
            data[i], data[min_dix] =data[min_dix], data[i]
    return data

print(SelectionSort(data))