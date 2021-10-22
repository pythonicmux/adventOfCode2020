import sys

floating_bits = []
mem = {}

# Zero out n's i'th bit from the left of the LSB
def reset_bit(n, i):
    n = ~n
    n |= (1 << i)
    n = ~n
    return n

# Set n's i'th bit from the left of the LSB
def set_bit(n, i):
    n |= (1 << i)
    return n

# DFS all potential values of a number with floating bits
# at specified indices
def get_potential_values(val, floating_bits):
    output = set()
    if(floating_bits == []):
        output.add(val)
        # print(val, floating_bits, output)
        return output

    vals = get_potential_values(val, floating_bits[1:])

    for val in vals:
        output.add(reset_bit(val, floating_bits[0]))
        output.add(set_bit(val, floating_bits[0]))

    # print(val, floating_bits, output)
    return output

with open('day14.txt', 'r') as f:
    for line in f:
        if(line.startswith("mask")):
            floating_bits = []
            mask = line.split()[2][::-1]
            # print("new mask:", mask)
            for i in range(len(mask)):
                if mask[i] == 'X':
                    floating_bits.append(i)
            # print("floating bits:", floating_bits)

        else:
            addr_word = line.split()[0]
            address = int(addr_word[addr_word.index('[') + 1 : addr_word.index(']')])
            # print(address, "{0:b}".format(address))
            for i in range(len(mask)):
                if mask[i] == '1':
                    address = set_bit(address, i)
            # print(address, "{0:b}".format(address))
            addresses = get_potential_values(address, floating_bits)
            # print(addresses)
            # print("\n")

            val = int(line.split()[2])
            for a in addresses:
                mem[a] = val

print(mem)

s = 0
for k in mem:
    s += mem[k]

print(s)
