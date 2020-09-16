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

num_cases = int(input("Total of cases that you want test: "))
if ((num_cases >= 40) or (num_cases <= 0)):
     print("You dont enter with valid number of cases")    
else:
    i=0;
    print("Input with you word: ");
    while i <= num_cases:
        entry = input();
        cases = 0;
        for char in entry:
             cases += verify_words(char);   
        print(entry + ' ' , cases);
        i +=1;