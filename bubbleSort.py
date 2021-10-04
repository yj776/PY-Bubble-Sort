def bubble_sort(test_list):

    swapped = True

    while(swapped):
        swapped=False

        for i in range(len(test_list)-1):
            for j in range(len(test_list) - 1):
                if test_list[j] > test_list[j+1]:
                    test_list[j], test_list[j+1] = test_list[j+1], test_list[j]
                    swapped = True
        
        return test_list

# Code to test function
sample_list = [1, 5, 2, 6, 7]
print(f"Unsorted list: {sample_list}")
bubble_sort(sample_list)
print(f"Sorted list: {sample_list}")