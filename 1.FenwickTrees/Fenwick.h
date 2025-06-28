#if !defined(__FENWICK_H__)
#define __FENWICK_H__

#include <vector>

class fenwickTree
{
public:
    fenwickTree( const std::vector<int>& arr );
    ~fenwickTree();
    void update( const int val, const int index );
    int sum( int index ) const;
    int rangeSum( const int start, const int end ) const;
    const std::vector<int>& getTree() const;
protected:
    void init( const std::vector<int>& arr );
    static int next( int index );
    static int parent( int index );
private:
    int m_size;
    std::vector<int> *m_tree;
};

#endif // __FENWICK_H__
