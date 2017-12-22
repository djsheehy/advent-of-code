package main

import (
	"bufio"
	"fmt"
	"os"

	"./cpu"
)

func callback(x int) {
	fmt.Println("Received", x)
	os.Exit(0)
}

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()
	lines := make([]string, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	c := cpu.New(lines, callback)
	for c.Execute() {

	}
}
