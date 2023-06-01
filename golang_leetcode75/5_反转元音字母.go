package main

import "fmt"

// 给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。
// 元音字母包括 "a"、"e"、"i"、"o"、"u"，且可能以大小写两种形式出现不止一次。

// 示例 1：
// 输入：s = "hello"
// 输出："holle"
// 示例 2：
// 输入：s = "leetcode"
// 输出："leotcede"

func IsContain(items []string, item string) bool {
	for _, eachItem := range items {
		if eachItem == item {
			return true
		}
	}
	return false
}

func reverseVowels(s string) string {
	t := []byte(s)
	u_str := []string{"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
	i, j := 0, len(s)-1
	for j > i {
		for i < len(s) && !IsContain(u_str, string(s[i])) {
			i++
		}
		for j > 0 && !IsContain(u_str, string(s[j])) {
			j--
		}
		if i < j {
			t[i], t[j] = t[j], t[i]
			i++
			j--
		}
	}
	return string(t)
}

func main() {

	s := "hello"
	ret := reverseVowels(s)
	fmt.Println(ret)

	s1 := "leetcode"
	ret = reverseVowels(s1)
	fmt.Println(ret)

	s2 := "leotcede"
	ret = reverseVowels(s2)
	fmt.Println(ret)
}
