#nested loops
"""
for i in range(0,3):
    print("i is: ",i)

    for j in range(0,5):
        print(j,end=" ")
"""
#print chess board
black="\u25A1"
white="\u25A0"
b_king="\u2654"
w_king="\u265A"
b_rook="\u2656"
b_knight="\u2658"
b_bishop="\u2657"
b_queen="\u2655"
b_pawn="\u2659"
w_rook="\u265C"
w_bishop="\u265D"
w_knight="\u265E"
w_pawn="\u265f"
w_queen="\u265B"
for i in range(0,8):
    
    for j in range(0,8):
        if (i%2==0 & i!=0 & i!=6 & i!=1 & i!=7 & i!=3 & i!=5):
            if j%2==0:
                print(black,end=" ")
            else:
                print(white,end=" ")
        elif(i==3 or i==5):
            if j%2==0:
               print(black,end=" ")
            else:
               print(white,end=" ")
        elif(i==2 or i==4):
            if j%2==0:
               print(white,end=" ")
            else:
               print(black,end=" ")
        elif(i==0):
            if(j==0 or j==7):
                print(b_rook,end=" ")
            elif(j==1 or j==6):
                print(b_knight,end=" ")  
            elif(j==2 or j==5):
                print(b_bishop,end=" ")      
            elif(j==3):
                print(b_king,end=" ")
            elif(j==4):
                print(b_queen,end=" ")
        elif(i==1):
            for j in range(0,1):
                print(b_pawn,end=" ")
        
        elif(i==6):
            for j in range(0,1):
                print(w_pawn,end=" ")
        elif(i==7):
            if(j==0 or j==7):
                print(w_rook,end=" ")
            elif(j==1 or j==6):
                print(w_knight,end=" ")  
            elif(j==2 or j==5):
                print(w_bishop,end=" ")  
            elif j==3:
              print(w_queen,end=" ")
            elif(j==4):
                print(w_king,end=" ")
        
            
        
    print()

#hw: place king and queen on theur right positions
#place knights