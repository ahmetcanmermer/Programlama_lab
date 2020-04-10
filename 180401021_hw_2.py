import csv
import sys
def ortalama(liste):
    toplam = 0
    for i in range(0,len(liste)):
        toplam += liste[i]
    return int(toplam/len(liste))
def histo(liste):
    dict_1 = {}
    for item in liste:
        if(item in dict_1):
            dict_1[item] = dict_1[item]+1
        else:
            dict_1[item] = 1
    return dict_1
def bubble_sort(list_):
    n = len(list_)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if(list_[j]>list_[j+1]):
                temp = list_[j]
                list_[j] = list_[j+1]
                list_[j+1] = temp
    return list_
with open(sys.argv[1]+"input_hw_2.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=';')
    liste = []
    for line in csv_reader:
        liste.append(line)
aylar = []
for ay in range(0,len(liste)):
    aylar.append(str(liste[ay][3][5])+str(liste[ay][3][6]))
histogram = histo(aylar)
deger = []
for key,value in histogram.items():
    print(f"{key}. ay {value} kişi ayrıldı")
    deger.append(value)
bubble_sort(deger)
ortalama = ortalama(deger)
medyan = deger[len(deger)//2]
print(ortalama )
print(medyan)
with open(sys.argv[2]+"180401021_hw_2_output.txt","w") as txt_file:
    txt_file.write(f"ortalama={ortalama}\nmedyan={medyan}")
    
