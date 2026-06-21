def find_words_longer_than_n(lst, n):
    result = []
    for i in lst:
        if (len(i) > n):
            result.append(i)
        else:
            continue
    return result


if __name__ == "__main__":

 sentence = list(input("Enter the sentence : ").split())
 n = int(input())

 print(find_words_longer_than_n(sentence, n)).