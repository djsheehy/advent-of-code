package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	jumps := make([]int, 0, 100)
	file, _ := os.Open("input.txt")
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		n := scanner.Text()
		number, _ := strconv.Atoi(n)
		jumps = append(jumps, number)
	}
	file.Close()

	i := 0
	steps := 0
	for i >= 0 && i < len(jumps) {
		x := jumps[i]
		if x >= 3 {
			jumps[i]--
		} else {
			jumps[i]++
		}
		i += x
		steps++
	}
	fmt.Println("Steps:", steps)
}
