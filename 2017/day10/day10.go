package main

import (
	"fmt"

	"./knothash"
)

func main() {
	input := []int{183, 0, 31, 146, 254, 240, 223, 150, 2, 206, 161, 1, 255, 232, 199, 88}
	text := []rune("1,2,3")
	for _, r := range []rune{17, 31, 73, 47, 23} {
		text = append(text, r)
	}
	h := knothash.New(256)
	for _, n := range input {
		h.Reverse(n)
	}
	x := h.List.Value.(int)
	y := h.List.Next().Value.(int)
	fmt.Println("Answer 1:", x*y)

	h = knothash.New(256)
	for i := 0; i < 64; i++ {
		h.Round(text)
	}
	sparse := h.SparseHash()
	dense := knothash.DenseHash(sparse)
	fmt.Printf("Answer 2: %x\n", dense)
}
