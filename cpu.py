import sys
import instruction


class CPU:
    # Class constant definitions
    NUM_REGISTERS = 16
    MEM_SIZE = 65536

    # Construct a new CPU with empty memory and register values.
    def __init__(self):
        self.program_counter = 0
        self.next_pc = 0
        self.memory = [0] * CPU.MEM_SIZE
        self.registers = [0] * CPU.NUM_REGISTERS

    def build_instruction(self, opcode, rd=None, rs1=None, rs2=None, immed=None):
        instr = opcode << 28
        if rd is not None:
            instr = instr + (rd << 24)
        if rs1 is not None:
            instr = instr + (rs1 << 20)
        if rs2 is not None:
            instr = instr + (rs2 << 16)
        if immed is not None:
            instr = instr + immed
        return instr

    # Fetch the instruction at the current program counter; update the PC.
    def fetch_instruction(self):
        return self.memory[self.program_counter]

    # Decode an instruction using bitwise operators from a 32-bit integer.
    def instruction_decode(self, instr: int):
        immed = int(instr & 65535)
        rs2 = int((instr >> 16) & 15)
        rs1 = int((instr >> 20) & 15)
        rd = int((instr >> 24) & 15)
        opcode = int((instr >> 28) & 15)

        return instruction.Instruction(opcode, rd, rs1, rs2, immed)

    # Execute an instruction.
    def execute(self, instr: instruction.Instruction):
        opcode = instr.opcode

        match opcode:
            case 0:
                self.__noop()
            case 1:
                self.__add(instr.rd, instr.rs1, instr.rs2)
            case 2:
                self.__add_i(instr.rd, instr.rs1, instr.immed)
            case 3:
                self.__beq(instr.rs1, instr.rs2, instr.immed)
            case 4:
                self.__jal(instr.rd, instr.immed)
            case 5:
                self.__lw(instr.rd, instr.rs1, instr.immed)
            case 6:
                self.__sw(instr.rs1, instr.rs2, instr.immed)
            case 7:
                self.__return()


    # No operation: do nothing.
    def __noop(self):
        pass

    # Add the contents of rs1 and rs2; place in rd
    def __add(self, rd: int, rs1: int, rs2: int):
        if rd != 0:
            self.registers[rd] = self.registers[rs1] + self.registers[rs2]

    # Add the contents of rs1 and immed; place in rd
    def __add_i(self, rd: int, rs1: int, immed: int):
        if rd != 0:
            self.registers[rd] = self.registers[rs1] + immed

    # Compare: if rs1 == rs2, imcrement the PC by immed
    def __beq(self, rs1: int, rs2: int, immed: int):
        if self.registers[rs1] == self.registers[rs2]:
            self.next_pc = self.program_counter + immed

    # Place (pc + 1) into rd, put (pc + immed) in next pc
    def __jal(self, rd: int, immed: int):
        if rd != 0:
            alu_result = self.program_counter + 1
            self.registers[rd] = alu_result

        self.next_pc = self.program_counter + immed

    # Get the memory index val(rs1) + immed; place its contents into rd
    def __lw(self, rd: int, rs1: int, immed: int):
        if rd != 0:
            eff_address = immed + self.registers[rs1]
            self.registers[rd] = self.memory[eff_address]

    # Place contents of rs1 into register (val(rs2) + immed)
    def __sw(self, rs1: int, rs2: int, immed: int):
        eff_address = self.registers[rs2] + immed
        self.memory[eff_address] = self.registers[rs1]

    def __return(self):
        sys.exit()