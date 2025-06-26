
class fenwick:
    
    def __init__( self, nums : list[int] ):
        self.nums = nums
        self.size = len(nums)
        
    def construct( self ):
        # Instantiate the fenwick array
        self.tree = [0 for _ in range( self.size + 1) ]
        
        for i in range( 0, self.size):
            # Update tree with new value from index. Fenwick array is 1 indexed
            self.update( i+1, self.nums[i] )
            
    def sum( self, index ):
        res = 0
        
        # Adjust for fenwick indexing
        index += 1
        
        # Handle out of bounds index
        if (index <= 0) or (index >= self.size+1): return 0
        
        while index > 0:
            # Add binary indexed sum
            res += self.tree[index]
            # Move up to the parent index
            index = self.parent(index)
            
        return res

    def rangeSum( self, start, end ):
        return self.sum(end) - self.sum( start - 1 )
    
    def update( self, index, num ):
        """Includes Num in the binary indexed prefix sum

        Args:
            index (int): Position in the fenwick tree
            num (int): value to distribute
        """
        
        # Update the values in the tree
        while index < (self.size + 1):
            # Populate the new value
            self.tree[index] += num
            # Get the next index
            index = self.next(index)
            
    def next( self, index ):
        return index + (index & (-index))
    
    def parent( self, index ):
        return index - (index & (-index))
    
    
nums = [3,2,-1,6,7,4,-3, 3, 7, 2, 3]

fnTree = fenwick( nums )
fnTree.construct()

print(fnTree.tree)
print(fnTree.rangeSum(0, len(nums)-1))