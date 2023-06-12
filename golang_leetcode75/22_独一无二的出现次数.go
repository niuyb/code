package main

import "fmt"

// 给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。
// 如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。
// 示例 1：
// 输入：arr = [1,2,2,1,1,3]
// 输出：true
// 解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。
// 示例 2：
// 输入：arr = [1,2]
// 输出：false
// 示例 3：
// 输入：arr = [-3,0,1,-3,1,1,1,-3,10,0]
// 输出：true

func uniqueOccurrences(arr []int) bool {
	count_map := make(map[int]int)
	for _, k := range arr {
		count_map[k]++
	}
	occur_count := make(map[int]int)
	for _, v := range count_map {
		occur_count[v] = 1
	}
	return len(occur_count) == len(count_map)
}

func main() {
	arr := []int{1, 2, 2, 1, 1, 3}
	ret := uniqueOccurrences(arr)
	fmt.Println(ret)

	arr = []int{-3, 0, 1, -3, 1, 1, 1, -3, 10, 0}
	ret = uniqueOccurrences(arr)
	fmt.Println(ret)

	arr = []int{1, 2}
	ret = uniqueOccurrences(arr)
	fmt.Println(ret)
}
