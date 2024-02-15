def binary_search(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, low, mid-1)
        else:
            return binary_search(arr, target, mid+1, high)

    return -1


if __name__ == "__main__":

    numbers = [1, 2, 3, 4, 5]
    target = 3
    index = binary_search(numbers, target, 0, len(numbers)-1)
    print(f"The target: {target} exists at index: {index}")


