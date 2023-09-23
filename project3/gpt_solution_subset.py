def find_subsets(input_set):
    if len(input_set) == 0:
        return [[]]  # Base case: The only subset of an empty set is the empty set itself
    
    first_element = input_set[0]
    rest_of_elements = input_set[1:]
    
    # Recursive call to find subsets without the first element
    subsets_without_first = find_subsets(rest_of_elements)
    
    # Add subsets with the first element to the result
    subsets_with_first = [[first_element] + subset for subset in subsets_without_first]
    
    # Combine subsets with and without the first element
    all_subsets = subsets_with_first + subsets_without_first
    
    return all_subsets

# Example usage:
my_set = [1, 2, 3, 4]
result = find_subsets(my_set)
print(result)
