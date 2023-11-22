1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]

lst =  [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]

def flatten_list(lst):  
     flattened = []  

     for item in lst:  
         if isinstance(item, list): # isinstane fonksiyonu ile döndürdüğümüz item liste mi değil mi bunu kontrol ediyoruz.
             flattened.extend(flatten_list(item))  #eğer liste ise yazdığımız fonksiyon içinde tekrar kullanıp liste olmayana kadar çıkartıyoruz.
        
         else:
             flattened.append(item)  #liste değilse flattened listesi içine ekliyoruz.

     return flattened
    

outputlist = flatten_list(lst)
print(outputlist)

2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]

l = [[1, 2], [3, 4], [5, 6, 7]]

def new_list(l):
    for i in l:
        i.reverse()
    l.reverse()
    return(l)
