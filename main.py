names = ["Vera", "Chuck", "Samantha", "Roberto", "Joe", "Dave", "Tina", "Ringo"]
salaries = [2000, 18000, 18000, 21000, 2000, 2200, 2300, 1900]

count = len(names)
for c in range(count):
    print(f"{names[c]}, %{salaries[c]}")