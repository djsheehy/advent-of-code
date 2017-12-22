package utils

import "testing"

func TestIntsToString(t *testing.T) {
	nums := []int{1, 2, 3, 4}
	expected := "1,2,3,4"
	got := IntsToString(nums)
	if got != expected {
		t.Errorf(`Expected "%s", got "%s"`, expected, got)
	}
}

func TestDistribute(t *testing.T) {
	nums := []int{0, 2, 7, 0}
	expected := []int{2, 4, 1, 2}
	Distribute(nums)
	if !SliceEquals(expected, nums) {
		t.Errorf(`Expected %v, got %v`, expected, nums)
	}
}
