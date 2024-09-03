# Ordstatistik
# Din uppgift är att läsa in text från filen som är angiven.
# Därefter ska ditt program räkna ut följande:
# - Antal ord
# - Mest frekventa ord
# - Genomsnittlig ordlängd
# Gör en funktion för varje.

# Bonus, gör en i taget, skapa en funktion för varje: 
# - Längsta och kortaste ordet - om det finns flera, bestäm själv om du skriver ut ett eller flera
# - Räkna antalet unika ord (alltså ord som bara förekommer en gång)


def read_from_file(path: str):
    """Reads a file with the given parameter path and returns the file as a list of strings, split on newline (\n).

    Args:
        path (str): the path of the readable file

    Returns:
        list(str): list of strings
    """

    with open(path, "r" ,encoding="utf-8") as f:
        return f.readlines()
    
def count_words(sentences):
    total_words = 0
    for sentence in sentences:
        words = sentence.split(' ')
        total_words += len(words)  
    return total_words  

def frequency_of_words(sentences):
    word_frequency = {}
    for sentence in sentences:
        words = sentence.split(' ')
        for word in words:
            word = word.lower()
            word = word.strip('.,!?;:')
            if word:  
                word_frequency[word] = word_frequency.get(word, 0) + 1

    most_frequent = max(word_frequency, key=word_frequency.get)  
    return most_frequent, word_frequency[most_frequent]

def average_word_length(sentences):
    total_length = 0
    total_words = 0

    for sentence in sentences:
        words = sentence.split(' ')  
        total_words += len(words)
        for word in words:
            word = word.strip(",.!?;:")  
            total_length += len(word)  
            

    if total_words == 0:
        return 0

    return total_length / total_words

def main():
    sentences = read_from_file("en_resa_genom_svenska_skogen.txt")
    
    total_words = count_words(sentences)
    print(f"Totalt antal ord: {total_words}")
    
    most_freq_word, count = frequency_of_words(sentences)
    print(f"Mest frekventa ordet: '{most_freq_word}' med {count} förekomster")

    avg_length = average_word_length(sentences)
    print(f"Genomsnittlig ordlängd: {avg_length:.2f} tecken")

if __name__ == "__main__":
    main()
