package main

import "fmt"

type Heap []int

// 小堆代码实现

// 交换
func (h Heap) swap(i, j int) {
	if i != j {
		h[i], h[j] = h[j], h[i]
	}
}

// 比较
func (h Heap) less(i, j int) bool {
	return h[i] < h[j]
}

// 上浮
func (h *Heap) push(x int) {
	*h = append(*h, x)
	h.up(len(*h) - 1)
}

func (h Heap) up(i int) {
	for {
		//查找父节点
		f := (i - 1) / 2
		if i == f || h.less(f, i) {
			break
		}
		h.swap(i, f)
		i = f
	}
}

// 删除
func (h *Heap) remove(i int) (bool, int) {
	if i < 0 || i > len(*h)-1 {
		return false, 0
	}
	// 需要删除元素与叶子节点（最后元素）交换
	n := len(*h) - 1
	h.swap(i, n)
	// 删除最后一个元素
	x := (*h)[n]
	*h = (*h)[0:n]
	if len(*h) == 0 {
		return true, x
	}
	//如果当前元素大于父节点，继续向下
	if (*h)[i] > (*h)[(i-1)/2] || i == 0 {
		h.down(i)
	} else {
		// 当前元素小于父节点时，向上
		h.up(i)
	}
	return true, x
}

func (h Heap) down(i int) {
	for {
		// 左子节点
		l := 2*i + 1
		// 右子节点
		r := 2*i + 2
		if l > len(h)-1 {
			break
		}
		// 找出左右节点最小值
		// 先假设 左子节点为最小
		j := l
		// 判断右子节点是否为最小
		if r < len(h) && h.less(r, l) {
			j = r
		}
		// 如果父节点比子节点小，则不交换
		if h.less(i, j) {
			break
		}
		// 交换节点
		h.swap(i, j)
		// 继续向下比较
		i = j
	}
}

// 弹出栈顶元素，删除i=0的元素
func (h *Heap) pop() int {
	flag, x := h.remove(0)
	if flag {
		return x
	} else {
		return 0
	}
}

// 建立最小堆
func BuildHeap(arr []int) Heap {
	h := Heap(arr)
	n := len(h)
	// 从第一个非叶子节点，到根节点
	// 先处理右子树，找到最小值放在右子树顶
	// 在处理左子树，找到最小值放在左子树顶
	// 在处理根节点，处理左右子树树顶元素与根元素关系
	for i := n/2 - 1; i >= 0; i-- {
		h.down(i)
	}
	return h
}

// 堆排序
func HeapSort(arr []int) {
	// 创建堆
	heap := BuildHeap(arr)
	fmt.Println("heap", heap)
	var sortedArr []int
	for len(heap) > 0 {
		sortedArr = append(sortedArr, heap.pop())
	}
	fmt.Println(sortedArr)
}

func main() {

	arr := Heap{1, 3, 6, 4, 8, 7, 5}
	// h := BuildHeap(arr)
	// fmt.Println(h)

	HeapSort(arr)
}
