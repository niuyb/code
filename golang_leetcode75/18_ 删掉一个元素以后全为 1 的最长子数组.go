package main

import "fmt"

// 给你一个二进制数组 nums ，你需要从中删掉一个元素。
// 请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。
// 如果不存在这样的子数组，请返回 0 。
//
// 提示 1：
// 输入：nums = [1,1,0,1]
// 输出：3
// 解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。
// 示例 2：
// 输入：nums = [0,1,1,1,0,1,1,0,1]
// 输出：5
// 解释：删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1] 。
// 示例 3：
// 输入：nums = [1,1,1]
// 输出：2
// 解释：你必须要删除一个元素。

func longestSubarray(nums []int) int {
	right, left, zeros := len(nums)-1, 0, 0
	for r := 0; r < len(nums); r++ {
		zeros += 1 - nums[r]
		if zeros > 1 {
			zeros -= 1 - nums[left]
			left++
		}
	}
	fmt.Println(left, right)
	return right - left
}

func main() {
	nums := []int{1, 1, 0, 1}
	ret := longestSubarray(nums)
	fmt.Println(ret)

	nums1 := []int{0, 1, 1, 1, 0, 1, 1, 0, 1}
	ret1 := longestSubarray(nums1)
	fmt.Println(ret1)

	nums2 := []int{1, 1, 1}
	ret2 := longestSubarray(nums2)
	fmt.Println(ret2)
}
