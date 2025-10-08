def reverse_words():
    s = input()
    words = s.split()
    return " ".join(reversed(words))

print(reverse_words())
