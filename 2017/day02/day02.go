package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func getNumbers(text string) []int {
	text = strings.Replace(text, "\t", " ", -1)
	words := strings.Split(text, " ")
	nums := make([]int, len(words))
	for i := range words {
		nums[i], _ = strconv.Atoi(words[i])
	}
	return nums
}

func minMaxDiff(nums []int) int {
	min := nums[0]
	max := nums[0]
	for i := 1; i < len(nums); i++ {
		if min > nums[i] {
			min = nums[i]
		}
		if max < nums[i] {
			max = nums[i]
		}
	}
	return max - min
}

func divisible(nums []int) (int, int) {
	for i, x := range nums {
		for j, y := range nums {
			if i == j {
				continue
			}
			if x%y == 0 {
				return x, y
			}
		}
	}
	return 1, 1
}

func main() {
	file, _ := os.Open("input.txt")
	scanner := bufio.NewScanner(file)
	sum := 0
	sum2 := 0
	for scanner.Scan() {
		nums := getNumbers(scanner.Text())
		sum += minMaxDiff(nums)
		x, y := divisible(nums)
		sum2 += x / y
	}
	fmt.Println("Sum 1:", sum)
	fmt.Println("Sum 2:", sum2)
	file.Close()
}
