def binarySearch(arr, key):
    low = 0;
    high = len(arr)-1;
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid

        if arr[mid] < key:
            low = mid + 1

        elif arr[mid] > key:
            high = mid -1
    return -1

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,29,20];
print(binarySearch(arr,10))