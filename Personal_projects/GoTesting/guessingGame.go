package main
import (
	"fmt"
	"math/rand"
	"time"
)

func main(){

	GuessingGame()
	
}

func GuessingGame(){

		//This fixes random int always returning the same answer???
		rand.Seed(time.Now().UnixNano()) //TODO look this up and understand whats happening.

		var userNumber int
		var answer int = rand.Intn(10)
	
		fmt.Println("Pick a number ")
		fmt.Scan(&userNumber)
		fmt.Println("You chose ", userNumber)
		fmt.Println("the correct number is ", answer)
	
		if userNumber == answer {
			fmt.Println("You win!!!")
		} else {
			fmt.Println("You lose...")
		}
}
