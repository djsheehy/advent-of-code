package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const (
	Up    = iota
	Down  = iota
	Left  = iota
	Right = iota
)

func move(x, y, dir int) (int, int) {
	switch dir {
	case Up:
		y--
	case Down:
		y++
	case Left:
		x--
	case Right:
		x++
	}
	return x, y
}

func walk(diagram []string) (string, int) {
	var x, y int
	x = strings.IndexRune(diagram[0], '|')
	ans := ""
	cur := diagram[y][x]
	dir := Down
	steps := 0
	for cur != ' ' {
		switch cur {
		case '-', '|':
			break
		case '+':
			switch dir {
			case Up, Down:
				switch {
				case diagram[y][x-1] == '-':
					dir = Left
				case diagram[y][x+1] == '-':
					dir = Right
				}
			case Left, Right:
				switch {
				case diagram[y-1][x] == '|':
					dir = Up
				case diagram[y+1][x] == '|':
					dir = Down
				}
			}
		default:
			ans += string(cur)
		}
		x, y = move(x, y, dir)
		cur = diagram[y][x]
		steps++
	}

	return ans, steps
}

func main() {
	file, _ := os.Open("input.txt")
	diagram := make([]string, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		diagram = append(diagram, scanner.Text())
	}

	ans, steps := walk(diagram)
	fmt.Println(ans, steps)

}
