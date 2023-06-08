package main

import (
	"fmt"
)

// 给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。
// 请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。
// 任何误差小于 10-5 的答案都将被视为正确答案。

// 示例 1：
// 输入：nums = [1,12,-5,-6,50,3], k = 4
// 输出：12.75
// 解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
// 示例 2
// 输入：nums = [5], k = 1
// 输出：5.00000

// 提示：
// n == nums.length
// 1 <= k <= n <= 105
// -104 <= nums[i] <= 104

func findMaxAverage2(nums []int, k int) float64 {
	sum := 0
	for _, v := range nums[:k] {
		sum += v
	}
	avg := float64(sum) / float64(k)
	var temp_avg float64
	for i, j := k, 1; i < len(nums) && j < len(nums); i, j = i+1, j+1 {
		sum = nums[i] + sum - nums[j-1]
		temp_avg = float64(sum) / float64(k)
		if temp_avg > avg {
			avg = temp_avg
		}
	}
	return avg
}

func findMaxAverage(nums []int, k int) float64 {
	sum := 0
	for _, v := range nums[:k] {
		sum += v
	}
	max_sum := sum
	for i := k; i < len(nums); i++ {
		sum = nums[i] + sum - nums[i-k]
		if sum > max_sum {
			max_sum = sum
		}
	}
	return float64(max_sum) / float64(k)
}

func findMaxAverage3(nums []int, k int) float64 {
	sum := 0
	for _, v := range nums[:k] {
		sum += v
	}
	maxSum := sum
	for i := k; i < len(nums); i++ {
		sum = sum - nums[i-k] + nums[i]
		maxSum = max(maxSum, sum)
	}
	return float64(maxSum) / float64(k)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	// nums := []int{1, 12, -5, -6, 50, 3}
	// k := 4
	// ret := findMaxAverage2(nums, k)
	// fmt.Println(ret)

	nums := []int{4, 2, 1, 3, 3}
	k := 1
	ret := findMaxAverage(nums, k)
	fmt.Println(ret)

	// nums = []int{0, 4, 0, 3, 2}
	// k = 1
	// ret = findMaxAverage3(nums, k)
	// fmt.Println(ret)
}
