package main

import (
	"fmt"
	"strconv"
	"strings"
)

// 给定一个经过编码的字符串，返回它解码后的字符串。
// 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。
// 注意 k 保证为正整数。
// 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
// 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
//
// 示例 1：
// 输入：s = "3[a]2[bc]"
// 输出："aaabcbc"
// 示例 2：
// 输入：s = "3[a2[c]]"
// 输出："accaccacc"
// 示例 3：
// 输入：s = "2[abc]3[cd]ef"
// 输出："abcabccdcdcdef"
// 示例 4：
// 输入：s = "abc3[cd]xyz"
// 输出："abccdcdcdxyz"

func decodeString(s string) string {
	//栈队列
	stack := make([]string, 0)
	// 临时解码的字符串队列
	temp_str := make([]string, 0)
	//指针
	p := &stack
	// 重复数的数组 - 处理多位数情况
	var number []string
	// 倒转重复数 最终结果
	var count string

	for _, val := range s {
		val := string(val)
		//结束入栈操作
		if val == "]" {
			// 出栈操作 遍历栈
			// 是否找到了重复数
			find_number := false
			// 重置
			number = number[0:0]
			count = ""
			temp_str = temp_str[0:0]
			// 结束解码标识
			end_flag := 0
			for i := len(*p) - 1; i >= 0; i-- {
				// 遇到出栈符号 //找到与遇到的第一个]的
				if !find_number && (*p)[i] == "[" {
					// 前面都应该是数字
					find_number = true
				} else if find_number {
					// 找到第一个不是数字的停止
					if _, err := strconv.Atoi((*p)[i]); err == nil {
						number = append(number, (*p)[i])
					} else {
						end_flag = i + 1
						break
					}
				} else {
					// 重复的字符串
					temp_str = append(temp_str, (*p)[i])
				}
			}
			// [2[a]] 与 [2[20[bc] 都需要处理
			for i := len(number) - 1; i >= 0; i-- {
				count += number[i]
			}
			// 处理栈队列，出清正在处理的
			(*p) = (*p)[:end_flag]
			// 求出 重复数字 int
			repeat, err := strconv.Atoi(count)
			if err != nil {
				panic("err1")
			} else {
				// 反转重复的字符串
				for i, j := 0, len(temp_str)-1; i < j; i, j = i+1, j-1 {
					temp_str[i], temp_str[j] = temp_str[j], temp_str[i]
				}
				// 拼接
				temp_total_str := ""
				temp_target_str := strings.Join(temp_str, "")
				//重复
				for i := 0; i < repeat; i++ {
					temp_total_str += temp_target_str
				}
				//重新入栈
				*p = append(*p, temp_total_str)
			}
		} else {
			*p = append(*p, val)
		}
	}
	return strings.Join((*p), "")
}

func main() {
	// s := "3[a]2[bc]"
	// ret := decodeString(s)
	// fmt.Println(ret)

	// s1 := "3[a2[c]]"
	// ret1 := decodeString(s1)
	// fmt.Println(ret1)

	s2 := "2[20[bc]31[xy]]xd4[rt]"
	ret2 := decodeString(s2)
	fmt.Println(ret2)

}
