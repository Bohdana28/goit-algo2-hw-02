def find_min_max(arr):

    if len(arr) == 1:
        return arr[0], arr[0]
    
    if len(arr)==2:
        return (arr[0], arr[1]) if arr[0]<arr[1] else (arr[1], arr[0])
    
    mid = len(arr) //2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[:mid])

    overall_min = left_min if left_min<right_min else right_min
    overall_max = left_max if left_max> right_max else right_max
    
    return overall_min, overall_max

numbers = [5, 3, 9, 1, 7, -2, 8, 4]
result = find_min_max(numbers)
print("Мінімум:", result[0])
print("Максимум:", result[1])