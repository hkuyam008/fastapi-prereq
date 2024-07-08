def capitalize(s):
    if 1000>len(s)>0:
        return " ".join([word if len(word) == 0 or word[0].isnumeric() else word.title() for word in s.split(" ")])
    else:
        return s
    #return s.split(" ")

def main():
    while True:
        s = input()
        if s.lower() == "exit":
            break
        else:
            print(capitalize(s))
        
main()