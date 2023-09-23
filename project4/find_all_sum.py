def find_all_sum(collection, Number):
    # Base case: If N becomes 0, we've found a combination, so print it
    if Number == 0:
        print(collection)
        return

    # Recursive case:
    for i in range(1, Number + 1):
        # Try adding each number from 1 to N to the list
        collection.append(i)
        # Recursively find combinations with the updated list and reduced N
        find_all_sum(collection, Number - i)
        # Remove the last element to backtrack and try other combinations
        collection.pop()

# Example usage:
find_all_sum([], 5)
