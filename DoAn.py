import pygame
import random, time,os
import queue
# Khởi tạo pygame()
pygame.init()
# Định nghĩa các màu
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
#Khởi tạo màn hình width and height, background
size = (500, 500)
screen = pygame.display.set_mode(size)
screen.fill(WHITE)
#Tựa đề 
pygame.display.set_caption("Traffic racing")
#Biến done=True khi nhấn vào dấu "X" tắt màn hình
done = False
AmountOfImpediment=0 #Biến chứa số lượng vật cản
Impediment=[] #List chứa tọa độ vật cản
AmountOfGasStation=0 #Biến chứa số lượng cây căng
GasStation=[] #List chứa tọa độ cây xăng
AmountOfGas=0 #Số lượng lít xăng
Destination=[] # Vị trí đích đến
Car=[]# vị trí xe
# hình ảnh
GasStationImage=pygame.transform.scale(pygame.image.load(os.path.join('E:5.3\AI\đồ án thực hành\Gas.PNG')),(38,38))#Hình ảnh cây xăng
FlagImage=pygame.transform.scale(pygame.image.load(os.path.join('E:5.3\AI\đồ án thực hành\Vietnam.PNG')),(38,38)) #Hình ảnh lá cờ đích đến
MotoBikeImage=pygame.transform.scale(pygame.image.load(os.path.join('E:5.3\AI\đồ án thực hành\Motorbike.PNG')),(38,38))

#Đọc file load lên tất cả lít xăng, địa điểm chứa cây xăng, vật cản.
f=open('E:5.3\AI\đồ án thực hành\DoAn.txt','r+')
Data=f.readlines()
AmountOfGas=int(Data[0])
for i in range(1,len(Data)):    
    if(Data[i].strip().upper()=='VAT CAN'):
        AmountOfImpediment=int(Data [i+1])#Biến chứa số lượng cây căng
        for j in range(i+2,len(Data)):
            if Data[j].upper().strip() !='CAY XANG':
                Impediment.append(Data[j].strip().split())
            else:
                break
    if(Data[i].upper().strip()=='CAY XANG'):
        AmountOfGasStation=int(Data[i+1])
        for j in range(i+2,len(Data)):
            if Data[j].upper().strip() !='VAT CAN' and Data[j].upper().strip() !='DICH DEN':
                GasStation.append(Data[j].strip().split())
            else:
                break
    if(Data[i].upper().strip()=='DICH DEN'):
        Destination.append(Data[i+1].strip().split())
        
    if (Data[i].upper().strip()=='XE'):
        Car.append(Data[i+1].strip().split())
        break
    graph= [[0,1,2,3,4,5,6,7,8,9], 
    [0,1,2,3,4,5,6,7,8,9],
    [0,1,2,3,4,5,6,7,8,9],
    [0,1,2,3,4,5,6,7,8,9],
    [0,1,2,3,4,5,6,7,8,9],
    [0,1,2,3,4,5,6,7,8,9],
    [0,1,2,3,4,5,6,7,8,9],
    [0,1,2,3,4,5,6,7,8,9],
    [0,1,2,3,4,5,6,7,8,9],
    [0,1,2,3,4,5,6,7,8,9]]
    def BFS(graph,star):
        for AmountOfGas in Data:
            if Car+1:
                AmountOfGas-1
                print(AmountOfGas)

    #-------------------------- BFS -----------------
    #graph={ 0:[0,0], 1:[1,1], 2:[1,2], 3:[3,3], 4:[4,4], 5:[5,5], 6:[6,6], 7[7,7], 8[8,8], 9[9,9] }
 
f.close()
print(Destination)
print(GasStation)
#print(Car)
while not done:
    #Khi gặp sự kiện nhấn vào dấu "X" sẽ thoát vòng lặp
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #Vẽ bản đồ tại vị trí x=50, y=50
    #Bản đồ với chiều dài là 10 ô vuông
    for i in range(10):
        #Chiều rộng 10 ô vuông
        for j in range(10):
            #Vẽ các khối vuông có chiều dài 40, chiều rộng 40, khung viền là 1
            pygame.draw.rect(screen, BLACK, [50 + 40 * j, 50 + 40 * i, 40, 40], 1)

    #tô màu những ô là vật cản
    for i in range(len(Impediment)):
        pygame.draw.rect(screen, GRAY, [50 + 40 * int(Impediment[i][1]), 50 + 40 * int(Impediment[i][0]), 40, 40])

    for i in range(len(GasStation)):
        screen.blit(GasStationImage,(50 + 40 * int(GasStation[i][1]), 50 + 40 * int(GasStation[i][0])))
    #màn hình lá cờ
    screen.blit(FlagImage,(50 + 40 * int(Destination[0][1]), 50 + 40 * int(Destination[0][0])))
    #màn hình xe
    screen.blit(MotoBikeImage,(50 + 40 * int(Car[0][1]), 50 + 40 * int(Car[0][0])))
    #Cập nhật lại vị trí trên màn hình pygame
    pygame.display.flip()
#Đóng chương trình
pygame.quit()
