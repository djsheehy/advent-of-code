package square

import "testing"

func checkSquares(t *testing.T, s1, s2 Square) {
	if s1.String() != s2.String() {
		t.Errorf("Expected %s, got %s\n", s1.String(), s2.String())
	}
}

func TestCount(t *testing.T) {
	sq := NewSquare("#./..")
	count := sq.Count()
	if count != 1 {
		t.Errorf("Expected 1, got %d\n", count)
	}
}

func TestRotate(t *testing.T) {
	sq := NewSquare("###/.../...")
	sq2 := NewSquare("..#/..#/..#")
	rot := sq.Rotate()
	if sq2.String() != rot.String() {
		t.Errorf("Expected %s, got %s\n", sq2.String(), rot.String())
	}
}

func TestFlipVertical(t *testing.T) {
	sq := NewSquare("###/.#./...")
	sq2 := NewSquare(".../.#./###")
	flip := sq.FlipVertical()
	if sq2.String() != flip.String() {
		t.Errorf("Expected %s, got %s\n", sq2.String(), flip.String())
	}
}

func TestFlipHorizontal(t *testing.T) {
	s1 := NewSquare("#../#../##.")
	s2 := NewSquare("..#/..#/.##")
	flip := s1.FlipHorizontal()
	if s2.String() != flip.String() {
		t.Errorf("Expected %s, got %s\n", s2.String(), flip.String())
	}
}

func TestSlice(t *testing.T) {
	source := NewSquare("...../.###./.#.#./.###./.....")
	goal := NewSquare("###/#.#/###")
	actual := source.Slice(1, 1, 3)
	checkSquares(t, goal, actual)
}

func TestMerge(t *testing.T) {
	chunks := [][]Square{
		{NewSquare("#./.."), NewSquare(".#/..")},
		{NewSquare("../#."), NewSquare("../.#")},
	}
	expected := NewSquare("#..#/..../..../#..#")
	actual := Merge(chunks)
	checkSquares(t, expected, actual)
}

func TestDivide(t *testing.T) {
	s1 := NewSquare("##../##../..##/..##")
	div := s1.Divide()
	if len(div) != 2 {
		t.Errorf("square split wrong size: %d\n", len(div))
	}
	if len(div[0][0]) != 2 {
		t.Errorf("each square wrong size: %d\n", len(div[0][0]))
	}
}
