package test_folder;

import java.io.*;

import FrameWork.Framework;

public class TestingFramework extends Framework {

    public static void main(String[] args) {

        runCommand("echo hello");
    }

    /**
     * A function to run a command within a java application
     * Uses process builder a class that can create an OS process using java
     * 
     * @param command
     */
    public static void runCommand(String command) {

        try {
            ProcessBuilder processBuilder = new ProcessBuilder(command.split("\\s+"));

            File testOutputFilePath = new File("TestOutputFile.log");

            try (PrintWriter writer = new PrintWriter(new FileWriter(testOutputFilePath, true))) {
                writer.println("-----Start-----");
                writer.println(command);
            }

            processBuilder.redirectOutput(ProcessBuilder.Redirect.appendTo(testOutputFilePath)); // Append output to
                                                                                                 // file

            processBuilder.redirectErrorStream(true); // Sends error steam to output

            Process process = processBuilder.start(); // Run

            InputStream inputStream = process.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));

            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            int exitCode = process.waitFor();
            System.out.println("Command: "+command);
            System.out.println("Command exited with code " + exitCode);
            System.out.println("");
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
