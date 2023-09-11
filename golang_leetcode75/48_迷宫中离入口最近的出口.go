package main

import (
	"fmt"
)

// 给你一个 m x n 的迷宫矩阵 maze （下标从 0 开始），矩阵中有空格子（用 '.' 表示）和墙（用 '+' 表示）
// 同时给你迷宫的入口 entrance ，用 entrance = [entrancerow, entrancecol]
// 表示你一开始所在格子的行和列。
// 每一步操作，你可以往 上，下，左 或者 右 移动一个格子。你不能进入墙所在的格子，你也不能离开迷宫。
// 你的目标是找到离 entrance 最近 的出口。出口 的含义是 maze 边界 上的 空格子。
// entrance 格子 不算 出口。
// 请你返回从 entrance 到最近出口的最短路径的 步数 ，如果不存在这样的路径，请你返回 -1 。

// 输入：maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
// 输出：1
// 解释：总共有 3 个出口，分别位于 (1,0)，(0,2) 和 (2,3) 。
// 一开始，你在入口格子 (1,2) 处。
// - 你可以往左移动 2 步到达 (1,0) 。
// - 你可以往上移动 1 步到达 (0,2) 。
// 从入口处没法到达 (2,3) 。
// 所以，最近的出口是 (0,2) ，距离为 1 步。

var Null int

type moveNode struct {
	x int
	y int
}

func fixborder(x, x_len int) int {
	if x > x_len-1 {
		x = x_len - 1
	} else if x < 0 {
		x = 0
	}
	return x
}

func nearestExit(maze [][]byte, entrance []int) int {
	var ans int
	move := []moveNode{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	y_len, x_len := len(maze), len(maze[0])
	curr_pos := moveNode{entrance[1], entrance[0]}
	// 标记已经遍历过的
	maze[curr_pos.y][curr_pos.x] = 0
	steak := make([]moveNode, 0)
	steak = append(steak, curr_pos)
	for len(steak) > 0 {
		temp_steak := steak
		steak = nil
		ans++
		for _, preNode := range temp_steak {
			for _, move_pos := range move {
				des_y := preNode.y + move_pos.y
				des_y = fixborder(des_y, y_len)
				des_x := preNode.x + move_pos.x
				des_x = fixborder(des_x, x_len)
				fmt.Println(des_y, des_x)
				pos_val := maze[des_y][des_x]
				if pos_val == '.' {
					if des_x == 0 || des_y == 0 || des_x == x_len-1 || des_y == y_len-1 {
						return ans
					}
					steak = append(steak, moveNode{des_x, des_y})
					maze[des_y][des_x] = 0
				}
			}
		}
	}
	return -1
}

func main() {

	maze := make([][]byte, 3)
	maze[0] = []byte{'+', '+', '.', '+'}
	maze[1] = []byte{'.', '.', '.', '+'}
	maze[2] = []byte{'+', '+', '+', '.'}

	entrance := []int{1, 2}

	ret1 := nearestExit(maze, entrance)
	fmt.Println("ret1 ---->", ret1)

}
