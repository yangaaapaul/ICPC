from collections import defaultdict
input()
dutch = input().split()
lines = [input().split() for i in range(int(input()))]
total_translations, correct_translations = 1,1
mp = [defaultdict(list), defaultdict(list)]
for line in lines:
    mp[0 if line[2] == "correct" else 1][line[0]].append(line[1])


for word in dutch:
    correct, incorrect = len(mp[0][word]), len(mp[1][word])
    total_translations *= (correct + incorrect)
    correct_translations *= correct
incorrect_translations = total_translations - correct_translations
if correct_translations + incorrect_translations  == 1:
    if correct_translations == 1:
        print(" ".join(mp[0][word][0] for word in dutch))
        print("correct")
    else:
        print(" ".join(mp[1][word][0] if mp[1][word] else mp[0][word][0] for word in dutch))  
        print("incorrect")
else:
    print(f"{correct_translations} correct")
    print(f"{incorrect_translations} incorrect")

    
