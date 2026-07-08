import copy

class BinaryOps:

    @staticmethod
    def BinaryToStr( num ):
        
        i = 0
        s = ["0" for i in range(32)]

        while num:
            if num & 1:
                s[i] = '1'
            num >>= 1
            i += 1
        
        return "".join(s[::-1])
        
    @staticmethod
    def CountTrailingBits( num ):
        cnt = 32

        if num > 0:
            cnt -= 1
        
        if num & 0x0000FFFF:
            cnt -= 16

        if num & 0x00FF00FF:
            cnt -= 8

        if num & 0x0F0F0F0F:
            cnt -= 4

        if num & 0x33333333:
            cnt -= 2

        if num & 0x55555555:
            cnt -= 1

        return cnt
    
    @staticmethod
    def LastSetBitMask( num ):
        return num & (-num)

    
    @staticmethod
    def NextLexographic( current ):
        t = current | (current - 1)
        t1 = t + 1
        t2 = ~t & (-~t)
        cnt = BinaryOps.CountTrailingBits( current )
        next = t1 | ((t2 - 1) >> (cnt + 1))
        return next

class FenwickTree:

    def __init__(self, initArr : list[int]):
        self.mArray = copy.deepcopy( arr )
        self.mSum = [0 for i in range( len(arr) + 1 )]

    def construct( self ):

        for i in range( 0, len( self.mArray ) ):
            self.Update( i, self.mArray[i] )

    @staticmethod
    def Parent( index ):
        return index - BinaryOps.LastSetBitMask(index)

    def Next( index ):
        return index + BinaryOps.LastSetBitMask( index )

    def Update( self, index, val ):
        fIdx = index + 1
        self.mArray[index] = val

        while fIdx < len( self.mSum ):
            self.mSum[ fIdx  ] += val
            fIdx = FenwickTree.Next( fIdx )

    def RangeSum( self, start, end ):
        return self.Sum( end ) - self.Sum( start - 1 )

    def Sum( self, index ):
        
        res = 0
        fIndex = index + 1

        while fIndex > 0:
            res += self.mSum[fIndex]
            fIndex = FenwickTree.Parent( fIndex )

        return res

    def __str__(self):
        arrayStr = ", ".join([ str(i) for i in self.mArray])
        sumStr = ", ".join([ str(i) for i in self.mSum])
        return f"Array: {arrayStr}\nSum: {sumStr}"


if __name__ == "__main__":
    arr = [ 3, 2, -1, 6, 7, 4, -3, 3, 7, 2, 3 ]
    tree = FenwickTree( arr )
    tree.construct()
    
    print( str(tree) )
    tree.Update(2, 0 - arr[2])
    print( str(tree) )

