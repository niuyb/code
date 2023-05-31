package main

import (
	"fmt"
	"reflect"
)

// 给你两个字符串 word1 和 word2 。请你从 word1 开始，通过交替添加字母来合并字符串。
// 如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。
// 返回 合并后的字符串 。

// 输入：word1 = "abc", word2 = "pqr"
// 输出："apbqcr"
// 解释：字符串合并情况如下所示：
// word1：  a   b   c
// word2：    p   q   r
// 合并后：  a p b q c r

// 输入：word1 = "ab", word2 = "pqrs"
// 输出："apbqrs"
// 解释：注意，word2 比 word1 长，"rs" 需要追加到合并后字符串的末尾。
// word1：  a   b
// word2：    p   q   r   s
// 合并后：  a p b q   r   s

func mergeAlternately(str1, str2 string) string {
	str1_len := len(str1)
	str2_len := len(str2)
	ret := make([]byte, 0)
	for i := 0; i < str1_len || i < str2_len; i++ {
		if i < str1_len {
			ret = append(ret, str1[i])
		}
		if i < str2_len {
			ret = append(ret, str2[i])
		}
	}
	return string(ret)
}

func main() {
	word1 := "abc"
	word2 := "pqr"
	ret := mergeAlternately(word1, word2)
	fmt.Println(ret)
	fmt.Println(reflect.TypeOf(ret))

	word1 = "ab"
	word2 = "pqrs"
	ret = mergeAlternately(word1, word2)
	fmt.Println(ret)
	fmt.Println(reflect.TypeOf(ret))
}
