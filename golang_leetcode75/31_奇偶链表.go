package main

import (
	"fmt"
)

// 给定单链表的头节点 head ，将所有索引为奇数的节点和索引为偶数的节点分别组合在一起，然后返回重新排序的列表。
// 第一个节点的索引被认为是 奇数 ， 第二个节点的索引为 偶数 ，以此类推。
// 请注意，偶数组和奇数组内部的相对顺序应该与输入时保持一致。
// 你必须在 O(1) 的额外空间复杂度和 O(n) 的时间复杂度下解决这个问题。

// 示例 1:
// 输入: head = [1,2,3,4,5]
// 输出: [1,3,5,2,4]
// 示例 2:
// 输入: head = [2,1,3,5,6,4,7]
// 输出: [2,3,6,7,1,5,4]

type ListNode struct {
	Val  int
	Next *ListNode
}

func oddEvenList1(head *ListNode) *ListNode {
	var odd, even, ret_head, odd_head *ListNode
	var index int
	for {
		index++
		if head != nil {
			if index%2 == 0 {
				if odd == nil {
					odd = &ListNode{
						Val: head.Val,
					}
					odd_head = odd
				} else {
					odd.Next = &ListNode{
						Val: head.Val,
					}
					odd = odd.Next
				}
			} else {
				if even == nil {
					even = &ListNode{
						Val: head.Val,
					}
					ret_head = even
				} else {
					even.Next = &ListNode{
						Val: head.Val,
					}
					even = even.Next
				}
			}
			head = head.Next
		} else {
			break
		}
	}
	even.Next = odd_head
	return ret_head
}


func oddEvenList(head *ListNode) *ListNode {
    if head == nil {
        return head
    }
    evenHead := head.Next
    odd := head
    even := evenHead
    for even != nil && even.Next != nil {
        odd.Next = even.Next
        odd = odd.Next
        even.Next = odd.Next
        even = even.Next
    }
    odd.Next = evenHead
    return head
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
	// check
	check := head
	fmt.Println("check --->")
	for {
		if check.Next != nil {
			fmt.Println(check.Val)
			check = check.Next
		} else {
			fmt.Println(check.Val)
			break
		}
	}

	ret_head := oddEvenList1(head)
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
