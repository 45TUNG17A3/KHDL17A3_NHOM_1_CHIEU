def check_chebyshev_conditions(table):
    # Extract Xi and P from the table
    Xi, P = table

    # Calculate the mean and variance
    mean = sum(Xi[i] * P[i] for i in range(len(Xi)))
    variance = sum((Xi[i] - mean) ** 2 * P[i] for i in range(len(Xi)))

    # Check if variance exists (greater than zero)
    return variance > 0

# Define the tables
table_a = ([-3**0.5, 0, 3**0.5], [1/3, 1/3, 1/3])
table_b = ([a, i, -i], [a/(2*i+1), i/(2*i+1), -i/(2*i+1)])

# Check conditions for both tables
result_a = check_chebyshev_conditions(table_a)
result_b = check_chebyshev_conditions(table_b)

print(f"Can apply Chebyshev's inequality for Table (a): {result_a}")
print(f"Can apply Chebyshev's inequality for Table (b): {result_b}")