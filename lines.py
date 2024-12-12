import sys


def main():
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        if not file_path.endswith(".py"):
            print(f"Not a python file")
            sys.exit(1)
        try:
            file =open(file_path, "r")
        except FileNotFoundError:
            print(f"File doesn't exist")
            sys.exit(1)
        else:
            program_lines = [line.strip(" ").strip("\t") for line in file.readlines()]

            formated_lines = [line for line in program_lines if not line.startswith("#") and not line.isspace()]
            print(len(formated_lines))
            return len(formated_lines)
        finally:
            file.close()
    elif len(sys.argv) < 2:
        print(f"Too few command-line arguments")
        sys.exit(1)
    else:
        print(f"Too many command-line arguments")
        sys.exit(1)

if __name__ == "__main__":
    main()