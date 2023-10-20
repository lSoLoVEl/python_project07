# character in stiring has index number
# 01234567890123
infoA = 'Hello SAU 2023'
#43240987654321 ติด -

print(infoA[6]) #s
print(infoA[-8]) #s

#เข้าถึงตัวอักษรหลายๆ ตัวใน String เราจะใช้วิธี Slicing ด้วย index number
#SAU
print(infoA[6:9]) #ซ้ายไปขวา
print(infoA[-8:-5]) #ขวาไปซ้าย

# o SAU 20
print(infoA[4:12])


#string Method
print(infoA.upper())
print(infoA.lower())
print(infoA.capitalize())
print(infoA.title())
print(infoA.count('SAU'))
print(infoA.isdigit())
print(infoA.islower())
infoB = infoA.replace('SAU','IOT')
print(infoB)
print(infoB.replace('Hello','Hi...'))

#String String
print(len(infoA))

print('SAU',35) #SAU 35
print('SAU'+str(35)) #SAU35
print('SAU',35,sep='') #SAU35

