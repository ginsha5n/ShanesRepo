/* */

fun main(){

    val nums1: IntArray = intArrayOf(2,7,11,15)
    val target1 = 9

    twoSum(nums1, target1)
    //TODO Make a validate function where i can input what i know the answer is and compare it against what the function returns, return true for mathc and false for no.

}

//TODO add some documentation of what the problem is and how the algoritm goes about solving it.
fun twoSum(nums: IntArray, target: Int): IntArray{ // : IntArray means its expecting an integer array to be returned.

    for (i in 0 until nums.size-1){

          for (j in i+1 until nums.size){

            if(nums[i] + nums[j] == target){
              println("$i $j")  
              return intArrayOf(i,j)
              
            }
          }
        }
        return intArrayOf()
}
