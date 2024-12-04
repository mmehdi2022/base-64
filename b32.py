import string


alphabets = string.ascii_uppercase + '234567'

def __enc_cal(bin_str:str):
    if len(bin_str) < 5:
        bin_str += '0'*(5-len(bin_str))
    s = []
    for i in range(len(bin_str)):
        if bin_str[i] == '1':
            t = 16
            for _ in range(i):
                t /= 2
            s.append(t)
    return int(sum(s))

def __dec_cal(bin_str:str):
    s = []
    for i in range(len(bin_str)):
        if bin_str[i] == '1':
            t = 128
            for _ in range(i):
                t /= 2
            s.append(t)
    return int(sum(s))

def encoder(text:str):
    binarys = [str(bin(ord(i)))[2:] for i in text]
    for i in range(len(binarys)):
        if len(binarys[i]) < 8:
            binarys[i] = '0'*(8-len(binarys[i])) + binarys[i]
    binary_str = ''.join(binarys)
    binarys.clear()
    for i in range(5, len(binary_str)+5, 5):
        binarys.append(binary_str[i-5:i])
    encoded = ''
    for i in binarys:
        if len(i) == 3:
            encoded += alphabets[__enc_cal(i)] + '======' 
        elif len(i) == 1:
            encoded += alphabets[__enc_cal(i)] + '===='
        elif len(i) == 4:
            encoded += alphabets[__enc_cal(i)] + '==='
        elif len(i) == 2:
            encoded += alphabets[__enc_cal(i)] + '='
        else:
            encoded += alphabets[__enc_cal(i)]
    return encoded


def decoder(text:str):
    n = text.count('=')
    text = text.replace('=','')
    binarys = [str(bin(alphabets.index(i))[2:]) for i in text]
    for i in range(len(binarys)):
        if len(binarys[i]) < 5:
            binarys[i] = '0'*(5 - len(binarys[i])) + binarys[i]
    if n == 6:
        binarys[-1] = binarys[-1][:-2]
    elif n == 4:
        binarys[-1] = binarys[-1][0]
    elif n == 3:
        binarys[-1] = binarys[-1][:-1]
    elif n == 1:
        binarys[-1] = binarys[-1]
    binary_str = ''.join(binarys)
    binarys.clear()
    for i in range(8, len(binary_str)+8, 8):
        binarys.append(binary_str[i-8:i])
    decoded = ''
    for i in binarys:
        decoded += chr(__dec_cal(i))
    return decoded


# 2 = 6
# 4 = 4
# 1 = 3
# 3 = 1
