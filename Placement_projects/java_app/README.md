# Intro
This project takes two text files and uses them to produce an outfile of words taken from both files and mixed together.

Different variations of output can be produced by passing in the number of words you want taken from one or both files.

-p {integer number} specifies how many words to take from file one (positive words file)
-n {integer number} specifies how many words to take from file two (negative words file)

There are currently 2 versions, app.java and app_copy.java.
app_copy.java is a further developed version that takes it default values from a txt file that can be specified "-f {filePath} or left blank and use defaultValues.txt

app.java just uses the value 2 as the default amount of words to take from the files if no arguments are provided.

The reason there are two files is because when I orginally got app.java to a working condition and decided i was going to change its functionality i didnt want ot break what i had so i created
app_copy.java to continue the work on while keeping the original in order.
A future improvement or something to keep in mind in future projects is to use version control such as git to keep my file structure cleaner and less confusing. I could have created app.java in 
a repository, got it to a working state and then when i wanted to change the functionality i could have created a branch and work on that version until I achieved the goal and then merge it 
back to the main branch with the changes.

# Testing

from java_app directory, run java test_folder/testing.java
This will run the testing file which runs the app multiple times.
