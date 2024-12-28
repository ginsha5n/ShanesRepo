package main
import(
	"fmt"
	"strconv"
  )
func main(){

number:= 121
isPalindrome(number)

number2 := 0
isPalindrome(number2)

number3 := 35
isPalindrome(number3)

}

func isPalindrome(x int) bool {
	  
	numString := strconv.Itoa(x)

	for i,j := 0, len(numString)-1; i<j; i,j = i+1, j-1 {
	if numString[i] != numString[j]{
		fmt.Println("false")
		return false
	}
	}
	fmt.Println("true")
	return true
	
}

