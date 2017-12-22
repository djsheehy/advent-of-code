package utils

import (
	"strconv"
	"strings"
)

// Distribute Finds the biggest number and distributes it evenly among the rest.
func Distribute(blocks []int) []int {
	biggest := 0
	besti := 0
	for i, x := range blocks {
		if x > biggest {
			besti = i
			biggest = x
		}
	}
	blocks2 := make([]int, len(blocks))
	copy(blocks2, blocks)
	x := blocks2[besti]
	blocks2[besti] = 0
	i := (besti + 1) % len(blocks)
	for x > 0 {
		blocks2[i]++
		x--
		i = (i + 1) % len(blocks)
	}
	return blocks2
}

// SliceEquals tests if two slices of ints are equal.
func SliceEquals(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

// Merge Converts a slice of ints to a string.
func Merge(nums []int) string {
	strs := make([]string, len(nums))
	for i, n := range nums {
		strs[i] = strconv.Itoa(n)
	}
	return strings.Join(strs, ",")
}

// Split splits a string of comma-separated numbers into a slice of ints.
func Split(s string) []int {
	strs := strings.Split(s, ",")
	nums := make([]int, len(strs))
	for i, str := range strs {
		nums[i], _ = strconv.Atoi(str)
	}
	return nums
}
