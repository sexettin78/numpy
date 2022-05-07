import numpy as np
x = np.array([1,2,3,4])
print(type(x)) #x'in tipi 
z = np.zeros((10)) #10 tane 0'dan oluşan bir array oluşturur
v = np.ones((10)) #10 tane 1'den oluşan bir array oluşturur
g = np.ones((10))*6 #10 tane 6'dan oluşan bir array oluşturur
i=0
zuzu = np.arange(10,50,5) #5'er 5'er artan bir array
ondalik = np.arange(0,2,0.2)#0.2 arta arta devam eden dize
lin=np.linspace(0,4,12) #0 ile 4 arasında olan 12 tane sayı koy diyoruz
rands = np.random.rand(6,7)  #rastgele sayılardan oluşan 6 satır 7 sütün
goz =np.eye(5) #5 satır 5 sütünlu birim matrix oluşturur
np.random.randint(1,50,15) #1'den 50'ye kadar 15 tane rastgele sayı oluşturur
#zuzu.reshape(6,4) #dizeyi 6 satır 4 sütunlu hale getirir
#rands.reshape(2,3,4) #dizeyi 2 tane 3 satırlı 4 sütunlu array oluşturur
x.max() #dizedeki en yüksek sayı
x.min() #dizideki en düşük sayı
x.argmax() #dizedeki en yüksek sayının indexi
x.argmin() #dizideki en düşük sayının indexi
x.ravel() #x'i eski haline getirir
# *2 iki ile çarparken **2 karesini alır
x[1:4] #1^den 4 e kadar olan indexler
#np.hstack((x,v)) #x ile v'yi yatay olarak birleştirir
#np.vstack((x,v)) #x ile v'yi dikey olarak (alt alta) birleştirir
#np.concatenate((a,b),axis=0) aşağı doğru birleştirir. axis=1 yaparsan yan yana birleştirir eğer axis 1 hata verirse b.T yaparsın
xtopla = x.sum() #tüm elemanları topladık
x.sum(axis = 1) #aşağı doğru toplar ama bizim x tek boyutlu dize olduğu için hata verecektir. aşağı doğru toplayamadığı için
x.mean() #x dizesinin ortalamasını bulur
np.median(x) #x'in medianını gösterir
np.std(x) #x'in standart sapmasını gösterir
np.var(x) #x'in varyasyonunu gösterir
kopya = x.copy() #x'i kopyalar
np.unique(x) #x'in tek gecen değerlerini sıralar
print(xtopla)
for i in range(0,4):
    print(x[i])