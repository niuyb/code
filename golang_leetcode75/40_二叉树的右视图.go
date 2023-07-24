package main

import (
	"fmt"
	"math"
	"strconv"
)

// 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，
// 返回从右侧所能看到的节点值。
//  
// 示例 1:
// 输入: [1,2,3,null,5,null,4]
// 输出: [1,3,4]
// 示例 2
// 输入: [1,null,3]
// 输出: [1,3]
// 示例 3:
// 输入: []
// 输出: []


var Null int

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func getTreeHeight(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return int(1 + math.Max(float64(getTreeHeight(root.Left)), float64(getTreeHeight(root.Right))))
}
func writeArray(root *TreeNode, row, column, treeHeight int, resArray [][]string) {
	if root == nil {
		return
	}
	resArray[row][column] = strconv.Itoa(root.Val)
	currentHeight := (row + 1) / 2 // 当前高度
	if currentHeight == treeHeight {
		return // 下面没有子节点了
	}
	gap := treeHeight - currentHeight - 1 // 到左/右儿子的距离
	// 填充左儿子
	if root.Left != nil {
		// 先写树结构符号
		resArray[row+1][column-gap] = "/"
		// 再写左儿子
		writeArray(root.Left, row+2, column-gap*2, treeHeight, resArray)
	}
	// 填充右儿子
	if root.Right != nil {
		resArray[row+1][column+gap] = "\\"
		writeArray(root.Right, row+2, column+gap*2, treeHeight, resArray)
	}
}
func printAvlTree(root *TreeNode) {
	height := getTreeHeight(root)
	fmt.Printf("height: %v\n", height)
	// 总宽度为节点高度 * 2 - 1, 因为还要画树枝符号
	totalHeight := height*2 - 1
	// 最大宽度为3 * 2^(n - 1) + 1，公式如下：
	/**
	   父亲节点占1, 两个孩子空间各占1, 连接线各占1, 每个父子关系共占5, 每个关系之间空1, 最左最右各空1
	  第2行： 5 + 2 （1个父子结构占位+左右两个空格分割）
	  第3行：2 * 5 + (1 + 2) （2个父子结构占位+1个相邻父子结构间空格+左右两个空格分割）
	  第4行：4 * 5 + (3 + 2) （4个父子结构占位+3个相邻父子结构间空格+左右两个空格分割）
	  第5行：8 * 5 + (7 + 2)
	  第n行：5 * 2 ^ (n - 2) + (2 ^ (n - 2) - 1) + 2 = 6 * 2 ^ (n-2) + 1 = 3 * 2 ^ (n - 1) + 1
	*/
	var totalWidth int
	if height == 0 {
		totalWidth = 1
	} else {
		totalWidth = (2<<(height-2))*3 + 1
	}

	// 创建数组
	printArray := make([][]string, totalHeight)
	for i := range printArray {
		printArray[i] = make([]string, totalWidth)
		for j := range printArray[i] {
			printArray[i][j] = " "
		}
	}

	// 计算打印数组
	writeArray(root, 0, totalWidth/2, height, printArray)

	// 打印
	for i := range printArray {
		var res string
		for j := range printArray[i] {
			res = res + printArray[i][j]
		}
		fmt.Println(res)
	}
}

// 广度遍历数组生成树
func bfsArrayToTree(tree_list []int) *TreeNode {
	// 二叉树元素栈
	var tree_stack []*TreeNode
	// root 节点
	root := &TreeNode{
		Val: tree_list[0],
	}
	// 节点数组去除根结点
	tree_list = tree_list[1:]
	// 根节点入栈
	tree_stack = append(tree_stack, root)
	// 循环建立二叉树
	bfsBuildTree(tree_list, tree_stack)
	return root
}
func bfsBuildTree(tree_list []int, tree_stack []*TreeNode) {
	// 无栈可出时退出，说明遍历结束
	for len(tree_stack) > 0 {
		// 深copy 栈 用于不受清空栈操作影响
		temp_tree_stack := make([]*TreeNode, len(tree_stack))
		copy(temp_tree_stack, tree_stack)
		// 清空栈 不影响后续元素获取子节点
		tree_stack = tree_stack[0:0]
		// 遍历栈 出栈
		for _, node := range temp_tree_stack {
			// 出栈 链接左右子节点
			if len(tree_list) > 0 {
				if tree_list[0] != Null {
					node.Left = &TreeNode{
						Val: tree_list[0],
					}
					// 左右子节点再次入栈
					tree_stack = append(tree_stack, node.Left)
				}
				if tree_list[1] != Null {
					node.Right = &TreeNode{
						Val: tree_list[1],
					}
					// 左右子节点再次入栈
					tree_stack = append(tree_stack, node.Right)
				}
				// 二叉树左右子节点 只有2个
				tree_list = tree_list[2:]
			}
		}

	}
}

// bfs
func rightSideView2(root *TreeNode) []int {
	var ret []int
	if root == nil {
		return ret
	}
	tree_stack := make([]*TreeNode, 0)
	tree_stack = append(tree_stack, root)
	for len(tree_stack) > 0 {
		temp_tree_stack := make([]*TreeNode, len(tree_stack))
		copy(temp_tree_stack, tree_stack)
		ret = append(ret, tree_stack[len(tree_stack)-1].Val)
		tree_stack = tree_stack[0:0]
		for _, node := range temp_tree_stack {
			if node.Left != nil {
				tree_stack = append(tree_stack, node.Left)
			}
			if node.Right != nil {
				tree_stack = append(tree_stack, node.Right)
			}
		}
	}
	return ret
}

// dfs
func rightSideView(root *TreeNode) []int {
	var ret []int
	var dfs func(root *TreeNode, depth int)
	dfs = func(root *TreeNode, depth int) {
		if root == nil {
			return
		}
		if len(ret) <= depth {
			ret = append(ret, root.Val)
		}
		dfs(root.Right, depth+1)
		dfs(root.Left, depth+1)
	}
	dfs(root, 0)
	return ret
}

func main() {
	// tree_list := []int{1, 2, 3, 0, 5, 0, 4}
	tree_list := []int{1, 2, 3, 4, 5, 0, 6, 0, 7, 0, 0, 8, 0, 0, 9, 0, 0, 0, 10, 0, 0}

	root := bfsArrayToTree(tree_list)
	printAvlTree(root)

	ret := rightSideView(root)
	fmt.Println("ret ---->", ret)
}
