nums = list(map(int, input("Enter numbers: ").split()))
print(['over' if n>100 else n for n in nums])
