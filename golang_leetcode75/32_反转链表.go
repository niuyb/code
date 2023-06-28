package main

import "fmt"

// 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表
// 输入：head = [1,2,3,4,5]
// 输出：[5,4,3,2,1]
// 示例 2：
// 输入：head = [1,2]
// 输出：[2,1]
// 示例 3：
// 输入：head = []
// 输出：[]

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList1(head *ListNode) *ListNode {
	var pre *ListNode
	// 当前节点
	curr := head
	//当前节点为空时，遍历完成所有节点
	for curr != nil {
		//获取下一个节点
		next := curr.Next
		// pre 之前节点与下一个节点，指向反转
		curr.Next = pre
		// 当前节点改为之前节点
		pre = curr
		// 下一个节点为当前节点
		curr = next
	}
	// next 下一个节点 pre 之前节点 next 当前节点
	return pre
}

func main() {
	head_list := []int{1, 2, 3, 4, 5}
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
	// // check
	// check := head
	// fmt.Println("check --->")
	// for {
	// 	if check.Next != nil {
	// 		fmt.Println(check.Val)
	// 		check = check.Next
	// 	} else {
	// 		fmt.Println(check.Val)
	// 		break
	// 	}
	// }

	ret_head := reverseList1(head)
	fmt.Println("ret --->")
	for {
		if ret_head.Next != nil {
			fmt.Println(ret_head.Val)
			ret_head = ret_head.Next
		} else {
			fmt.Println(ret_head.Val)
			break
		}
	}
}
