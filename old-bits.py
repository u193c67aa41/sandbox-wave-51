"""Quick helpers."""

def flatten(xs):
    return [y for x in xs for y in x]

def clamp(value, low, high):
    return max(low, min(value, high))

if __name__ == "__main__":
    print(clamp(8, 0, 12))

# see notes
