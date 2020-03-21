package main

import "fmt"

func gcd(x,y int) int {
	tmp := x%y
	for tmp !=0{
		x = y
		y = tmp
		tmp = x%y
	}
	return y
}
func canMeasureWater(x,y,z int) bool {
	if x == 0 || y==0{
		return z==0 || x+y==z
	}
	if x + y < z{
		return false
	}
	if x>y{
		x,y = y,x
	}
	common := gcd(x,y)
	return z%common==0

}

func main()  {
	fmt.Println(canMeasureWater(4,6,8))
}