package main

// 给你字符串 s 和整数 k 。
// 请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。
// 英文中的 元音字母 为（a, e, i, o, u）。

// 示例 1：
// 输入：s = "abciiidef", k = 3
// 输出：3
// 解释：子字符串 "iii" 包含 3 个元音字母。
// 示例 2：
// 输入：s = "aeiou", k = 2
// 输出：2
// 解释：任意长度为 2 的子字符串都包含 2 个元音字母。
// 示例 3：
// 输入：s = "leetcode", k = 3
// 输出：2
// 解释："lee"、"eet" 和 "ode" 都包含 2 个元音字母。
// 示例 4：
// 输入：s = "rhythms", k = 4
// 输出：0
// 解释：字符串 s 中不含任何元音字母。
// 示例 5：
// 输入：s = "tryhard", k = 4
// 输出：1

func maxVowels(s string, k int) int {
	count := 0
	// 计算第一个窗口的元音数量
	for i := 0; i < k; i++ {
		if s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' {
			count++
		}
	}
	// 初始化最大值
	maxcount := count
	// 遍历
	for i := k; i < len(s); i++ {
		// 如果窗口第一个数为元音，减1
		if s[i-k] == 'a' || s[i-k] == 'e' || s[i-k] == 'i' || s[i-k] == 'o' || s[i-k] == 'u' {
			count--
		}
		// 如果下一个窗口的下一个数值为元音，加1
		if s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' {
			count++
		}
		// 更新最大值
		if maxcount < count {
			maxcount = count
		}
	}
	// 返回最大值
	return maxcount
}
