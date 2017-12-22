package main

import (
	"bufio"
	"fmt"
	"os"

	"./tree"
)

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()
	scanner := bufio.NewScanner(file)
	t := tree.NewTree()
	for scanner.Scan() {
		text := scanner.Text()
		node := tree.Parse(text)
		t.AddNode(node)
	}

	root := t.GetRoot()
	fmt.Println("Root:", root.Name)
	bad, sibling := root.GetBadNode(0)
	diff := bad.GetWeight() - sibling
	answer := bad.Weight - diff
	fmt.Println("Answer 2:", answer)
	fmt.Println("Bad node's name:", bad.Name)
}
