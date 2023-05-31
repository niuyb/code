package main

import (
	"fmt"
	"strings"
)

// 对于字符串 s 和 t，只有在 s = t + ... + t（t 自身连接 1 次或多次）时，我们才认定 “t 能除尽 s”。
// 给定两个字符串 str1 和 str2 。返回 最长字符串 x，要求满足 x 能除尽 str1 且 x 能除尽 str2 。

// 示例 1：
// 输入：str1 = "ABCABC", str2 = "ABC"
// 输出："ABC"
// 示例 2：
// 输入：str1 = "ABABAB", str2 = "ABAB"
// 输出："AB"
// 示例 3：
// 输入：str1 = "LEET", str2 = "CODE"
// 输出：""

func gcdOfStrings(str1 string, str2 string) string {
	max := -1
	base := str2
	if len(str1) < len(str2) {
		base = str1
	}
	//寻找可替换字符串的最长长度
	for i := len(base); i > 0; i-- {
		if len(str1)%i == 0 && len(str2)%i == 0 {
			if i > max {
				max = i
			}
		}
	}
	for i := 0; i < len(base); {
		//防止溢出，到这里也就说明不可能有结果了
		if max*(i+1) > len(base) {
			break
		}
		//以max为长度进行替换测试，如果两个字符串都为空，返回该结果
		if strings.ReplaceAll(str1, base[i*max:max*(i+1)], "") == "" && strings.ReplaceAll(str2, base[i*max:max*(i+1)], "") == "" {
			return base[i*max : max*(i+1)]
		}
		i += max
	}
	return ""
}

func main() {
	str1 := "ABCABC"
	str2 := "ABC"

	ret := gcdOfStrings(str1, str2)
	fmt.Println(ret)
}
