package main

import "fmt"
import "time"

func main() {
	start := time.Now()
	//	a := []int{4, -3, 5, -2, -1, 2, 6, -2}
	a := []int{5, 9, -3, 0, 7, -9}
	maxsum := 0
	for i, _ := range a {
		j := i
		fmt.Println(j)
		for j, _ := range a {
			thissum := 0
			for k := i; k <= j; k++ {
				thissum += a[k]

			}
			if thissum > maxsum {
				maxsum = thissum
				fmt.Println(maxsum)

			}
		}
	}
	t := time.Now()
	passtime := t.Sub(start)
	fmt.Println(maxsum)
	fmt.Println(passtime)

}
