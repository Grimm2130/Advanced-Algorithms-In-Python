
def RabinKarpSearch( haystack:str, needle:str):

    # class RabinFingerPrint:

    #     def __init__(self, sequence, scale, window_len ):
    #         self.sequence = sequence
    #         self.scale = scale
    #         self.window_len = window_len
    #         self._hash = 0

    def RabinFingerPrint( curr_hash : int, window_len : int, scale : int, mod : int,  old_val : int, new_val : int ):

        new_hash = curr_hash
        new_hash = (new_hash - (old_val * pow(scale, window_len-1, mod)))
        new_hash =  ((new_hash * scale) + new_val) % mod

        return new_hash

    def IsMatch( sequence, subsequence, start_idx )-> bool:

        if (len(sequence) - start_idx) < len(subsequence):
            return False

        i = start_idx
        j = 0
        
        while (i < len(sequence)) and (j < len(subsequence)) and (sequence[i] == subsequence[j]):
            i += 1
            j += 1

        return j == len(subsequence)

    scale = 127
    needle_hash = 0
    haystack_hash = 0
    window_len = len(needle)
    mod = 113

    # Intialize needle and hay hashes
    for i in range(window_len):
        needle_hash = RabinFingerPrint( needle_hash, window_len, scale, mod, 0, ord(needle[i]) )
        haystack_hash = RabinFingerPrint( haystack_hash, window_len, scale, mod, 0, ord(haystack[i]) )

    i, j = 0, window_len

    if (needle_hash == haystack_hash) and IsMatch(haystack, needle, 0 ):
        return 0
    else:
        while( j < len(haystack) ):

            # print(f"\tComparing Sequence '{haystack[i+1:j+1]}' to '{needle}'")
            # Update hash function
            haystack_hash = RabinFingerPrint( haystack_hash, window_len, scale, mod, ord(haystack[i]), ord(haystack[j]) )
            
            i += 1
            j += 1
            
            if (needle_hash == haystack_hash) and IsMatch(haystack, needle, i ):
                return i

    return -1
            
    