def main():
    n = int(input("Enter array size: "))
    arr = []
    
    print("Enter array elements:")
    for i in range(n):
        arr.append(int(input()))
    
    p = 0
    for i in range(n):
        if arr[i] != 0:
            arr[p] = arr[i]
            p += 1
    
    while p < n:
        arr[p] = 0
        p += 1
    
    print("After moving zeroes:", end=" ")
    for x in arr:
        print(x, end=" ")
    print()

if __name__ == "__main__":
    main()
