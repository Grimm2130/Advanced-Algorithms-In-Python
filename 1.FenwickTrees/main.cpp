#include "Fenwick.h"
#include <iostream>

fenwickTree* ftree;
std::vector<int> arr = {3,2,-1,6,7,4,-3, 3, 7, 2, 3};

int main()
{
    int start = 0, end = arr.size()-1;
    ftree = new fenwickTree( arr );
    
    printf("Elements in the tree: ");
    for( const int elm : ftree->getTree() )
    {
        printf("%d, ", elm );
    }
    printf("\n");
    
    printf("Sum of elements in range [%d, %d] = %d\n", 
        start, 
        end, 
        ftree->rangeSum( start, end ) 
    );

    return 0;
}