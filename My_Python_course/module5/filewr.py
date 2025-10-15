
from pathlib import Path

path = Path(__file__).parent / "fake.txt"
# f = open(path, "r")
# d = f.read()

# try:
#     name = "Nick"
#     f.write(name)

# print(d)

with open(path, "r") as file:
    data = []
    data = file.read()
    

print(data)