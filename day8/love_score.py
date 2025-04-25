
def calc_truelove(arr1, arr2):
    true_score = 0
    love_score = 0

    for letter in arr1:
        if letter == 't':
            true_score += 1
        if letter == 'r':
            true_score += 1
        if letter == 'u':
            true_score += 1
        if letter == 'e':
            true_score += 1
        if letter == 'l':
            love_score += 1
        if letter == 'o':
            love_score += 1
        if letter == 'v':
            love_score += 1
        if letter == 'e':
            love_score += 1

    for letter in arr2:
        if letter == 't':
            true_score += 1
        if letter == 'r':
            true_score += 1
        if letter == 'u':
            true_score += 1
        if letter == 'e':
            true_score += 1
        if letter == 'l':
            love_score += 1
        if letter == 'o':
            love_score += 1
        if letter == 'v':
            love_score += 1
        if letter == 'e':
            love_score += 1
    
    return(f'{true_score}{love_score}')
    



def calc_love_score(name1, name2):
    
    name1_arr = list(name1.lower())
    name2_arr = list(name2.lower())

    love_score = calc_truelove(name1_arr, name2_arr)

    print(f"{name1} and {name2}'s love score is {love_score}")

   

    

    

calc_love_score('Kanye West', 'Kim Kardashian')