def decimal_to_binary(n,len): 
    n_binary =bin(n &0xffffffff).replace("0b", "")
    n_binary = n_binary.zfill(32)  
    len=32-len
    print(n_binary)
    return n_binary[len:]

reg_dict = {
    "zero": "00000", "ra": "00001", "sp": "00010", "gp": "00011", "tp": "00100",
    "t0": "00101", "t1": "00110", "t2": "00111", "s0": "01000", "fp": "01000",
    "s1": "01001", "a0": "01010", "a1": "01011", "a2": "01100", "a3": "01101",
    "a4": "01110", "a5": "01111", "a6": "10000", "a7": "10001", "s2": "10010",
    "s3": "10011", "s4": "10100", "s5": "10101", "s6": "10110", "s7": "10111",
    "s8": "11000", "s9": "11001", "s10": "11010", "s11": "11011", "t3": "11100",
    "t4": "11101", "t5": "11110", "t6": "11111"
}

def twos_complement(num):
    return bin(2**12 + num)[2:].zfill(12)
    

def twos_complement_bits(num,bits):
    return bin(num & (2**bits - 1))[2:].zfill(bits)


def assemble_r_type_instruction(instruction, rd, rs1, rs2):
    funct3 = {"ADD": "000","SUB": "000","SLT": "010","SLTU": "011","XOR": "100","SLL": "001","SRL": "101","OR": "110","AND": "111"}
    funct7 = {"ADD": "0000000","SUB": "0100000","SLT": "0000000","SLTU": "0000000","XOR": "0000000","SLL": "0000000","SRL": "0000000","OR": "0000000","AND": "0000000"}

    opcode_binary ="0110011"
    print (opcode_binary)
    rd_binary = reg_dict[rd]
    rs1_binary = reg_dict[rs1]
    rs2_binary = reg_dict[rs2]
    funct3_binary = funct3[instruction]
    funct7_binary = funct7[instruction]

    # Concatenate all parts to form the binary instruction
    binary_instruction = funct7_binary + rs2_binary + rs1_binary + funct3_binary + rd_binary + opcode_binary
    return binary_instruction


def assemble_i_type_instruction(instruction, rd, rs1, imm):
    opcodes = {
        "lw": "0000011",
        "addi": "0010011",
        "sltiu": "0010011 ",
        "jalr": "1100111",    
    }
    funct3 = {
        "lw": "010",    
        "addi": "000",
        "sltiu": "011",
        "jalr": "000",
    }
    # Extracting the instruction name without any operands
    instruction_name = instruction.split()[0]
    opcode = opcodes[instruction_name]
    funct3_binary = funct3[instruction_name]
    # Convert register numbers and immediate value to binary strings
    rd_binary = reg_dict[rd]
    rs1_binary = reg_dict[rs1]
    imm_binary = decimal_to_binary(int(imm), 12)  # Sign-extend the immediate value
    # Concatenate all parts to form the binary instruction
    binary_instruction = imm_binary[:12] + rs1_binary + funct3_binary+ rd_binary+ opcode
    return binary_instruction

def assemble_s_type_binary_sw_modified(rs2, rs1, imm):
    if imm < -2048 or imm > 2047:
        return None

    rs2_binary = reg_dict[rs2]
    rs1_binary = reg_dict[rs1]
    opcode = '0100011'

    if imm < 0:
        imm = (1 << 12) + imm

    imm_upper = decimal_to_binary(imm >> 5, 7)
    imm_lower = decimal_to_binary(imm & 0x1F, 5)

    binary_instruction = f"{imm_upper} {rs2_binary} {rs1_binary} 010 {imm_lower} {opcode}"

    return binary_instruction

def assemble_u_type_instruction(opcode, rd, imm):
    opcodes = {
    "lui": "0110111",
    "auipc": "0010111"
    }
    imm_bin = twos_complement_bits(imm,32)  # Ensure immediate value is 20 bits wide
    imm_bin = imm_bin[:20]  # Take the least significant 20 bits
    rd_bin = reg_dict[rd]  # Get binary representation of rd from reg_dict
    machine_code = imm_bin+ rd_bin + opcodes[opcode]

    return machine_code

def assemble_j_type_instruction(rd, imm):
    imm = twos_complement_bits(imm,21) # Convert to two's complement
    imm=str(imm)
    #print(imm)
    x1=imm[0]
    x2=imm[10:20]
    x3=imm[9]
    x4=imm[1:9]
    rd_bin = reg_dict[rd]  # Get binary representation of the destination register
    machine_code = x1+x2+x3+x4 + rd_bin +"1101111"
    return machine_code

opcode = "lui"#input()
rd = "t0"#input()  # Accept register name directly
imm = 100 #int(input())



binary_instruction = assemble_u_type_instruction(opcode, rd, imm)
print(binary_instruction)
