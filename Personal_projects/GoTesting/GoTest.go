package main
import (
	"fmt"
	"time"

)
 
func main(){
	fmt.Println("Hello")
	t := time.Now()
	fmt.Println("Today is ", t.Format(time.RFC850))
}