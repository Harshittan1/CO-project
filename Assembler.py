Rtype=["add","sub","sll","slt","sltu","xor","srl","or","and"]
IType=["addi","sltiu","lw","jalr"]
Stype=["sw"]
Utype=["lui","auipc"]
Jtype=["jal"]
Btype=["beq","bne","blt","bge","bltu","bgeu"]


def decimal_to_binary(n,len): 
    n_binary =bin(n &0xffffffff).replace("0b", "")
    n_binary = n_binary.zfill(32)  
    len=32-len
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
    funct3 = {"add": "000","sub": "000","slt": "010","sltu": "011","xor": "100","sll": "001","srl": "101","or": "110","and": "111"}
    funct7 = {"add": "0000000","sub": "0100000","slt": "0000000","sltu": "0000000","xor": "0000000","sll": "0000000","srl": "0000000","or": "0000000","and": "0000000"}

    opcode_binary ="0110011"
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
        "sltiu": "0010011",
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
def assemble_u_type_instruction(instruction, rd, imm):
    opcodes = {
    "lui": "0110111",
    "auipc": "0010111"
    }
    imm_bin = twos_complement_bits(imm,32)  # Ensure immediate value is 20 bits wide
    imm_bin = imm_bin[:20]  # Take the least significant 20 bits
    rd_bin = reg_dict[rd]  # Get binary representation of rd from reg_dict
    machine_code = imm_bin+ rd_bin + opcodes[instruction]

    return machine_code
def assemble_j_type_instruction(rd, imm):
    imm = twos_complement_bits(imm,21) # Convert to two's complement
    imm=str(imm)
    x1=imm[0]
    x2=imm[10:20]
    x3=imm[9]
    x4=imm[1:9]
    rd_bin = reg_dict[rd]  # Get binary representation of the destination register
    machine_code = x1+x2+x3+x4 + rd_bin +"1101111"
    return machine_code
def assemble_b_type_instruction(instruction, rs1, rs2, imm):
    opcodes = {
        "beq": "000",
        "bne": "001",
        "blt": "100",
        "bge": "101",
        "bltu": "110",
        "bgeu": "111"
    }

    opcode = "1100011"
    funct3 = opcodes[instruction]

    # Encode rs1 and rs2 registers
    rs1_bin = reg_dict[rs1]
    rs2_bin = reg_dict[rs2]

    # Calculate the immediate offset and encode it in two's complement form
    offset = imm
    if offset < 0:
        offset = 2**13 + offset  # Convert negative offset to positive

    offset_bin = twos_complement_bits(offset, 13)

    # Extract different bits from the immediate offset for encoding
    imm_11 = offset_bin[0]  # Bit 11 of the immediate
    imm_1_to_4 = offset_bin[1:5]  # Bits [1:4] of the immediate
    imm_5_to_10 = offset_bin[5:11]  # Bits [5:10] of the immediate
    imm_12 = offset_bin[12]  # Bit 12 of the immediate

    # Concatenate the binary parts to form the complete binary instruction
    binary_instruction = imm_12 + imm_5_to_10 + rs2_bin + rs1_bin + funct3 + imm_1_to_4 + imm_11 + opcode

    return binary_instruction


with open('C:/Users/Harshit/Desktop/VSCode/Python/CO proj/input.txt', 'r') as file:
    countf = sum(1 for line in file)
with open('C:/Users/Harshit/Desktop/VSCode/Python/CO proj/input.txt', 'r') as file:
    with open('C:/Users/Harshit/Desktop/VSCode/Python/CO proj/output.txt', 'w') as output_file:
        count=0
        for line in file:
            instruction, temp1= line.split()
            if instruction in Rtype:
                rd, rs1, rs2 = temp1.split(",")
                binary_instruction = assemble_r_type_instruction(instruction, rd, rs1, rs2)
                if count!=countf-1:
                    output_file.write(binary_instruction + "\n")
                else:
                    output_file.write(binary_instruction)
                count+=1
            elif instruction in IType:
                rd, rs1, imm = temp1.split(",")
                binary_instruction = assemble_i_type_instruction(instruction, rd, rs1, int(imm))
                if count!=countf-1:
                    output_file.write(binary_instruction + "\n")
                else:
                    output_file.write(binary_instruction)
                count+=1
            elif instruction in Stype:
                rs2, rs1, imm = temp1.split(",")
                binary_instruction = assemble_s_type_binary_sw_modified(rs2, rs1, int(imm))
                if count!=countf-1:
                    output_file.write(binary_instruction + "\n")
                else:
                    output_file.write(binary_instruction)
                count+=1
            elif instruction in Utype:
                rd, imm = temp1.split(",")
                binary_instruction = assemble_u_type_instruction(instruction, rd, int(imm))  
                if count!=countf-1:
                    output_file.write(binary_instruction + "\n")
                else:
                    output_file.write(binary_instruction)
                count+=1
            elif instruction in Jtype:
                rd, imm = temp1.split(",")
                binary_instruction = assemble_j_type_instruction(rd, int(imm))
                if count!=countf-1:
                    output_file.write(binary_instruction + "\n")
                else:
                    output_file.write(binary_instruction)
                count+=1
            elif instruction in Btype:
                rs1, rs2, imm = temp1.split(",")
                binary_instruction = assemble_b_type_instruction(instruction, rs1, rs2, int(imm))       
                if count!=countf-1:
                    output_file.write(binary_instruction + "\n")
                else:
                    output_file.write(binary_instruction)
                count+=1
            else:
                if count!=countf-1:
                    output_file.write("invalid instruction" + "\n")
                else:
                    output_file.write("invalid instruction")
                count+=1
