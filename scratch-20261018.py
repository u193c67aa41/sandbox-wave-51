"""Scratch module."""

def load_lines(path):
    with open(path, encoding="utf-8") as f:
        return [ln.strip() for ln in f if ln.strip()]

def flatten(xs):
    return [y for x in xs for y in x]

if __name__ == "__main__":
    print(list(chunks(range(7), 7)))

# quick sketch
