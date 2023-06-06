from enum import Enum

class Input_Type(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Accessing enum values
print(Color.RED)         # Color.RED
print(Color.RED.value)   # 1

# Iterating over enum values
for color in Color:
    print(color)

# Output:
# Color.RED
# Color.GREEN
# Color.BLUE