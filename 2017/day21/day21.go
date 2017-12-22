package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	sqr "./square"
)

const image = ".#./..#/###"
const iters = 18

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()
	scanner := bufio.NewScanner(file)
	rules := sqr.Rulebook(make(map[string]string))
	for scanner.Scan() {
		line := scanner.Text()
		split := strings.Split(line, " => ")
		rules.Store(split[0], split[1])
	}

	square := sqr.NewSquare(image)
	for i := 0; i < iters; i++ {
		square = square.Enhance(rules)
	}

	fmt.Println(square.Count())
	fmt.Printf("Size: %d\n", len(square))
}
