package main

import (
	"fmt"
)

// 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
// 值 0 代表空单元格；
// 值 1 代表新鲜橘子；
// 值 2 代表腐烂的橘子。
// 每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。
// 返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

// 示例 1：
// 输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
// 输出：4
// 示例 2：

// 输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
// 输出：-1
// 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
// 示例 3：

// 输入：grid = [[0,2]]
// 输出：0
// 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。

type Node struct {
	x int
	y int
}

func print2Array(grid [][]int) {
	for _, prey := range grid {
		fmt.Println(prey)
	}
}

func orangesRotting(grid [][]int) int {
	steak := make([]Node, 0)
	y_len, x_len := len(grid), len(grid[0])
	count := 0
	fresh := 0

	for y, prey := range grid {
		for x, perx := range prey {
			if perx == 2 {
				steak = append(steak, Node{x, y})
			} else if perx == 1 {
				fresh++
			}
		}
	}
	fmt.Println("fresh --->", fresh)

	for len(steak) > 0 {
		move := []Node{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
		temp_steak := steak
		steak = nil
		for _, perNode := range temp_steak {
			for _, perMove := range move {
				des_x := perNode.x + perMove.x
				des_y := perNode.y + perMove.y
				if des_x < 0 || des_x >= x_len || des_y < 0 || des_y >= y_len {
					continue
				} else {
					if grid[des_y][des_x] == 1 {
						grid[des_y][des_x] = 2
						fresh--
						steak = append(steak, Node{des_x, des_y})
					}
				}
			}
		}
		if len(steak) > 0 {
			count++
		}
	}
	if fresh > 0 {
		return -1
	}
	return count
}

func main() {

	// grid := make([][]int, 3)
	// grid[0] = []int{2, 1, 1}
	// grid[1] = []int{1, 1, 0}
	// grid[2] = []int{0, 1, 1}

	// ret1 := orangesRotting(grid)
	// fmt.Println("ret1 ---->", ret1)

	grid := make([][]int, 3)
	grid[0] = []int{2, 1, 1}
	grid[1] = []int{0, 1, 1}
	grid[2] = []int{1, 0, 1}

	ret2 := orangesRotting(grid)
	fmt.Println("ret2 ---->", ret2)

}
