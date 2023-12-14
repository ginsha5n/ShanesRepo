package main

import(
	"fmt"
	"os"
	"bufio"
	"strings"
)

func main(){

	path_to_positive_words_file := "word_files/positive.txt"
	read_file_and_print_contents(path_to_positive_words_file)

}

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

func read_file_and_print_contents(path_to_file string){
		// Open the file
		file, err := os.Open(path_to_file)
		if err != nil {
			fmt.Println("Error opening file:", err)
			return
		}
		defer file.Close()
	
		// Create a scanner to read the file
		scanner := bufio.NewScanner(file)
	
		// Loop through each line of the file
		for scanner.Scan() {
			line := scanner.Text()
	
			// Split the line into words
			words := strings.Fields(line)
	
			// Print each word
			for _, word := range words {
				fmt.Println(word)
			}
		}
	
		// Check for errors during scanning
		if err := scanner.Err(); err != nil {
			fmt.Println("Error reading file:", err)
		}
	}

