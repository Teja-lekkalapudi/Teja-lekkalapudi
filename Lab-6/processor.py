def sanitize_string(data):
    """
    Removes special characters and trims the input.
    Assumes data is a non-empty string.
    """
    data = data.strip()
    for ch in ['!', '@', '#', '$', '%']:
        data = data.replace(ch, '')
    return data

def parse_int_list(csv_string):
    if not csv_string or not isinstance(csv_string, str):
        return []
    parts = csv_string.split(',')
    result = []
    for p in parts:
        try:
            result.append(int(p))
        except Exception:
            continue  # skip non-integer parts
    return result

def reverse_words(sentence):
    if not isinstance(sentence, str):
        return ""
    return " ".join(reversed(sentence.split()))

def main():
    print("==== Running sanitize_string ====")
    raw_string = input("Enter a string with special characters (!,@,#,$,%): ")
    clean_string = sanitize_string(raw_string)
    print("Sanitized String:", clean_string)

    print("\n==== Running parse_int_list ====")
    csv_input = input("Enter a CSV of integers (e.g. 1,2,3,4): ")
    int_list = parse_int_list(csv_input)
    print("Parsed Integer List:", int_list)

    print("\n==== Running reverse_words ====")
    sentence_input = input("Enter a sentence without punctuation: ")
    reversed_sentence = reverse_words(sentence_input)
    print("Reversed Words Sentence:", reversed_sentence)

if __name__ == "__main__":
    main()
