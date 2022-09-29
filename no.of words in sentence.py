def countwords(s):
    if s.strip()==" ":
        return 0
    words =s.split()
    return len(words)
if __name__=="__main__":
    s="saveetha university"
    print("no of words:",countwords(s))
