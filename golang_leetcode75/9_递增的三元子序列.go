package main

import (
	"fmt"
	"math"
)

// 给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。
// 如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，
// 使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。

// 示例 1：
// 输入：nums = [1,2,3,4,5]
// 输出：true
// 解释：任何 i < j < k 的三元组都满足题意
// 示例 2：
// 输入：nums = [5,4,3,2,1]
// 输出：false
// 解释：不存在满足题意的三元组
// 示例 3：
// 输入：nums = [2,1,5,0,4,6]
// 输出：true
// 解释：三元组 (3, 4, 5) 满足题意，因为 nums[3] == 0 < nums[4] == 4 < nums[5] == 6

func increasingTriplet(nums []int) bool {
	min := math.Inf(1)
	mid := math.Inf(1)

	for i := 0; i < len(nums); i++ {
		float64_i := float64(nums[i])
		if float64(min) >= float64_i {
			min = float64_i
			fmt.Println("min---->", int(min), int(float64_i))
		} else if float64(mid) >= float64_i {
			mid = float64_i
			fmt.Println("mid---->", int(mid), int(float64_i))
		} else {
			fmt.Println("max---->", int(float64_i))
			return true
		}
	}
	return false
}

func main() {
	nums := []int{1, 2, 3, 4, 5}
	ret := increasingTriplet(nums)
	fmt.Println(ret)

	nums = []int{5, 4, 3, 2, 1}
	ret = increasingTriplet(nums)
	fmt.Println(ret)

	nums = []int{2, 1, 5, 0, 4, 6}
	ret = increasingTriplet(nums)
	fmt.Println(ret)
}
