fibonacci_sequence = [1, 1]
upper_bound = int(input("Input highest number:\n"))
i = 1
print(f"\n{fibonacci_sequence[0]}\n{fibonacci_sequence[1]}")
while fibonacci_sequence[i] <= upper_bound:
    fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i])
    print(fibonacci_sequence[i]);
    i += 1