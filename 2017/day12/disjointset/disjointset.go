package disjointset

// DisjointSet finds the connected components in a graph.
type DisjointSet struct {
	parent []int
	rank   []int
}

// NewSet makes a new DisjointSet of size count.
func NewSet(count int) *DisjointSet {
	djs := new(DisjointSet)
	djs.parent = make([]int, count)
	djs.rank = make([]int, count)
	for i := range djs.parent {
		djs.parent[i] = i
		djs.rank[i] = 0
	}
	return djs
}

// Find returns an element that contains the set x is in.
func (s *DisjointSet) Find(x int) int {
	if s.parent[x] == x {
		return x
	}
	result := s.Find(s.parent[x])
	s.parent[x] = result
	return result
}

// Union merges the sets that include x and y.
func (s *DisjointSet) Union(x, y int) {
	xroot, yroot := s.Find(x), s.Find(y)
	xrank, yrank := s.rank[x], s.rank[y]

	// same set
	if xroot == yroot {
		return
	}
	if xrank < yrank {
		s.parent[xroot] = yroot
	} else if yrank < xrank {
		s.parent[yroot] = xroot
	} else {
		s.parent[xroot] = yroot
		s.rank[yroot]++
	}
}

// UnionAll merges x's set with each of nums' sets.
func (s *DisjointSet) UnionAll(x int, nums []int) {
	for _, n := range nums {
		s.Union(x, n)
	}
}
