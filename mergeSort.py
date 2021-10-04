def merge_sort(test_list):
    if len(test_list) > 1:
        mid = len(test_list)//2
        left_half = test_list[:mid]
        right_half = test_list[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                test_list[k] = left_half[i]
                i += 1
            else: 
                test_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            test_list[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            test_list[k] = right_half[j]
            j += 1
            k += 1
    return test_list

# Code to test function
sample_list = [1, 5, 7, 6, 2]
print(f"Unsorted list: {sample_list}")
merge_sort(sample_list)
print(f"Sorted list: {sample_list}")