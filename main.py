import cpu

# Opcode constants
NOOP = 0
ADD = 1
ADD_I = 2
BEQ = 3
JAL = 4
LW = 5
SW = 6
RETURN = 7


# As RETURN stops all execution, comment out one test case.
def main():
    test_case_one()
    # test_case_two()


# Test case 1 as found in the assignment doc.
def test_case_one():
    core = cpu.CPU()

    # Load test instructions
    i0 = core.build_instruction(NOOP)
    i1 = core.build_instruction(ADD_I, 1, 0, None, 8)
    i2 = core.build_instruction(ADD_I, 2, 0, None, 7)
    i3 = core.build_instruction(ADD, 3, 1, 1, None)
    i4 = core.build_instruction(ADD, 4, 2, 2, None)
    i5 = core.build_instruction(BEQ, None, 3, 4, 3)
    i6 = core.build_instruction(ADD_I, 8, 0, None, 10)
    i7 = core.build_instruction(JAL, 0, None, None, 2)
    i8 = core.build_instruction(ADD_I, 8, 0, None, 1000)
    i9 = core.build_instruction(SW, None, 2, 8, 16)
    i10 = core.build_instruction(LW, 5, 8, None, 16)
    i11 = core.build_instruction(RETURN)

    # Load instructions to memory, set pc counter to 100
    core.memory[100] = i0
    core.memory[101] = i1
    core.memory[102] = i2
    core.memory[103] = i3
    core.memory[104] = i4
    core.memory[105] = i5
    core.memory[106] = i6
    core.memory[107] = i7
    core.memory[108] = i8
    core.memory[109] = i9
    core.memory[110] = i10
    core.memory[111] = i11
    core.program_counter = 100

    # CPU operation
    while True:
        instr = core.fetch_instruction()
        core.next_pc = core.program_counter + 1
        instr = core.instruction_decode(instr)
        if instr.opcode == RETURN:
            print(f"Test case 1 - end of execution. Ending register values: {core.registers} \n"
                  f"Memory index 26: {core.memory[26]}")
        core.execute(instr)
        core.program_counter = core.next_pc


# Testcase #2 as found in the assignment doc.
def test_case_two():
    core = cpu.CPU()

    # Build instructions
    i0 = core.build_instruction(ADD_I, 1, 0, None, 5)
    i1 = core.build_instruction(ADD_I, 2, 0, None, 6)
    i2 = core.build_instruction(ADD, 3, 2, 1, None)
    i3 = core.build_instruction(ADD, 4, 1, 2, None)
    i4 = core.build_instruction(BEQ, None, 3, 4, 3)
    i5 = core.build_instruction(ADD_I, 8, 0, None, 10)
    i6 = core.build_instruction(JAL, 0, None, None, 2)
    i7 = core.build_instruction(ADD_I, 8, 0, None, 30)
    i8 = core.build_instruction(SW, None, 3, 8, 10)
    i9 = core.build_instruction(LW, 5, 8, None, 10)
    i10 = core.build_instruction(RETURN)

    core.memory[100] = i0
    core.memory[101] = i1
    core.memory[102] = i2
    core.memory[103] = i3
    core.memory[104] = i4
    core.memory[105] = i5
    core.memory[106] = i6
    core.memory[107] = i7
    core.memory[108] = i8
    core.memory[109] = i9
    core.memory[110] = i10
    core.program_counter = 100

    # CPU operation
    while True:
        instr = core.fetch_instruction()
        core.next_pc = core.program_counter + 1
        instr = core.instruction_decode(instr)
        if instr.opcode == RETURN:
            print(f"Test case 2 - end of execution. Ending register values: {core.registers} \n"
                  f"Memory index 40: {core.memory[40]}")
        core.execute(instr)
        core.program_counter = core.next_pc


if __name__ == '__main__':
    main()