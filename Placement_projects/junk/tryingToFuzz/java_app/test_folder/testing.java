package test_folder;


public class testing {

    public static void main(String[] args) {
        
        //TestingFramework runCommandTest = new TestingFramework();
        //Testing the run command 
        //TestingFramework.runCommand("echo 'Hello World'");

        System.out.println("");

        //TestingFramework.runCommand("cd ..");
        TestingFramework.runCommand("java src/app.java -n 1 -p 3");

        TestingFramework.runCommand("java src/app.java -n 4 -p 4");

        // No arguments given should read values from default file.
        TestingFramework.runCommand("java src/app.java"); 

        // Testing when given a file to read values from.
        TestingFramework.runCommand("java src/app.java -f testOtherInputValues.txt");
    }
}

