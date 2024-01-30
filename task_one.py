import random



def quick_sort(array):
    sorted_array = []
    sorted_array = array[:]

    if len(sorted_array) == 0:
        return sorted_array

    pivot = sorted_array[0]

    lower_array = [element for element in sorted_array if element < pivot]
    top_array = [element for element in sorted_array if element > pivot]

    return (
        quick_sort(lower_array) + 
        [element for element in sorted_array if element == pivot] +
        quick_sort(top_array)
    )


def main():
    ifellow_arr = []
    for i in range(100):
        ifellow_arr.append(float(random.random()))
    ifellow_arr = quick_sort(ifellow_arr)
    
    print(ifellow_arr[0])
    print(ifellow_arr[len(ifellow_arr)//2])
    print(ifellow_arr[-1])

if __name__ == "__main__":
    main()