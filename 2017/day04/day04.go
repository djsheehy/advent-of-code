package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

func valid(words []string) bool {
	uniques := make(map[string]bool)
	for _, w := range words {
		_, ok := uniques[w]
		if ok {
			return false
		}
		uniques[w] = true
	}
	return true
}

func sortChars(str string) string {
	chars := strings.Split(str, "")
	sort.Strings(chars)
	return strings.Join(chars, "")
}

func mapString(fn func(string) string, strs []string) []string {
	out := make([]string, len(strs))
	for i, s := range strs {
		out[i] = fn(s)
	}
	return out
}

func valid2(words []string) bool {
	sorted := mapString(sortChars, words)
	return valid(sorted)
}

func main() {
	file, _ := os.Open("input.txt")
	scanner := bufio.NewScanner(file)
	var ans1, ans2 int
	for scanner.Scan() {
		text := scanner.Text()
		words := strings.Split(text, " ")
		if valid(words) {
			ans1++
		}
		if valid2(words) {
			ans2++
		}
	}
	fmt.Println("Answer 1:", ans1)
	fmt.Println("Answer 2:", ans2)
}
