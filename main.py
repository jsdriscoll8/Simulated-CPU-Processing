import cpu
def main():
    core = cpu.CPU()

    while True:
        core.fetch_instruction()


if __name__ == '__main__':
    main()