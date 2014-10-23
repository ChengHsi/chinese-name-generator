import random


def rand_ch_ch():
    head = random.randint(0xB0, 0xDF)
    body = random.randint(0xA, 0xF)
    tail = random.randint(0, 0xF)
    val = (head << 0x8) | (body << 0x4) | tail
    print head, body, tail, val
    str = "%x" % val
    return str.decode('hex').decode('big5')

if __name__ == '__main__':
    print rand_ch_ch()
