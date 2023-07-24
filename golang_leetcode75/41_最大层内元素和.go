package main

import (
	"fmt"
	"math"
	"strconv"
)

// 给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。
// 请返回层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中 最小 的那个。
//
// 示例 1：
// 输入：root = [1,7,0,7,-8,null,null]
// 输出：2
// 解释：
// 第 1 层各元素之和为 1，
// 第 2 层各元素之和为 7 + 0 = 7，
// 第 3 层各元素之和为 7 + -8 = -1，
// 所以我们返回第 2 层的层号，它的层内元素之和最大。
// 示例 2：
// 输入：root = [989,null,10250,98693,-89388,null,null,null,-32127]
// 输出：2

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
func maxLevelSum2(root *TreeNode) int {
	var tree_stack []*TreeNode
	sum := make([]int, 0)
	var min_floor int

	tree_stack = append(tree_stack, root)
	for len(tree_stack) > 0 {
		temp_tree_stack := make([]*TreeNode, len(tree_stack))
		copy(temp_tree_stack, tree_stack)
		tree_stack = tree_stack[0:0]
		var temp_max int
		for _, node := range temp_tree_stack {
			temp_max += node.Val
			if node.Left != nil {
				tree_stack = append(tree_stack, node.Left)
			}
			if node.Right != nil {
				tree_stack = append(tree_stack, node.Right)
			}
		}
		sum = append(sum, temp_max)
	}
	fmt.Println(sum)
	for d, v := range sum {
		if v > sum[min_floor] {
			min_floor = d
		}
	}
	return min_floor + 1
}

// dfs
func maxLevelSum(root *TreeNode) int {
	var sum []int
	var min_floor int
	var dfs func(*TreeNode, int)
	dfs = func(node *TreeNode, depth int) {
		if node == nil {
			return
		}
		if len(sum) <= depth {
			sum = append(sum, node.Val)
		} else {
			sum[depth] += node.Val
		}
		dfs(node.Left, depth+1)
		dfs(node.Right, depth+1)
	}
	dfs(root, 0)
	for index, val := range sum {
		if val > sum[min_floor] {
			min_floor = index
		}
	}
	// 层数从1开始计算
	return min_floor + 1
}

func main() {
	tree_list := []int{1, 2, 3, 4, 5, 0, 6, 0, 7, 0, 0, 8, 0, 0, 9, 0, 0, 0, 10, 0, 0}

	root := bfsArrayToTree(tree_list)
	printAvlTree(root)

	ret := maxLevelSum2(root)
	fmt.Println("ret ---->", ret)
}
