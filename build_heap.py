# python3


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(int((n/2)-1),-1,-1):
        l = 2*i+1
        r = 2*i+2
        if l < n and data[l] < data[i]:
            smallest = l
        else:
            smallest = i
        if r < n and data[r] < data[smallest]:
            smallest = r
        if smallest != i:
            data[i], data[smallest] = data[smallest], data[i]
            swaps.append((i,smallest))
        i=smallest
        l = 2*i+1
        r = 2*i+2
        if l < n and data[l] < data[i]:
            smallest = l
        else:
            smallest = i
        if r < n and data[r] < data[smallest]:
            smallest = r
        if smallest != i:
            data[i], data[smallest] = data[smallest], data[i]
            swaps.append((i,smallest))
    return swaps


def main():
    print("Input Mode: ")
    mode = input()
    if "I" in mode:
        print("Input: ")
        n = int(input())
        data = list(map(int, input().split()))
    else:
        print("Input File: ")
        filename= input()
        if "a" in filename:
            print("Filename containing a is not allowed")
            return
        folder = './tests/'
        file = open(folder + filename, 'r')
        n = int(file.readline())
        data = list(map(int, file.readline().split()))
    
    assert len(data) == n
    swaps = build_heap(data)

    

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
