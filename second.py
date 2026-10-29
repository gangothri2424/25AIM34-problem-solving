def ror(binary, positions):
    print("\nRotate Right Without Carry (ROR)")
    print("Original number:", binary)

    for i in range(positions):
        last_bit = binary[-1]
        binary = last_bit + binary[:-1]
        print("Step", i + 1, ":", binary)

    print("Final result:", binary)
    return binary


def rcr(binary, carry, positions):
    print("\nRotate Right With Carry (RCR)")
    print("Original number:", binary)
    print("Initial carry:", carry)

    for i in range(positions):
        last_bit = binary[-1]
        binary = carry + binary[:-1]
        carry = last_bit
        print("Step", i + 1, ":", binary, "| Carry:", carry)

    print("Final result:", binary)
    print("Final carry:", carry)
    return binary, carry


number = "11010101"

result_ror = ror(number, 2)
result_rcr, final_carry = rcr(number, "0", 2)

print("\nVerification")
print("ROR correct:", result_ror == "01110101")
print("RCR correct:", result_rcr == "01101010" and final_carry == "1")