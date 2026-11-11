
def NaiveSearch( haystack : str, needle : str ):

    start = -1

    for i in range(len(haystack)):

        if haystack[i] == needle[0]:
            j = i
            k = 0

            while (j < len(haystack)) and (k < len(needle)) and (haystack[j] == needle[k]):
                j += 1
                k += 1

            if k == len(needle):
                start = i
                break


    return start