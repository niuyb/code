package main

import (
	"fmt"
	"math"
	"strconv"
)

// 给你一棵根为 root 的二叉树，请你返回二叉树中好节点的数目。
// 「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值
//
// 示例 1：
// 输入：root = [3,1,4,3,null,1,5]
// 输出：4
// 解释：图中蓝色节点为好节点。
// 根节点 (3) 永远是个好节点。
// 节点 4 -> (3,4) 是路径中的最大值。
// 节点 5 -> (3,4,5) 是路径中的最大值。
// 节点 3 -> (3,1,3) 是路径中的最大值。
// 示例 2：
// 输入：root = [3,3,null,4,2]
// 输出：3
// 解释：节点 2 -> (3, 3, 2) 不是好节点，因为 "3" 比它大。
// 示例 3：
// 输入：root = [1]
// 输出：1
// 解释：根节点是好节点。

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

// dfs 使用前序遍历，中序、后序遍历暂时不写

// dfs + 递归
func goodNodes1(root *TreeNode) (ret []int) {
	var dfs_call func(node *TreeNode)
	dfs_call = func(node *TreeNode) {
		if node == nil {
			return
		}
		ret = append(ret, node.Val)
		dfs_call(node.Left)
		dfs_call(node.Right)
	}
	dfs_call(root)
	return
}

// dfs + 迭代
// 遍历方向 1-2-4-4 left nil- 4 right nil - 5 - 5 left nil - 5 right nil - ....
func goodNodes2(root *TreeNode) (ret []int) {
	// 初始化遍历栈
	var tree_stack []*TreeNode
	// 游标
	node := root
	// node 为nil 并且 tree_stack 为空时 停止遍历
	for node != nil || len(tree_stack) > 0 {
		// 单树左节点 深入遍历 知道 左节点为nil 停止
		for node != nil {
			// 结果入结果集
			ret = append(ret, node.Val)
			// 遍历的节点入栈
			tree_stack = append(tree_stack, node)
			// 当前节点更换为 左节点
			node = node.Left
		}
		// 出循环说明左节点遍历到底了，取出当前节点的父节遍历其右节点
		node = tree_stack[len(tree_stack)-1].Right
		// 已经遍历过的节点出栈
		tree_stack = tree_stack[:len(tree_stack)-1]
	}
	return
}

// bfs + 递归
func goodNodes3(root *TreeNode) (ret []int) {
	var bfs_call func(node *TreeNode, level int)
	var depth [][]int
	var level int
	bfs_call = func(node *TreeNode, level int) {
		if node == nil {
			return
		}
		// 二维数组 树高作为二维数组的下标 保存每层的节点
		if len(depth) == level {
			depth = append(depth, []int{})
		}
		depth[level] = append(depth[level], node.Val)
		if node.Left != nil {
			bfs_call(node.Left, level+1)
		}
		if node.Right != nil {
			bfs_call(node.Right, level+1)
		}
	}
	bfs_call(root, level)
	for _, temp := range depth {
		ret = append(ret, temp...)
	}
	return

}

// bfs + 迭代
func goodNodes4(root *TreeNode) (ret []int) {
	var tree_stack []*TreeNode
	tree_stack = append(tree_stack, root)
	for len(tree_stack) > 0 {
		temp_stack := make([]*TreeNode, len(tree_stack))
		copy(temp_stack, tree_stack)
		tree_stack = tree_stack[0:0]
		for _, node := range temp_stack {
			if node != nil {
				ret = append(ret, node.Val)
			}
			if node.Left != nil {
				tree_stack = append(tree_stack, node.Left)
			}
			if node.Right != nil {
				tree_stack = append(tree_stack, node.Right)
			}
		}
	}
	return
}

func main() {

	// tree_list := []int{3, 1, 4, 3, 0, 1, 5}
	tree_list := []int{1, 2, 3, 4, 5, 6, 7}

	root := bfsArrayToTree(tree_list)
	printAvlTree(root)

	var ret []int
	ret = goodNodes1(root)
	fmt.Println("goodnode 1 --->", ret)

	ret = goodNodes2(root)
	fmt.Println("goodnode 2 --->", ret)

	ret = goodNodes3(root)
	fmt.Println("goodnode 3 --->", ret)

	ret = goodNodes4(root)
	fmt.Println("goodnode 4 --->", ret)
}
