
print("\nImagine the Rubik's Cube as letter 'T' and enter the color of each piece from top most left side to the right and then downwards :")

asc=64
color = [[['\0' for z in range(3)]for y in range(3)] for x in range(6)]
for e in range(6):
    for f in range(3):
        for g in range(3):
            color[e][f][g]=input()

for w in range(6):
    temp=color[w][1][1]
    asc = asc + 1
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if color[i][j][k]==temp:
                    color[i][j][k]=chr(asc)
# B

def B():

    temp=color[1][0][0]
    color[1][0][0]=color[2][0][0]
    color[2][0][0]=color[4][2][2]
    color[4][2][2]=color[0][0][0]
    color[0][0][0]=temp

    temp=color[1][0][1]
    color[1][0][1]=color[2][0][1]
    color[2][0][1]=color[4][2][1]
    color[4][2][1]=color[0][0][1]
    color[0][0][1]=temp

    temp=color[1][0][2]
    color[1][0][2]=color[2][0][2]
    color[2][0][2]=color[4][2][0]
    color[4][2][0]=color[0][0][2]
    color[0][0][2]=temp

    temp=color[5][0][0]
    color[5][0][0]=color[5][2][0]
    color[5][2][0]=color[5][2][2]
    color[5][2][2]=color[5][0][2]
    color[5][0][2]=temp

    temp=color[5][0][1]
    color[5][0][1]=color[5][1][0]
    color[5][1][0]=color[5][2][1]
    color[5][2][1]=color[5][1][2]
    color[5][1][2]=temp
    
# b

def b():
    
    temp=color[1][0][0]
    color[1][0][0]=color[0][0][0]
    color[0][0][0]=color[4][2][2]
    color[4][2][2]=color[2][0][0]
    color[2][0][0]=temp

    temp=color[1][0][1]
    color[1][0][1]=color[0][0][1]
    color[0][0][1]=color[4][2][1]
    color[4][2][1]=color[2][0][1]
    color[2][0][1]=temp
    
    temp=color[1][0][2]
    color[1][0][2]=color[0][0][2]
    color[0][0][2]=color[4][2][0]
    color[4][2][0]=color[2][0][2]
    color[2][0][2]=temp

    temp=color[5][0][0]
    color[5][0][0]=color[5][0][2]
    color[5][0][2]=color[5][2][2]
    color[5][2][2]=color[5][2][0]
    color[5][2][0]=temp

    temp=color[5][0][1]
    color[5][0][1]=color[5][1][2]
    color[5][1][2]=color[5][2][1]
    color[5][2][1]=color[5][1][0]
    color[5][1][0]=temp
    
# L

def L():

    temp=color[1][0][0]
    color[1][0][0]=color[5][0][0]
    color[5][0][0]=color[4][0][0]
    color[4][0][0]=color[3][0][0]
    color[3][0][0]=temp

    temp=color[1][1][0]
    color[1][1][0]=color[5][1][0]
    color[5][1][0]=color[4][1][0]
    color[4][1][0]=color[3][1][0]
    color[3][1][0]=temp

    temp=color[1][2][0]
    color[1][2][0]=color[5][2][0]
    color[5][2][0]=color[4][2][0]
    color[4][2][0]=color[3][2][0]
    color[3][2][0]=temp

    temp=color[0][0][0]
    color[0][0][0]=color[0][2][0]
    color[0][2][0]=color[0][2][2]
    color[0][2][2]=color[0][0][2]
    color[0][0][2]=temp

    temp=color[0][0][1]
    color[0][0][1]=color[0][1][0]
    color[0][1][0]=color[0][2][1]
    color[0][2][1]=color[0][1][2]
    color[0][1][2]=temp

# l

def l():

    temp=color[1][0][0]
    color[1][0][0]=color[3][0][0]
    color[3][0][0]=color[4][0][0]
    color[4][0][0]=color[5][0][0]
    color[5][0][0]=temp
    
    temp=color[1][1][0]
    color[1][1][0]=color[3][1][0]
    color[3][1][0]=color[4][1][0]
    color[4][1][0]=color[5][1][0]
    color[5][1][0]=temp

    temp=color[1][2][0]
    color[1][2][0]=color[3][2][0]
    color[3][2][0]=color[4][2][0]
    color[4][2][0]=color[5][2][0]
    color[5][2][0]=temp

    temp=color[0][0][0]
    color[0][0][0]=color[0][0][2]
    color[0][0][2]=color[0][2][2]
    color[0][2][2]=color[0][2][0]
    color[0][2][0]=temp

    temp=color[0][0][1]
    color[0][0][1]=color[0][1][2]
    color[0][1][2]=color[0][2][1]
    color[0][2][1]=color[0][1][0]
    color[0][1][0]=temp

# R

def R():

    temp=color[1][0][2]
    color[1][0][2]=color[3][0][2]
    color[3][0][2]=color[4][0][2]
    color[4][0][2]=color[5][0][2]
    color[5][0][2]=temp
    
    temp=color[1][1][2]
    color[1][1][2]=color[3][1][2]
    color[3][1][2]=color[4][1][2]
    color[4][1][2]=color[5][1][2]
    color[5][1][2]=temp

    temp=color[1][2][2]
    color[1][2][2]=color[3][2][2]
    color[3][2][2]=color[4][2][2]
    color[4][2][2]=color[5][2][2]
    color[5][2][2]=temp

    temp=color[2][0][0]
    color[2][0][0]=color[2][2][0]
    color[2][2][0]=color[2][2][2]
    color[2][2][2]=color[2][0][2]
    color[2][0][2]=temp

    temp=color[2][0][1]
    color[2][0][1]=color[2][1][0]
    color[2][1][0]=color[2][2][1]
    color[2][2][1]=color[2][1][2]
    color[2][1][2]=temp

# r

def r():

    temp=color[1][0][2]
    color[1][0][2]=color[5][0][2]
    color[5][0][2]=color[4][0][2]
    color[4][0][2]=color[3][0][2]
    color[3][0][2]=temp

    temp=color[1][1][2]
    color[1][1][2]=color[5][1][2]
    color[5][1][2]=color[4][1][2]
    color[4][1][2]=color[3][1][2]
    color[3][1][2]=temp

    temp=color[1][2][2]
    color[1][2][2]=color[5][2][2]
    color[5][2][2]=color[4][2][2]
    color[4][2][2]=color[3][2][2]
    color[3][2][2]=temp

    temp=color[2][0][0]
    color[2][0][0]=color[2][0][2]
    color[2][0][2]=color[2][2][2]
    color[2][2][2]=color[2][2][0]
    color[2][2][0]=temp

    temp=color[2][0][1]
    color[2][0][1]=color[2][1][2]
    color[2][1][2]=color[2][2][1]
    color[2][2][1]=color[2][1][0]
    color[2][1][0]=temp

# F

def F():

    temp=color[1][2][0]
    color[1][2][0]=color[0][2][0]
    color[0][2][0]=color[4][0][2]
    color[4][0][2]=color[2][2][0]
    color[2][2][0]=temp

    temp=color[1][2][1]
    color[1][2][1]=color[0][2][1]
    color[0][2][1]=color[4][0][1]
    color[4][0][1]=color[2][2][1]
    color[2][2][1]=temp
    
    temp=color[1][2][2]
    color[1][2][2]=color[0][2][2]
    color[0][2][2]=color[4][0][0]
    color[4][0][0]=color[2][2][2]
    color[2][2][2]=temp

    temp=color[3][0][0]
    color[3][0][0]=color[3][2][0]
    color[3][2][0]=color[3][2][2]
    color[3][2][2]=color[3][0][2]
    color[3][0][2]=temp

    temp=color[3][0][1]
    color[3][0][1]=color[3][1][0]
    color[3][1][0]=color[3][2][1]
    color[3][2][1]=color[3][1][2]
    color[3][1][2]=temp
    
# f

def f():

    temp=color[1][2][0]
    color[1][2][0]=color[2][2][0]
    color[2][2][0]=color[4][0][2]
    color[4][0][2]=color[0][2][0]
    color[0][2][0]=temp

    temp=color[1][2][1]
    color[1][2][1]=color[2][2][1]
    color[2][2][1]=color[4][0][1]
    color[4][0][1]=color[0][2][1]
    color[0][2][1]=temp

    temp=color[1][2][2]
    color[1][2][2]=color[2][2][2]
    color[2][2][2]=color[4][0][0]
    color[4][0][0]=color[0][2][2]
    color[0][2][2]=temp

    temp=color[3][0][0]
    color[3][0][0]=color[3][0][2]
    color[3][0][2]=color[3][2][2]
    color[3][2][2]=color[3][2][0]
    color[3][2][0]=temp

    temp=color[3][0][1]
    color[3][0][1]=color[3][1][2]
    color[3][1][2]=color[3][2][1]
    color[3][2][1]=color[3][1][0]
    color[3][1][0]=temp

# D

def D():

    temp=color[3][2][0]
    color[3][2][0]=color[0][0][0]
    color[0][0][0]=color[5][0][2]
    color[5][0][2]=color[2][2][2]
    color[2][2][2]=temp
    
    temp=color[3][2][1]
    color[3][2][1]=color[0][1][0]
    color[0][1][0]=color[5][0][1]
    color[5][0][1]=color[2][1][2]
    color[2][1][2]=temp
    
    temp=color[3][2][2]
    color[3][2][2]=color[0][2][0]
    color[0][2][0]=color[5][0][0]
    color[5][0][0]=color[2][0][2]
    color[2][0][2]=temp
    
    temp=color[4][0][0]
    color[4][0][0]=color[4][2][0]
    color[4][2][0]=color[4][2][2]
    color[4][2][2]=color[4][0][2]
    color[4][0][2]=temp

    temp=color[4][0][1]
    color[4][0][1]=color[4][1][0]
    color[4][1][0]=color[4][2][1]
    color[4][2][1]=color[4][1][2]
    color[4][1][2]=temp

# d

def d():

    temp=color[3][2][0]
    color[3][2][0]=color[2][2][2]
    color[2][2][2]=color[5][0][2]
    color[5][0][2]=color[0][0][0]
    color[0][0][0]=temp
    
    temp=color[3][2][1]
    color[3][2][1]=color[2][1][2]
    color[2][1][2]=color[5][0][1]
    color[5][0][1]=color[0][1][0]
    color[0][1][0]=temp
    
    temp=color[3][2][2]
    color[3][2][2]=color[2][0][2]
    color[2][0][2]=color[5][0][0]
    color[5][0][0]=color[0][2][0]
    color[0][2][0]=temp
    
    temp=color[4][0][0]
    color[4][0][0]=color[4][0][2]
    color[4][0][2]=color[4][2][2]
    color[4][2][2]=color[4][2][0]
    color[4][2][0]=temp

    temp=color[4][0][1]
    color[4][0][1]=color[4][1][2]
    color[4][1][2]=color[4][2][1]
    color[4][2][1]=color[4][1][0]
    color[4][1][0]=temp
    
# Top 4 edges

booked=[[-1 for a in range(3)]for b in range(4)]
result=[]
w=0
while w<4 :
    for x in range(6):
        for y in range(3):
            for z in range(3):
            
                if ((y==0 and z==1) or (y==1 and z==0) or (y==1 and z==2) or (y==2 and z==1)) and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:

                    if [x,y,z]==[1,0,1] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        B()
                        result.append('B')
                        B()
                        result.append('B')
                        if color[5][0][1]==color[5][1][1]:
                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[5][0][1]==color[0][1][1]:
                            D()
                            result.append('D')
                            L()
                            result.append('L')
                            L()
                            result.append('L')

                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                        elif color[5][0][1]==color[2][1][1]:
                            d()
                            result.append('d')
                            R()
                            result.append('R')
                            R()
                            result.append('R')
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             
                        elif color[5][0][1]==color[3][1][1]:
                            D()
                            result.append('D')
                            D()
                            result.append('D')
                            F()
                            result.append('F')
                            F()
                            result.append('F')

                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1
                             
                    elif [x,y,z]==[1,1,0] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        L()
                        result.append('L')
                        L()
                        result.append('L')
                        if color[0][1][0]==color[0][1][1]:
                            L()
                            result.append('L')
                            L()
                            result.append('L')
                            
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                        elif color[0][1][0]==color[3][1][1]:
                            D()
                            result.append('D')
                            F()
                            result.append('F')
                            F()
                            result.append('F')
                            
                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[0][1][0]==color[5][1][1]:
                            d()
                            result.append('d')
                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             

                        elif color[0][1][0]==color[2][1][1]:
                            D()
                            result.append('D')
                            D()
                            result.append('D')
                            R()
                            result.append('R')
                            R()
                            result.append('R')

                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             
                    elif [x,y,z]==[1,1,2] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        R()
                        result.append('R')
                        R()
                        result.append('R')
                        if color[2][1][2]==color[2][1][1]:
                            R()
                            result.append('R')
                            R()
                            result.append('R')
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             
                        elif color[2][1][2]==color[5][1][1]:
                            D()
                            result.append('D')
                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[2][1][2]==color[3][1][1]:
                            d()
                            result.append('d')
                            F()
                            result.append('F')
                            F()
                            result.append('F')
                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[2][1][2]==color[0][1][1]:
                            
                            D()
                            result.append('D')
                            D()
                            result.append('D')
                            L()
                            result.append('L')
                            L()
                            result.append('L')
                            
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                    elif [x,y,z]==[1,2,1] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        F()
                        result.append('F')
                        F()
                        result.append('F')
                        if color[3][2][1]==color[3][1][1]:
                            
                            F()
                            result.append('F')
                            F()
                            result.append('F')

                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[3][2][1]==color[2][1][1]:
                            
                            D()
                            result.append('D')
                            R()
                            result.append('R')
                            R()
                            result.append('R')
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             
                        elif color[3][2][1]==color[0][1][1]:
                            d()
                            result.append('d')
                            L()
                            result.append('L')
                            L()
                            result.append('L')
                            
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                        elif color[3][2][1]==color[5][1][1]:
                            D()
                            result.append('D')
                            D()
                            result.append('D')

                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             
                    elif [x,y,z]==[5,2,1] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        B()
                        result.append('B')
                        l()
                        result.append('l')
                        d()
                        result.append('d')
                        L()
                        result.append('L')
                        D()
                        result.append('D')
                        b()
                        result.append('b')
                        if color[0][1][0]==color[0][1][1]:
                            L()
                            result.append('L')
                            L()
                            result.append('L')
                            
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                        elif color[0][1][0]==color[3][1][1]:
                            D()
                            result.append('D')
                            F()
                            result.append('F')
                            F()
                            result.append('F')
                            
                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[0][1][0]==color[5][1][1]:
                            d()
                            result.append('d')
                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[0][1][0]==color[2][1][1]:
                            D()
                            result.append('D')
                            D()
                            result.append('D')
                            R()
                            result.append('R')
                            R()
                            result.append('R')

                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             
                    elif [x,y,z]==[5,1,2] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        R()
                        result.append('R')
                        D()
                        result.append('D')
                        r()
                        result.append('r')
                        if color[5][0][1]==color[5][1][1]:
                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[5][0][1]==color[2][1][1]:
                            d()
                            result.append('d')
                            R()
                            result.append('R')
                            R()
                            result.append('R')
                            
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             
                        elif color[5][0][1]==color[0][1][1]:
                            D()
                            result.append('D')
                            L()
                            result.append('L')
                            L()
                            result.append('L')
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                        elif color[5][0][1]==color[3][1][1]:
                            D()
                            result.append('D')
                            D()
                            result.append('D')
                            F()
                            result.append('F')
                            F()
                            result.append('F')
                            
                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1
                             
                    elif [x,y,z]==[5,1,0] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        l()
                        result.append('l')
                        d()
                        result.append('d')
                        L()
                        result.append('L')
                        if color[5][0][1]==color[5][1][1]:
                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[5][0][1]==color[2][1][1]:
                            d()
                            result.append('d')
                            R()
                            result.append('R')
                            R()
                            result.append('R')
                            
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             
                        elif color[5][0][1]==color[0][1][1]:
                            D()
                            result.append('D')
                            L()
                            result.append('L')
                            L()
                            result.append('L')
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                        elif color[5][0][1]==color[3][1][1]:
                            D()
                            result.append('D')
                            D()
                            result.append('D')
                            F()
                            result.append('F')
                            F()
                            result.append('F')
                            
                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1
                             
                    elif [x,y,z]==[5,0,1] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        B()
                        result.append('B')
                        R()
                        result.append('R')
                        D()
                        result.append('D')
                        r()
                        result.append('r')
                        d()
                        result.append('d')
                        b()
                        result.append('b')
                        if color[2][1][2]==color[2][1][1]:
                            R()
                            result.append('R')
                            R()
                            result.append('R')
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             
                        elif color[2][1][2]==color[5][1][1]:
                            D()
                            result.append('D')
                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[2][1][2]==color[3][1][1]:
                            d()
                            result.append('d')
                            F()
                            result.append('F')
                            F()
                            result.append('F')
                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[2][1][2]==color[0][1][1]:
                            D()
                            result.append('D')
                            D()
                            result.append('D')
                            L()
                            result.append('L')
                            L()
                            result.append('L')
                            
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                    elif [x,y,z]==[0,1,2] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        L()
                        result.append('L')
                        f()
                        result.append('f')
                        d()
                        result.append('d')
                        F()
                        result.append('F')
                        D()
                        result.append('D')
                        l()
                        result.append('l')
                        
                        if color[3][2][1]==color[3][1][1]:
                            
                            F()
                            result.append('F')
                            F()
                            result.append('F')

                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[3][2][1]==color[2][1][1]:
                            
                            D()
                            result.append('D')
                            R()
                            result.append('R')
                            R()
                            result.append('R')
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             
                        elif color[3][2][1]==color[0][1][1]:
                            d()
                            result.append('d')
                            L()
                            result.append('L')
                            L()
                            result.append('L')
                            
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                        elif color[3][2][1]==color[5][1][1]:
                            D()
                            result.append('D')
                            D()
                            result.append('D')

                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             
                    elif [x,y,z]==[0,0,1] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        B()
                        result.append('B')
                        D()
                        result.append('D')
                        b()
                        result.append('b')
                        
                        if color[0][1][0]==color[0][1][1]:
                            L()
                            result.append('L')
                            L()
                            result.append('L')
                            
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                        elif color[0][1][0]==color[3][1][1]:
                            D()
                            result.append('D')
                            F()
                            result.append('F')
                            F()
                            result.append('F')
                            
                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[0][1][0]==color[5][1][1]:
                            d()
                            result.append('d')
                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[0][1][0]==color[2][1][1]:
                            D()
                            result.append('D')
                            D()
                            result.append('D')
                            R()
                            result.append('R')
                            R()
                            result.append('R')

                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             
                    elif [x,y,z]==[0,2,1] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        f()
                        result.append('f')
                        d()
                        result.append('d')
                        F()
                        result.append('F')
                        if color[0][1][0]==color[0][1][1]:
                            L()
                            result.append('L')
                            L()
                            result.append('L')
                            
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                        elif color[0][1][0]==color[3][1][1]:
                            D()
                            result.append('D')
                            F()
                            result.append('F')
                            F()
                            result.append('F')
                            
                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[0][1][0]==color[5][1][1]:
                            d()
                            result.append('d')
                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[0][1][0]==color[2][1][1]:
                            D()
                            result.append('D')
                            D()
                            result.append('D')
                            R()
                            result.append('R')
                            R()
                            result.append('R')

                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             
                    elif [x,y,z]==[0,1,0] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        l()
                        result.append('l')
                        f()
                        result.append('f')
                        d()
                        result.append('d')
                        F()
                        result.append('F')
                        D()
                        result.append('D')
                        L()
                        result.append('L')
                        if color[3][2][1]==color[3][1][1]:
                            
                            F()
                            result.append('F')
                            F()
                            result.append('F')

                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[3][2][1]==color[2][1][1]:
                            
                            D()
                            result.append('D')
                            R()
                            result.append('R')
                            R()
                            result.append('R')
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             
                        elif color[3][2][1]==color[0][1][1]:
                            d()
                            result.append('d')
                            L()
                            result.append('L')
                            L()
                            result.append('L')
                            
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                        elif color[3][2][1]==color[5][1][1]:
                            D()
                            result.append('D')
                            D()
                            result.append('D')

                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             
                    elif [x,y,z]==[2,1,0] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        r()
                        result.append('r')
                        F()
                        result.append('F')
                        D()
                        result.append('D')
                        f()
                        result.append('f')
                        d()
                        result.append('d')
                        R()
                        result.append('R')
                        
                        if color[3][2][1]==color[3][1][1]:
                            
                            F()
                            result.append('F')
                            F()
                            result.append('F')

                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[3][2][1]==color[2][1][1]:
                            
                            D()
                            result.append('D')
                            R()
                            result.append('R')
                            R()
                            result.append('R')
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             
                        elif color[3][2][1]==color[0][1][1]:
                            d()
                            result.append('d')
                            L()
                            result.append('L')
                            L()
                            result.append('L')
                            
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                        elif color[3][2][1]==color[5][1][1]:
                            D()
                            result.append('D')
                            D()
                            result.append('D')

                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             
                    elif [x,y,z]==[2,2,1] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        F()
                        result.append('F')
                        d()
                        result.append('d')
                        f()
                        result.append('f')
                        if color[0][1][0]==color[0][1][1]:
                            L()
                            result.append('L')
                            L()
                            result.append('L')
                            
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                        elif color[0][1][0]==color[3][1][1]:
                            D()
                            result.append('D')
                            F()
                            result.append('F')
                            F()
                            result.append('F')
                            
                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[0][1][0]==color[5][1][1]:
                            d()
                            result.append('d')
                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[0][1][0]==color[2][1][1]:
                            D()
                            result.append('D')
                            D()
                            result.append('D')
                            R()
                            result.append('R')
                            R()
                            result.append('R')

                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             
                    elif [x,y,z]==[2,0,1] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        b()
                        result.append('b')
                        D()
                        result.append('D')
                        B()
                        result.append('B')
                        if color[0][1][0]==color[0][1][1]:
                            L()
                            result.append('L')
                            L()
                            result.append('L')
                            
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                        elif color[0][1][0]==color[3][1][1]:
                            D()
                            result.append('D')
                            F()
                            result.append('F')
                            F()
                            result.append('F')
                            
                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[0][1][0]==color[5][1][1]:
                            d()
                            result.append('d')
                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[0][1][0]==color[2][1][1]:
                            D()
                            result.append('D')
                            D()
                            result.append('D')
                            R()
                            result.append('R')
                            R()
                            result.append('R')

                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             

                    elif [x,y,z]==[2,1,2] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        R()
                        result.append('R')
                        F()
                        result.append('F')
                        D()
                        result.append('D')
                        f()
                        result.append('f')
                        d()
                        result.append('d')
                        r()
                        result.append('r')

                        if color[3][2][1]==color[3][1][1]:
                            
                            F()
                            result.append('F')
                            F()
                            result.append('F')

                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[3][2][1]==color[2][1][1]:
                            
                            D()
                            result.append('D')
                            R()
                            result.append('R')
                            R()
                            result.append('R')
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             
                        elif color[3][2][1]==color[0][1][1]:
                            d()
                            result.append('d')
                            L()
                            result.append('L')
                            L()
                            result.append('L')
                            
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                        elif color[3][2][1]==color[5][1][1]:
                            D()
                            result.append('D')
                            D()
                            result.append('D')

                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             
                    elif [x,y,z]==[3,0,1] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        F()
                        result.append('F')
                        r()
                        result.append('r')
                        d()
                        result.append('d')
                        R()
                        result.append('R')
                        D()
                        result.append('D')
                        f()
                        result.append('f')
                        if color[2][1][2]==color[2][1][1]:
                            R()
                            result.append('R')
                            R()
                            result.append('R')
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             
                        elif color[2][1][2]==color[5][1][1]:
                            D()
                            result.append('D')
                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[2][1][2]==color[3][1][1]:
                            d()
                            result.append('d')
                            F()
                            result.append('F')
                            F()
                            result.append('F')
                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[2][1][2]==color[0][1][1]:
                            D()
                            result.append('D')
                            D()
                            result.append('D')
                            L()
                            result.append('L')
                            L()
                            result.append('L')
                            
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                    elif [x,y,z]==[3,1,0] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        L()
                        result.append('L')
                        D()
                        result.append('D')
                        l()
                        result.append('l')
                        if color[3][2][1]==color[3][1][1]:
                            
                            F()
                            result.append('F')
                            F()
                            result.append('F')

                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[3][2][1]==color[2][1][1]:
                            
                            D()
                            result.append('D')
                            R()
                            result.append('R')
                            R()
                            result.append('R')
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             
                        elif color[3][2][1]==color[0][1][1]:
                            d()
                            result.append('d')
                            L()
                            result.append('L')
                            L()
                            result.append('L')
                            
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                        elif color[3][2][1]==color[5][1][1]:
                            D()
                            result.append('D')
                            D()
                            result.append('D')
                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             
                    elif [x,y,z]==[3,1,2] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        r()
                        result.append('r')
                        d()
                        result.append('d')
                        R()
                        result.append('R')
                        
                        if color[3][2][1]==color[3][1][1]:
                            
                            F()
                            result.append('F')
                            F()
                            result.append('F')

                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[3][2][1]==color[2][1][1]:
                            
                            D()
                            result.append('D')
                            R()
                            result.append('R')
                            R()
                            result.append('R')
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             
                        elif color[3][2][1]==color[0][1][1]:
                            d()
                            result.append('d')
                            L()
                            result.append('L')
                            L()
                            result.append('L')
                            
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                        elif color[3][2][1]==color[5][1][1]:
                            D()
                            result.append('D')
                            D()
                            result.append('D')

                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             
                    elif [x,y,z]==[3,2,1] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        F()
                        result.append('F')
                        L()
                        result.append('L')
                        D()
                        result.append('D')
                        l()
                        result.append('l')
                        d()
                        result.append('d')
                        f()
                        result.append('f')
                        if color[0][1][0]==color[0][1][1]:
                            L()
                            result.append('L')
                            L()
                            result.append('L')
                            
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                        elif color[0][1][0]==color[3][1][1]:
                            D()
                            result.append('D')
                            F()
                            result.append('F')
                            F()
                            result.append('F')
                            
                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[0][1][0]==color[5][1][1]:
                            d()
                            result.append('d')
                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             

                        elif color[0][1][0]==color[2][1][1]:
                            D()
                            result.append('D')
                            D()
                            result.append('D')
                            R()
                            result.append('R')
                            R()
                            result.append('R')

                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             
                    elif [x,y,z]==[4,0,1] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        if color[3][2][1]==color[3][1][1]:
                            
                            F()
                            result.append('F')
                            F()
                            result.append('F')

                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[3][2][1]==color[2][1][1]:
                            
                            D()
                            result.append('D')
                            R()
                            result.append('R')
                            R()
                            result.append('R')
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             
                        elif color[3][2][1]==color[0][1][1]:
                            d()
                            result.append('d')
                            L()
                            result.append('L')
                            L()
                            result.append('L')
                            
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                        elif color[3][2][1]==color[5][1][1]:
                            D()
                            result.append('D')
                            D()
                            result.append('D')

                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             
                    elif [x,y,z]==[4,1,0] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        if color[0][1][0]==color[0][1][1]:
                            L()
                            result.append('L')
                            L()
                            result.append('L')
                            
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                        elif color[0][1][0]==color[3][1][1]:
                            D()
                            result.append('D')
                            F()
                            result.append('F')
                            F()
                            result.append('F')
                            
                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[0][1][0]==color[5][1][1]:
                            d()
                            result.append('d')
                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             

                        elif color[0][1][0]==color[2][1][1]:
                            D()
                            result.append('D')
                            D()
                            result.append('D')
                            R()
                            result.append('R')
                            R()
                            result.append('R')

                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             
                    elif [x,y,z]==[4,1,2] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        if color[2][1][2]==color[2][1][1]:
                            R()
                            result.append('R')
                            R()
                            result.append('R')
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             
                        elif color[2][1][2]==color[5][1][1]:
                            D()
                            result.append('D')
                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[2][1][2]==color[3][1][1]:
                            d()
                            result.append('d')
                            F()
                            result.append('F')
                            F()
                            result.append('F')
                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[2][1][2]==color[0][1][1]:
                            
                            D()
                            result.append('D')
                            D()
                            result.append('D')
                            L()
                            result.append('L')
                            L()
                            result.append('L')
                            
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                    elif [x,y,z]==[4,2,1] and color[x][y][z]==color[1][1][1] and w<4 and not [x,y,z]==booked[0] and not [x,y,z]==booked[1] and not [x,y,z]==booked[2]:
                        if color[5][0][1]==color[5][1][1]:
                            B()
                            result.append('B')
                            B()
                            result.append('B')
                            booked[w][0]=1
                            booked[w][1]=0
                            booked[w][2]=1
                            w=w+1
                             
                        elif color[5][0][1]==color[2][1][1]:
                            d()
                            result.append('d')
                            R()
                            result.append('R')
                            R()
                            result.append('R')
                            
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=2
                            w=w+1
                             
                        elif color[5][0][1]==color[0][1][1]:
                            D()
                            result.append('D')
                            L()
                            result.append('L')
                            L()
                            result.append('L')
                            booked[w][0]=1
                            booked[w][1]=1
                            booked[w][2]=0
                            w=w+1
                             
                        elif color[5][0][1]==color[3][1][1]:
                            D()
                            result.append('D')
                            D()
                            result.append('D')
                            F()
                            result.append('F')
                            F()
                            result.append('F')
                            
                            booked[w][0]=1
                            booked[w][1]=2
                            booked[w][2]=1
                            w=w+1

result.append('+')

# 2nd layer 4 edges

if not (color[0][0][1]==color[0][1][1] and color[5][1][0]==color[5][1][1]):
    if color[0][0][1]==color[5][1][1] and color[5][1][0]==color[0][1][1]:
        B()
        result.append('B')
        D()
        result.append('D')
        b()
        result.append('b')
        d()
        result.append('d')
        l()
        result.append('l')
        D()
        result.append('D')
        L()
        result.append('L')
    elif color[0][2][1]==color[0][1][1] and color[3][1][0]==color[5][1][1]:
        f()
        result.append('f')
        B()
        result.append('B')
        D()
        result.append('D')
        D()
        result.append('D')
        b()
        result.append('b')
        F()
        result.append('F')
    elif color[0][2][1]==color[5][1][1] and color[3][1][0]==color[0][1][1]:
        L()
        result.append('L')
        d()
        result.append('d')
        l()
        result.append('l')
        D()
        result.append('D')
        B()
        result.append('B')
        d()
        result.append('d')
        b()
        result.append('b')
    elif color[0][1][0]==color[0][1][1] and color[4][1][0]==color[5][1][1]:
        d()
        result.append('d')
        l()
        result.append('l')
        D()
        result.append('D')
        L()
        result.append('L')
    elif color[0][1][0]==color[5][1][1] and color[4][1][0]==color[0][1][1]:
        B()
        result.append('B')
        d()
        result.append('d')
        b()
        result.append('b')
    elif color[2][0][1]==color[0][1][1] and color[5][1][2]==color[5][1][1]:
        R()
        result.append('R')
        l()
        result.append('l')
        D()
        result.append('D')
        D()
        result.append('D')
        L()
        result.append('L')
        r()
        result.append('r')
    elif color[2][0][1]==color[5][1][1] and color[5][1][2]==color[0][1][1]:
        b()
        result.append('b')
        D()
        result.append('D')
        B()
        result.append('B')
        d()
        result.append('d')
        l()
        result.append('l')
        D()
        result.append('D')
        L()
        result.append('L')
    elif color[2][2][1]==color[0][1][1] and color[3][1][2]==color[5][1][1]:
        F()
        result.append('F')
        B()
        result.append('B')
        D()
        result.append('D')
        D()
        result.append('D')
        b()
        result.append('b')
        f()
        result.append('f')
    elif color[2][2][1]==color[5][1][1] and color[3][1][2]==color[0][1][1]:
        r()
        result.append('r')
        B()
        result.append('B')
        D()
        result.append('D')
        b()
        result.append('b')
        R()
        result.append('R')
    elif color[2][1][2]==color[0][1][1] and color[4][1][2]==color[5][1][1]:
        l()
        result.append('l')
        D()
        result.append('D')
        D()
        result.append('D')
        L()
        result.append('L')
    elif color[2][1][2]==color[5][1][1] and color[4][1][2]==color[0][1][1]:
        B()
        result.append('B')
        D()
        result.append('D')
        b()
        result.append('b')
    elif color[3][2][1]==color[0][1][1] and color[4][0][1]==color[5][1][1]:
        l()
        result.append('l')
        d()
        result.append('d')
        L()
        result.append('L')
    elif color[3][2][1]==color[5][1][1] and color[4][0][1]==color[0][1][1]:
        B()
        result.append('B')
        D()
        result.append('D')
        D()
        result.append('D')
        b()
        result.append('b')
    elif color[5][0][1]==color[0][1][1] and color[4][2][1]==color[5][1][1]:
        l()
        result.append('l')
        D()
        result.append('D')
        L()
        result.append('L')
    elif color[5][0][1]==color[5][1][1] and color[4][2][1]==color[0][1][1]:
        D()
        result.append('D')
        B()
        result.append('B')
        d()
        result.append('d')
        b()
        result.append('b')
        
result.append('+')

if not (color[0][2][1]==color[0][1][1] and color[3][1][0]==color[3][1][1]):
    if color[0][2][1]==color[3][1][1] and color[3][1][0]==color[0][1][1]:
        f()
        result.append('f')
        d()
        result.append('d')
        F()
        result.append('F')
        D()
        result.append('D')
        L()
        result.append('L')
        d()
        result.append('d')
        l()
        result.append('l')
    elif  color[0][0][1]==color[0][1][1] and color[5][1][0]==color[3][1][1]:
        B()
        result.append('B')
        f()
        result.append('f')
        D()
        result.append('D')
        D()
        result.append('D')
        F()
        result.append('F')
        b()
        result.append('b')
    elif color[0][0][1]==color[3][1][1] and color[5][1][0]==color[0][1][1]:
        l()
        result.append('l')
        D()
        result.append('D')
        L()
        result.append('L')
        d()
        result.append('d')
        f()
        result.append('f')
        D()
        result.append('D')
        F()
        result.append('F')
    elif color[0][1][0]==color[0][1][1] and color[4][1][0]==color[3][1][1]:
        D()
        result.append('D')
        L()
        result.append('L')
        d()
        result.append('d')
        l()
        result.append('l')
    elif color[0][1][0]==color[3][1][1] and color[4][1][0]==color[0][1][1]:
        f()
        result.append('f')
        D()
        result.append('D')
        F()
        result.append('F')
    elif color[2][0][1]==color[0][1][1] and color[5][1][2]==color[3][1][1]:
        b()
        result.append('b')
        f()
        result.append('f')
        D()
        result.append('D')
        D()
        result.append('D')
        F()
        result.append('F')
        B()
        result.append('B')
    elif color[2][0][1]==color[3][1][1] and color[5][1][2]==color[0][1][1]:
        b()
        result.append('b')
        D()
        result.append('D')
        D()
        result.append('D')
        B()
        result.append('B')
        L()
        result.append('L')
        d()
        result.append('d')
        l()
        result.append('l')
    elif color[2][2][1]==color[0][1][1] and color[3][1][2]==color[3][1][1]:
        r()
        result.append('r')
        L()
        result.append('L')
        D()
        result.append('D')
        D()
        result.append('D')
        l()
        result.append('l')
        R()
        result.append('R')
    elif color[2][2][1]==color[3][1][1] and color[3][1][2]==color[0][1][1]:
        F()
        result.append('F')
        d()
        result.append('d')
        f()
        result.append('f')
        D()
        result.append('D')
        L()
        result.append('L')
        d()
        result.append('d')
        l()
        result.append('l')
    elif color[2][1][2]==color[0][1][1] and color[4][1][2]==color[3][1][1]:
        L()
        result.append('L')
        D()
        result.append('D')
        D()
        result.append('D')
        l()
        result.append('l')
    elif color[2][1][2]==color[3][1][1] and color[4][1][2]==color[0][1][1]:
        f()
        result.append('f')
        d()
        result.append('d')
        F()
        result.append('F')
    elif color[3][2][1]==color[0][1][1] and color[4][0][1]==color[3][1][1]:
        L()
        result.append('L')
        d()
        result.append('d')
        l()
        result.append('l')
    elif color[3][2][1]==color[3][1][1] and color[4][0][1]==color[0][1][1]:
        d()
        result.append('d')
        f()
        result.append('f')
        D()
        result.append('D')
        F()
        result.append('F')
    elif color[5][0][1]==color[0][1][1] and color[4][2][1]==color[3][1][1]:
        L()
        result.append('L')
        D()
        result.append('D')
        l()
        result.append('l')
    elif color[5][0][1]==color[3][1][1] and color[4][2][1]==color[0][1][1]:
        f()
        result.append('f')
        D()
        result.append('D')
        D()
        result.append('D')
        F()
        result.append('F')

result.append('+')

if not (color[2][0][1]==color[2][1][1] and color[5][1][2]==color[5][1][1]):
    if color[2][0][1]==color[5][1][1] and color[5][1][2]==color[2][1][1]:
        R()
        result.append('R')
        D()
        result.append('D')
        r()
        result.append('r')
        d()
        result.append('d')
        b()
        result.append('b')
        D()
        result.append('D')
        B()
        result.append('B')
    elif color[2][2][1]==color[2][1][1] and color[3][1][2]==color[5][1][1]:
        F()
        result.append('F')
        b()
        result.append('b')
        D()
        result.append('D')
        D()
        result.append('D')
        B()
        result.append('B')
        f()
        result.append('f')
    elif color[2][2][1]==color[5][1][1] and color[3][1][2]==color[2][1][1]:
        r()
        result.append('r')
        D()
        result.append('D')
        R()
        result.append('R')
        d()
        result.append('d')
        b()
        result.append('b')
        D()
        result.append('D')
        B()
        result.append('B')
    elif color[2][1][2]==color[2][1][1] and color[4][1][2]==color[5][1][1]:
        D()
        result.append('D')
        R()
        result.append('R')
        d()
        result.append('d')
        r()
        result.append('r')
    elif color[2][1][2]==color[5][1][1] and color[4][1][2]==color[2][1][1]:
        b()
        result.append('b')
        D()
        result.append('D')
        B()
        result.append('B')
    elif color[0][0][1]==color[2][1][1] and color[5][1][0]==color[5][1][1]:
        l()
        result.append('l')
        R()
        result.append('R')
        D()
        result.append('D')
        D()
        result.append('D')
        r()
        result.append('r')
        L()
        result.append('L')
    elif color[0][0][1]==color[5][1][1] and color[5][1][0]==color[2][1][1]:
        B()
        result.append('B')
        d()
        result.append('d')
        b()
        result.append('b')
        D()
        result.append('D')
        R()
        result.append('R')
        d()
        result.append('d')
        r()
        result.append('r')
    elif color[0][2][1]==color[2][1][1] and color[3][1][0]==color[5][1][1]:
        f()
        result.append('f')
        b()
        result.append('b')
        D()
        result.append('D')
        D()
        result.append('D')
        B()
        result.append('B')
        F()
        result.append('F')
    elif color[0][2][1]==color[5][1][1] and color[3][1][0]==color[2][1][1]:
        L()
        result.append('L')
        D()
        result.append('D')
        D()
        result.append('D')
        l()
        result.append('l')
        b()
        result.append('b')
        D()
        result.append('D')
        B()
        result.append('B')
    elif color[0][1][0]==color[2][1][1] and color[4][1][0]==color[5][1][1]:
        R()
        result.append('R')
        D()
        result.append('D')
        D()
        result.append('D')
        r()
        result.append('r')
    elif color[0][1][0]==color[5][1][1] and color[4][1][0]==color[2][1][1]:
        b()
        result.append('b')
        d()
        result.append('d')
        B()
        result.append('B')
    elif color[3][2][1]==color[2][1][1] and color[4][0][1]==color[5][1][1]:
        R()
        result.append('R')
        D()
        result.append('D')
        r()
        result.append('r')
    elif color[3][2][1]==color[5][1][1] and color[4][0][1]==color[2][1][1]:
        b()
        result.append('b')
        D()
        result.append('D')
        D()
        result.append('D')
        B()
        result.append('B')
    elif color[5][0][1]==color[2][1][1] and color[4][2][1]==color[5][1][1]:
        R()
        result.append('R')
        d()
        result.append('d')
        r()
        result.append('r')
    elif color[5][0][1]==color[5][1][1] and color[4][2][1]==color[2][1][1]:
        d()
        result.append('d')
        b()
        result.append('b')
        D()
        result.append('D')
        B()
        result.append('B')

result.append('+')

if not (color[2][2][1]==color[2][1][1] and color[3][1][2]==color[3][1][1]):
    if color[2][2][1]==color[3][1][1] and color[3][1][2]==color[2][1][1]:
        F()
        result.append('F')
        D()
        result.append('D')
        f()
        result.append('f')
        d()
        result.append('d')
        r()
        result.append('r')
        D()
        result.append('D')
        R()
        result.append('R')
    elif color[2][0][1]==color[2][1][1] and color[5][1][2]==color[3][1][1]:
        b()
        result.append('b')
        F()
        result.append('F')
        D()
        result.append('D')
        D()
        result.append('D')
        f()
        result.append('f')
        B()
        result.append('B')
    elif color[2][0][1]==color[3][1][1] and color[5][1][2]==color[2][1][1]:
        R()
        result.append('R')
        d()
        result.append('d')
        r()
        result.append('r')
        D()
        result.append('D')
        F()
        result.append('F')
        d()
        result.append('d')
        f()
        result.append('f')
    elif color[2][1][2]==color[2][1][1] and color[4][1][2]==color[3][1][1]:
        d()
        result.append('d')
        r()
        result.append('r')
        D()
        result.append('D')
        R()
        result.append('R')
    elif color[2][1][2]==color[3][1][1] and color[4][1][2]==color[2][1][1]:
        F()
        result.append('F')
        d()
        result.append('d')
        f()
        result.append('f')
    elif color[0][0][1]==color[2][1][1] and color[5][1][0]==color[3][1][1]:
        l()
        result.append('l')
        r()
        result.append('r')
        D()
        result.append('D')
        D()
        result.append('D')
        R()
        result.append('R')
        L()
        result.append('L')
    elif color[0][0][1]==color[3][1][1] and color[5][1][0]==color[2][1][1]:
        l()
        result.append('l')
        D()
        result.append('D')
        L()
        result.append('L')
        d()
        result.append('d')
        F()
        result.append('F')
        d()
        result.append('d')
        f()
        result.append('f')
    elif color[0][2][1]==color[2][1][1] and color[3][1][0]==color[3][1][1]:
        L()
        result.append('L')
        R()
        result.append('R')
        D()
        result.append('D')
        D()
        result.append('D')
        r()
        result.append('r')
        l()
        result.append('l')
    elif color[0][2][1]==color[3][1][1] and color[3][1][0]==color[2][1][1]:
        f()
        result.append('f')
        D()
        result.append('D')
        F()
        result.append('F')
        d()
        result.append('d')
        r()
        result.append('r')
        D()
        result.append('D')
        R()
        result.append('R')
    elif color[0][1][0]==color[2][1][1] and color[4][1][0]==color[3][1][1]:
        r()
        result.append('r')
        D()
        result.append('D')
        D()
        result.append('D')
        R()
        result.append('R')
    elif color[0][1][0]==color[3][1][1] and color[4][1][0]==color[2][1][1]:
        F()
        result.append('F')
        D()
        result.append('D')
        f()
        result.append('f')
    elif color[3][2][1]==color[2][1][1] and color[4][0][1]==color[3][1][1]:
        r()
        result.append('r')
        D()
        result.append('D')
        R()
        result.append('R')
    elif color[3][2][1]==color[3][1][1] and color[4][0][1]==color[2][1][1]:
        D()
        result.append('D')
        F()
        result.append('F')
        d()
        result.append('d')
        f()
        result.append('f')
    elif color[5][0][1]==color[2][1][1] and color[4][2][1]==color[3][1][1]:
        r()
        result.append('r')
        d()
        result.append('d')
        R()
        result.append('R')
    elif color[5][0][1]==color[3][1][1] and color[4][2][1]==color[2][1][1]:
        F()
        result.append('F')
        D()
        result.append('D')
        D()
        result.append('D')
        f()
        result.append('f')

result.append('+')

# Top 4 corners

if not color[0][0][2]==color[0][1][1] or not color[1][0][0]==color[1][1][1] or not color[5][2][0]==color[5][1][1] :
    if (color[0][0][2]==color[0][1][1] or color[0][0][2]==color[1][1][1] or color[0][0][2]==color[5][1][1]) and (color[1][0][0]==color[0][1][1] or color[1][0][0]==color[1][1][1] or color[1][0][0]==color[5][1][1]) and (color[5][2][0]==color[0][1][1] or color[5][2][0]==color[1][1][1] or color[5][2][0]==color[5][1][1]):
        h=0
        for h in range(3):
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
        if color[4][2][0]==color[1][1][1]:
            h=0
            for h in range(3):
                l()
                result.append('l')
                d()
                result.append('d')
                L()
                result.append('L')
                D()
                result.append('D')
        elif color[0][0][0]==color[1][1][1]:
            d()
            result.append('d')
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
        elif color[5][0][0]==color[1][1][1]:
            D()
            result.append('D')
            B()
            result.append('B')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')
    elif (color[0][2][2]==color[0][1][1] or color[0][2][2]==color[1][1][1] or color[0][2][2]==color[5][1][1]) and (color[1][2][0]==color[0][1][1] or color[1][2][0]==color[1][1][1] or color[1][2][0]==color[5][1][1]) and (color[3][0][0]==color[0][1][1] or color[3][0][0]==color[1][1][1] or color[3][0][0]==color[5][1][1]):
        h=0
        for h in range(3):
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
        d()
        result.append('d')
        if color[4][2][0]==color[1][1][1]:
            h=0
            for h in range(3):
                l()
                result.append('l')
                d()
                result.append('d')
                L()
                result.append('L')
                D()
                result.append('D')
        elif color[0][0][0]==color[1][1][1]:
            d()
            result.append('d')
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
        elif color[5][0][0]==color[1][1][1]:
            D()
            result.append('D')
            B()
            result.append('B')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')
    elif (color[2][0][0]==color[0][1][1] or color[2][0][0]==color[1][1][1] or color[2][0][0]==color[5][1][1]) and (color[1][0][2]==color[0][1][1] or color[1][0][2]==color[1][1][1] or color[1][0][2]==color[5][1][1]) and (color[5][2][2]==color[0][1][1] or color[5][2][2]==color[1][1][1] or color[5][2][2]==color[5][1][1]):
        h=0
        for h in range (3):
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
        D()
        result.append('D')
        if color[4][2][0]==color[1][1][1]:
            h=0
            for h in range(3):
                l()
                result.append('l')
                d()
                result.append('d')
                L()
                result.append('L')
                D()
                result.append('D')
        elif color[0][0][0]==color[1][1][1]:
            d()
            result.append('d')
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
        elif color[5][0][0]==color[1][1][1]:
            D()
            result.append('D')
            B()
            result.append('B')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')
    elif (color[2][2][0]==color[0][1][1] or color[2][2][0]==color[1][1][1] or color[2][2][0]==color[5][1][1]) and (color[1][2][2]==color[0][1][1] or color[1][2][2]==color[1][1][1] or color[1][2][2]==color[5][1][1]) and (color[3][0][2]==color[0][1][1] or color[3][0][2]==color[1][1][1] or color[3][0][2]==color[5][1][1]):
        h=0
        for h in range (3):
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
        D()
        result.append('D')
        D()
        result.append('D')
        if color[4][2][0]==color[1][1][1]:
            h=0
            for h in range(3):
                l()
                result.append('l')
                d()
                result.append('d')
                L()
                result.append('L')
                D()
                result.append('D')
        elif color[0][0][0]==color[1][1][1]:
            d()
            result.append('d')
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
        elif color[5][0][0]==color[1][1][1]:
            D()
            result.append('D')
            B()
            result.append('B')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')
    elif (color[0][0][0]==color[0][1][1] or color[0][0][0]==color[1][1][1] or color[0][0][0]==color[5][1][1]) and (color[5][0][0]==color[0][1][1] or color[5][0][0]==color[1][1][1] or color[5][0][0]==color[5][1][1]) and (color[4][2][0]==color[0][1][1] or color[4][2][0]==color[1][1][1] or color[4][2][0]==color[5][1][1]):
        if color[4][2][0]==color[1][1][1]:
            h=0
            for h in range(3):
                l()
                result.append('l')
                d()
                result.append('d')
                L()
                result.append('L')
                D()
                result.append('D')
        elif color[0][0][0]==color[1][1][1]:
            d()
            result.append('d')
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
        elif color[5][0][0]==color[1][1][1]:
            D()
            result.append('D')
            B()
            result.append('B')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')
    elif (color[0][2][0]==color[0][1][1] or color[0][2][0]==color[1][1][1] or color[0][2][0]==color[5][1][1]) and (color[3][2][0]==color[0][1][1] or color[3][2][0]==color[1][1][1] or color[3][2][0]==color[5][1][1]) and (color[4][0][0]==color[0][1][1] or color[4][0][0]==color[1][1][1] or color[4][0][0]==color[5][1][1]):
        d()
        result.append('d')
        if color[4][2][0]==color[1][1][1]:
            h=0
            for h in range(3):
                l()
                result.append('l')
                d()
                result.append('d')
                L()
                result.append('L')
                D()
                result.append('D')
        elif color[0][0][0]==color[1][1][1]:
            d()
            result.append('d')
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
        elif color[5][0][0]==color[1][1][1]:
            D()
            result.append('D')
            B()
            result.append('B')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')
    elif (color[2][0][2]==color[0][1][1] or color[2][0][2]==color[1][1][1] or color[2][0][2]==color[5][1][1]) and (color[5][0][2]==color[0][1][1] or color[5][0][2]==color[1][1][1] or color[5][0][2]==color[5][1][1]) and (color[4][2][2]==color[0][1][1] or color[4][2][2]==color[1][1][1] or color[4][2][2]==color[5][1][1]):
        D()
        result.append('D')
        if color[4][2][0]==color[1][1][1]:
            h=0
            for h in range(3):
                l()
                result.append('l')
                d()
                result.append('d')
                L()
                result.append('L')
                D()
                result.append('D')
        elif color[0][0][0]==color[1][1][1]:
            d()
            result.append('d')
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
        elif color[5][0][0]==color[1][1][1]:
            D()
            result.append('D')
            B()
            result.append('B')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')
    elif (color[2][2][2]==color[0][1][1] or color[2][2][2]==color[1][1][1] or color[2][2][2]==color[5][1][1]) and (color[3][2][2]==color[0][1][1] or color[3][2][2]==color[1][1][1] or color[3][2][2]==color[5][1][1]) and (color[4][0][2]==color[0][1][1] or color[4][0][2]==color[1][1][1] or color[4][0][2]==color[5][1][1]):
        D()
        result.append('D')
        D()
        result.append('D')
        if color[4][2][0]==color[1][1][1]:
            h=0
            for h in range(3):
                l()
                result.append('l')
                d()
                result.append('d')
                L()
                result.append('L')
                D()
                result.append('D')
        elif color[0][0][0]==color[1][1][1]:
            d()
            result.append('d')
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
        elif color[5][0][0]==color[1][1][1]:
            D()
            result.append('D')
            B()
            result.append('B')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')

result.append('+')

if not color[0][2][2]==color[0][1][1] or not color[1][2][0]==color[1][1][1] or not color[3][0][0]==color[3][1][1] :
    if (color[0][2][2]==color[0][1][1] or color[0][2][2]==color[1][1][1] or color[0][2][2]==color[3][1][1]) and (color[1][2][0]==color[0][1][1] or color[1][2][0]==color[1][1][1] or color[1][2][0]==color[3][1][1]) and (color[3][0][0]==color[0][1][1] or color[3][0][0]==color[1][1][1] or color[3][0][0]==color[3][1][1]):
        h=0
        for h in range (3):
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
        if color[4][0][0]==color[1][1][1]:
            h=0
            for h in range (3):
                f()
                result.append('f')
                d()
                result.append('d')
                F()
                result.append('F')
                D()
                result.append('D')
        elif color[3][2][0]==color[1][1][1]:
            d()
            result.append('d')
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
        elif color[0][2][0]==color[1][1][1]:
            D()
            result.append('D')
            L()
            result.append('L')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')
    elif (color[0][0][2]==color[0][1][1] or color[0][0][2]==color[1][1][1] or color[0][0][2]==color[3][1][1]) and (color[1][0][0]==color[0][1][1] or color[1][0][0]==color[1][1][1] or color[1][0][0]==color[3][1][1]) and (color[5][2][0]==color[0][1][1] or color[5][2][0]==color[1][1][1] or color[5][2][0]==color==[3][1][1]):
        h=0
        for h in range(3):
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
        D()
        result.append('D')
        if color[4][0][0]==color[1][1][1]:
            h=0
            for h in range (3):
                f()
                result.append('f')
                d()
                result.append('d')
                F()
                result.append('F')
                D()
                result.append('D')
        elif color[3][2][0]==color[1][1][1]:
            d()
            result.append('d')
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
        elif color[0][2][0]==color[1][1][1]:
            D()
            result.append('D')
            L()
            result.append('L')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')
    elif (color[2][0][0]==color[0][1][1] or color[2][0][0]==color[1][1][1] or color[2][0][0]==color[3][1][1]) and (color[1][0][2]==color[0][1][1] or color[1][0][2]==color[1][1][1] or color[1][0][2]==color[3][1][1]) and (color[5][2][2]==color[0][1][1] or color[5][2][2]==color[1][1][1] or color[5][2][2]==color[3][1][1]):
        h=0
        for h in range (3):
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
        D()
        result.append('D')
        D()
        result.append('D')
        if color[4][0][0]==color[1][1][1]:
            h=0
            for h in range (3):
                f()
                result.append('f')
                d()
                result.append('d')
                F()
                result.append('F')
                D()
                result.append('D')
        elif color[3][2][0]==color[1][1][1]:
            d()
            result.append('d')
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
        elif color[0][2][0]==color[1][1][1]:
            D()
            result.append('D')
            L()
            result.append('L')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')
    elif (color[2][2][0]==color[0][1][1] or color[2][2][0]==color[1][1][1] or color[2][2][0]==color[3][1][1]) and (color[1][2][2]==color[0][1][1] or color[1][2][2]==color[1][1][1] or color[1][2][2]==color[3][1][1]) and (color[3][0][2]==color[0][1][1] or color[3][0][2]==color[1][1][1] or color[3][0][2]==color[3][1][1]):
        h=0
        for h in range (3):
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
        d()
        result.append('d')
        if color[4][0][0]==color[1][1][1]:
            h=0
            for h in range (3):
                f()
                result.append('f')
                d()
                result.append('d')
                F()
                result.append('F')
                D()
                result.append('D')
        elif color[3][2][0]==color[1][1][1]:
            d()
            result.append('d')
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
        elif color[0][2][0]==color[1][1][1]:
            D()
            result.append('D')
            L()
            result.append('L')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')
    elif (color[0][2][0]==color[0][1][1] or color[0][2][0]==color[1][1][1] or color[0][2][0]==color[3][1][1]) and (color[3][2][0]==color[0][1][1] or color[3][2][0]==color[1][1][1] or color[3][2][0]==color[3][1][1]) and (color[4][0][0]==color[0][1][1] or color[4][0][0]==color[1][1][1] or color[4][0][0]==color[3][1][1]):
        if color[4][0][0]==color[1][1][1]:
            h=0
            for h in range (3):
                f()
                result.append('f')
                d()
                result.append('d')
                F()
                result.append('F')
                D()
                result.append('D')
        elif color[3][2][0]==color[1][1][1]:
            d()
            result.append('d')
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
        elif color[0][2][0]==color[1][1][1]:
            D()
            result.append('D')
            L()
            result.append('L')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')
    elif (color[0][0][0]==color[0][1][1] or color[0][0][0]==color[1][1][1] or color[0][0][0]==color[3][1][1]) and (color[5][0][0]==color[0][1][1] or color[5][0][0]==color[1][1][1] or color[5][0][0]==color[3][1][1]) and (color[4][2][0]==color[0][1][1] or color[4][2][0]==color[1][1][1] or color[4][2][0]==color[3][1][1]):
        D()
        result.append('D')
        if color[4][0][0]==color[1][1][1]:
            h=0
            for h in range (3):
                f()
                result.append('f')
                d()
                result.append('d')
                F()
                result.append('F')
                D()
                result.append('D')
        elif color[3][2][0]==color[1][1][1]:
            d()
            result.append('d')
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
        elif color[0][2][0]==color[1][1][1]:
            D()
            result.append('D')
            L()
            result.append('L')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')
    elif (color[2][0][2]==color[0][1][1] or color[2][0][2]==color[1][1][1] or color[2][0][2]==color[3][1][1]) and (color[5][0][2]==color[0][1][1] or color[5][0][2]==color[1][1][1] or color[5][0][2]==color[3][1][1]) and (color[4][2][2]==color[0][1][1] or color[4][2][2]==color[1][1][1] or color[4][2][2]==color[3][1][1]):
        D()
        result.append('D')
        D()
        result.append('D')
        if color[4][0][0]==color[1][1][1]:
            h=0
            for h in range (3):
                f()
                result.append('f')
                d()
                result.append('d')
                F()
                result.append('F')
                D()
                result.append('D')
        elif color[3][2][0]==color[1][1][1]:
            d()
            result.append('d')
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
        elif color[0][2][0]==color[1][1][1]:
            D()
            result.append('D')
            L()
            result.append('L')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')
    elif (color[2][2][2]==color[0][1][1] or color[2][2][2]==color[1][1][1] or color[2][2][2]==color[3][1][1]) and (color[3][2][2]==color[0][1][1] or color[3][2][2]==color[1][1][1] or color[3][2][2]==color[3][1][1]) and (color[4][0][2]==color[0][1][1] or color[4][0][2]==color[1][1][1] or color[4][0][2]==color[3][1][1]):
        d()
        result.append('d')
        if color[4][0][0]==color[1][1][1]:
            h=0
            for h in range (3):
                f()
                result.append('f')
                d()
                result.append('d')
                F()
                result.append('F')
                D()
                result.append('D')
        elif color[3][2][0]==color[1][1][1]:
            d()
            result.append('d')
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
        elif color[0][2][0]==color[1][1][1]:
            D()
            result.append('D')
            L()
            result.append('L')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
            l()
            result.append('l')
            d()
            result.append('d')

result.append('+')

if not color[2][0][0]==color[2][1][1] or not color[1][0][2]==color[1][1][1] or not color[5][2][2]==color[5][1][1] :
    if (color[2][0][0]==color[2][1][1] or color[2][0][0]==color[1][1][1] or color[2][0][0]==color[5][1][1]) and (color[1][0][2]==color[2][1][1] or color[1][0][2]==color[1][1][1] or color[1][0][2]==color[5][1][1]) and (color[5][2][2]==color[2][1][1] or color[5][2][2]==color[1][1][1] or color[5][2][2]==color[5][1][1]):
        h=0
        for h in range (3):
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
        if color[4][2][2]==color[1][1][1]:
            h=0
            for h in range (3):
                b()
                result.append('b')
                d()
                result.append('d')
                B()
                result.append('B')
                D()
                result.append('D')
        elif color[5][0][2]==color[1][1][1]:
            d()
            result.append('d')
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
        elif color[2][0][2]==color[1][1][1]:
            D()
            result.append('D')
            R()
            result.append('R')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')
    elif (color[2][2][0]==color[2][1][1] or color[2][2][0]==color[1][1][1] or color[2][2][0]==color[5][1][1]) and (color[1][2][2]==color[2][1][1] or color[1][2][2]==color[1][1][1] or color[1][2][2]==color[5][1][1]) and (color[3][0][2]==color[2][1][1] or color[3][0][2]==color[1][1][1] or color[3][0][2]==color[5][1][1]):
        h=0
        for h in range (3):
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
        D()
        result.append('D')
        if color[4][2][2]==color[1][1][1]:
            h=0
            for h in range (3):
                b()
                result.append('b')
                d()
                result.append('d')
                B()
                result.append('B')
                D()
                result.append('D')
        elif color[5][0][2]==color[1][1][1]:
            d()
            result.append('d')
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
        elif color[2][0][2]==color[1][1][1]:
            D()
            result.append('D')
            R()
            result.append('R')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')
    elif (color[0][0][2]==color[2][1][1] or color[0][0][2]==color[1][1][1] or color[0][0][2]==color[5][1][1]) and (color[1][0][0]==color[2][1][1] or color[1][0][0]==color[1][1][1] or color[1][0][0]==color[5][1][1]) and (color[5][2][0]==color[2][1][1] or color[5][2][0]==color[1][1][1] or color[5][2][0]==color[5][1][1]):
        h=0
        for h in range(3):
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
        d()
        result.append('d')
        if color[4][2][2]==color[1][1][1]:
            h=0
            for h in range (3):
                b()
                result.append('b')
                d()
                result.append('d')
                B()
                result.append('B')
                D()
                result.append('D')
        elif color[5][0][2]==color[1][1][1]:
            d()
            result.append('d')
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
        elif color[2][0][2]==color[1][1][1]:
            D()
            result.append('D')
            R()
            result.append('R')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')
    elif (color[0][2][2]==color[2][1][1] or color[0][2][2]==color[1][1][1] or color[0][2][2]==color[5][1][1]) and (color[1][2][0]==color[2][1][1] or color[1][2][0]==color[1][1][1] or color[1][2][0]==color[5][1][1]) and (color[3][0][0]==color[2][1][1] or color[3][0][0]==color[1][1][1] or color[3][0][0]==color[5][1][1]):
        h=0
        for h in range(3):
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
        D()
        result.append('D')
        D()
        result.append('D')
        if color[4][2][2]==color[1][1][1]:
            h=0
            for h in range (3):
                b()
                result.append('b')
                d()
                result.append('d')
                B()
                result.append('B')
                D()
                result.append('D')
        elif color[5][0][2]==color[1][1][1]:
            d()
            result.append('d')
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
        elif color[2][0][2]==color[1][1][1]:
            D()
            result.append('D')
            R()
            result.append('R')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')
    elif (color[2][0][2]==color[2][1][1] or color[2][0][2]==color[1][1][1] or color[2][0][2]==color[5][1][1]) and (color[5][0][2]==color[2][1][1] or color[5][0][2]==color[1][1][1] or color[5][0][2]==color[5][1][1]) and (color[4][2][2]==color[2][1][1] or color[4][2][2]==color[1][1][1] or color[4][2][2]==color[5][1][1]):
        if color[4][2][2]==color[1][1][1]:
            h=0
            for h in range (3):
                b()
                result.append('b')
                d()
                result.append('d')
                B()
                result.append('B')
                D()
                result.append('D')
        elif color[5][0][2]==color[1][1][1]:
            d()
            result.append('d')
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
        elif color[2][0][2]==color[1][1][1]:
            D()
            result.append('D')
            R()
            result.append('R')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')
    elif (color[2][2][2]==color[2][1][1] or color[2][2][2]==color[1][1][1] or color[2][2][2]==color[5][1][1]) and (color[3][2][2]==color[2][1][1] or color[3][2][2]==color[1][1][1] or color[3][2][2]==color[5][1][1]) and (color[4][0][2]==color[2][1][1] or color[4][0][2]==color[1][1][1] or color[4][0][2]==color[5][1][1]):
        D()
        result.append('D')
        if color[4][2][2]==color[1][1][1]:
            h=0
            for h in range (3):
                b()
                result.append('b')
                d()
                result.append('d')
                B()
                result.append('B')
                D()
                result.append('D')
        elif color[5][0][2]==color[1][1][1]:
            d()
            result.append('d')
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
        elif color[2][0][2]==color[1][1][1]:
            D()
            result.append('D')
            R()
            result.append('R')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')
    elif (color[0][0][0]==color[2][1][1] or color[0][0][0]==color[1][1][1] or color[0][0][0]==color[5][1][1]) and (color[5][0][0]==color[2][1][1] or color[5][0][0]==color[1][1][1] or color[5][0][0]==color[5][1][1]) and (color[4][2][0]==color[2][1][1] or color[4][2][0]==color[1][1][1] or color[4][2][0]==color[5][1][1]):
        d()
        result.append('d')
        if color[4][2][2]==color[1][1][1]:
            h=0
            for h in range (3):
                b()
                result.append('b')
                d()
                result.append('d')
                B()
                result.append('B')
                D()
                result.append('D')
        elif color[5][0][2]==color[1][1][1]:
            d()
            result.append('d')
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
        elif color[2][0][2]==color[1][1][1]:
            D()
            result.append('D')
            R()
            result.append('R')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')
    elif (color[0][2][0]==color[2][1][1] or color[0][2][0]==color[1][1][1] or color[0][2][0]==color[5][1][1]) and (color[3][2][0]==color[2][1][1] or color[3][2][0]==color[1][1][1] or color[3][2][0]==color[5][1][1]) and (color[4][0][0]==color[2][1][1] or color[4][0][0]==color[1][1][1] or color[4][0][0]==color[5][1][1]):
        D()
        result.append('D')
        D()
        result.append('D')
        if color[4][2][2]==color[1][1][1]:
            h=0
            for h in range (3):
                b()
                result.append('b')
                d()
                result.append('d')
                B()
                result.append('B')
                D()
                result.append('D')
        elif color[5][0][2]==color[1][1][1]:
            d()
            result.append('d')
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
            D()
            result.append('D')
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
        elif color[2][0][2]==color[1][1][1]:
            D()
            result.append('D')
            R()
            result.append('R')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')

result.append('+')

if not color[2][2][0]==color[2][1][1] or not color[1][2][2]==color[1][1][1] or not color[3][0][2]==color[3][1][1] :
    if (color[2][2][0]==color[2][1][1] or color[2][2][0]==color[1][1][1] or color[2][2][0]==color[3][1][1]) and (color[1][2][2]==color[2][1][1] or color[1][2][2]==color[1][1][1] or color[1][2][2]==color[3][1][1]) and (color[3][0][2]==color[2][1][1] or color[3][0][2]==color[1][1][1] or color[3][0][2]==color[3][1][1]):
        h=0
        for h in range (3):
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
        if color[4][0][2]==color[1][1][1]:
            h=0
            for h in range (3):
                r()
                result.append('r')
                d()
                result.append('d')
                R()
                result.append('R')
                D()
                result.append('D')
        elif color[2][2][2]==color[1][1][1]:
            d()
            result.append('d')
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
        elif color[3][2][2]==color[1][1][1]:
            D()
            result.append('D')
            F()
            result.append('F')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')
    elif (color[2][0][0]==color[2][1][1] or color[2][0][0]==color[1][1][1] or color[2][0][0]==color[3][1][1]) and (color[1][0][2]==color[2][1][1] or color[1][0][2]==color[1][1][1] or color[1][0][2]==color[3][1][1]) and (color[5][2][2]==color[2][1][1] or color[5][2][2]==color[1][1][1] or color[5][2][2]==color[3][1][1]):
        h=0
        for h in range (3):
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            D()
            result.append('D')
        d()
        result.append('d')
        if color[4][0][2]==color[1][1][1]:
            h=0
            for h in range (3):
                r()
                result.append('r')
                d()
                result.append('d')
                R()
                result.append('R')
                D()
                result.append('D')
        elif color[2][2][2]==color[1][1][1]:
            d()
            result.append('d')
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
        elif color[3][2][2]==color[1][1][1]:
            D()
            result.append('D')
            F()
            result.append('F')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')
    elif (color[0][0][2]==color[2][1][1] or color[0][0][2]==color[1][1][1] or color[0][0][2]==color[3][1][1]) and (color[1][0][0]==color[2][1][1] or color[1][0][0]==color[1][1][1] or color[1][0][0]==color[3][1][1]) and (color[5][2][0]==color[2][1][1] or color[5][2][0]==color[1][1][1] or color[5][2][0]==color==[3][1][1]):
        h=0
        for h in range(3):
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            D()
            result.append('D')
        D()
        result.append('D')
        D()
        result.append('D')
        if color[4][0][2]==color[1][1][1]:
            h=0
            for h in range (3):
                r()
                result.append('r')
                d()
                result.append('d')
                R()
                result.append('R')
                D()
                result.append('D')
        elif color[2][2][2]==color[1][1][1]:
            d()
            result.append('d')
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
        elif color[3][2][2]==color[1][1][1]:
            D()
            result.append('D')
            F()
            result.append('F')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')
    elif (color[0][2][2]==color[2][1][1] or color[0][2][2]==color[1][1][1] or color[0][2][2]==color[3][1][1]) and (color[1][2][0]==color[2][1][1] or color[1][2][0]==color[1][1][1] or color[1][2][0]==color[3][1][1]) and (color[3][0][0]==color[2][1][1] or color[3][0][0]==color[1][1][1] or color[3][0][0]==color[3][1][1]):
        h=0
        for h in range (3):
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
        D()
        result.append('D')
        if color[4][0][2]==color[1][1][1]:
            h=0
            for h in range (3):
                r()
                result.append('r')
                d()
                result.append('d')
                R()
                result.append('R')
                D()
                result.append('D')
        elif color[2][2][2]==color[1][1][1]:
            d()
            result.append('d')
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
        elif color[3][2][2]==color[1][1][1]:
            D()
            result.append('D')
            F()
            result.append('F')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')
    elif (color[2][2][2]==color[2][1][1] or color[2][2][2]==color[1][1][1] or color[2][2][2]==color[3][1][1]) and (color[3][2][2]==color[2][1][1] or color[3][2][2]==color[1][1][1] or color[3][2][2]==color[3][1][1]) and (color[4][0][2]==color[2][1][1] or color[4][0][2]==color[1][1][1] or color[4][0][2]==color[3][1][1]):
        if color[4][0][2]==color[1][1][1]:
            h=0
            for h in range (3):
                r()
                result.append('r')
                d()
                result.append('d')
                R()
                result.append('R')
                D()
                result.append('D')
        elif color[2][2][2]==color[1][1][1]:
            d()
            result.append('d')
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
        elif color[3][2][2]==color[1][1][1]:
            D()
            result.append('D')
            F()
            result.append('F')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')
    elif (color[2][0][2]==color[2][1][1] or color[2][0][2]==color[1][1][1] or color[2][0][2]==color[3][1][1]) and (color[5][0][2]==color[2][1][1] or color[5][0][2]==color[1][1][1] or color[5][0][2]==color[3][1][1]) and (color[4][2][2]==color[2][1][1] or color[4][2][2]==color[1][1][1] or color[4][2][2]==color[3][1][1]):
        d()
        result.append('d')
        if color[4][0][2]==color[1][1][1]:
            h=0
            for h in range (3):
                r()
                result.append('r')
                d()
                result.append('d')
                R()
                result.append('R')
                D()
                result.append('D')
        elif color[2][2][2]==color[1][1][1]:
            d()
            result.append('d')
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
        elif color[3][2][2]==color[1][1][1]:
            D()
            result.append('D')
            F()
            result.append('F')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')
    elif (color[0][0][0]==color[2][1][1] or color[0][0][0]==color[1][1][1] or color[0][0][0]==color[3][1][1]) and (color[5][0][0]==color[2][1][1] or color[5][0][0]==color[1][1][1] or color[5][0][0]==color[3][1][1]) and (color[4][2][0]==color[2][1][1] or color[4][2][0]==color[1][1][1] or color[4][2][0]==color[3][1][1]):
        D()
        result.append('D')
        D()
        result.append('D')
        if color[4][0][2]==color[1][1][1]:
            h=0
            for h in range (3):
                r()
                result.append('r')
                d()
                result.append('d')
                R()
                result.append('R')
                D()
                result.append('D')
        elif color[2][2][2]==color[1][1][1]:
            d()
            result.append('d')
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
        elif color[3][2][2]==color[1][1][1]:
            D()
            result.append('D')
            F()
            result.append('F')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')
    elif (color[0][2][0]==color[2][1][1] or color[0][2][0]==color[1][1][1] or color[0][2][0]==color[3][1][1]) and (color[3][2][0]==color[2][1][1] or color[3][2][0]==color[1][1][1] or color[3][2][0]==color[3][1][1]) and (color[4][0][0]==color[2][1][1] or color[4][0][0]==color[1][1][1] or color[4][0][0]==color[3][1][1]):
        D()
        result.append('D')
        if color[4][0][2]==color[1][1][1]:
            h=0
            for h in range (3):
                r()
                result.append('r')
                d()
                result.append('d')
                R()
                result.append('R')
                D()
                result.append('D')
        elif color[2][2][2]==color[1][1][1]:
            d()
            result.append('d')
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
            D()
            result.append('D')
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            D()
            result.append('D')
        elif color[3][2][2]==color[1][1][1]:
            D()
            result.append('D')
            F()
            result.append('F')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')
            d()
            result.append('d')
            F()
            result.append('F')
            D()
            result.append('D')
            f()
            result.append('f')
            d()
            result.append('d')

result.append('+')

# Bottom Cross

if not color[4][0][1]==color[4][1][0]==color[4][1][1]==color[4][1][2]==color[4][2][1] and ((not color[4][0][1]==color[4][1][1] and not color[4][1][0]==color[4][1][1] and not color[4][1][2]==color[4][1][1] and not color[4][2][1]==color[4][1][1]) or (color[4][0][1]==color[4][1][1] and not color[4][1][0]==color[4][1][1] and not color[4][1][2]==color[4][1][1] and not color[4][2][1]==color[4][1][1]) or (color[4][1][0]==color[4][1][1] and not color[4][0][1]==color[4][1][1] and not color[4][1][2]==color[4][1][1] and not color[4][2][1]==color[4][1][1]) or (color[4][1][2]==color[4][1][1] and not color[4][1][0]==color[4][1][1] and not color[4][0][1]==color[4][1][1] and not color[4][2][1]==color[4][1][1]) or (color[4][2][1]==color[4][1][1] and not color[4][1][0]==color[4][1][1] and not color[4][1][2]==color[4][1][1] and not color[4][0][1]==color[4][1][1])) :
    f()
    result.append('f')
    r()
    result.append('r')
    d()
    result.append('d')
    R()
    result.append('R')
    D()
    result.append('D')
    F()
    result.append('F')
if not color[4][0][1]==color[4][1][0]==color[4][1][1]==color[4][1][2]==color[4][2][1] and (((color[4][0][1]==color[4][1][1]==color[4][1][2]==color[4][2][1] and not color[4][1][0]==color[4][1][1]) or (color[4][0][1]==color[4][1][0]==color[4][1][1]==color[4][1][2] and not color[4][2][1]==color[4][1][1]) or (color[4][0][1]==color[4][1][1]==color[4][1][2] and not color[4][1][0]==color[4][1][1] and not color[4][2][1]==color[4][1][1])) or ((color[4][0][1]==color[4][1][0]==color[4][1][1]==color[4][2][1] and not color[4][1][2]==color[4][1][1]) or (color[4][1][0]==color[4][1][1]==color[4][1][2]==color[4][2][1] and not color[4][0][1]==color[4][1][1]) or (color[4][1][0]==color[4][1][1]==color[4][2][1] and not color[4][0][1]==color[4][1][1] and not color[4][1][2]==color[4][1][1])) or (color[4][0][1]==color[4][1][0]==color[4][1][1] and not color[4][1][2]==color[4][1][1] and not color[4][2][1]==color[4][1][1]) or (color[4][1][1]==color[4][1][2]==color[4][2][1] and not color[4][0][1]==color[4][1][1] and not color[4][1][0]==color[4][1][1])) :
    if (color[4][0][1]==color[4][1][1]==color[4][1][2]==color[4][2][1] and not color[4][1][0]==color[4][1][1]) or (color[4][0][1]==color[4][1][0]==color[4][1][1]==color[4][1][2] and not color[4][2][1]==color[4][1][1]) or (color[4][0][1]==color[4][1][1]==color[4][1][2] and not color[4][1][0]==color[4][1][1] and not color[4][2][1]==color[4][1][1]) :
        f()
        result.append('f')
        r()
        result.append('r')
        d()
        result.append('d')
        R()
        result.append('R')
        D()
        result.append('D')
        F()
        result.append('F')
    elif (color[4][0][1]==color[4][1][0]==color[4][1][1]==color[4][2][1] and not color[4][1][2]==color[4][1][1]) or (color[4][1][0]==color[4][1][1]==color[4][1][2]==color[4][2][1] and not color[4][0][1]==color[4][1][1]) or (color[4][1][0]==color[4][1][1]==color[4][2][1] and not color[4][0][1]==color[4][1][1] and not color[4][1][2]==color[4][1][1]) :
        b()
        result.append('b')
        l()
        result.append('l')
        d()
        result.append('d')
        L()
        result.append('L')
        D()
        result.append('D')
        B()
        result.append('B')
    elif color[4][0][1]==color[4][1][0]==color[4][1][1] and not color[4][1][2]==color[4][1][1] and not color[4][2][1]==color[4][1][1] :
        l()
        result.append('l')
        f()
        result.append('f')
        d()
        result.append('d')
        F()
        result.append('F')
        D()
        result.append('D')
        L()
        result.append('L')
    elif color[4][1][1]==color[4][1][2]==color[4][2][1] and not color[4][0][1]==color[4][1][1] and not color[4][1][0]==color[4][1][1] :
        r()
        result.append('r')
        b()
        result.append('b')
        d()
        result.append('d')
        B()
        result.append('B')
        D()
        result.append('D')
        R()
        result.append('R')
if not color[4][0][1]==color[4][1][0]==color[4][1][1]==color[4][1][2]==color[4][2][1] and (color[4][0][1]==color[4][1][1]==color[4][2][1] or color[4][1][0]==color[4][1][1]==color[4][1][2]) :
    if color[4][0][1]==color[4][1][1]==color[4][2][1] :
        r()
        result.append('r')
        b()
        result.append('b')
        d()
        result.append('d')
        B()
        result.append('B')
        D()
        result.append('D')
        R()
        result.append('R')
    elif color[4][1][0]==color[4][1][1]==color[4][1][2] :
        f()
        result.append('f')
        r()
        result.append('r')
        d()
        result.append('d')
        R()
        result.append('R')
        D()
        result.append('D')
        F()
        result.append('F')
        
result.append('+')
        
# OLL

if (color[4][0][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1]) or (color[4][0][2]==color[4][1][1] and not color[4][0][0]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1]) or (color[4][2][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][0][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1]) or (color[4][2][2]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][0][0]==color[4][1][1]) :
    if color[4][0][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
        r()
        result.append('r')
        d()
        result.append('d')
        R()
        result.append('R')
        d()
        result.append('d')
        r()
        result.append('r')
        d()
        result.append('d')
        d()
        result.append('d')
        R()
        result.append('R')
    elif color[4][0][2]==color[4][1][1] and not color[4][0][0]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
        b()
        result.append('b')
        d()
        result.append('d')
        B()
        result.append('B')
        d()
        result.append('d')
        b()
        result.append('b')
        d()
        result.append('d')
        d()
        result.append('d')
        B()
        result.append('B')
    elif color[4][2][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][0][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
        f()
        result.append('f')
        d()
        result.append('d')
        F()
        result.append('F')
        d()
        result.append('d')
        f()
        result.append('f')
        d()
        result.append('d')
        d()
        result.append('d')
        F()
        result.append('F')
    elif color[4][2][2]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][0][0]==color[4][1][1] :
        l()
        result.append('l')
        d()
        result.append('d')
        L()
        result.append('L')
        d()
        result.append('d')
        l()
        result.append('l')
        d()
        result.append('d')
        d()
        result.append('d')
        L()
        result.append('L')
    if color[4][0][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
        r()
        result.append('r')
        d()
        result.append('d')
        R()
        result.append('R')
        d()
        result.append('d')
        r()
        result.append('r')
        d()
        result.append('d')
        d()
        result.append('d')
        R()
        result.append('R')
    elif color[4][0][2]==color[4][1][1] and not color[4][0][0]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
        b()
        result.append('b')
        d()
        result.append('d')
        B()
        result.append('B')
        d()
        result.append('d')
        b()
        result.append('b')
        d()
        result.append('d')
        d()
        result.append('d')
        B()
        result.append('B')
    elif color[4][2][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][0][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
        f()
        result.append('f')
        d()
        result.append('d')
        F()
        result.append('F')
        d()
        result.append('d')
        f()
        result.append('f')
        d()
        result.append('d')
        d()
        result.append('d')
        F()
        result.append('F')
    elif color[4][2][2]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][0][0]==color[4][1][1] :
        l()
        result.append('l')
        d()
        result.append('d')
        L()
        result.append('L')
        d()
        result.append('d')
        l()
        result.append('l')
        d()
        result.append('d')
        d()
        result.append('d')
        L()
        result.append('L')
elif not color[4][0][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
    if not color[3][2][0]==color[4][1][1] and not color[3][2][1]==color[4][1][1] and not color[3][2][2]==color[4][1][1] :
        r()
        result.append('r')
        d()
        result.append('d')
        R()
        result.append('R')
        d()
        result.append('d')
        r()
        result.append('r')
        d()
        result.append('d')
        d()
        result.append('d')
        R()
        result.append('R')
    elif not color[0][0][0]==color[4][1][1] and not color[0][1][0]==color[4][1][1] and not color[0][2][0]==color[4][1][1] :
        f()
        result.append('f')
        d()
        result.append('d')
        F()
        result.append('F')
        d()
        result.append('d')
        f()
        result.append('f')
        d()
        result.append('d')
        d()
        result.append('d')
        F()
        result.append('F')
    elif not color[2][0][2]==color[4][1][1] and not color[2][1][2]==color[4][1][1] and not color[2][2][2]==color[4][1][1] :
        b()
        result.append('b')
        d()
        result.append('d')
        B()
        result.append('B')
        d()
        result.append('d')
        b()
        result.append('b')
        d()
        result.append('d')
        d()
        result.append('d')
        B()
        result.append('B')
    elif not color[5][0][0]==color[4][1][1] and not color[5][0][1]==color[4][1][1] and not color[5][0][2]==color[4][1][1] :
        l()
        result.append('l')
        d()
        result.append('d')
        L()
        result.append('L')
        d()
        result.append('d')
        l()
        result.append('l')
        d()
        result.append('d')
        d()
        result.append('d')
        L()
        result.append('L')
    if color[4][0][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
        r()
        result.append('r')
        d()
        result.append('d')
        R()
        result.append('R')
        d()
        result.append('d')
        r()
        result.append('r')
        d()
        result.append('d')
        d()
        result.append('d')
        R()
        result.append('R')
    elif color[4][0][2]==color[4][1][1] and not color[4][0][0]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
        b()
        result.append('b')
        d()
        result.append('d')
        B()
        result.append('B')
        d()
        result.append('d')
        b()
        result.append('b')
        d()
        result.append('d')
        d()
        result.append('d')
        B()
        result.append('B')
    elif color[4][2][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][0][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
        f()
        result.append('f')
        d()
        result.append('d')
        F()
        result.append('F')
        d()
        result.append('d')
        f()
        result.append('f')
        d()
        result.append('d')
        d()
        result.append('d')
        F()
        result.append('F')
    elif color[4][2][2]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][0][0]==color[4][1][1] :
        l()
        result.append('l')
        d()
        result.append('d')
        L()
        result.append('L')
        d()
        result.append('d')
        l()
        result.append('l')
        d()
        result.append('d')
        d()
        result.append('d')
        L()
        result.append('L')
    if color[4][0][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
        r()
        result.append('r')
        d()
        result.append('d')
        R()
        result.append('R')
        d()
        result.append('d')
        r()
        result.append('r')
        d()
        result.append('d')
        d()
        result.append('d')
        R()
        result.append('R')
    elif color[4][0][2]==color[4][1][1] and not color[4][0][0]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
        b()
        result.append('b')
        d()
        result.append('d')
        B()
        result.append('B')
        d()
        result.append('d')
        b()
        result.append('b')
        d()
        result.append('d')
        d()
        result.append('d')
        B()
        result.append('B')
    elif color[4][2][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][0][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
        f()
        result.append('f')
        d()
        result.append('d')
        F()
        result.append('F')
        d()
        result.append('d')
        f()
        result.append('f')
        d()
        result.append('d')
        d()
        result.append('d')
        F()
        result.append('F')
    elif color[4][2][2]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][0][0]==color[4][1][1] :
        l()
        result.append('l')
        d()
        result.append('d')
        L()
        result.append('L')
        d()
        result.append('d')
        l()
        result.append('l')
        d()
        result.append('d')
        d()
        result.append('d')
        L()
        result.append('L')
elif (color[4][0][0]==color[4][0][1]==color[4][1][0]==color[4][1][1]==color[4][1][2]==color[4][2][0]==color[4][2][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][2]==color[4][1][1]) or (color[4][0][0]==color[4][0][1]==color[4][0][2]==color[4][1][0]==color[4][1][1]==color[4][1][2]==color[4][2][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1]) or (color[4][0][1]==color[4][0][2]==color[4][1][0]==color[4][1][1]==color[4][1][2]==color[4][2][1]==color[4][2][2] and not color[4][0][0]==color[4][1][1] and not color[4][2][0]==color[4][1][1]) or (color[4][0][1]==color[4][1][0]==color[4][1][1]==color[4][1][2]==color[4][2][0]==color[4][2][1]==color[4][2][2] and not color[4][0][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1]) or (color[4][0][0]==color[4][0][1]==color[4][1][0]==color[4][1][1]==color[4][1][2]==color[4][2][1]==color[4][2][2] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1]) or (color[4][0][1]==color[4][0][2]==color[4][1][0]==color[4][1][1]==color[4][1][2]==color[4][2][0]==color[4][2][1] and not color[4][0][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1]) :
    if color[4][0][0]==color[4][0][1]==color[4][1][0]==color[4][1][1]==color[4][1][2]==color[4][2][0]==color[4][2][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
        l()
        result.append('l')
        d()
        result.append('d')
        L()
        result.append('L')
        d()
        result.append('d')
        l()
        result.append('l')
        d()
        result.append('d')
        d()
        result.append('d')
        L()
        result.append('L')
    elif color[4][0][0]==color[4][0][1]==color[4][0][2]==color[4][1][0]==color[4][1][1]==color[4][1][2]==color[4][2][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
        f()
        result.append('f')
        d()
        result.append('d')
        F()
        result.append('F')
        d()
        result.append('d')
        f()
        result.append('f')
        d()
        result.append('d')
        d()
        result.append('d')
        F()
        result.append('F')
    elif color[4][0][1]==color[4][0][2]==color[4][1][0]==color[4][1][1]==color[4][1][2]==color[4][2][1]==color[4][2][2] and not color[4][0][0]==color[4][1][1] and not color[4][2][0]==color[4][1][1] :
        r()
        result.append('r')
        d()
        result.append('d')
        R()
        result.append('R')
        d()
        result.append('d')
        r()
        result.append('r')
        d()
        result.append('d')
        d()
        result.append('d')
        R()
        result.append('R')
    elif color[4][0][1]==color[4][1][0]==color[4][1][1]==color[4][1][2]==color[4][2][0]==color[4][2][1]==color[4][2][2] and not color[4][0][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1] :
        b()
        result.append('b')
        d()
        result.append('d')
        B()
        result.append('B')
        d()
        result.append('d')
        b()
        result.append('b')
        d()
        result.append('d')
        d()
        result.append('d')
        B()
        result.append('B')
    elif color[4][0][0]==color[4][0][1]==color[4][1][0]==color[4][1][1]==color[4][1][2]==color[4][2][1]==color[4][2][2] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1] :
        f()
        result.append('f')
        d()
        result.append('d')
        F()
        result.append('F')
        d()
        result.append('d')
        f()
        result.append('f')
        d()
        result.append('d')
        d()
        result.append('d')
        F()
        result.append('F')
    elif color[4][0][1]==color[4][0][2]==color[4][1][0]==color[4][1][1]==color[4][1][2]==color[4][2][0]==color[4][2][1] and not color[4][0][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
        l()
        result.append('l')
        d()
        result.append('d')
        L()
        result.append('L')
        d()
        result.append('d')
        l()
        result.append('l')
        d()
        result.append('d')
        d()
        result.append('d')
        L()
        result.append('L')
    if not color[4][0][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
        if not color[3][2][0]==color[4][1][1] and not color[3][2][1]==color[4][1][1] and not color[3][2][2]==color[4][1][1] :
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            d()
            result.append('d')
            r()
            result.append('r')
            d()
            result.append('d')
            d()
            result.append('d')
            R()
            result.append('R')
        elif not color[0][0][0]==color[4][1][1] and not color[0][1][0]==color[4][1][1] and not color[0][2][0]==color[4][1][1] :
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            d()
            result.append('d')
            f()
            result.append('f')
            d()
            result.append('d')
            d()
            result.append('d')
            F()
            result.append('F')
        elif not color[2][0][2]==color[4][1][1] and not color[2][1][2]==color[4][1][1] and not color[2][2][2]==color[4][1][1] :
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            d()
            result.append('d')
            b()
            result.append('b')
            d()
            result.append('d')
            d()
            result.append('d')
            B()
            result.append('B')
        elif not color[2][2][2]==color[4][1][1] and not color[2][1][2]==color[4][1][1] and not color[2][0][2]==color[4][1][1] :
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            d()
            result.append('d')
            l()
            result.append('l')
            d()
            result.append('d')
            d()
            result.append('d')
            L()
            result.append('L')
        if color[4][0][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            d()
            result.append('d')
            r()
            result.append('r')
            d()
            result.append('d')
            d()
            result.append('d')
            R()
            result.append('R')
        elif color[4][0][2]==color[4][1][1] and not color[4][0][0]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            d()
            result.append('d')
            b()
            result.append('b')
            d()
            result.append('d')
            d()
            result.append('d')
            B()
            result.append('B')
        elif color[4][2][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][0][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            d()
            result.append('d')
            f()
            result.append('f')
            d()
            result.append('d')
            d()
            result.append('d')
            F()
            result.append('F')
        elif color[4][2][2]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][0][0]==color[4][1][1] :
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            d()
            result.append('d')
            l()
            result.append('l')
            d()
            result.append('d')
            d()
            result.append('d')
            L()
            result.append('L')
        if color[4][0][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            d()
            result.append('d')
            r()
            result.append('r')
            d()
            result.append('d')
            d()
            result.append('d')
            R()
            result.append('R')
        elif color[4][0][2]==color[4][1][1] and not color[4][0][0]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            d()
            result.append('d')
            b()
            result.append('b')
            d()
            result.append('d')
            d()
            result.append('d')
            B()
            result.append('B')
        elif color[4][2][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][0][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            d()
            result.append('d')
            f()
            result.append('f')
            d()
            result.append('d')
            d()
            result.append('d')
            F()
            result.append('F')
        elif color[4][2][2]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][0][0]==color[4][1][1] :
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            d()
            result.append('d')
            l()
            result.append('l')
            d()
            result.append('d')
            d()
            result.append('d')
            L()
            result.append('L')
    elif (color[4][0][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1]) or (color[4][0][2]==color[4][1][1] and not color[4][0][0]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1]) or (color[4][2][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][0][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1]) or (color[4][2][2]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][0][0]==color[4][1][1]) :
        if color[4][0][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            d()
            result.append('d')
            r()
            result.append('r')
            d()
            result.append('d')
            d()
            result.append('d')
            R()
            result.append('R')
        elif color[4][0][2]==color[4][1][1] and not color[4][0][0]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            d()
            result.append('d')
            b()
            result.append('b')
            d()
            result.append('d')
            d()
            result.append('d')
            B()
            result.append('B')
        elif color[4][2][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][0][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            d()
            result.append('d')
            f()
            result.append('f')
            d()
            result.append('d')
            d()
            result.append('d')
            F()
            result.append('F')
        elif color[4][2][2]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][0][0]==color[4][1][1] :
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            d()
            result.append('d')
            l()
            result.append('l')
            d()
            result.append('d')
            d()
            result.append('d')
            L()
            result.append('L')
        if color[4][0][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
            r()
            result.append('r')
            d()
            result.append('d')
            R()
            result.append('R')
            d()
            result.append('d')
            r()
            result.append('r')
            d()
            result.append('d')
            d()
            result.append('d')
            R()
            result.append('R')
        elif color[4][0][2]==color[4][1][1] and not color[4][0][0]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
            b()
            result.append('b')
            d()
            result.append('d')
            B()
            result.append('B')
            d()
            result.append('d')
            b()
            result.append('b')
            d()
            result.append('d')
            d()
            result.append('d')
            B()
            result.append('B')
        elif color[4][2][0]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][0][0]==color[4][1][1] and not color[4][2][2]==color[4][1][1] :
            f()
            result.append('f')
            d()
            result.append('d')
            F()
            result.append('F')
            d()
            result.append('d')
            f()
            result.append('f')
            d()
            result.append('d')
            d()
            result.append('d')
            F()
            result.append('F')
        elif color[4][2][2]==color[4][1][1] and not color[4][0][2]==color[4][1][1] and not color[4][2][0]==color[4][1][1] and not color[4][0][0]==color[4][1][1] :
            l()
            result.append('l')
            d()
            result.append('d')
            L()
            result.append('L')
            d()
            result.append('d')
            l()
            result.append('l')
            d()
            result.append('d')
            d()
            result.append('d')
            L()
            result.append('L')

result.append('+')

# PLL

if not color[3][2][0]==color[3][2][2] and not color[0][0][0]==color[0][2][0] and not color[2][0][2]==color[2][2][2] and not color[5][0][0]==color[5][0][2] :
    r()
    result.append('r')
    B()
    result.append('B')
    r()
    result.append('r')
    F()
    result.append('F')
    F()
    result.append('F')
    R()
    result.append('R')
    b()
    result.append('b')
    r()
    result.append('r')
    F()
    result.append('F')
    F()
    result.append('F')
    R()
    result.append('R')
    R()
    result.append('R')
if color[3][2][0]==color[3][2][2] and (not color[0][0][0]==color[0][2][0] or not color[2][0][2]==color[2][2][2] or not color[5][0][0]==color[5][0][2]) :
    if color[3][2][0]==color[3][2][2]==color[3][1][1] :
        r()
        result.append('r')
        B()
        result.append('B')
        r()
        result.append('r')
        F()
        result.append('F')
        F()
        result.append('F')
        R()
        result.append('R')
        b()
        result.append('b')
        r()
        result.append('r')
        F()
        result.append('F')
        F()
        result.append('F')
        R()
        result.append('R')
        R()
        result.append('R')
    elif color[3][2][0]==color[3][2][2]==color[0][1][1] :
        d()
        result.append('d')
        f()
        result.append('f')
        R()
        result.append('R')
        f()
        result.append('f')
        L()
        result.append('L')
        L()
        result.append('L')
        F()
        result.append('F')
        r()
        result.append('r')
        f()
        result.append('f')
        L()
        result.append('L')
        L()
        result.append('L')
        F()
        result.append('F')
        F()
        result.append('F')
    elif color[3][2][0]==color[3][2][2]==color[2][1][1] :
        D()
        result.append('D')
        b()
        result.append('b')
        L()
        result.append('L')
        b()
        result.append('b')
        R()
        result.append('R')
        R()
        result.append('R')
        B()
        result.append('B')
        l()
        result.append('l')
        b()
        result.append('b')
        R()
        result.append('R')
        R()
        result.append('R')
        B()
        result.append('B')
        B()
        result.append('B')
    elif color[3][2][0]==color[3][2][2]==color[5][1][1] :
        D()
        result.append('D')
        D()
        result.append('D')
        l()
        result.append('l')
        F()
        result.append('F')
        l()
        result.append('l')
        B()
        result.append('B')
        B()
        result.append('B')
        L()
        result.append('L')
        f()
        result.append('f')
        l()
        result.append('l')
        B()
        result.append('B')
        B()
        result.append('B')
        L()
        result.append('L')
        L()
        result.append('L')
elif color[0][0][0]==color[0][2][0] and (not color[3][2][0]==color[3][2][2] or not color[2][0][2]==color[2][2][2] or not color[5][0][0]==color[5][0][2]) :
    if color[0][0][0]==color[0][2][0]==color[0][1][1] :
        f()
        result.append('f')
        R()
        result.append('R')
        f()
        result.append('f')
        L()
        result.append('L')
        L()
        result.append('L')
        F()
        result.append('F')
        r()
        result.append('r')
        f()
        result.append('f')
        L()
        result.append('L')
        L()
        result.append('L')
        F()
        result.append('F')
        F()
        result.append('F')
    elif color[0][0][0]==color[0][2][0]==color[5][1][1] :
        d()
        result.append('d')
        l()
        result.append('l')
        F()
        result.append('F')
        l()
        result.append('l')
        B()
        result.append('B')
        B()
        result.append('B')
        L()
        result.append('L')
        f()
        result.append('f')
        l()
        result.append('l')
        B()
        result.append('B')
        B()
        result.append('B')
        L()
        result.append('L')
        L()
        result.append('L')
    elif color[0][0][0]==color[0][2][0]==color[3][1][1] :
        D()
        result.append('D')
        r()
        result.append('r')
        B()
        result.append('B')
        r()
        result.append('r')
        F()
        result.append('F')
        F()
        result.append('F')
        R()
        result.append('R')
        b()
        result.append('b')
        r()
        result.append('r')
        F()
        result.append('F')
        F()
        result.append('F')
        R()
        result.append('R')
        R()
        result.append('R')
    elif color[0][0][0]==color[0][2][0]==color[2][1][1] :
        D()
        result.append('D')
        D()
        result.append('D')
        b()
        result.append('b')
        L()
        result.append('L')
        b()
        result.append('b')
        R()
        result.append('R')
        R()
        result.append('R')
        B()
        result.append('B')
        l()
        result.append('l')
        b()
        result.append('b')
        R()
        result.append('R')
        R()
        result.append('R')
        B()
        result.append('B')
        B()
        result.append('B')
elif color[2][0][2]==color[2][2][2] and (not color[0][0][0]==color[0][2][0] or not color[3][2][0]==color[3][2][2] or not color[5][0][0]==color[5][0][2]) :
    if color[2][0][2]==color[2][2][2]==color[2][1][1] :
        b()
        result.append('b')
        L()
        result.append('L')
        b()
        result.append('b')
        R()
        result.append('R')
        R()
        result.append('R')
        B()
        result.append('B')
        l()
        result.append('l')
        b()
        result.append('b')
        R()
        result.append('R')
        R()
        result.append('R')
        B()
        result.append('B')
        B()
        result.append('B')
    elif color[2][0][2]==color[2][2][2]==color[3][1][1] :
        d()
        result.append('d')
        r()
        result.append('r')
        B()
        result.append('B')
        r()
        result.append('r')
        F()
        result.append('F')
        F()
        result.append('F')
        R()
        result.append('R')
        b()
        result.append('b')
        r()
        result.append('r')
        F()
        result.append('F')
        F()
        result.append('F')
        R()
        result.append('R')
        R()
        result.append('R')
    elif color[2][0][2]==color[2][2][2]==color[5][1][1] :
        D()
        result.append('D')
        l()
        result.append('l')
        F()
        result.append('F')
        l()
        result.append('l')
        B()
        result.append('B')
        B()
        result.append('B')
        L()
        result.append('L')
        f()
        result.append('f')
        l()
        result.append('l')
        B()
        result.append('B')
        B()
        result.append('B')
        L()
        result.append('L')
        L()
        result.append('L')
    elif color[2][0][2]==color[2][2][2]==color[0][1][1] :
        D()
        result.append('D')
        D()
        result.append('D')
        f()
        result.append('f')
        R()
        result.append('R')
        f()
        result.append('f')
        L()
        result.append('L')
        L()
        result.append('L')
        F()
        result.append('F')
        r()
        result.append('r')
        f()
        result.append('f')
        L()
        result.append('L')
        L()
        result.append('L')
        F()
        result.append('F')
        F()
        result.append('F')
elif color[5][0][0]==color[5][0][2] and (not color[0][0][0]==color[0][2][0] or not color[2][0][2]==color[2][2][2] or not color[3][2][0]==color[3][2][2]) :
    if color[5][0][0]==color[5][0][2]==color[5][1][1] :
        l()
        result.append('l')
        F()
        result.append('F')
        l()
        result.append('l')
        B()
        result.append('B')
        B()
        result.append('B')
        L()
        result.append('L')
        f()
        result.append('f')
        l()
        result.append('l')
        B()
        result.append('B')
        B()
        result.append('B')
        L()
        result.append('L')
        L()
        result.append('L')
    elif color[5][0][0]==color[5][0][2]==color[2][1][1] :
        d()
        result.append('d')
        b()
        result.append('b')
        L()
        result.append('L')
        b()
        result.append('b')
        R()
        result.append('R')
        R()
        result.append('R')
        B()
        result.append('B')
        l()
        result.append('l')
        b()
        result.append('b')
        R()
        result.append('R')
        R()
        result.append('R')
        B()
        result.append('B')
        B()
        result.append('B')
    elif color[5][0][0]==color[5][0][2]==color[0][1][1] :
        D()
        result.append('D')
        f()
        result.append('f')
        R()
        result.append('R')
        f()
        result.append('f')
        L()
        result.append('L')
        L()
        result.append('L')
        F()
        result.append('F')
        r()
        result.append('r')
        f()
        result.append('f')
        L()
        result.append('L')
        L()
        result.append('L')
        F()
        result.append('F')
        F()
        result.append('F')
    elif color[5][0][0]==color[5][0][2]==color[3][1][1] :
        D()
        result.append('D')
        D()
        result.append('D')
        r()
        result.append('r')
        B()
        result.append('B')
        r()
        result.append('r')
        F()
        result.append('F')
        F()
        result.append('F')
        R()
        result.append('R')
        b()
        result.append('b')
        r()
        result.append('r')
        F()
        result.append('F')
        F()
        result.append('F')
        R()
        result.append('R')
        R()
        result.append('R')

if color[3][2][0]==color[3][2][2]==color[2][1][1]:
    D()
    result.append('D')
elif color[3][2][0]==color[3][2][2]==color[0][1][1]:
    d()
    result.append('d')
elif color[3][2][0]==color[3][2][2]==color[5][1][1]:
    D()
    result.append('D')
    D()  
    result.append('D')

if (color[3][2][0]==color[3][2][1]==color[3][2][2] and not color[0][0][0]==color[0][1][0]==color[0][2][0] and not color[2][0][2]==color[2][1][2]==color[2][2][2] and not color[5][0][0]==color[5][0][1]==color[5][0][2]) or (color[0][0][0]==color[0][1][0]==color[0][2][0] and not color[3][2][0]==color[3][2][1]==color[3][2][2] and not color[2][0][2]==color[2][1][2]==color[2][2][2] and not color[5][0][0]==color[5][0][1]==color[5][0][2]) or (color[2][0][2]==color[2][1][2]==color[2][2][2] and not color[0][0][0]==color[0][1][0]==color[0][2][0] and not color[3][2][0]==color[3][2][1]==color[3][2][2] and not color[5][0][0]==color[5][0][1]==color[5][0][2]) or (color[5][0][0]==color[5][0][1]==color[5][0][2] and not color[0][0][0]==color[0][1][0]==color[0][2][0] and not color[3][2][0]==color[3][2][1]==color[3][2][2] and not color[2][0][2]==color[2][1][2]==color[2][2][2]) :
    if color[3][2][0]==color[3][2][1]==color[3][2][2] and not color[0][0][0]==color[0][1][0]==color[0][2][0] and not color[2][0][2]==color[2][1][2]==color[2][2][2] and not color[5][0][0]==color[5][0][1]==color[5][0][2] :
        if color[3][2][0]==color[3][2][1]==color[3][2][2]==color[3][1][1] :
            B()
            result.append('B')
            B()
            result.append('B')
            if color[5][1][1]==color[0][1][0] :
                d()
                result.append('d')
                temp = 'd'
            else :
                D()
                result.append('D')
                temp = 'D'
            L()
            result.append('L')
            r()
            result.append('r')
            B()
            result.append('B')
            B()
            result.append('B')
            l()
            result.append('l')
            R()
            result.append('R')
            if temp == 'd' :
                d()
                result.append('d')
            else :
                D()
                result.append('D')
            B()
            result.append('B')
            B()
            result.append('B')
        elif color[3][2][0]==color[3][2][1]==color[3][2][2]==color[0][1][1] :
            d()
            result.append('d')
            R()
            result.append('R')
            R()
            result.append('R')
            if color[2][1][1]==color[3][2][1] :
                D()
                result.append('D')
                temp = 'D'
            else :
                d()
                result.append('d')
                temp = 'd'
            B()
            result.append('B')
            f()
            result.append('f')
            R()
            result.append('R')
            R()
            result.append('R')
            b()
            result.append('b')
            F()
            result.append('F')
            if temp == 'D' :
                D()
                result.append('D')
            else :
                d()
                result.append('d')
            R()
            result.append('R')
            R()
            result.append('R')
        elif color[3][2][0]==color[3][2][1]==color[3][2][2]==color[2][1][1] :
            D()
            result.append('D')
            L()
            result.append('L')
            L()
            result.append('L')
            if color[3][2][1]==color[0][1][1] :
                d()
                result.append('d')
                temp = 'd'
            else :
                D()
                result.append('D')
                temp = 'D'
            b()
            result.append('b')
            F()
            result.append('F')
            L()
            result.append('L')
            L()
            result.append('L')
            B()
            result.append('B')
            f()
            result.append('f')
            if temp == 'd' :
                d()
                result.append('d')
            else :
                D()
                result.append('D')
            L()
            result.append('L')
            L()
            result.append('L')
        elif color[3][2][0]==color[3][2][1]==color[3][2][2]==color[5][1][1] :
            D()
            result.append('D')
            D()
            result.append('D')
            F()
            result.append('F')
            F()
            result.append('F')
            if color[3][1][1]==color[0][1][0] :
                D()
                result.append('D')
                temp = 'D'
            else :
                d()
                result.append('d')
                temp = 'd'
            l()
            result.append('l')
            R()
            result.append('R')
            F()
            result.append('F')
            F()
            result.append('F')
            L()
            result.append('L')
            r()
            result.append('r')
            if temp == 'D' :
                D()
                result.append('D')
            else :
                d()
                result.append('d')
            F()
            result.append('F')
            F()
            result.append('F')
    elif color[0][0][0]==color[0][1][0]==color[0][2][0] and not color[3][2][0]==color[3][2][1]==color[3][2][2] and not color[2][0][2]==color[2][1][2]==color[2][2][2] and not color[5][0][0]==color[5][0][1]==color[5][0][2] :
        if color[0][0][0]==color[0][1][0]==color[0][2][0]==color[3][1][1] :
            D()
            result.append('D')
            B()
            result.append('B')
            B()
            result.append('B')
            if color[5][1][1]==color[0][1][0] :
                d()
                result.append('d')
                temp = 'd'
            else :
                D()
                result.append('D')
                temp = 'D'
            L()
            result.append('L')
            r()
            result.append('r')
            B()
            result.append('B')
            B()
            result.append('B')
            l()
            result.append('l')
            R()
            result.append('R')
            if temp == 'd' :
                d()
                result.append('d')
            else :
                D()
                result.append('D')
            B()
            result.append('B')
            B()
            result.append('B')
        elif color[0][0][0]==color[0][1][0]==color[0][2][0]==color[0][1][1] :
            R()
            result.append('R')
            R()
            result.append('R')
            if color[2][1][1]==color[3][2][1] :
                D()
                result.append('D')
                temp = 'D'
            else :
                d()
                result.append('d')
                temp = 'd'
            B()
            result.append('B')
            f()
            result.append('f')
            R()
            result.append('R')
            R()
            result.append('R')
            b()
            result.append('b')
            F()
            result.append('F')
            if temp == 'D' :
                D()
                result.append('D')
            else :
                d()
                result.append('d')
            R()
            result.append('R')
            R()
            result.append('R')
        elif color[0][0][0]==color[0][1][0]==color[0][2][0]==color[2][1][1] :
            D()
            result.append('D')
            D()
            result.append('D')
            L()
            result.append('L')
            L()
            result.append('L')
            if color[3][2][1]==color[0][1][1] :
                d()
                result.append('d')
                temp = 'd'
            else :
                D()
                result.append('D')
                temp = 'D'
            b()
            result.append('b')
            F()
            result.append('F')
            L()
            result.append('L')
            L()
            result.append('L')
            B()
            result.append('B')
            f()
            result.append('f')
            if temp == 'd' :
                d()
                result.append('d')
            else :
                D()
                result.append('D')
            L()
            result.append('L')
            L()
            result.append('L')
        elif color[0][0][0]==color[0][1][0]==color[0][2][0]==color[5][1][1] :
            d()
            result.append('d')
            F()
            result.append('F')
            F()
            result.append('F')
            if color[3][1][1]==color[0][1][0] :
                D()
                result.append('D')
                temp = 'D'
            else :
                d()
                result.append('d')
                temp = 'd'
            l()
            result.append('l')
            R()
            result.append('R')
            F()
            result.append('F')
            F()
            result.append('F')
            L()
            result.append('L')
            r()
            result.append('r')
            if temp == 'D' :
                D()
                result.append('D')
            else :
                d()
                result.append('d')
            F()
            result.append('F')
            F()
            result.append('F')
    elif color[2][0][2]==color[2][1][2]==color[2][2][2] and not color[0][0][0]==color[0][1][0]==color[0][2][0] and not color[3][2][0]==color[3][2][1]==color[3][2][2] and not color[5][0][0]==color[5][0][1]==color[5][0][2] :
        if color[2][0][2]==color[2][1][2]==color[2][2][2]==color[3][1][1] :
            d()
            result.append('d')
            B()
            result.append('B')
            B()
            result.append('B')
            if color[5][1][1]==color[0][1][0] :
                d()
                result.append('d')
                temp = 'd'
            else :
                D()
                result.append('D')
                temp = 'D'
            L()
            result.append('L')
            r()
            result.append('r')
            B()
            result.append('B')
            B()
            result.append('B')
            l()
            result.append('l')
            R()
            result.append('R')
            if temp == 'd' :
                d()
                result.append('d')
            else :
                D()
                result.append('D')
            B()
            result.append('B')
            B()
            result.append('B')
        elif color[2][0][2]==color[2][1][2]==color[2][2][2]==color[0][1][1] :
            D()
            result.append('D')
            D()
            result.append('D')
            R()
            result.append('R')
            R()
            result.append('R')
            if color[2][1][1]==color[3][2][1] :
                D()
                result.append('D')
                temp = 'D'
            else :
                d()
                result.append('d')
                temp = 'd'
            B()
            result.append('B')
            f()
            result.append('f')
            R()
            result.append('R')
            R()
            result.append('R')
            b()
            result.append('b')
            F()
            result.append('F')
            if temp == 'D' :
                D()
                result.append('D')
            else :
                d()
                result.append('d')
            R()
            result.append('R')
            R()
            result.append('R')
        elif color[2][0][2]==color[2][1][2]==color[2][2][2]==color[2][1][1] :
            L()
            result.append('L')
            L()
            result.append('L')
            if color[3][2][1]==color[0][1][1] :
                d()
                result.append('d')
                temp = 'd'
            else :
                D()
                result.append('D')
                temp = 'D'
            b()
            result.append('b')
            F()
            result.append('F')
            L()
            result.append('L')
            L()
            result.append('L')
            B()
            result.append('B')
            f()
            result.append('f')
            if temp == 'd' :
                d()
                result.append('d')
            else :
                D()
                result.append('D')
            L()
            result.append('L')
            L()
            result.append('L')
        elif color[2][0][2]==color[2][1][2]==color[2][2][2]==color[5][1][1] :
            D()
            result.append('D')
            F()
            result.append('F')
            F()
            result.append('F')
            if color[3][1][1]==color[0][1][0] :
                D()
                result.append('D')
                temp = 'D'
            else :
                d()
                result.append('d')
                temp = 'd'
            l()
            result.append('l')
            R()
            result.append('R')
            F()
            result.append('F')
            F()
            result.append('F')
            L()
            result.append('L')
            r()
            result.append('r')
            if temp == 'D' :
                D()
                result.append('D')
            else :
                d()
                result.append('d')
            F()
            result.append('F')
            F()
            result.append('F')
    elif color[5][0][0]==color[5][0][1]==color[5][0][2] and not color[0][0][0]==color[0][1][0]==color[0][2][0] and not color[3][2][0]==color[3][2][1]==color[3][2][2] and not color[2][0][2]==color[2][1][2]==color[2][2][2] :
        if color[5][0][0]==color[5][0][1]==color[5][0][2]==color[3][1][1] :
            D()
            result.append('D')
            D()
            result.append('D')
            B()
            result.append('B')
            B()
            result.append('B')
            if color[5][1][1]==color[0][1][0] :
                d()
                result.append('d')
                temp = 'd'
            else :
                D()
                result.append('D')
                temp = 'D'
            L()
            result.append('L')
            r()
            result.append('r')
            B()
            result.append('B')
            B()
            result.append('B')
            l()
            result.append('l')
            R()
            result.append('R')
            if temp == 'd' :
                d()
                result.append('d')
            else :
                D()
                result.append('D')
            B()
            result.append('B')
            B()
            result.append('B')
        elif color[5][0][0]==color[5][0][1]==color[5][0][2]==color[0][1][1] :
            D()
            result.append('D')
            R()
            result.append('R')
            R()
            result.append('R')
            if color[2][1][1]==color[3][2][1] :
                D()
                result.append('D')
                temp = 'D'
            else :
                d()
                result.append('d')
                temp = 'd'
            B()
            result.append('B')
            f()
            result.append('f')
            R()
            result.append('R')
            R()
            result.append('R')
            b()
            result.append('b')
            F()
            result.append('F')
            if temp == 'D' :
                D()
                result.append('D')
            else :
                d()
                result.append('d')
            R()
            result.append('R')
            R()
            result.append('R')
        elif color[5][0][0]==color[5][0][1]==color[5][0][2]==color[2][1][1] :
            d()
            result.append('d')
            L()
            result.append('L')
            L()
            result.append('L')
            if color[3][2][1]==color[0][1][1] :
                d()
                result.append('d')
                temp = 'd'
            else :
                D()
                result.append('D')
                temp = 'D'
            b()
            result.append('b')
            F()
            result.append('F')
            L()
            result.append('L')
            L()
            result.append('L')
            B()
            result.append('B')
            f()
            result.append('f')
            if temp == 'd' :
                d()
                result.append('d')
            else :
                D()
                result.append('D')
            L()
            result.append('L')
            L()
            result.append('L')
        elif color[5][0][0]==color[5][0][1]==color[5][0][2]==color[5][1][1] :
            F()
            result.append('F')
            F()
            result.append('F')
            if color[3][1][1]==color[0][1][0] :
                D()
                result.append('D')
                temp = 'D'
            else :
                d()
                result.append('d')
                temp = 'd'
            l()
            result.append('l')
            R()
            result.append('R')
            F()
            result.append('F')
            F()
            result.append('F')
            L()
            result.append('L')
            r()
            result.append('r')
            if temp == 'D' :
                D()
                result.append('D')
            else :
                d()
                result.append('d')
            F()
            result.append('F')
            F()
            result.append('F')

elif not color[3][2][0]==color[3][2][1]==color[3][2][2] and not color[5][0][0]==color[5][0][1]==color[5][0][2] and not color[0][0][0]==color[0][1][0]==color[0][2][0] and not color[2][0][2]==color[2][1][2]==color[2][2][2] and ((color[3][2][1]==color[5][1][1] and color[5][0][1]==color[3][1][1]) or (color[3][2][1]==color[2][1][1] and color[2][1][2]==color[3][1][1]) or (color[3][2][1]==color[0][1][1] and color[0][1][0]==color[3][1][1])):      
    if color[3][2][1]==color[5][1][1] and color[5][0][1]==color[3][1][1] :
        F()
        result.append('F')
        F()
        result.append('F')
        if color[3][1][1]==color[0][1][0] :
            D()
            result.append('D')
            temp = 'D'
        else :
            d()
            result.append('d')
            temp = 'd'
        l()
        result.append('l')
        R()
        result.append('R')
        F()
        result.append('F')
        F()
        result.append('F')
        L()
        result.append('L')
        r()
        result.append('r')
        if temp == 'D' :
            D()
            result.append('D')
        else :
            d()
            result.append('d')
        F()
        result.append('F')
        F()
        result.append('F')
    elif color[3][2][1]==color[2][1][1] and color[2][1][2]==color[3][1][1] :
        F()
        result.append('F')
        F()
        result.append('F')
        if color[3][1][1]==color[0][1][0] :
            D()
            result.append('D')
            temp = 'D'
        else :
            d()
            result.append('d')
            temp = 'd'
        l()
        result.append('l')
        R()
        result.append('R')
        F()
        result.append('F')
        F()
        result.append('F')
        L()
        result.append('L')
        r()
        result.append('r')
        if temp == 'D' :
            D()
            result.append('D')
        else :
            d()
            result.append('d')
        F()
        result.append('F')
        F()
        result.append('F')
    elif color[3][2][1]==color[0][1][1] and color[0][1][0]==color[3][1][1] :
        R()
        result.append('R')
        R()
        result.append('R')
        if color[2][1][1]==color[3][2][1] :
            D()
            result.append('D')
            temp = 'D'
        else :
            d()
            result.append('d')
            temp = 'd'
        B()
        result.append('B')
        f()
        result.append('f')
        R()
        result.append('R')
        R()
        result.append('R')
        b()
        result.append('b')
        F()
        result.append('F')
        if temp == 'D' :
            D()
            result.append('D')
        else :
            d()
            result.append('d')
        R()
        result.append('R')
        R()
        result.append('R')

if color[3][2][0]==color[3][2][2]==color[2][1][1]:
    D()
    result.append('D')
elif color[3][2][0]==color[3][2][2]==color[0][1][1]:
    d()
    result.append('d')
elif color[3][2][0]==color[3][2][2]==color[5][1][1]:
    D()
    result.append('D')
    D()  
    result.append('D')
    
if (color[3][2][0]==color[3][2][1]==color[3][2][2] and not color[0][0][0]==color[0][1][0]==color[0][2][0] and not color[2][0][2]==color[2][1][2]==color[2][2][2] and not color[5][0][0]==color[5][0][1]==color[5][0][2]) or (color[0][0][0]==color[0][1][0]==color[0][2][0] and not color[3][2][0]==color[3][2][1]==color[3][2][2] and not color[2][0][2]==color[2][1][2]==color[2][2][2] and not color[5][0][0]==color[5][0][1]==color[5][0][2]) or (color[2][0][2]==color[2][1][2]==color[2][2][2] and not color[0][0][0]==color[0][1][0]==color[0][2][0] and not color[3][2][0]==color[3][2][1]==color[3][2][2] and not color[5][0][0]==color[5][0][1]==color[5][0][2]) or (color[5][0][0]==color[5][0][1]==color[5][0][2] and not color[0][0][0]==color[0][1][0]==color[0][2][0] and not color[3][2][0]==color[3][2][1]==color[3][2][2] and not color[2][0][2]==color[2][1][2]==color[2][2][2]) :
    if color[3][2][0]==color[3][2][1]==color[3][2][2] and not color[0][0][0]==color[0][1][0]==color[0][2][0] and not color[2][0][2]==color[2][1][2]==color[2][2][2] and not color[5][0][0]==color[5][0][1]==color[5][0][2] :
        if color[3][2][0]==color[3][2][1]==color[3][2][2]==color[3][1][1] :
            B()
            result.append('B')
            B()
            result.append('B')
            if color[5][1][1]==color[0][1][0] :
                d()
                result.append('d')
                temp = 'd'
            else :
                D()
                result.append('D')
                temp = 'D'
            L()
            result.append('L')
            r()
            result.append('r')
            B()
            result.append('B')
            B()
            result.append('B')
            l()
            result.append('l')
            R()
            result.append('R')
            if temp =='d' :
                d()
                result.append('d')
            else :
                D()
                result.append('D')
            B()
            result.append('B')
            B()
            result.append('B')
        elif color[3][2][0]==color[3][2][1]==color[3][2][2]==color[0][1][1] :
            d()
            result.append('d')
            R()
            result.append('R')
            R()
            result.append('R')
            if color[2][1][1]==color[3][2][1] :
                D()
                result.append('D')
                temp = 'D'
            else :
                d()
                result.append('d')
                temp = 'd'
            B()
            result.append('B')
            f()
            result.append('f')
            R()
            result.append('R')
            R()
            result.append('R')
            b()
            result.append('b')
            F()
            result.append('F')
            if temp == 'D' :
                D()
                result.append('D')
            else :
                d()
                result.append('d')
            R()
            result.append('R')
            R()
            result.append('R')
        elif color[3][2][0]==color[3][2][1]==color[3][2][2]==color[2][1][1] :
            D()
            result.append('D')
            L()
            result.append('L')
            L()
            result.append('L')
            if color[3][2][1]==color[0][1][1] :
                d()
                result.append('d')
                temp = 'd'
            else :
                D()
                result.append('D')
                temp = 'D'
            b()
            result.append('b')
            F()
            result.append('F')
            L()
            result.append('L')
            L()
            result.append('L')
            B()
            result.append('B')
            f()
            result.append('f')
            if temp == 'd' :
                d()
                result.append('d')
            else :
                D()
                result.append('D')
            L()
            result.append('L')
            L()
            result.append('L')
        elif color[3][2][0]==color[3][2][1]==color[3][2][2]==color[5][1][1] :
            D()
            result.append('D')
            D()
            result.append('D')
            F()
            result.append('F')
            F()
            result.append('F')
            if color[3][1][1]==color[0][1][0] :
                D()
                result.append('D')
                temp = 'D'
            else :
                d()
                result.append('d')
                temp = 'd'
            l()
            result.append('l')
            R()
            result.append('R')
            F()
            result.append('F')
            F()
            result.append('F')
            L()
            result.append('L')
            r()
            result.append('r')
            if temp == 'D' :
                D()
                result.append('D')
            else :
                d()
                result.append('d')
            F()
            result.append('F')
            F()
            result.append('F')
    elif color[0][0][0]==color[0][1][0]==color[0][2][0] and not color[3][2][0]==color[3][2][1]==color[3][2][2] and not color[2][0][2]==color[2][1][2]==color[2][2][2] and not color[5][0][0]==color[5][0][1]==color[5][0][2] :
        if color[0][0][0]==color[0][1][0]==color[0][2][0]==color[3][1][1] :
            D()
            result.append('D')
            B()
            result.append('B')
            B()
            result.append('B')
            if color[5][1][1]==color[0][1][0] :
                d()
                result.append('d')
                temp = 'd'
            else :
                D()
                result.append('D')
                temp = 'D'
            L()
            result.append('L')
            r()
            result.append('r')
            B()
            result.append('B')
            B()
            result.append('B')
            l()
            result.append('l')
            R()
            result.append('R')
            if temp == 'd' :
                d()
                result.append('d')
            else :
                D()
                result.append('D')
            B()
            result.append('B')
            B()
            result.append('B')
        elif color[0][0][0]==color[0][1][0]==color[0][2][0]==color[0][1][1] :
            R()
            result.append('R')
            R()
            result.append('R')
            if color[2][1][1]==color[3][2][1] :
                D()
                result.append('D')
                temp = 'D'
            else :
                d()
                result.append('d')
                temp = 'd'
            B()
            result.append('B')
            f()
            result.append('f')
            R()
            result.append('R')
            R()
            result.append('R')
            b()
            result.append('b')
            F()
            result.append('F')
            if temp == 'D' :
                D()
                result.append('D')
            else :
                d()
                result.append('d')
            R()
            result.append('R')
            R()
            result.append('R')
        elif color[0][0][0]==color[0][1][0]==color[0][2][0]==color[2][1][1] :
            D()
            result.append('D')
            D()
            result.append('D')
            L()
            result.append('L')
            L()
            result.append('L')
            if color[3][2][1]==color[0][1][1] :
                d()
                result.append('d')
                temp = 'd'
            else :
                D()
                result.append('D')
                temp = 'D'
            b()
            result.append('b')
            F()
            result.append('F')
            L()
            result.append('L')
            L()
            result.append('L')
            B()
            result.append('B')
            f()
            result.append('f')
            if temp == 'd' :
                d()
                result.append('d')
            else :
                D()
                result.append('D')
            L()
            result.append('L')
            L()
            result.append('L')
        elif color[0][0][0]==color[0][1][0]==color[0][2][0]==color[5][1][1] :
            d()
            result.append('d')
            F()
            result.append('F')
            F()
            result.append('F')
            if color[3][1][1]==color[0][1][0] :
                D()
                result.append('D')
                temp = 'D'
            else :
                d()
                result.append('d')
                temp = 'd'
            l()
            result.append('l')
            R()
            result.append('R')
            F()
            result.append('F')
            F()
            result.append('F')
            L()
            result.append('L')
            r()
            result.append('r')
            if temp == 'D' :
                D()
                result.append('D')
            else :
                d()
                result.append('d')
            F()
            result.append('F')
            F()
            result.append('F')
    elif color[2][0][2]==color[2][1][2]==color[2][2][2] and not color[0][0][0]==color[0][1][0]==color[0][2][0] and not color[3][2][0]==color[3][2][1]==color[3][2][2] and not color[5][0][0]==color[5][0][1]==color[5][0][2] :
        if color[2][0][2]==color[2][1][2]==color[2][2][2]==color[3][1][1] :
            d()
            result.append('d')
            B()
            result.append('B')
            B()
            result.append('B')
            if color[5][1][1]==color[0][1][0] :
                d()
                result.append('d')
                temp = 'd'
            else :
                D()
                result.append('D')
                temp = 'D'
            L()
            result.append('L')
            r()
            result.append('r')
            B()
            result.append('B')
            B()
            result.append('B')
            l()
            result.append('l')
            R()
            result.append('R')
            if temp == 'd' :
                d()
                result.append('d')
            else :
                D()
                result.append('D')
            B()
            result.append('B')
            B()
            result.append('B')
        elif color[2][0][2]==color[2][1][2]==color[2][2][2]==color[0][1][1] :
            D()
            result.append('D')
            D()
            result.append('D')
            R()
            result.append('R')
            R()
            result.append('R')
            if color[2][1][1]==color[3][2][1] :
                D()
                result.append('D')
                temp = 'D'
            else :
                d()
                result.append('d')
                temp = 'd'
            B()
            result.append('B')
            f()
            result.append('f')
            R()
            result.append('R')
            R()
            result.append('R')
            b()
            result.append('b')
            F()
            result.append('F')
            if temp == 'D' :
                D()
                result.append('D')
            else :
                d()
                result.append('d')
            R()
            result.append('R')
            R()
            result.append('R')
        elif color[2][0][2]==color[2][1][2]==color[2][2][2]==color[2][1][1] :
            L()
            result.append('L')
            L()
            result.append('L')
            if color[3][2][1]==color[0][1][1] :
                d()
                result.append('d')
                temp = 'd'
            else :
                D()
                result.append('D')
                temp = 'D'
            b()
            result.append('b')
            F()
            result.append('F')
            L()
            result.append('L')
            L()
            result.append('L')
            B()
            result.append('B')
            f()
            result.append('f')
            if temp == 'd' :
                d()
                result.append('d')
            else :
                D()
                result.append('D')
            L()
            result.append('L')
            L()
            result.append('L')
        elif color[2][0][2]==color[2][1][2]==color[2][2][2]==color[5][1][1] :
            D()
            result.append('D')
            F()
            result.append('F')
            F()
            result.append('F')
            if color[3][1][1]==color[0][1][0] :
                D()
                result.append('D')
                temp = 'D'
            else :
                d()
                result.append('d')
                temp = 'd'
            l()
            result.append('l')
            R()
            result.append('R')
            F()
            result.append('F')
            F()
            result.append('F')
            L()
            result.append('L')
            r()
            result.append('r')
            if temp == 'D' :
                D()
                result.append('D')
            else :
                d()
                result.append('d')
            F()
            result.append('F')
            F()
            result.append('F')
    elif color[5][0][0]==color[5][0][1]==color[5][0][2] and not color[0][0][0]==color[0][1][0]==color[0][2][0] and not color[3][2][0]==color[3][2][1]==color[3][2][2] and not color[2][0][2]==color[2][1][2]==color[2][2][2] :
        if color[5][0][0]==color[5][0][1]==color[5][0][2]==color[3][1][1] :
            D()
            result.append('D')
            D()
            result.append('D')
            B()
            result.append('B')
            B()
            result.append('B')
            if color[5][1][1]==color[0][1][0] :
                d()
                result.append('d')
                temp = 'd'
            else :
                D()
                result.append('D')
                temp = 'D'
            L()
            result.append('L')
            r()
            result.append('r')
            B()
            result.append('B')
            B()
            result.append('B')
            l()
            result.append('l')
            R()
            result.append('R')
            if temp == 'd' :
                d()
                result.append('d')
            else :
                D()
                result.append('D')
            B()
            result.append('B')
            B()
            result.append('B')
        elif color[5][0][0]==color[5][0][1]==color[5][0][2]==color[0][1][1] :
            D()
            result.append('D')
            R()
            result.append('R')
            R()
            result.append('R')
            if color[2][1][1]==color[3][2][1] :
                D()
                result.append('D')
                temp = 'D'
            else :
                d()
                result.append('d')
                temp = 'd'
            B()
            result.append('B')
            f()
            result.append('f')
            R()
            result.append('R')
            R()
            result.append('R')
            b()
            result.append('b')
            F()
            result.append('F')
            if temp == 'D' :
                D()
                result.append('D')
            else :
                d()
                result.append('d')
            R()
            result.append('R')
            R()
            result.append('R')
        elif color[5][0][0]==color[5][0][1]==color[5][0][2]==color[2][1][1] :
            d()
            result.append('d')
            L()
            result.append('L')
            L()
            result.append('L')
            if color[3][2][1]==color[0][1][1] :
                d()
                result.append('d')
                temp = 'd'
            else :
                D()
                result.append('D')
                temp = 'D'
            b()
            result.append('b')
            F()
            result.append('F')
            L()
            result.append('L')
            L()
            result.append('L')
            B()
            result.append('B')
            f()
            result.append('f')
            if temp == 'd' :
                d()
                result.append('d')
            else :
                D()
                result.append('D')
            L()
            result.append('L')
            L()
            result.append('L')
        elif color[5][0][0]==color[5][0][1]==color[5][0][2]==color[5][1][1] :
            F()
            result.append('F')
            F()
            result.append('F')
            if color[3][1][1]==color[0][1][0] :
                D()
                result.append('D')
                temp = 'D'
            else :
                d()
                result.append('d')
                temp = 'd'
            l()
            result.append('l')
            R()
            result.append('R')
            F()
            result.append('F')
            F()
            result.append('F')
            L()
            result.append('L')
            r()
            result.append('r')
            if temp == 'D' :
                D()
                result.append('D')
            else :
                d()
                result.append('d')
            F()
            result.append('F')
            F()
            result.append('F')

elif not color[3][2][0]==color[3][2][1]==color[3][2][2] and not color[5][0][0]==color[5][0][1]==color[5][0][2] and not color[0][0][0]==color[0][1][0]==color[0][2][0] and not color[2][0][2]==color[2][1][2]==color[2][2][2] and ((color[3][2][1]==color[5][1][1] and color[5][0][1]==color[3][1][1]) or (color[3][2][1]==color[2][1][1] and color[2][1][2]==color[3][1][1]) or (color[3][2][1]==color[0][1][1] and color[0][1][0]==color[3][1][1])):      
    if color[3][2][1]==color[5][1][1] and color[5][0][1]==color[3][1][1] :
        F()
        result.append('F')
        F()
        result.append('F')
        if color[3][1][1]==color[0][1][0] :
            D()
            result.append('D')
            temp = 'D'
        else :
            d()
            result.append('d')
            temp = 'd'
        l()
        result.append('l')
        R()
        result.append('R')
        F()
        result.append('F')
        F()
        result.append('F')
        L()
        result.append('L')
        r()
        result.append('r')
        if temp == 'D' :
            D()
            result.append('D')
        else :
            d()
            result.append('d')
        F()
        result.append('F')
        F()
        result.append('F')
    elif color[3][2][1]==color[2][1][1] and color[2][1][2]==color[3][1][1] :
        F()
        result.append('F')
        F()
        result.append('F')
        if color[3][1][1]==color[0][1][0] :
            D()
            result.append('D')
            temp = 'D'
        else :
            d()
            result.append('d')
            temp = 'd'
        l()
        result.append('l')
        R()
        result.append('R')
        F()
        result.append('F')
        F()
        result.append('F')
        L()
        result.append('L')
        r()
        result.append('r')
        if temp == 'D' :
            D()
            result.append('D')
        else :
            d()
            result.append('d')
        F()
        result.append('F')
        F()
        result.append('F')
    elif color[3][2][1]==color[0][1][1] and color[0][1][0]==color[3][1][1] :
        R()
        result.append('R')
        R()
        result.append('R')
        if color[2][1][1]==color[3][2][1] :
            D()
            result.append('D')
            temp = 'D'
        else :
            d()
            result.append('d')
            temp = 'd'
        B()
        result.append('B')
        f()
        result.append('f')
        R()
        result.append('R')
        R()
        result.append('R')
        b()
        result.append('b')
        F()
        result.append('F')
        if temp == 'D' :
            D()
            result.append('D')
        else :
            d()
            result.append('d')
        R()
        result.append('R')
        R()
        result.append('R')

if color[3][2][0]==color[3][2][1]==color[3][2][2]==color[2][1][1] :
    D()
    result.append('D')
elif color[3][2][0]==color[3][2][1]==color[3][2][2]==color[0][1][1] :
    d()
    result.append('d')
elif color[3][2][0]==color[3][2][1]==color[3][2][2]==color[5][1][1] :
    D()
    result.append('D')
    D()
    result.append('D')

print(result)
