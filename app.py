FILE_PATH = "./data/output.txt"

with open(FILE_PATH, "r") as f:
    lines = f.readlines()
    last_value = int(lines[-1].strip())

with open(FILE_PATH, "a") as f:
    f.write("\n")
    f.write(f"{last_value + 1}")

with open(FILE_PATH, "r") as f:
    print("File contents:\n")
    print(f.read())
