def vowel_count(str):
    count=0
    vowel=set("aeiouAEIOU")
    for alphabet in str:
        if alphabet is vowel:
            count=count+1
            print("no.of vowels:",count)
str="geeksforgeeks"
vowel_count(str)
