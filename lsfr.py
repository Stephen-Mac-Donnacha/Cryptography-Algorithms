def lsfr():
    # 2 initialization vectors for the problem
    init_vector_1 = 0b11001010110011001010011010110010
    init_vector_2 = 0b00110110111100101001010010011010

    for i in range(20):
        # XOR the last 2 bits of each input vector to produce the bit of the output string
        output_bit = ((init_vector_1 & 1) ^ (init_vector_2 & 1))

        # res will store our output bit string
        res = 0
        res = ((res << 1) | output_bit)

        # Update init vector 1
        # Using taps 16, 12, 8
        # Then shift the vector right by 1 and then add the new bit to the start via shifting it 31 bits to the left
        new_bit_1 = (init_vector_1 ^ (init_vector_1 >> 16) ^ (init_vector_1 >> 20) ^ (init_vector_1 >> 24)) & 1
        init_vector_1 = (init_vector_1 >> 1) | (new_bit_1 << 31)

        # Update init vector 2
        # Using taps 5, 22, 26
        # Then do the same bitwise shifting as with the other vector
        new_bit_2 = (init_vector_2 ^ (init_vector_2 >> 5) ^ (init_vector_2 >> 10) ^ (init_vector_2 >> 6)) & 1
        init_vector_2 = (init_vector_2 >> 1) | (new_bit_2 << 31)

        print(res)

