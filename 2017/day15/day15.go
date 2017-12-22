package main

import "fmt"

type pair struct{ x, y uint16 }

func (p *pair) generate() bool {
	p.x *= 16807
	p.y *= 48271
	return p.x == p.y
}

func main() {
	p := &pair{783, 325}
	count := 0
	var i uint64
	for i = 0; i < 40000000; i++ {
		g := p.generate()
		if g {
			count++
		}
	}
	fmt.Println(count)
}
