import os

# One-Line Laugh Sprint: single original everyday-life line, 134 chars.
LINE = "My plants have started leaning toward the window when I walk in, which feels less like photosynthesis and more like an escape attempt."

def main():
    os.makedirs("/output", mode=0o755, exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
