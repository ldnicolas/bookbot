import sys
def main():
    #check if we have the right number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    #get the path and book text
    path = sys.argv[1]
    text = get_book_text(path)

    #print the header 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    #counts words and prints total
    num_words = word_count(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    #count the words and print the total
    #num_words = word_count(text)
    #print(f"{num_words} words found in the document")

    #count characters (lowercased)
    char_counts = character_count(text)

    #filter out non-alphabetical characters
    filtered_counts = {char: count for char, count in char_counts.items() if char.isalpha()}

    #sort the counts
    sorted_list = dict_to_list(filtered_counts)

    #print the top 5 entries
    #print(sorted_list[:5])

    #print sorted characters coutns
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item['char']}: {item['count']}")

    #print the footer
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
        #splits by whitespace to count the words
        word_count = len(text.split())
        return word_count

def character_count(text):
    char_count = {}

    for char in text:
        char = char.lower() # normalize to lowercase 
        
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def dict_to_list(char_counts):
    # convert dictionary to list of dicts and sort by count (descending)
    return sorted(
    [{"char": key, "count": value} for key, value in char_counts.items()],
    key = lambda x: x["count"],
    reverse = True
)

if __name__ == "__main__":
    
    #get the book path from command line arguments
    path = sys.argv[1]
    
    #read the book text
    with open(path, "r") as f:
        text = f.read()

    #count the characters
    char_counts = character_count(text)

    #filter out non-alphabetical characters
    filtered_counts = {char: count for char, count in char_counts.items() if char.isalpha()}
    
    #sort the counts into a list using dict_to_list
    sorted_list = dict_to_list(filtered_counts)

    #print the sorted list
    print(sorted_list[:5])

main()