package main

import "fmt"

// 给你一个链表的头节点 head 。删除 链表的 中间节点 ，并返回修改后的链表的头节点 head 。
// 长度为 n 链表的中间节点是从头数起第 ⌊n / 2⌋ 个节点（下标从 0 开始），
// 其中 ⌊x⌋ 表示小于或等于 x 的最大整数。
// 对于 n = 1、2、3、4 和 5 的情况，中间节点的下标分别是 0、1、1、2 和 2 。

// 示例 1：
// 输入：head = [1,3,4,7,1,2,6]
// 输出：[1,3,4,1,2,6]
// 解释：
// 上图表示给出的链表。节点的下标分别标注在每个节点的下方。
// 由于 n = 7 ，值为 7 的节点 3 是中间节点，用红色标注。
// 返回结果为移除节点后的新链表。
// 示例 2：
// 输入：head = [1,2,3,4]
// 输出：[1,2,4]
// 解释：
// 上图表示给出的链表。
// 对于 n = 4 ，值为 3 的节点 2 是中间节点，用红色标注。
// 示例 3：
// 输入：head = [2,1]
// 输出：[2]
// 解释：
// 上图表示给出的链表。
// 对于 n = 2 ，值为 1 的节点 1 是中间节点，用红色标注。
// 值为 2 的节点 0 是移除节点 1 后剩下的唯一一个节点。

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteMiddle(head *ListNode) *ListNode {
	n := 1
	var index_mid int
	pre := head
	check_n := head
	for check_n.Next != nil {
		n++
		check_n = check_n.Next
	}
    if n == 1{
        return nil
    }
    index_mid = (n / 2)
	for i := 0; i < index_mid; i++ {
		if i == index_mid-1 {
			pre.Next = pre.Next.Next
			break
		}
		pre = pre.Next
	}
	return head
}


func main() {
	head_list := []int{1, 3, 4, 7, 1, 2, 6}
	var head *ListNode
	var per *ListNode
	// var
	for index, val := range head_list {
		temp := ListNode{
			Val:  val,
			Next: nil,
		}
		if index == 0 {
			head = &temp
			per = head
		}
		per.Next = &temp
		per = &temp
	}
	// fmt.Println(head.Val)
	// check
	check := head
	fmt.Println("check --->")
	for check.Next != nil {
		check = check.Next
		fmt.Println(check.Val)
	}
	ret_head := deleteMiddle(head)
	fmt.Println("ret --->")
	ret := ret_head
	for ret.Next != nil {
		fmt.Println(ret.Val)
		ret = ret.Next
	}
	// fmt.Println(7%2, 7/2)

}
