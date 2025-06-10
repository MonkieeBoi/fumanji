from py_fumen import decode, VersionException
from sys import argv


EMOJI_MAP = {
    ord('I'): '📘',
    ord('J'): '🟦',
    ord('L'): '🟧',
    ord('O'): '🟨',
    ord('S'): '🟩',
    ord('T'): '🟪',
    ord('Z'): '🟥',
    ord('X'): '⬜',
    ord('_'): '⬛'
}


def main():
    if len(argv) < 2:
        print("invalid fumen")
        return
    fumen = argv[1]
    try:
        pages = decode(fumen)
    except VersionException:
        print("invalid fumen")
        return
    for i, page in enumerate(pages):
        print(f"Page {i+1}")
        print(page.get_field().string().translate(EMOJI_MAP))


if __name__ == "__main__":
    main()
