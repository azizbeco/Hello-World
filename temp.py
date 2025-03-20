

# def times(x,y):
#     return x*y

# print(times(4,'no'))


# def kesishmalar(soz1,soz2):
#     res =[]
#     for x in soz1:
#         if x in soz2:
#             res.append(x)
    
#     return res

# num1=[1,2,3,4,5,8,9,10]
# num2=[2,3,5,6,8,10,9,7]

# print(kesishmalar(num1,num2))




# def hello():
#     x= 5
#     def inner():
#         x=4
#         print(x)
#     print(x)
#     inner()

# hello()


#      Global  x 
# z=5
# def global_change():
#     global z
#     z=4
#     print(z)

# global_change()
# print(z)




# nonlocal

# x=5
# def hello():
#     x=3
#     def inner():
#         nonlocal x
#         x=2
#     inner()
#     print(x)
# hello()
# print(x)

# all=0
# while True:
  
#     def count():
#         all
#     count()  

#     if all == 10:break
#     all+=1
    
# print(all)    
          






WIDTH,HEIGHT=5,5

playerX,playerY=3,3

def draw():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if x==playerX and y==playerY:
                print('|',end=' ')
            else:
                print('*' , end=' ')
        print()

def move(moveTo):
    global playerX,playerY
    if moveTo=='w' and playerY>0:
        playerY-=1
    elif moveTo=='s' and playerX < HEIGHT-1:
        playerY+=1
    elif moveTo=='a' and playerX > 0:
        playerX-=1
    elif moveTo=='d' and playerX < WIDTH-1:
        playerX+=1


while True:
    draw()
    moveTo=input("Qatga yuramiza")
    move(moveTo)



# shaxmat
# dolar ushlash
# lift

