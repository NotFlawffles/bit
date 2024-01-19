import sys


def main(value: any) -> None:
    as_raw = 0
    as_hex = ""
    as_bin = 0
    as_chr = ''
    is_text = False

    if value[0].isalpha():
        as_raw = ord(value[0])
        as_hex = hex(as_raw)
        as_bin = bin(as_raw)
        is_text = len(value) > 1

        for char in value:
            if not(char.isalpha()):
                is_text = False

    elif value.startswith("0x"):
        as_raw = int(value, 0x10)
        as_hex = hex(as_raw)
        as_bin = bin(as_raw)

    elif value.startswith("0b"):
        as_raw = int(value, 0x2)
        as_hex = hex(as_raw)
        as_bin = bin(as_raw)

    else:
        as_raw = value
        as_hex = hex(int(as_raw))
        as_bin = bin(int(as_raw))

    try:
        as_chr = chr(int(as_raw))

        if as_chr == '\n':
            as_chr = '\\n'
    except:
        pass

    primitive_sizes = {
        1: "bit",
        4: "nibble",
        8: "byte",
        16: "word",
        32: "dword",
        64: "qword"
    }

    bits_count = len(str(as_bin)) - 2
    bits_identifier = ""
    
    if bits_count in primitive_sizes:
        bits_identifier = f"({primitive_sizes[bits_count]})"

    print(f"'{as_chr}'\t{as_raw}\t{as_hex}\t{as_bin}\t{bits_count} bit{'s' if bits_count > 1 else ''} {bits_identifier}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
