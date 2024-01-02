//package my_go_project
package main

import(
	"fmt"
	"os"
	"bufio"
	"strings"
)

// func main(){

// 	path_to_positive_words_file := "word_files/positive.txt"
// 	read_file_and_print_contents(path_to_positive_words_file)

// }

//TODO read from both files and put their inputs into an output file.

// func read_word_files_and_write_to_output_file(){

// 	output_file_path := "output.txt"

// 	open_file("word_files/positive.txt")
// 	open_file("word_files/negative.txt")

// 	outputFile, err := os.Create(output_file_path)
// 	if err != nil{
// 		return nil, err
// 	}
// 	return file, nil
// }

// func open_file(file_path string)error{

// 	file, err := os.Open(file_path)
// 	if err != nil {
// 		fmt.Println("Error opening file",err)
// 		return
// 	}
// 	defer file.Close()

// 	scanner := bufio.NewScanner(file)

// 	for scanner.Scan(){
// 		line := scanner.Text()
// 		fmt.Println(line)
// 	}

// 	if err := scanner.Err(); err != nil {
// 		fmt.Println("Error reading file:", err)
// 	}
// }

// func copy_contents_to_file(file *os.File, output *bufi.Writer) error{
// 	scanner := bufio.NewScanner(file)
// 	for scanner.Scan(){
// 		line := scanner.Text()
// 		_, err :=destination.WriteString(line +"\n")
// 		if err != nil {
// 			return err
// 		}
// 	}
// 	return scanner.Err()
// }

// func read_file_and_print_contents(path_to_file string){

// 		file, err := os.Open(path_to_file)
// 		if err != nil {
// 			fmt.Println("Error opening file:", err)
// 			return
// 		}
// 		defer file.Close()
	
// 		scanner := bufio.NewScanner(file)
	
// 		for scanner.Scan() {
// 			line := scanner.Text()
// 			words := strings.Fields(line)
// 			for _, word := range words {
// 				fmt.Println(word)
// 			}
// 		}
	
// 		if err := scanner.Err(); err != nil {
// 			fmt.Println("Error reading file:", err) // Check for errors during scanning
// 		}
// 	}
func read_file_and_print_contents(pathToFile, content string) error {
	// Instead of opening a file, create a reader from the fuzzed content
	reader := strings.NewReader(content)

	scanner := bufio.NewScanner(reader)

	for scanner.Scan() {
		line := scanner.Text()
		words := strings.Fields(line)
		for _, word := range words {
			fmt.Println(word)
		}
	}

	return scanner.Err()
}

func Fuzz(data []byte) int {
	content := string(data)

	file_path := "word_files/positive.txt"

	err := read_file_and_print_contents(file_path, content)
	if err != nil {
		return 0
	}
	return 1 //return 1 with success
}

