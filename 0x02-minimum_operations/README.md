We need to find the factors of n to understand the pattern of operations.
If n is prime, it's impossible to achieve and we return 0.
Otherwise, we iteratively divide n by its factors to find the minimum operations.
For each factor, we calculate the operations required to achieve that factor,
then recursively calculate the operations required for the quotient.
