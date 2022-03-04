shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
i = 0;
for show in shows:
    print(show)
    print(i)
    i += 1

print("")   
# could also do

for index, show in enumerate(shows):
    print(show)
    print(index)