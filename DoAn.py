import heapq
import sys
import pygame
import random,os
from termcolor import colored
pygame.init()
# Định nghĩa các màu
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
#Khởi tạo màn hình width and height, background
size = (500, 500)
screen = pygame.display.set_mode(size)
#background color
screen.fill(WHITE)
#Tựa đề 
pygame.display.set_caption("Traffic racing")
button = pygame.Rect(0, 100, 200, 200)
#Biến done=True khi nhấn vào dấu "X" tắt màn hình
done=False
AmountOfImpediment=0 #Biến chứa số lượng vật cản
Impediment=[] #List chứa tọa độ vật cản
AmountOfGasStation=0 #Biến chứa số lượng cây căng
GasStation=[] #List chứa tọa độ cây xăng
AmountOfGas=0 #Số lượng lít xăng
Destination=[] # Vị trí đích đến
Car=[]# vị trí xe
 #Hình ảnh cây xăng
GasStationImage=pygame.transform.scale(pygame.image.load(os.path.join('E:5.3\AI\đồ án thực hành\Gas.PNG')),(40,40))
#Hình ảnh lá cờ đích đến
FlagImage=pygame.transform.scale(pygame.image.load(os.path.join('E:5.3\AI\đồ án thực hành\Flag.PNG')),(40,40)) 
#Hình ảnh nơi xuất phát
MotoBikeImage=pygame.transform.scale(pygame.image.load(os.path.join('E:5.3\AI\đồ án thực hành\Motorbike.PNG')),(40,40))

#load file txt lên tất cả lít xăng, địa điểm chứa cây xăng, vật cản.
f=open('E:5.3\AI\đồ án thực hành\map.txt','r+')
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
f.close()
print(Destination)
print(GasStation)
print(Car)
print(Impediment)
#  BINDING
while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done =True
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
class PriorityQueue:
  def __init__(self):
    self.queue = []
  
  def push(self, value, label):
    heapq.heappush(self.queue, (value, label))
  
  def pop(self):
    return heapq.heappop(self.queue)
  
  def is_empty(self):
    # print(self.q)
    return len(self.queue) == 0

class Grid:
  def __init__(self, A, walls):
    self.n = len(A)
    self.m = len(A[0])
    self.A = A
    self.walls = walls

  def in_bounds(self, p):
    x,y  = p
    return x >=0 and y>=0 and x<self.n and y<self.m

  def passable(self, p):
    for wall_pos in self.walls:
      if wall_pos == p:
        return False
    return True
  
  def neighbors(self, p):
    x, y = p
    neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    # print(neighbors)
    valid_neighbors = []
    for pos in neighbors:
      if self.in_bounds(pos) and self.passable(pos):
        valid_neighbors.append(pos)

    # print(valid_neighbors)
    return valid_neighbors

  def draw(self, show_weight=False, path=[]):
    #Bản đồ với chiều dài là 10 ô vuông
      for i in range(self.n):
        #Chiều rộng 10 ô vuông
         for j in range(self.m):
            if(i,j) in path:
                        #màn hình lá cờ
              screen.blit(FlagImage,(50 + 40 * int(Destination[0][1]), 50 + 40 * int(Destination[0][1])))
                             #màn hình xe
              screen.blit(MotoBikeImage,(50 + 40 * int(Car[0][1]), 50 + 40 * int(Car[0][1])))
 #ve duong di
              pygame.draw.rect(screen,BLACK,[50+40*j,50+40*i,40,40])
    
            elif self.passable((i,j)):
              pygame.draw.rect(screen,BLACK,[50+40*j,50+40*i,40,40],1)
            else:
              pygame.draw.rect(screen,GRAY,[50+40*j,50+40*i,40,40])
                    #Cập nhật lại vị trí trên màn hình pygame4
                    # 
                    # 
            pygame.display.flip()



class SearchAlg:
  def __init__(self, grid, start, goal):
    self.grid = grid
    self.start = start
    self.goal = goal
    self.came_from = {}

  def trace_path(self):
    curr =  self.goal
    path = []
    while curr != self.start:
      path.append(curr)
      curr = self.came_from[curr]
    
    path.append(self.start)
    path.reverse()
    return path

  def heuristic(self,p1, p2, heu_type="Manhanttan"):
    if heu_type == "Manhanttan":
      return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
    elif heu_type == "Euclidean":
      
      pass
    
    return sys.maxsize

  def aStar(self):
    open_list = PriorityQueue()
    gScore = {self.start: 0}  # lưu giá trị G của mỗi đỉnh
    fScore_start = self.heuristic(self.start, self.goal) # f = g + h = 0 + heuristic(start, goal)
    open_list.push(fScore_start, self.start) # push(value, label_node)
    self.came_from = {} # dùng để lưu dấu đường đi

    while not open_list.is_empty():
        curr = open_list.pop()  # lấy đỉnh curr có fScore nhỏ nhất
        # print(curr) # trả về (curr_fScore, curr_node)
        curr_fScore, curr_node = curr
        if curr_node == self.goal:
            print(colored("Finded aStar!", "yellow"))
            path = self.trace_path()
            self.grid.draw(path=path)
            return True
        for next_node in self.grid.neighbors(curr_node):
            new_g = gScore[curr_node] + self.grid.A[next_node[0]][next_node[1]]  # next_g = curr_g + A[curr_node->next_node]
            if (next_node not in gScore) or (new_g < gScore[next_node]): 
                gScore[next_node] = new_g
                fScore_next_node = gScore[next_node] + self.heuristic(next_node, self.goal)  # Khác với UCS là có thêm hàm Heuristic ở đây!
                open_list.push(fScore_next_node, next_node)
                self.came_from[next_node] = curr_node

        print(f"f{curr_node}: f{open_list.queue}")
    
    print(colored("Khong tim thay duong di", "red"))
    return False

  def DFS(self):
    open_list = PriorityQueue()
    gScore = {self.start: 0}  # lưu giá trị G của mỗi đỉnh
    fScore_start =self.start #giá trị node
    open_list.push(fScore_start, self.start) # push(value, label_node)
    self.came_from = {} # dùng để lưu dấu đường đi

    while not open_list.is_empty():
        curr = open_list.pop()  # lấy đỉnh curr có fScore nhỏ nhất
        # print(curr) # trả về (curr_fScore, curr_node)
        curr_fScore, curr_node = curr
        if curr_node == self.goal:
            print(colored("Finded DFS!", " yellow "))
            path = self.trace_path()
            self.grid.draw(path=path)
            return True
        for next_node in self.grid.neighbors(curr_node):
            new_g =  self.grid.A[next_node[0]][next_node[1]]  # next_g = A[curr_node->next_node] giá trị của node
            if (next_node not in gScore): 
                gScore[next_node] = new_g
                fScore_next_node = gScore[next_node]
                open_list.push(fScore_next_node, next_node)
                self.came_from[next_node] = curr_node

        print(f"{curr_node}: f{open_list.queue}")
    
    print(colored("Khong tim thay duong di", "red"))
    return False

  def UCS(self):
    open_list = PriorityQueue()
    gScore = {self.start: 0}  # lưu giá trị G của mỗi đỉnh
    fScore_start = self.heuristic(self.start, self.goal) # f = g + h = 0 + heuristic(start, goal)
    open_list.push(fScore_start,self.start) # push(value, label_node)
    self.came_from = {} # dùng để lưu dấu đường đi

    while not open_list.is_empty():
        curr = open_list.pop()  # lấy đỉnh curr có fScore nhỏ nhất
        #print(curr) # trả về (curr_fScore, curr_node)
        curr_fScore, curr_node = curr
        if curr_node == self.goal:
            print(colored("Finded UCS!", "red"))
            path = self.trace_path()
            self.grid.draw(path=path)
            return True
        for next_node in self.grid.neighbors(curr_node):
            # next_g = curr_g + A[curr_node->next_node]
            new_g = gScore[curr_node] + self.grid.A[next_node[0]][next_node[1]]
            if (next_node not in gScore) or (new_g < gScore[next_node]): 
                gScore[next_node] = new_g
                fScore_next_node = gScore[next_node]
                open_list.push(fScore_next_node, next_node)
                self.came_from[next_node] = curr_node

        print(f"f{curr_node}: f{open_list.queue}")
    
    print(colored("Khong tim thay duong di.", "red"))
    return False

#toa do vat can
VatCan=[ (0,3),(1,5),(2,2),(2,5),(3,1),(3,7),(4,4),(5,1),(5,6),(6,2),(6,3),(7,5),(7,6),(7,8),(8,0),(8,3),(8,5),(9,4)]
#vi tri xuat phat
start=(int(Car[0][1]),int(Car[0][1]))
#noi ket thuc
end=(int(Destination[0][1]),int (Destination[0][1]))
#toa do trong game
A =[[1,1,1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1,1,1]]

g = Grid(A,VatCan)

search = SearchAlg(g,start,end)
g.draw()
search.UCS()
""" 
search.UCS()
search.DFS() """

#Đóng chương trình
pygame.quit()

