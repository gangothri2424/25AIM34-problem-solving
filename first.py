def to_8bit_twos_complement(n):
    """Convert a signed integer to 8-bit 2's complement binary string."""
    if n < 0:
        n = (1 << 8) + n  # Compute two's complement for negative
    return format(n & 0xFF, '08b')

def twos_complement_to_int(b):
    """Convert 8-bit 2's complement binary string to signed integer."""
    if b[0] == '0':
        return int(b, 2)
    else:
        return int(b, 2) - (1 << 8)

def add_8bit_binary(bin1, bin2):
    """Add two 8-bit binary strings representing signed numbers."""
    sum_int = twos_complement_to_int(bin1) + twos_complement_to_int(bin2)
    # Detect overflow: result not in -128 to 127
    overflow = not (-128 <= sum_int <= 127)
    # Limit result to 8 bits
    result_bin = to_8bit_twos_complement(sum_int)
    # Convert back to signed int for final result
    result_int = twos_complement_to_int(result_bin)
    return result_bin, result_int, overflow

def subtract_8bit_binary(bin1, bin2):
    """Subtract bin2 from bin1 in 8-bit 2's complement."""
    int1 = twos_complement_to_int(bin1)
    int2 = twos_complement_to_int(bin2)
    diff_int = int1 - int2
    overflow = not (-128 <= diff_int <= 127)
    result_bin = to_8bit_twos_complement(diff_int)
    result_int = twos_complement_to_int(result_bin)
    return result_bin, result_int, overflow

def print_operation(op_desc, a, b, operation):
    print(f"Operation: {op_desc}")
    bin_a = to_8bit_twos_complement(a)
    bin_b = to_8bit_twos_complement(b)

    print(f"Operand A: {a} -> binary: {bin_a}")
    print(f"Operand B: {b} -> binary: {bin_b}")

    if operation == 'add':
        res_bin, res_int, overflow = add_8bit_binary(bin_a, bin_b)
        print(f"Result binary (A + B): {res_bin}")
    elif operation == 'subtract':
        res_bin, res_int, overflow = subtract_8bit_binary(bin_a, bin_b)
        print(f"Result binary (A - B): {res_bin}")
    else:
        raise ValueError("Unsupported operation")

    print(f"Result decimal: {res_int}")
    if overflow:
        print("Overflow detected!")
    else:
        print("No overflow.")
    print("-" * 40)

# Test cases:
print_operation("+48 + (+23)", 48, 23, 'add')
print_operation("(-46) - (-29)", -46, -29, 'subtract')
