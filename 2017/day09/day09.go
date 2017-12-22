package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strings"
)

func solve(s string) (ans int, gscore int) {
	depth := 0
	garbage := false
	for _, c := range strings.Split(s, "") {
		if garbage {
			if c == ">" {
				garbage = false
			} else {
				gscore++
			}
			continue
		}
		switch c {
		case "{":
			depth++
		case "}":
			ans += depth
			depth--
		case "<":
			garbage = true
		case ",":
			continue
		}
	}
	return
}

func cancel(s string) string {
	rx := regexp.MustCompile("!.")
	return rx.ReplaceAllString(s, "")
}

func main() {
	file, _ := os.Open("input.txt")
	scan := bufio.NewScanner(file)
	scan.Scan()
	stream := cancel(scan.Text())
	score, garbage := solve(stream)
	fmt.Println("Score:", score)
	fmt.Println("Garbage:", garbage)

	file.Close()
}
