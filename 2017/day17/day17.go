package main

import (
	"fmt"

	"./spinlock"
)

func main() {
	input := 386
	lock := spinlock.New()
	for i := 0; i < 50000000; i++ {
		lock.Step(input)
		if i%1000000 == 0 {
			fmt.Printf("%d million\n", i/1000000)
		}
	}
	fmt.Println("Answer:", lock.SecondValue())
}
