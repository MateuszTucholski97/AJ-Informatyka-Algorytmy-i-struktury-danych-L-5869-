def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key

# Przykładowe użycie
arr = [5, 2, 4, 6, 1, 3]
insertion_sort(arr)
print("Posortowana tablica:", arr)
