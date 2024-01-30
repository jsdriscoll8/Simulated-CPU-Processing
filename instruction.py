class Instruction:

    # Create a new Instruction with opcode, register, and immediate values.
    def __init__(self, opcode, rd, rs1, rs2, immed):
        self.opcode = opcode
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
        self.immed = immed