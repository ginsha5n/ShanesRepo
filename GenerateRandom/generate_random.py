import random
import string

def generate_random_content(lines, length):
    characters = string.ascii_letters + string.digits + string.punctuation + ' '

    random_content = "\n".join(" ".join(random.choice(characters)
                                        for i in range(length)) for j in range(lines))
    return random_content

def write_random_content_to_file(file_path, content_lines,  content_length):
    random_content = generate_random_content(content_lines, content_length)

    with open(file_path, "w") as f:
        f.write(random_content)

def get_random_words(file_path, num_words):
    with open(file_path, "r") as f:
        words = f.read().splitlines()
    return random.sample(words, num_words)

def write_random_sentences(new_file, num_sentences, words_per_sentence):
    with open(new_file, "w") as file:
        for _ in range(num_sentences):
            sentence = " ".join(get_random_words("words/randomWords.txt", words_per_sentence))
            file.write(sentence + "\n")



def main():
    write_random_content_to_file("random.txt", 25, 1000)
    write_random_sentences("newRandom.txt", 15, 7)

if __name__ == "__main__":
    main()
