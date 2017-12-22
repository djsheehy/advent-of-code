package knothash

import (
	"container/ring"
)

// KnotHash implements the knot hash function described in http://adventofcode.com/2017/day/10
type KnotHash struct {
	List    *ring.Ring
	Current *ring.Ring
	Skip    int
}

// New creates a new KnotHash with length items.
func New(length int) *KnotHash {
	h := new(KnotHash)
	h.List = ring.New(length)
	h.Current = h.List
	r := h.List
	for i := 0; i < length; i++ {
		r.Value = i
		r = r.Next()
	}
	return h
}

// Reverse reverses length numbers starting with the current node
// then skips ahead length + h.Skip steps, then increases h.Skip by 1.
func (h *KnotHash) Reverse(length int) {
	start, end := h.Current, h.Current
	for i := 0; i < length; i++ {
		end = end.Next()
	}
	for i := 0; i < length/2; i++ {
		start.Value, end.Value = end.Value, start.Value
		start = start.Next()
		end = end.Prev()
	}
	move := length + h.Skip
	for i := 0; i < move; i++ {
		h.Current = h.Current.Next()
	}
	h.Skip++
}

// Round runs a round of the Knot Hash algorithm.
func (h *KnotHash) Round(input []rune) {
	for _, r := range input {
		h.Reverse(int(r))
	}
}

func (h *KnotHash) SparseHash() []int {
	hash := make([]int, 0)
	h.List.Do(func(x interface{}) {
		n := x.(int)
		hash = append(hash, n)
	})
	return hash
}

func DenseHash(sparse []int) []byte {
	dense := make([]byte, 16)
	for i := 0; i < 16; i++ {
		block := sparse[i*16 : i*16+16]
		x := block[1]
		for _, n := range block[1:] {
			x ^= n
		}
		dense[i] = byte(x)
	}
	return dense
}
