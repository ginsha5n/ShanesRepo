fun main(args: Array<String>) {
    println("Hello World!")

    val mylist = intArrayOf(1, 22, 7, 9, 14, 2)

    println("This is an unsorted array")
    printList(mylist)
    println("")

    println("This is a sorted array using a bubble sort.")
    bubbleSort(mylist)
    printList(mylist)
}

/**
 * This is the documentation for printList function
 * It takes an integer array as an argument and prints them
 * It uses print() function instead of println() to keep the output on one line.
 * it uses "$i " as i found this is kotlins equivalent of f strings
 */
fun printList(arr: IntArray){
    for( i in arr){
        print("$i ")
    }
}

/**
 * Bubble Sort in Kotlin
 *
 * For each element of the list i
 * Go through each element and compare it to the element in front of it
 * If the following element (j+1) is larger than at the current position (j) swap and move on to the next index position.
 */
fun bubbleSort(arr: IntArray){
    val n = arr.size


    for (i in 1..<n){
        for (j in 0..<n-i){
            if(arr[j] > arr[j+1]){
                val temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            }
        }
    }
}