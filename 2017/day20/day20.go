package main

import (
	"os"
)

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()
	i := 0
	closest := 0 // closest particle to origin
	bestDist := 1000000000

}
