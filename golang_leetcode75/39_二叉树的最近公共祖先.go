package main

import (
	"fmt"
	"math"
	"strconv"
)

// 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
// 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，
// 满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
// 示例 1：

// 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
// 输出：3
// 解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
// 示例 2：
// 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
// 输出：5
// 解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
// 示例 3：
// 输入：root = [1,2], p = 1, q = 2
// 输出：1

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

// 找出目标节点的所有父节点
func findAllFatherRoootInner2(node *TreeNode, target int) (ret []int) {
	var findFatherNode func(node *TreeNode) bool
	findFatherNode = func(node *TreeNode) bool {
		if node == nil {
			return false
		}
		ret = append(ret, node.Val)
		if node.Val == target {
			return true
		}
		l_flag := findFatherNode(node.Left)
		r_flag := findFatherNode(node.Right)
		if l_flag == false && r_flag == false {
			for index, val := range ret {
				if val == node.Val {
					ret = append(ret[:index], ret[index+1:]...)
					return false
				}
			}
		}
		return true
	}
	findFatherNode(node)
	return
}
func findAllFatherRooot2(node *TreeNode, p, q int) (ret int) {
	ret1 := findAllFatherRoootInner2(node, p)
	ret2 := findAllFatherRoootInner2(node, q)
	for _, i := range ret1 {
		for _, j := range ret2 {
			if i == j {
				ret = j
			}
		}
	}
	return ret
}

func findAllFatherRoootInner(node, target *TreeNode) (ret []*TreeNode) {
	var findFatherNode func(node *TreeNode) bool
	findFatherNode = func(node *TreeNode) bool {
		if node == nil {
			return false
		}
		ret = append(ret, node)
		if node == target {
			return true
		}
		l_flag := findFatherNode(node.Left)
		r_flag := findFatherNode(node.Right)
		if l_flag == false && r_flag == false {
			for index, ret_node := range ret {
				if ret_node == node {
					ret = append(ret[:index], ret[index+1:]...)
					return false
				}
			}
		}
		return true
	}
	findFatherNode(node)
	return
}

func findAllFatherRooot(node, p, q *TreeNode) (ret *TreeNode) {
	ret1 := findAllFatherRoootInner(node, p)
	ret2 := findAllFatherRoootInner(node, q)
	for _, i := range ret1 {
		for _, j := range ret2 {
			if i == j {
				ret = j
			}
		}
	}
	return ret
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	if root == p || root == q {
		return root
	}
	left := lowestCommonAncestor(root.Left, p, q)
	right := lowestCommonAncestor(root.Right, p, q)
	if left != nil && right != nil {
		return root
	}
	if left == nil {
		return right
	}
	return left
}

func main() {
	tree_list := []int{3, 5, 1, 6, 2, -1, 8, 0, 0, 7, 4}
	root := bfsArrayToTree(tree_list)
	printAvlTree(root)

	// ret := findAllFatherRoootInner2(root, 7)
	// fmt.Println("ret --->", ret)

	// ret2 := findAllFatherRoootInner2(root, 6)
	// fmt.Println("ret2 --->", ret2)

	ret3 := findAllFatherRooot2(root, 7, 4)
	fmt.Println("ret3 --->", ret3)
}
