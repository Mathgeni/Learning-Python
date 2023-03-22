pairs = {'A': 'B', 'X': 'Y'}
pairs.update({value: key for key, value in pairs.items()})

def close_pairs(s):
    count = 0
    new_s = ''
    i = 0
    while i < len(s) - 1:
        if pairs[s[i]] == s[i + 1]:
            count += 1
            new_s += '  '
            i += 2
        else:
            new_s += s[i]
            i += 1
    if i == len(s) - 1:
        new_s += s[i]
    return ''.join(new_s.split()), count

def match(s):
    s, count = close_pairs(s)
    while 'AB' in s  or 'BA' in s or 'XY' in s or 'YX' in s:
        out = close_pairs(s)
        s = out[0]
        count += out[1]
    i = 0
    j = -1
    while i < len(s) // 2:
        if pairs[s[i]] == s[j]:
            count += 1
            i += 1
            j -= 1
        elif pairs[s[i]] == s[j - 1]:
            count += 1
            i += 1
            j -= 2
        elif pairs[s[i + 1]] == s[j]:
            count += 1
            i += 2
            j -= 1
        else:
            i += 1
            j -= 1
    return count


print(match('AAAABBBB'))