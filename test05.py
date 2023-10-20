#--------------------Tuple ข้อมูลหลายข้อมูล คนละชนิดได้ ซ้ำกันได้และมีลำดับ แต่แก้ไขไม่ได้ เพิ่มหรือลบก็ไม่ได้------------------------
#          0   1  2    3   4         5
my_tuple1=(10,20,True,10,'SAU',(20,'IOT'))
#         6   5   4   3   2        1    ติด-

#การเข้าถึงข้อมูลใน list เพื่อเอาข้อมูลมาใช้ 
#เข้าถึงทีละข้อมูล
print(my_tuple1[4])#SAU
print(my_tuple1[-2])#SAU
print(my_tuple1[5])#[20,'IOT']
print(my_tuple1[-1])#[20,'IOT']
print(my_tuple1[5][1]) # IOT
print(my_tuple1[-1][-1]) # IOT
#เข้าถึงทีละหลายข้อมูล
print(my_tuple1[1:4]) #20,True,10
print(my_tuple1[3:]) #10,'SAU',[20,'IOT']
print(my_tuple1[:3])  #10,20,True

#เข้าถึงทุกข้อมูล
for info in my_tuple1 :
    print(info, end=', ')

print()

# หากอยากจะแก้ไขข้อมูลใน Tuple ก็พอทำได้ แต่ต้องอ้อมหน่อย 
my_list = list(my_tuple1)
my_list[4] ='IOT'
my_tuple1 = tuple(my_list)
print(my_tuple1)

#Tuple Method
print(my_tuple1.count(10)) #2
print(my_tuple1.index('IOT')) 
my_tuple3 = (10,20,30,10,True)
print(len(my_tuple3))
print(min(my_tuple3))
print(max(my_tuple3))