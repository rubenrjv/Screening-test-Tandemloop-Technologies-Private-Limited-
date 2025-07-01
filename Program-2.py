def generate_odd_series(n: int):
    series = []
    for i in range(n):
        series.append(2 * i + 1)
    return series

user_input = int(input("Enter the number of terms (a): "))


result = generate_odd_series(user_input)

print("Output:", ", ".join(map(str, result)))
