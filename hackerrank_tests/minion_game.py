def minion_game(str):
    vowels_list = ['A', 'E', 'I', 'O', 'U']    
    stuart_score = 0    
    kevin_score = 0        
    str_len = len(str)
    
    for i in range(str_len):
        if str[i] in vowels_list:
            kevin_score+=(str_len-i)
        else:
            stuart_score+=(str_len-i)
                
    if stuart_score > kevin_score:        
        print(f"Stuart {stuart_score}")    
    elif stuart_score < kevin_score:        
        print(f"Kevin {kevin_score}")    
    else:        
        print("Draw")
                
            

if __name__ == '__main__':
    s = input()
    minion_game(s)