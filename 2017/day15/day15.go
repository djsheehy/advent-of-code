package main

import "fmt"

type pair struct{ x, y uint64 }

func (p *pair) judge() bool {
	return uint16(p.x) == uint16(p.y)
}

func genA(x uint64) uint64 {
	return (x * 16807) % 2147483647
}

func genB(x uint64) uint64 {
	return (x * 48271) % 2147483647
}

func (p *pair) generate() {
	p.x = genA(p.x)
	p.y = genB(p.y)
}

func (p *pair) generate2() {
	p.x = genA(p.x)
	for p.x%4 != 0 {
		p.x = genA(p.x)
	}
	p.y = genB(p.y)
	for p.y%8 != 0 {
		p.y = genB(p.y)
	}
}

const (
	X = 783
	Y = 325
)

func main() {
	p := pair{X, Y}
	count := 0
	for i := 0; i < 40000000; i++ {
		p.generate()
		if p.judge() {
			count++
		}
	}
	fmt.Println(count)
	p = pair{X, Y}
	count = 0
	for i := 0; i < 5000000; i++ {
		p.generate2()
		if p.judge() {
			count++
		}
	}
	fmt.Println(count)
}
