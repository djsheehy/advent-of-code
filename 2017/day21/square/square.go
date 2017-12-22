package square

import (
	"fmt"
	"strings"
)

// Square represents a square grid of pixels.
// For those reading the source code, "chunks" refer to Squares in a 2D grid.
type Square []string

// Rulebook keeps track of all the enhancement rules.
type Rulebook map[string]string

// NewSquare creates a new Square from a string.
func NewSquare(str string) Square {
	return strings.Split(str, "/")
}

// Print prints out a Square. Used for debugging.
func (sq Square) Print() {
	fmt.Println(strings.Join(sq, "\n"))
}

// Slice copies a piece of a square starting at (row, col) of the given size.
func (sq Square) Slice(row, col, size int) Square {
	out := make([]string, size)
	for i := 0; i < size; i++ {
		out[i] = sq[i+row][col : col+size]
	}
	return out
}

// Count returns the number of '#' in the square.
func (sq Square) Count() int {
	ans := 0
	for _, row := range sq {
		ans += strings.Count(row, "#")
	}
	return ans
}

func (sq Square) String() string {
	return strings.Join(sq, "/")
}

func fromGrid(grid [][]rune) Square {
	square := make([]string, len(grid))
	for i, row := range grid {
		square[i] = string(row)
	}
	return square
}

func (sq Square) toGrid() [][]rune {
	grid := make([][]rune, len(sq))
	for i, row := range sq {
		grid[i] = []rune(row)
	}
	return grid
}

// Rotate the square right 90 degrees.
func (sq Square) Rotate() Square {
	grid := make([][]rune, len(sq))
	for i := 0; i < len(sq); i++ {
		grid[i] = make([]rune, len(sq))
	}
	for i := 0; i < len(sq); i++ {
		for j := 0; j < len(sq); j++ {
			grid[i][j] = rune(sq[len(sq)-j-1][len(sq)-i-1])
		}
	}
	return fromGrid(grid)
}

// FlipVertical flips the square vertically.
func (sq Square) FlipVertical() Square {
	ans := make([]string, len(sq))
	for i, row := range sq {
		ans[len(ans)-i-1] = row
	}
	return ans
}

// FlipHorizontal flips the square horizontally.
func (sq Square) FlipHorizontal() Square {
	grid := sq.toGrid()
	l := len(sq)
	for i := range grid {
		for j := 0; j < l/2; j++ {
			grid[i][j], grid[i][l-j-1] = grid[i][l-j-1], grid[i][j]
		}
	}
	return fromGrid(grid)
}

// split a Square into smaller squares, each of size n
// assumes that len(sq) is evenly divides by n.
func (sq Square) split(n int) [][]Square {
	// build the grid
	gridSize := len(sq) / n
	grid := make([][]Square, gridSize)
	for i := 0; i < gridSize; i++ {
		grid[i] = make([]Square, gridSize)
	}

	// load up the grid
	for i := 0; i < gridSize; i++ {
		for j := 0; j < gridSize; j++ {
			grid[i][j] = sq.Slice(i*n, j*n, n)
		}
	}

	return grid
}

// Divide divides a square into 2x2 if size is divisible by 2
// Otherwise divides it into 3x3.
func (sq Square) Divide() [][]Square {
	if len(sq) == 2 || len(sq) == 3 {
		return [][]Square{{sq}}
	}
	if len(sq)%2 == 0 {
		return sq.split(2)
	}
	return sq.split(3)
}

// Lookup looks up the enhancement rule of a Square.
func (r Rulebook) Lookup(key Square) Square {
	str := key.String()
	val := strings.Split(r[str], "/")
	return val
}

// Store stores the enhancement rule of a square in string form.
// All rotations and flips are also stored.
func (r Rulebook) Store(key, val string) {
	r[key] = val
	sqKey := Square(strings.Split(key, "/"))
	k := sqKey
	for i := 0; i < 3; i++ {
		k = k.Rotate()
		r[k.String()] = val
	}

	k = sqKey.FlipHorizontal()
	r[k.String()] = val
	for i := 0; i < 3; i++ {
		k = k.Rotate()
		r[k.String()] = val
	}
	k = sqKey.FlipVertical()
	r[k.String()] = val
	for i := 0; i < 3; i++ {
		k = k.Rotate()
		r[k.String()] = val
	}
	k = sqKey.FlipHorizontal().FlipVertical()
	r[k.String()] = val
	for i := 0; i < 3; i++ {
		k = k.Rotate()
		r[k.String()] = val
	}
}

// add adds each row in other to sq starting at the given row.
func (sq Square) add(other Square, row int) {
	for i := range other {
		sq[i+row] += other[i]
	}
}

// Merge combines a grid of Squares into one big Square.
func Merge(chunks [][]Square) Square {
	gridSize := len(chunks)         // size of entire grid of squares
	squareSize := len(chunks[0][0]) // size of each square
	ans := Square(make([]string, gridSize*squareSize))
	for i, row := range chunks {
		for _, sq := range row {
			r := i * squareSize
			ans.add(sq, r)
		}
	}

	return ans
}

// Enhance runs an Enhance step on the Square.
func (sq Square) Enhance(rb Rulebook) Square {
	//fmt.Println("Before:")
	//sq.Print()
	chunks := sq.Divide()
	for i, row := range chunks {
		for j, s := range row {
			chunks[i][j] = rb.Lookup(s)
		}
	}
	sq2 := Merge(chunks)
	//fmt.Println("After:")
	//sq2.Print()
	return sq2
}
