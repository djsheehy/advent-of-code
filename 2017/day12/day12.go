package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"

	"./disjointset"
)

func convertStrings(strs []string) []int {
	nums := make([]int, len(strs))
	for i := range strs {
		nums[i], _ = strconv.Atoi(strs[i])
	}
	return nums
}

func loadData(file *os.File) map[int][]int {
	scanner := bufio.NewScanner(file)
	data := make(map[int][]int)
	for scanner.Scan() {
		sides := strings.Split(scanner.Text(), " <-> ")
		list := strings.Split(sides[1], ", ")
		nums := convertStrings(list)
		i, _ := strconv.Atoi(sides[0])
		data[i] = nums
	}
	return data
}

func getKeys(m map[int]bool) []int {
	keys := make([]int, 0, len(m))
	for k := range m {
		keys = append(keys, k)
	}
	return keys
}

func dfs(data map[int][]int, start int) []int {
	queue := []int{start}
	visited := make(map[int]bool)
	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		visited[node] = true
		nbrs := data[node]
		for _, n := range nbrs {
			v := visited[n]
			if !v {
				queue = append(queue, n)
			}
		}
	}
	return getKeys(visited)
}

func components(data map[int][]int) int {
	set := disjointset.NewSet(len(data))
	for n, others := range data {
		set.UnionAll(n, others)
	}
	comps := make(map[int]bool)
	for i := range data {
		root := set.Find(i)
		comps[root] = true
	}
	return len(comps)
}

func main() {
	file, _ := os.Open("input.txt")
	data := loadData(file)
	file.Close()
	ans := len(dfs(data, 0))
	fmt.Println(ans)
	fmt.Println(components(data))
}
