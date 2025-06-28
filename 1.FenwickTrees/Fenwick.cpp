#include "Fenwick.h"

#define DEFAULT_FENWICK_TREE_SIZE   100

fenwickTree::fenwickTree( const std::vector<int>& arr )
{
    m_size = arr.size()+1;
    m_tree = new std::vector<int>( arr.size() + 1, 0 );

    // Instantiate the elements of the tree
    this->init( arr );
}

fenwickTree::~fenwickTree()
{
    delete m_tree;
}

/// @brief Update the index of the tree
void fenwickTree::update( const int val, const int index )
{
    int i = index + 1;

    if( i <= 0 || i >= m_size )
    {
        // perror("Index out of bounds!!");
        return;
    }

    while( i < m_size )
    {
        m_tree->at(i) += val;
        // Get the next entry
        i = fenwickTree::next( i );
    }
}

int fenwickTree::sum( int index ) const
{
    int sum = 0;

    index++;

    if( index <= 0 || index >= m_size )
    {
        return sum;
    }


    while( index > 0 )
    {
        sum += m_tree->at(index);
        index = fenwickTree::parent(index);
    }

    return sum;
}

int fenwickTree::rangeSum( const int start, const int end ) const  
{
    return this->sum( end ) - this->sum( start - 1 );
}

void fenwickTree::init( const std::vector<int>& arr )
{
    for( int i = 0; i < arr.size(); i++ )
    {
        update( arr[i], i );
    }
}

/// @brief Remove the next
/// @param index 
/// @return 
int fenwickTree::next( int index )
{
    return index + ( index & (-index) );
}

int fenwickTree::parent( int index )
{
    return index - ( index & (-index) );
}

const std::vector<int>& fenwickTree::getTree() const
{
    return *m_tree;
}