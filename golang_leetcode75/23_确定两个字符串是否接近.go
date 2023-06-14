package main

// 如果可以使用以下操作从一个字符串得到另一个字符串，则认为两个字符串 接近 ：
// 操作 1：交换任意两个 现有 字符。
// 例如，abcde -> aecdb
// 操作 2：将一个 现有 字符的每次出现转换为另一个 现有 字符，并对另一个字符执行相同的操作。
// 例如，aacabb -> bbcbaa（所有 a 转化为 b ，而所有的 b 转换为 a ）
// 你可以根据需要对任意一个字符串多次使用这两种操作。
// 给你两个字符串，word1 和 word2 。如果 word1 和 word2 接近 ，就返回 true ；否则，返回 false 。
//
// 示例 1：
// 输入：word1 = "abc", word2 = "bca"
// 输出：true
// 解释：2 次操作从 word1 获得 word2 。
// 执行操作 1："abc" -> "acb"
// 执行操作 1："acb" -> "bca"
// 示例 2：
// 输入：word1 = "a", word2 = "aa"
// 输出：false
// 解释：不管执行多少次操作，都无法从 word1 得到 word2 ，反之亦然。
// 示例 3：
// 输入：word1 = "cabbba", word2 = "abbccc"
// 输出：true
// 解释：3 次操作从 word1 获得 word2 。
// 执行操作 1："cabbba" -> "caabbb"
// 执行操作 2："caabbb" -> "baaccc"
// 执行操作 2："baaccc" -> "abbccc"
// 示例 4：
// 输入：word1 = "cabbba", word2 = "aabbss"
// 输出：false
// 解释：不管执行多少次操作，都无法从 word1 得到 word2 ，反之亦然。

// 解题思路
// 发现如果两个字符串相近，那么字符串中：
// 1、长度相同
// 2、种类相同
// 3、字符串1中的每个字符数量只要在另一个字符串中能找到相同数量的字符即可（字符无需相同）
// 因此直接哈希完以后比较即可！

func closeStrings(word1 string, word2 string) bool {
	if len(word1) != len(word2) {
		return false
	} else {
		hash1 := make(map[rune]int)
		hash2 := make(map[rune]int)
		for _, v1 := range word1 {
			hash1[v1]++
		}
		for _, v2 := range word2 {
			hash2[v2]++
		}
		if len(hash1) != len(hash2) {
			return false
		}
		for k, _ := range hash1 {
			if _, ok := hash2[k]; !ok {
				return false
			}
		}
		for key, _ := range hash1 {
			for key2, _ := range hash2 {
				if hash1[key] == hash2[key2] {
					hash2[key2] = 0
					break
				}
			}
		}
		for _, v := range hash2 {
			if v != 0 {
				return false
			}
		}
		return true
	}
}

func main() {

}
