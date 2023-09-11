package main

import (
	"fmt"
	"math"
	"strconv"
)

// 有 n 个城市，其中一些彼此相连，另一些没有相连。
// 如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
// 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
// 给你一个 n x n 的矩阵 isConnected ，
// 其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，
// 而 isConnected[i][j] = 0 表示二者不直接相连。

// 输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
// 输出：2

// 输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
// 输出：3

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
func findCircleNum1(isConnected [][]int) int {
	steak := make([]int, 0)
	var count int
	arrive := make([]bool, len(isConnected))
	for pos, flag := range arrive {
		//未到达代表不同省份，count++
		if flag != true {
			count++
		}
		steak = append(steak, pos)
		// 栈中还有值则继续执行
		for len(steak) > 0 {
			from := steak[0]
			arrive[from] = true
			steak = steak[1:]
			//每个城市可以到达的地方入栈
			for to, path := range isConnected[from] {
				if path == 1 && !arrive[to] {
					steak = append(steak, to)
				}

			}
		}
	}
	return count
}

// dfs
func findCircleNum2(isConnected [][]int) int {
	var count int
	arrive := make([]bool, len(isConnected))
	var dfs func(int)
	dfs = func(from int) {
		arrive[from] = true
		for to, path := range isConnected[from] {
			if path == 1 && !arrive[to] {
				dfs(to)
			}
		}
	}
	for pos, flag := range arrive {
		if !flag {
			count++
			dfs(pos)
		}
	}
	return count
}

//并查集

func findCircleNum(isConnected [][]int) int {
	n := len(isConnected)
	var count int
	// 开始前，每个人的父节点都是自己
	root := make([]int, n)
	for i := range root {
		root[i] = i
	}
	// 递归找到最终父节点
	var find func(int) int
	find = func(x int) int {
		if root[x] != x {
			root[x] = find(root[x])
		}
		return root[x]
	}
	// 连接 from -> to 使用find直接赋值最终父节点
	union := func(from, to int) {
		root[find(from)] = find(to)
	}
	//遍历二维数组
	for i, row := range isConnected {
		for j := i + 1; j < n; j++ {
			if row[j] == 1 {
				union(i, j)
			}
		}
	}
	// 统计root中父节点个数，个数即为省树目
	for i, p := range root {
		if i == p {
			count++
		}
	}
	return count
}

func main() {

	isConnected := make([][]int, 3)
	isConnected[0] = []int{1, 1, 0}
	isConnected[1] = []int{1, 1, 0}
	isConnected[2] = []int{0, 0, 1}

	ret1 := findCircleNum(isConnected)
	fmt.Println("ret1 ---->", ret1)

}
