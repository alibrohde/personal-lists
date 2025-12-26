from pathlib import Path

FILE_PATH = Path("chrome-extensions.md")
CATEGORY_HEADER = "## Productivity and Navigation"
NEW_ITEM = "- [Example Extension](https://example.com)"

def add_item():
    text = FILE_PATH.read_text()

    if NEW_ITEM in text:
        print("Item already exists.")
        return

    parts = text.split(CATEGORY_HEADER)
    if len(parts) != 2:
        raise ValueError("Category header not found.")

    before, after = parts
    updated_after = f"\n{NEW_ITEM}\n" + after.lstrip("\n")

    FILE_PATH.write_text(before + CATEGORY_HEADER + updated_after)
    print("Item added.")

if __name__ == "__main__":
    add_item()
