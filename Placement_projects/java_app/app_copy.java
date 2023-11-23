
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.util.Collections;
import java.util.Scanner;
import java.io.File;

/**
 * app_copy.java, i got app.java to a working condition but before adding
 * additional functions and potentially breaking the original i created this
 * copy
 * to do further work without risking the original. Maybe i should be using
 * version control and making a branch but as this is a personal project and
 * no one else is looking at it ill just do this.
 */
public class app_copy {
    public static void main(String[] args) throws IOException {

        // If no argument is given both values default to 2
        String positiveWordsToRead = null;
        String negativeWordsToRead = null;
        String defaultValuesFilePath = "defaultValues.txt";

        for (int i = 0; i < args.length; i++) {
            if ("-p".equals(args[i]) && i + 1 < args.length) {
                positiveWordsToRead = args[i + 1];
            } else if ("-n".equals(args[i]) && i + 1 < args.length) {
                negativeWordsToRead = args[i + 1];
            } else if ("-i".equals(args[i]) && i +1 < args.length){
                defaultValuesFilePath = args[i + 1];
            }
        }

        // If the value isnt found in command line arguments open the default values
        // file,
        // find the corresponding argument and take the value from there.
        if (positiveWordsToRead == null) {
            try {
                Scanner fileScanner = new Scanner(new File(defaultValuesFilePath));
                while (fileScanner.hasNext()) {
                    String token = fileScanner.next();
                    if ("-p".equals(token) && fileScanner.hasNext()) { // if "-p" is found in the file and theres
                                                                       // something after it, take the following value
                                                                       // as positiveWordsToRead
                        positiveWordsToRead = fileScanner.next();
                        break;
                    }
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        if (negativeWordsToRead == null) {
            try {
                Scanner fileScanner2 = new Scanner(new File(defaultValuesFilePath));
                while (fileScanner2.hasNext()) {
                    String token2 = fileScanner2.next();
                    if ("-n".equals(token2) && fileScanner2.hasNext()) { // if "-n" is found in the file and theres
                                                                         // something after it, take the following value
                                                                         // as positiveWordsToRead
                        negativeWordsToRead = fileScanner2.next();
                        break;
                    }
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        int positiveWordsToReadInt = Integer.parseInt(positiveWordsToRead);
        int negativeWordsToReadInt = Integer.parseInt(negativeWordsToRead);

        FrameWork myApp = new FrameWork();
        myApp.print();

        String positiveFilePath = "words_folder/positive.txt";
        String negativeFilePath = "words_folder/negative.txt";
        String outputFilePath = "outputFile.txt";

        // Create arrays by reading words from given files
        List<String> positiveList = myApp.readWordsFromFile(positiveFilePath, positiveWordsToReadInt);
        List<String> negativeList = myApp.readWordsFromFile(negativeFilePath, negativeWordsToReadInt);

        // Print lists
        System.out.println(Arrays.toString(positiveList.toArray()));
        System.out.println(Arrays.toString(negativeList.toArray()));

        System.out.println("");

        // Create new file
        myApp.createNewFile(outputFilePath, positiveFilePath, positiveWordsToReadInt, negativeFilePath,
                negativeWordsToReadInt);

    }
}

class FrameWork{

    public void print() {
        System.out.println("Hello World");
    }

    /**
     * Function to create a new file by mixing the words taken from 2 other files
     * and mixing and writing those line
     * to another output file.
     * 
     * @param outputfilePath   path to where the file will write an output list
     * @param fileOne          path to a file that will have its contents read and
     *                         writen to output file
     * @param fileTwo          path to another file that will ahve its contents
     *                         mixed
     *                         with another to create another output.
     * @param wordsFromFileOne integer value of how many words to take from file
     *                         one.
     * @param wordsFromFileTwo integer vaue of how many words to take from file two.
     * @throws IOException
     */
    public void createNewFile(String outputfilePath, String fileOne, int wordsFromFileOne, String fileTwo,
            int wordsFromFileTwo) throws IOException {

        List<String> fileOneWords = this.readWordsFromFile(fileOne, wordsFromFileOne);
        List<String> fileTwoWords = this.readWordsFromFile(fileTwo, wordsFromFileTwo);
        List<String> outputWords = this.mixLists(fileOneWords, fileTwoWords);
        this.writeToFile(outputfilePath, outputWords);
        System.out.println("Words printed to file " + outputfilePath);
    }

    public List<String> readWordsFromFile(String fileName, int wordsToRead) throws IOException {
        List<String> words = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String line;
            int wordsRead = 0;
            while ((line = reader.readLine()) != null && wordsRead < wordsToRead) { // As long as the line being read != nothing and the word read count has not been reached
                words.add(line.trim()); // Each word is on a separate line
                wordsRead++;
            }
        }
        return words;
    }

    /**
     * Takes two lists and combines them together.
     * 
     * @param list1
     * @param list2
     * @return combined list1 and list2 in one string.
     */
    public List<String> mixLists(List<String> list1, List<String> list2) {
        List<String> mixedList = new ArrayList<>(list1);
        mixedList.addAll(list2);
        Collections.shuffle(mixedList);
        return mixedList;
    }

    /*
     * Given a path to a file and a list, the list items will create or overwrtie
     * the file with the items in the list.
     */
    public void writeToFile(String outputFilePath, List<String> words) throws IOException {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(outputFilePath))) {
            for (String word : words) {
                writer.write(word);
                writer.newLine();
            }
        }
    }
}
