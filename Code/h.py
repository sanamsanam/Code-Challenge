def LongestWord(sen):
    from string import ascii_letters, digits
    sen = " ".join([ch for ch in sen if ch in (ascii_letters + string.digits)])
    return sen


# keep this function call here
print LongestWord(raw_input())
