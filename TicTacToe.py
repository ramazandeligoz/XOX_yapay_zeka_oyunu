import random 
print('Hoşgeldiniz') 

oyunbitti=False ##Oyun bittiğinde bu değeri true yapacaz
sira= True      ##Sıranın oyuncuda olup olmadığını anlamak için kullandım
yapayzeka= False ##Sıranın Yapay zekada olup olmadığını anlamak için kullandım
beraberebitti=False ## Oyun berabere bittiğinde True Yapacaz ve oyunu bitireceğiz.

satir1 = ['-','-','-'] ## Oyundaki yerleri 3 liste yani satır olarak ayırdım
satir2 = ['-','-','-']
satir3 = ['-','-','-']

s1 = [0,0,0] ##BU LİSTENİN AMACI BİRAZ KARIŞIK GELEBİLİR BU BİZİM GÖRÜNMEYEN LİSTEMİZ ASLA OYUNCU BU LİSTEYİ GÖRMEYECEK ANCAK
s2 = [0,0,0] ##BÜTÜN İŞLEMLERİ BU LİSTE ÜZERİNDEN YAPACAĞIZ. 
s3 = [0,0,0] ##HER 'O' İŞARETİ 3 PUAN VE HER 'X' İŞARETİ 5 PUAN OLARAK VERDİM



def sonuc(): ## Sonuç fonksiyonu satırları yazdırıyor. Doğal olarak oyunun son halini bize gösteriyor.
    print (satir1)
    print (satir2)
    print (satir3)
    print('---------')


def kontrol():## Kontrol Fonksiyonu ise hamleler sonrası oyununun bitip bitmediğini kontrol ediyor.
    global oyunbitti,a,b,c,d,e,f,g,h,beraberebitti
    a = int(s1[0] + s1[1] + s1[2])##birinci satır toplamı
    b = int(s2[0] + s2[1] + s2[2])##ikinci satır toplamı
    c = int(s3[0] + s3[1] + s3[2])##üçüncü satır toplamı
    d = int(s1[0] + s2[0] + s3[0])##birinci sütun toplamı
    e = int(s1[1] + s2[1] + s3[1])##ikinci sütun toplamı
    f = int(s1[2] + s2[2] + s3[2])##üçüncü sütun toplamı
    g = int(s1[0] + s2[1] + s3[2])##çarpraz toplam
    h = int(s1[2] + s2[1] + s3[0])## ikinci çarpraz toplam
    if a == 9 or b == 9 or c == 9 or d == 9 or e == 9 or f == 9 or g == 9 or h == 9 :
        oyunbitti= True ##yukarıdaki herhangi bir değer 9 olursa 'O' yani oyuncu kazanır. oyun biter
        print('Kazandınız!!')
    elif a == 15 or b == 15 or c == 15 or d == 15 or e == 15 or f == 15 or g == 15 or h==15:
        oyunbitti=True ## toplam 15 olursa 5-5-5 olacağından bilgisayar kazanır
        print('Kaybettiniz :(')
    elif (a+b+c)==35:
        if beraberebitti== False: ## eğer iki tarafta kazanamazsa sütunların genel toplamı 35 olur (oyuncu yani o başladığı için)
            oyunbitti=True
            print('Berabere!')
            beraberebitti = True ## bu değişkenin amacı ekrana sadece birkez yazıyı yazdırması 
        
    
        

def yapay():
    global sira,yapayzeka,satir1,satir2,satir3,sar,sur,a,b,c,d,e,f,g,h,s1,s2,s3
    yapayzeka=False##hamle sonrası sırayı yapay zekadan oyuncuya devredecek 
    sira=True
    
    if oyunbitti == False:##oyun bitmemişse döngü çalışır
        if a == 10:## a değeri 10 ise boş kısma x koyar.
            if s1[0] == 0:## boş kısmı tarar
                s1[0]=5
                satir1[0]='X'
                sonuc()
                
            elif s1[1]==0:##boş kısmı tarar
                s1[1] = 5
                satir1[1] = 'X'
                sonuc()
            elif s1[2]==0:#boş kısmı tarar
                s1[2] = 5
                satir1[2] = 'X'
                sonuc()

        elif b == 10:
            if s2[0] == 0:
                s2[0]=5
                satir2[0]='X'
                sonuc()
            elif s2[1]==0:
                s2[1] = 5
                satir2[1] = 'X'
                sonuc()
            elif s2[2]==0:
                s2[2] = 5
                satir2[2] = 'X'
                sonuc()

        elif c == 10:
            if s3[0] == 0:
                s3[0]=5
                satir3[0]='X'
                sonuc()
            elif s3[1]==0:
                s3[1] = 5
                satir3[1] = 'X'
                sonuc()
            elif s3[2]==0:
                s3[2] = 5
                satir3[2] = 'X'
                sonuc()

        elif d == 10:
            if s1[0] == 0:
                s1[0]=5
                satir1[0]='X'
                sonuc()
            elif s2[0]==0:
                s2[0] = 5
                satir2[0] = 'X'
                sonuc()
            elif s3[0]==0:
                s3[0] = 5
                satir3[0] = 'X'
                sonuc()

        elif e == 10:
            if s1[1] == 0:
                s1[1]=5
                satir1[1]='X'
                sonuc()
            elif s2[1]==0:
                s2[1] = 5
                satir2[1] = 'X'
                sonuc()
            elif s3[1]==0:
                s3[1] = 5
                satir3[1] = 'X'
                sonuc()

        elif f == 10:
            if s1[2] == 0:
                s1[2]=5
                satir1[2]='X'
                sonuc()
            elif s2[2]==0:
                s2[2] = 5
                satir2[2] = 'X'
                sonuc()
            elif s3[2]==0:
                s3[2] = 5
                satir3[2] = 'X'
                sonuc()

        elif g == 10:
            if s1[0] == 0:
                s1[0]=5
                satir1[0]='X'
                sonuc()
            elif s2[1]==0:
                s2[1] = 5
                satir2[1] = 'X'
                sonuc()
            elif s3[2]==0:
                s3[2] = 5
                satir3[2] = 'X'
                sonuc()

        elif h == 10:
            if s1[2] == 0:
                s1[2]=5
                satir1[2]='X'
                sonuc()
            elif s2[1]==0:
                s2[1] = 5
                satir2[1] = 'X'
                sonuc()
            elif s3[0]==0:
                s3[0] = 5
                satir3[0] = 'X'
                sonuc()
        


        elif a == 6:## eğer değer 6 ya eşit ise boş kısma X koyarak savunma yapar.
            
            if s1[0] == 0:##boş kısım olup olmadığını anlamak için
                s1[0]=5
                satir1[0]='X'
                sonuc()
            elif s1[1]==0:##boş kısım olup olmadığını anlamak için
                s1[1] = 5
                satir1[1] = 'X'
                sonuc()
            elif s1[2]==0:##boş kısım olup olmadığını anlamak için
                s1[2] = 5
                satir1[2] = 'X'
                sonuc()

        elif b == 6:
            if s2[0] == 0:
                s2[0]=5
                satir2[0]='X'
                sonuc()
            elif s2[1]==0:
                s2[1] = 5
                satir2[1] = 'X'
                sonuc()
            elif s2[2]==0:
                s2[2] = 5
                satir2[2] = 'X'
                sonuc()

        elif c == 6:
            if s3[0] == 0:
                s3[0]=5
                satir3[0]='X'
                sonuc()
            elif s3[1]==0:
                s3[1] = 5
                satir3[1] = 'X'
                sonuc()
            elif s3[2]==0:
                s3[2] = 5
                satir3[2] = 'X'
                sonuc()

        elif d == 6:
            if s1[0] == 0:
                s1[0]=5
                satir1[0]='X'
                sonuc()
            elif s2[0]==0:
                s2[0] = 5
                satir2[0] = 'X'
                sonuc()
            elif s3[0]==0:
                s3[0] = 5
                satir3[0] = 'X'
                sonuc()

        elif e == 6:
            if s1[1] == 0:
                s1[1]=5
                satir1[1]='X'
                sonuc()
            elif s2[1]==0:
                s2[1] = 5
                satir2[1] = 'X'
                sonuc()
            elif s3[1]==0:
                s3[1] = 5
                satir3[1] = 'X'
                sonuc()

        elif f == 6:
            if s1[2] == 0:
                s1[2]=5
                satir1[2]='X'
                sonuc()
            elif s2[2]==0:
                s2[2] = 5
                satir2[2] = 'X'
                sonuc()
            elif s3[2]==0:
                s3[2] = 5
                satir3[2] = 'X'
                sonuc()

        elif g == 6:
            if s1[0] == 0:
                s1[0]=5
                satir1[0]='X'
                sonuc()
            elif s2[1]==0:
                s2[1] = 5
                satir2[1] = 'X'
                sonuc()
            elif s3[2]==0:
                s3[2] = 5
                satir3[2] = 'X'
                sonuc()

        elif h == 6:
            if s1[2] == 0:
                s1[2]=5
                satir1[2]='X'
                sonuc()
            elif s2[1]==0:
                s2[1] = 5
                satir2[1] = 'X'
                sonuc()
            elif s3[0]==0:
                s3[0] = 5
                satir3[0] = 'X'
                sonuc()


        else:
            if s2[1] == 0:##Tam orta kısım boşsa X koyar kazanma olasılığı artar.
                s2[1] = 5
                satir2[1] = 'X'
                sonuc()
            else:##Tam ortadaki kısım dolu ise köşelere koyar kazanma olasılığı artar. random değer üreterek bu işi yapar
                sar = random.randint(1, 3)
                sur = random.randint(1, 3)
                sur -= 1
                if sar==2 or sur == 1 :
                    yapay()
                else:
                    if sar == 1:
                        if satir1[sur] == 'X' or satir1[sur] == 'O':
                            yapay()
                        else:
                            satir1[sur] = 'X'
                            s1[sur] = 5
                            sonuc()
                    elif sar == 2:
                        if satir2[sur] == 'X' or satir2[sur] == 'O':
                            yapay()
                        else:
                            satir2[sur] = 'X'
                            s2[sur] = 5
                            sonuc()
                    elif sar == 3:
                        if satir3[sur] == 'X' or satir3[sur] == 'O':
                            yapay()
                        else:
                            satir3[sur] = 'X'
                            s3[sur] = 5
                            sonuc()
        kontrol() 
                

    if oyunbitti==False:## sonucu yazdırır ve kontrol fonksiyonunu  çağırır
        istek()
    

def istek() :
    
    name = input()

    if name == '1' or name == '2' or name == '3' or name == '4' or name == '5' or name == '6' or name == '7' or name == '8' or name =='9' :

        global sira
        global yapayzeka
        sira =False
        yapayzeka= True


        if name == '1':
            if satir1[0]== 'O' or satir1[0]=='X':
               print ('Lütfen Boş Bir Yer Seçin !')
               istek()
            else:
                satir1[0]='O'
                s1[0]=3
                sonuc()
                kontrol()

        elif name == '2':
            if satir1[1]== 'O' or satir1[1]=='X':
               print ('Lütfen Boş Bir Yer Seçin !')
               istek()
            else:
                satir1[1]='O'
                s1[1]=3
                sonuc()
                kontrol()
        elif name == '3':
            if satir1[2]== 'O' or satir1[2]=='X':
               print ('Lütfen Boş Bir Yer Seçin !')
               istek()
            else:
                satir1[2]='O'
                s1[2]=3
                sonuc()
                kontrol()
        elif name == '4':
            if satir2[0]== 'O' or satir2[0]=='X':
               print ('Lütfen Boş Bir Yer Seçin !')
               istek()
            else:
                satir2[0]='O'
                s2[0]=3
                sonuc()
                kontrol()
        elif name == '5':
            if satir2[1]== 'O' or satir2[1]=='X':
               print ('Lütfen Boş Bir Yer Seçin !')
               istek()
            else:
                satir2[1]='O'
                s2[1]=3
                sonuc()
                kontrol()
        elif name == '6':
            if satir2[2]== 'O' or satir2[2]=='X':
               print ('Lütfen Boş Bir Yer Seçin !')
               istek()
            else:
                satir2[2]='O'
                s2[2]=3
                sonuc()
                kontrol()
        elif name == '7':
            if satir3[0]== 'O' or satir3[0]=='X':
               print ('Lütfen Boş Bir Yer Seçin !')
               istek()
            else:
                satir3[0]='O'
                s3[0]=3
                sonuc()
                kontrol()
        elif name == '8':
            if satir3[1]== 'O' or satir3[1]=='X':
               print ('Lütfen Boş Bir Yer Seçin !')
               istek()
            else:
                satir3[1]='O'
                s3[1]=3
                sonuc()
                kontrol()
        elif name == '9':
            if satir3[2]== 'O' or satir3[2]=='X':
               print ('Lütfen Boş Bir Yer Seçin !')
               istek()
            else:
                satir3[2]='O'
                s3[2]=3
                sonuc()
                kontrol()
    else:
            print('Hatalı Tuş')
            istek()

    if oyunbitti==False:
            yapay()
        

sonuc()

print('Sizin sıranız (O)')

istek()

print('Oyun Bitti')
