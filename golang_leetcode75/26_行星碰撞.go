package main

import (
	"fmt"
)

// 给定一个整数数组 asteroids，表示在同一行的行星。
// 对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向
// （正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。
// 找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。
// 如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。
//
// 示例 1：
// 输入：asteroids = [5,10,-5]
// 输出：[5,10]
// 解释：10 和 -5 碰撞后只剩下 10 。 5 和 10 永远不会发生碰撞。
// 示例 2：
// 输入：asteroids = [8,-8]
// 输出：[]
// 解释：8 和 -8 碰撞后，两者都发生爆炸。
// 示例 3：
// 输入：asteroids = [10,2,-5]
// 输出：[10]
// 解释：2 和 -5 发生碰撞后剩下 -5 。10 和 -5 发生碰撞后剩下 10 。

func asteroidCollision2(asteroids []int) (st []int) {
	for _, aster := range asteroids {
		alive := true
		for alive && aster < 0 && len(st) > 0 && st[len(st)-1] > 0 {
			alive = st[len(st)-1] < -aster // aster 是否存在
			if st[len(st)-1] <= -aster {   // 栈顶行星爆炸
				st = st[:len(st)-1]
			}
		}
		if alive {
			st = append(st, aster)
		}
	}
	return
}

func asteroidCollision(asteroids []int) []int {
	ret := make([]int, 0)
	for i := 0; i < len(asteroids); i++ {
		flag := true
		for flag && len(ret) > 0 && ret[len(ret)-1] > 0 && asteroids[i] < 0 {
			// 后者大于前者时需要新增元素，但是大小相等时，不需要新增
			flag = ret[len(ret)-1] < -asteroids[i]
			// 大小相等，或者后者大于前者 栈顶的元素删除
			if ret[len(ret)-1] <= -asteroids[i] {
				ret = ret[0 : len(ret)-1]
			} else {
				// 栈顶元素和当前元素不符合相撞条件
				break
			}
		}
		// 兼容len=0
		if flag {
			ret = append(ret, asteroids[i])
		}
		fmt.Println(ret)
	}
	return ret
}

func main() {

	asteroids := []int{5, 10, -5}
	ret := asteroidCollision(asteroids)
	fmt.Println(ret)

	// asteroids = []int{8, -8}
	// ret = asteroidCollision(asteroids)
	// fmt.Println(ret)

	// asteroids = []int{10, 2, -5}
	// ret = asteroidCollision(asteroids)
	// fmt.Println(ret)

	// asteroids = []int{-2, 1, -1, -2}
	// ret = asteroidCollision(asteroids)
	// fmt.Println(ret)

	asteroids = []int{-2, 1, 1, -1}
	ret = asteroidCollision(asteroids)
	fmt.Println(ret)
}
