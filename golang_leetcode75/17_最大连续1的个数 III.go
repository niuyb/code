package main

import (
	"fmt"
)

// 给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续1的最大个数

// 示例 1：
// 输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
// 输出：6
// 解释：[1,1,1,0,0,1,1,1,1,1,1]
// 粗体数字从 0 翻转到 1，最长的子数组长度为 6。
// 示例 2：
// 输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
// 输出：10
// 解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
// 粗体数字从 0 翻转到 1，最长的子数组长度为 10。

func longestOnes(nums []int, k int) int {
	r, left, zeros := len(nums)-1, 0, 0
	for _, v := range nums {
		// fmt.Println(a, v)
		// 滑动窗口 右边界拓展1
		zeros += 1 - v
		if zeros > k {
			// 左边界收缩1
			zeros -= 1 - nums[left]
			left += 1
		}
		// fmt.Println(left, a, v)
	}
	// fmt.Println(r, left)
	// 求最大值，肯定是r越大最大值越大，因为r++ 有可能对应left++，最差也是left++，持平
	// 代码含义就变成了 在符合条件下r与left最大差值
	return r - left + 1
}

func main() {

	// nums := []int{1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0}
	// K := 2
	// ret := longestOnes(nums, K)
	// fmt.Println(ret)

	nums1 := []int{0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1}
	K1 := 3
	ret1 := longestOnes(nums1, K1)
	fmt.Println(ret1)
}
