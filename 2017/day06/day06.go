package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"

	"./utils"
)

func solve(memory []int) (int, []int) {
	chain := make(map[string]bool)
	key := utils.Merge(memory)
	next := memory
	for !chain[key] {
		chain[key] = true
		next = utils.Distribute(next)
		key = utils.Merge(next)
	}
	return len(chain), next
}

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	line := scanner.Text()
	words := strings.Split(line, "\t")
	memory := make([]int, len(words))

	for i, s := range words {
		memory[i], _ = strconv.Atoi(s)
	}

	loop1, start := solve(memory)
	loop2, _ := solve(start)

	fmt.Println("Answers:", loop1, loop2)
}
