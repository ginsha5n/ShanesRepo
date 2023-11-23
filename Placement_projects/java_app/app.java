import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.util.Collections;

/**
 * Java doc for public class app. Conains main program.
 */
public class app {
    public static void main(String[] args) throws IOException {

        // If no argument is given both values default to 2
        String positiveWordsToRead = "2";
        String negativeWordsToRead = "2";

        for (int i = 0; i < args.length; i++) {
            if ("-p".equals(args[i]) && i + 1 < args.length) {
                positiveWordsToRead = args[i + 1];
            } else if ("-n".equals(args[i]) && i + 1 < args.length) {
                negativeWordsToRead = args[i + 1];
            }
        }

        int positiveWordsToReadInt = Integer.parseInt(positiveWordsToRead);
        int negativeWordsToReadInt = Integer.parseInt(negativeWordsToRead);

        myframework myApp = new myframework();
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

class myframework {

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
