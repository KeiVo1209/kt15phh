#Nhập mảng 2 chiều
m=int(input("nhap so hang:"))
n=int(input("nhap so cot:"))
A=[]
for i in range (m):
    r=[]
    for j in range (n):
        x=int(input())
        r.append(x)
    A.append(r)
#Nhập mảng 2 chiều vippro
m = int(input("nhap so hang: "))
n = int(input("nhap so cot: "))
A = [[int(input()) for j in range(n)] for i in range(m)]

#Xuất mảng 2 chiều
for i in range(m):
    for j in range(n):
        print(A[i][j], end=" ")
    print() 
#Xuất mẩng 2 chiều siêu cấp ultra viprooooo
print(A)

#Tìm các phần tử lớn hơn 0 (bé hơn 0 thì đổi dấu > thành <, với đổi dòng )
print("Cac phan tu lon hon 0:")
for i in range(m):
    for j in range(n):
        if (A[i][j]>0): print(A[i][j])
#Cách tìm phần tử lớn/bé hơn 0 siêu cấp vippro( nhớ chú ý dấu >< khi so sánh với 0)
B= [A[i][j] for i in range(m) for j in range(n) if A[i][j] > 0]
print("Cac phan tu lon hon 0 la:", B )

#Tìm số lớn nhất/ nhỏ nhất trong mảng 2 chiều
Max = max(max(A[i]) for i in range(m)) # tìm số lớn nhất trong mảng 2 chiều bằng cách tìm số lớn nhất trong mỗi hàng
Min = min(min(A[i]) for i in range(m)) # tìm số nhỏ nhất trong mảng 2 chiều bằng cách tìm số nhỏ nhất trong mỗi hàng
print("So lon nhat la:", Max)
print("So nho nhat la:", Min)
 #Hoặc nếu thích thì duyệt qua từng thằng A[i][j] rồi tìm gtri lớn/ nhỏ nhất cũng đc

#TÌM SỐ NGUYÊN TỐ, SỐ CHÍNH PHƯƠNG, SỐ HOÀN HẢO( từ trên xuống dưới lần lượt là 3 ctr con kt ngto, chphuong,hhao)
#1:Viết 1 một chương trình con kiểm tra các số trong mảng xem số nào thỏa điều kiện 
#2:Duyệt qua từng phần tử trong mảng, nếu thỏa điều kiện ctr con thì push ptu đó vào 1 mảng khác (tạm gọi là C)
#3: In ra mảng C
#Ctr con kt số ng tố
def ktngto(n):
  if n < 2:
    return 0
  for i in range(2, int(n**0.5) + 1):
    if (n % i == 0):
      return 0
  return 1
    
#Ctr con kt số chính phương
def ktchphuong(n):
  jk = n ** 0.5
  if int(jk) == jk:
    return 1
  else:
    return 0
      
# Ctr con kt số hoàn hảo
def kthhao(n):
  sum = 0
  for i in range(1, n // 2 + 1):
    if n % i == 0:
      sum += i
  if sum == n:
    return 1
  else:
    return 0


#Dòng này để duyệt qua các ptu của A coi tk nào thỏa điều kiện ctr con=> push mấy tk thỏa đk vào 1 mảng C=> print C
C= [A[i][j] for i in range(m) for j in range(n) if ktngto(A[i][j])==1]
print("Trong cac so",A,"co cac so nguyen to la:", C )
#thay chỗ "ktngto" thành "ktchphuong", "kthhao" để chọn ra số chphuong, hhao..
    





        
            
            
