from pathlib import Path

def add_extension(file_path, section_name, extension_name, url):
    new_line = f"- [{extension_name}]({url})\n"
    text = file_path.read_text()

    if new_line.strip() in text:
        return False

    header = f"## {section_name}\n"
    if header not in text:
        raise ValueError(f'Section "{section_name}" not found.')

    before, after = text.split(header, 1)
    after_lines = after.splitlines(keepends=True)

    for i, line in enumerate(after_lines):
        if line.startswith("## "):
            insert_index = i
            break
    else:
        insert_index = len(after_lines)

    updated_after = (
        after_lines[:insert_index]
        + [new_line]
        + after_lines[insert_index:]
    )

    file_path.write_text(before + header + "".join(updated_after))
    return True


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print(
            'Usage:\n'
            '  python add_extension.py "Section Name" "Extension Name" "https://link"'
        )
        sys.exit(1)

    add_extension(
        Path("chrome-extensions.md"),
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
    )
