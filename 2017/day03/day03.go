package main

import "fmt"

/*
65  64  63  62  61  60  59  58  57	|	4
66  37  36  35  34  33  32  31  56	|	3
67  38  17  16  15  14  13  30  55	|	2
68  39  18   5   4   3  12  29  54	|	1
69  40  19   6   1   2  11  28  53 	|	0
70  41  20   7   8   9  10  27  52	|	-1
71  42  21  22  23  24  25  26  51	|	-2
72  43  44  45  46  47  48  49  50	|	-3
73  74  75  76  77  78  79  80  81	|	-4
*/

// Diagonal going NW from 1 is squares of even numbers + 1
// Diagonal going SE from 1 is squares of odd numbers
// n = (2x+1)^2
// sqrt(n) = 2x+1
// sqrt(n) - 1 = 2x
// (sqrt(n) - 1)/2 = x

// Coord is an (x,y) coordinate.
type Coord struct {
	X, Y int
}

func sumNeighbors(xy Coord, m map[Coord]int) int {
	for i := -1; i <= 1; i++ {
		for j := -1; j <= 1; j++ {
			if i == 0 && j == 0 {
				continue
			}
			m[xy] += m[Coord{xy.X + i, xy.Y + j}]
		}
	}
	return m[xy]
}

func getDir(dir int) (int, int) {
	switch dir {
	case 0:
		return 1, 0
	case 1:
		return 0, 1
	case 2:
		return -1, 0
	default:
		return 0, -1
	}
}

func changeDir(x, y int) bool {
	if x > 0 && y > 0 && x == y {
		return true
	}

	if x < 0 && y > 0 && -x == y {
		return true
	}

	if x < 0 && y < 0 && x == y {
		return true
	}

	if x > 0 && y <= 0 && x == -y+1 {
		return true
	}
	return false
}

func solve(in int, grid map[Coord]int) (ans1, ans2 int) {

	x, y := 0, 0
	dir := 0
	found := false
	for n := 1; n <= in; n++ {
		if !found {
			sum := sumNeighbors(Coord{x, y}, grid)
			fmt.Println(sum)
			if sum > in {
				ans2 = sum
				found = true
			}
		}
		dx, dy := getDir(dir)
		x += dx
		y += dy
		if changeDir(x, y) {
			dir = (dir + 1) % 4
		}
	}
	ans1 = intAbs(x) + intAbs(y) + 1 // the answer was off by 1
	return
}

func intAbs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	const input int = 368078
	grid := make(map[Coord]int)
	grid[Coord{0, 0}] = 1

	a, b := solve(input, grid)
	fmt.Printf("Answer 1: %d\nAnswer 2: %d\n", a, b)
}
