def checkio(text: str) -> str:
    counter = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter in counter:
                counter[letter] = counter.get(letter)+1
            else:
                counter[letter] = 1
        #else:
            #pass
    sorted_counter = dict(sorted(counter.items()))
    max_sorted_key = max(sorted_counter, key = sorted_counter.get)
    return max_sorted_key


if __name__ == '__main__':

    print(checkio("hello world"))
