package main

import (
	"fmt"
	"sort"
)

func minIncrementForUnique(A []int) int {
	sort.Ints(A)
	num := 0
	if len(A) == 0{
		return num
	}
	base := A[0]
	for i:=1; i<len(A); i++{
		if A[i] <= base{
			base ++
			num += base-A[i]
		} else {
			base = A[i]
		}

	}
	return num
}

func main()  {
	a := []int{3,2,1,2,1,7}
	fmt.Println(minIncrementForUnique(a))
}
