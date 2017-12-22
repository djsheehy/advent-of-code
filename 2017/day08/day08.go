package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

/*
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
*/

// Register keeps a map of registers and the max number ever held
type Register struct {
	reg map[string]int
	max int
}

// NewRegister creates a new register.
func NewRegister() *Register {
	r := new(Register)
	r.reg = make(map[string]int)
	return r
}

// Add adds a number to the given register
func (r *Register) Add(name string, value int) {
	x := r.reg[name] + value
	if x > r.max {
		r.max = x
	}
	r.reg[name] = x
}

// Get converts n into a number if valid, otherwise looks up n in register
func (r *Register) Get(n string) int {
	x, err := strconv.Atoi(n)
	if err != nil {
		return r.reg[n]
	}
	return x
}

// Execute executes a command.
func (r *Register) Execute(cmd string) {
	words := strings.Split(cmd, " ")
	a, verb, add, b, op, c := words[0], words[1], words[2], words[4], words[5], words[6]
	addNum, _ := strconv.Atoi(add)
	x, y := r.Get(b), r.Get(c)
	if verb == "dec" {
		addNum = -addNum
	}

	switch op {
	case "<":
		if x < y {
			r.Add(a, addNum)
		}
	case ">":
		if x > y {
			r.Add(a, addNum)
		}
	case "<=":
		if x <= y {
			r.Add(a, addNum)
		}
	case ">=":
		if x >= y {
			r.Add(a, addNum)
		}
	case "!=":
		if x != y {
			r.Add(a, addNum)
		}
	case "==":
		if x == y {
			r.Add(a, addNum)
		}
	}
}

func biggestValue(reg map[string]int) int {
	ans := 0
	for _, val := range reg {
		if val > ans {
			ans = val
		}
	}
	return ans
}

func (r *Register) Solution1() int {
	return biggestValue(r.reg)
}

func (r *Register) Solution2() int {
	return r.max
}

func main() {
	r := NewRegister()

	file, _ := os.Open("input.txt")
	scan := bufio.NewScanner(file)
	for scan.Scan() {
		r.Execute(scan.Text())
	}
	fmt.Println(r.Solution1())
	fmt.Println(r.Solution2())
	file.Close()
}
