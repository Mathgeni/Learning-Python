def rrr(rains: list[int]) -> list:
    full_lakes = list()
    if 0 not in rains:
        if len(rains) != len(set(rains)):
            return []
    for i in range(len(rains)):
        if rains[i] == 0:
            if full_lakes:
                flag = False
                for j in range(i + 1, len(rains)):
                    if rains[j] in full_lakes:
                        rains[i] = rains[j]
                        full_lakes.remove(rains[j])
                        flag = True
                        break
                if not flag:
                    rains[i] = full_lakes[0]
                    full_lakes.remove(full_lakes[0])
            else:
                rains[i] = 1
        else:
            if rains[i] in full_lakes:
                return []
            full_lakes.append(rains[i])
            rains[i] = -1
    return rains


if __name__ == '__main__':
    rains = [1, 0, 2, 0]
    print(rrr(rains))

