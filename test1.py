def verify_words(char):
    return {
        'A': 1,
        'B': 2,
        'D': 1,
        'O': 1,
        'P': 1,
        'Q': 1,
        'R': 1,
        '4' : 1,
        '6' : 1,
        '8' : 2,
        '9' : 1,
        '0' : 1
    }.get(char, 0)

num_cases = int(input("Total of cases that you want test: "));
if ((num_cases >= 40) or (num_cases < 0)):
    print("You dont enter with valid number of cases");    
else:
    total_entry= []
    i=0;
    while i < num_cases:
        entry = input()
        if(len(entry) < 100 and entry != ''):
            total_entry.append(entry)
        i+=1;
    for item in total_entry:
        total_holes=0;
        for char in item:
            total_holes += verify_words(char)
        print(total_holes)        
        
