def largest_subsequence_divisible_by_5(stone_values):
    n = len(stone_values)
    max_length = 0
    start_index = -1
    end_index = -1

    # Iterate through all possible starting points
    for i in range(n):
        current_sum = 0
        # Extend the subsequence from index i
        for j in range(i, n):
            current_sum += stone_values[j]
            # Check if the sum is divisible by 5
            if current_sum % 5 == 0:
                current_length = j - i + 1
                if current_length > max_length:
                    max_length = current_length
                    start_index = i
                    end_index = j

    # Return the result
    if max_length > 0:
        return stone_values[start_index:end_index + 1]
    else:
        return []

# Example Usage
stones = [2, 3, 10, 6, 5, 1]
result = largest_subsequence_divisible_by_5(stones)
print("Largest subsequence divisible by 5:", result)
