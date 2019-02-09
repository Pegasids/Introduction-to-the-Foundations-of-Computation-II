
# Checking Off
def f1(s1,s2):
    alist = list(s2)

    pos1 = 0
    matches = True
    op_count = 0
    diff_char = 0

    while pos1 < len(s1):
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            op_count += 1
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            diff_char += 1
            matches = False

        pos1 = pos1 + 1

    return matches, op_count, diff_char

# Sort and Compare 
def f2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    sorted1, op_count1 = msort(alist1, 0)
    sorted2, op_count2 = msort(alist2, 0)

    pos = 0
    matches = True
    op_count = 0
    diff_char = 0

    while pos < len(s1) and matches:
        op_count += 1
        if sorted1[pos] == sorted2[pos]:
            pos = pos + 1
        else:
            matches = False

    op_count = op_count + op_count1 + op_count2
    return matches, op_count, diff_char

# Merge Sort
def msort(x, op_count):
    result = []
    if len(x) < 2:
        return x, op_count
    mid = int(len(x)/2)
    y, op_count = msort(x[:mid], op_count)
    z, op_count = msort(x[mid:], op_count)
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]: 
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
        op_count += 1
    result += y[i:]
    result += z[j:]
    return result, op_count

# Brute Force
def f3(s1,s2):
    perms, found, op_count = all(s2, list(s1), [], [0]*len(s2), 0, False, 0 )
    return found, op_count, 0

# generates all permutations
def all(s2, inn, out, used, level, found, op_count):
    length = len(s2)
    if found:
        return out, True, op_count

    if level == length:
        for i in range(len(out)):
            op_count += 1
            if out[i] != s2[i]:
                return out, False, op_count
        return out, True, op_count

    for i in range(length):
        if used[i] == 1:
            continue
        
        out.append(inn[i])
        used[i] = 1
        out, found, op_count = all(s2, inn, out, used, level+1, found, op_count)
        if found:
            return out, True, op_count
        used[i] = 0
        out = out[:-1]

    return out, found, op_count

# Count and Compare
def f4(s1,s2):
    c1 = [0]*26
    c2 = [0]*26
    op_count = 0
    diff_char = 0

    for i in range(len(s1)):
        op_count += 1
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        op_count += 1
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    matches = True
    while j < 26:
        op_count += 1
        if c1[j] != c2[j]:
            diff_char += 1/2
            matches = False
        j = j + 1

    return matches, op_count, diff_char

def main():
    try:
        infile = open("input.txt")
    except:
        print("File input.txt not found.")
    else:
        print("-" * 70)
        print("%2s %8s %8s %8s %8s %8s %8s %8s" %
		("ID", "Match", "Op1", "Op2", "Op3", "Op4", "Diff1", "Diff4"))
        print("-" * 70)
        for line in infile:
            s = line.rstrip().split()

            # make sure the words are of equal length
            assert(len(s[1]) == len(s[2]))
 
            # call all four functions
            (match1, op1, diff1) = f1(s[1], s[2])
            (match2, op2, diff2) = f2(s[1], s[2])
            (match3, op3, diff3) = f3(s[1], s[2])
            (match4, op4, diff4) = f4(s[1], s[2])

            # make sure all four functions agree
            assert(match1 == match2 == match3 == match4)

            # output the results
            print("%2s %8d %8d %8d %8d %8d %8d %8d" %
		(s[0], match1, op1, op2, op3, op4, diff1, diff4))

        print("-" * 70)
        infile.close()

if __name__ == "__main__":
    main()