import string


def __decode_cal(bin_str:str):
    s = []
    for i in range(len(bin_str)):
        if bin_str[i] == '1':
            t = 128
            for _ in range(i):
                t /= 2
            s.append(t)
    return int(sum(s))

def __zero_adder(bin_str:str):
    if len(bin_str) < 8:
        return '0'*(8 - len(bin_str)) + bin_str

def __calculator(bin_str:str):
    if len(bin_str) == 4:
        bin_str += '00'
    elif len(bin_str) == 2:
        bin_str += '0000'
    s = []
    for i in range(len(bin_str)):
        if bin_str[i] == '1':
            t = 32
            for _ in range(i):
                t /= 2
            s.append(t)
    return int(sum(s))

def __chr(bin_str:str):
    if len(bin_str) == 4:
        return alphabet[__calculator(bin_str)] + '='
    elif len(bin_str) == 2:
        return alphabet[__calculator(bin_str)] + '=='
    else: return alphabet[__calculator(bin_str)]


alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'


def encoder(text:str):
    binarys = [bin(ord(i))[2:] for i in text]
    for i in range(len(binarys)):
        if len(binarys[i]) < 8:
            binarys[i] = '0'*(8 - len(binarys[i])) + binarys[i]
    binary_string = ''.join(binarys)
    binarys.clear()
    for n in range(6, len(binary_string)+6, 6):
        binarys.append(binary_string[n-6:n])
    encoded = ''.join([__chr(b) for b in binarys])
    return encoded
        

def decoder(text:str):
    n = text.count('=')
    text = text.replace('=', '')
    binarys = [__zero_adder(str(bin(alphabet.index(i))[2:])) for i in text]
    binary_str = ''.join(binarys)
    if n:
        binary_str = binary_str[:(n*2)*-1]
    binarys = [binary_str[i-8:i] for i in range(8, len(binary_str)+8, 8)]
    binary_str = ''
    for i in binarys:
        binary_str += i[2:]
    decoded = ''.join([chr(__decode_cal(binary_str[i-8:i])) for i in range(8, len(binary_str)+8, 8)])
    return decoded
    


