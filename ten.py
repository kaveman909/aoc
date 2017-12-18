from collections import deque

length_sequence = '183,0,31,146,254,240,223,150,2,206,161,1,255,232,199,88'


def rotate(lst, x):
    d = deque(lst)
    d.rotate(x)
    lst[:] = d


def reverse(lst, start, end):
    lst[start:end] = lst[start:end][::-1]
    return lst


def knot_hash(length_seq, print_out=False):
    length_seq = [ord(c) for c in length_seq]
    length_seq.extend([17, 31, 73, 47, 23])
    nums = list(range(256))
    skip_size = 0
    rotation_count = 0

    for i in range(64):
        for length in length_seq:
            reverse(nums, 0, length)
            rotation_count += length + skip_size
            rotate(nums, -(length + skip_size))
            skip_size += 1
    rotate(nums, rotation_count)

    dense_hash = []
    for i in range(16):
        xor = nums[i * 16]
        for j in range(1, 16):
            xor = xor ^ nums[i * 16 + j]
        dense_hash.append(xor)

    hex_hash = ""
    for i in dense_hash:
        hex_hash += '{0:02x}'.format(i)
    if print_out is True:
        print(hex_hash)
    return dense_hash

knot_hash(length_sequence, print_out=True)
