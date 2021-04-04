package main

import "fmt"
import "time"

func main() {

	start := time.Now()
	a := []int{4, -3, 5, -2, -1, 2, 6, -2, 4, -3, 5, -2, -1, 2, 6, -2}
	maxSum := 0
	thisSum := 0
	for i := 0; i < len(a); i++ {

		thisSum += a[i]
		if thisSum < 0 {

			thisSum := 0
			fmt.Println(thisSum)
		} else if thisSum > maxSum {
			maxSum = thisSum
		}

	}
	fmt.Println(maxSum)
	t := time.Now()
	passtime := t.Sub(start)
	fmt.Println(passtime)

}
