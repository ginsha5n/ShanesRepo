package main

import (
	"fmt"
	"os"
	"strconv"
)

/*
 This application takes an imput as a cli argument and converts it to an integer
 The application prints hello multiplied by the input integer.
*/
func main() {

	args := os.Args

	num, err := strconv.Atoi(args[1]) //Atoi Ascii to integer
	if err != nil {
		fmt.Println("Invalid input. Please provide a valid integer.")
		return
	}

	for i:= 0; i<num ; i++{
	print_hello()}

}

func print_hello() {
	fmt.Println("Hello")
}
