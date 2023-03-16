#  _________________________________________
# |Genlerin Senfonisi Gen - Nota Algoritması|
# |_________________________________________|
# Versiyon 0.1 (09.12.2022)
# Yenilikler : Nota anahtarı alma ve çözümleme eklendi, nota anahtarına göre nota yapma eklendi, nota anahtarını kontrol etme sistemi eklendi.
# -----------------------------------------
# Versiyon 0.2 (13.12.2022)
# Yenilikler : Bemol ve diyez eklendi, ters nükleotidler sistemi kaldırıldı.
# -----------------------------------------
# Versiyon 0.3 (20.12.2022) 
# Yenilikler : P53 geninin bazı mRNA varyantları eklendi.
# -----------------------------------------
# Versioyon 0.4 (13.01.2023)
# Yenilikler : Bazı hatalar düzeltildi.
# -----------------------------------------
# Versiyon 0.4.4 (13.01.2023)
# Yenilikler : Gereksiz kodlar temizlendi, optimizasyon arttırıldı.
# -----------------------------------------
# Versiyon 0.4.5 (14.01.2023)
# Yenilikler : Küçük düzenlemeler ve iyileştirmeler yapıldı.
# -----------------------------------------
# Versiyon 0.5 (05.02.2023)
# Yenilikler : Down sendromu, oksitozin ve büyüme hormonu genleri eklendi.
# -----------------------------------------
# Versiyon 0.5.1 (07.02.2023)
# Yenilikler : Kodlar temize çekildi ve .exe formatına dönüştürüldü.  

# Bazı kütüphanelerin eklenmesi
from random import shuffle

# Yazılımda sonradan kullanılmak üzere tanımlanan bir fonksiyon
def delete(num):
    for i in range(num): del bingen[z+1]

def genayir(gen):
    i = 0
    global bingen
    while i < len(gen):
            bingen.append(gen[i:i+2]) 
            i += 2

# Gerekli değiskenler (6 liste 4 tamsayı 1 karakter dizisi)
p53ekzon="tcccccttgccgtcccaagcaatggatgatttgatgctgtccccggacgatattgaacaatggttcactgaagacccaggtccagatgaagctcccagaatgccagaggctgctccccccgtggcccctgcaccagcagctcctacaccggcggcccctgcaccagccccctcctggcccctgtcatcttctgtcccttcccagaaaacctaccagggcagctacggtttccgtctgggcttcttgcattctgggacagccaagtctgtgacttgcacg"
downsendromu="atggaggaggtggacctgcaggacctgcccagcgccaccatcgcctgtcacctggacccgcgcgtgttcgtggacggcctgtgccgggccaaatttgagtccctctttaggacgtatgacaaggacatcacctttcagtattttaagagcttcaaacgagtcagaataaacttcagcaaccccttctccgcagcagatgccaggctccagctgcataagactgagtttctgggaaaggaaatgaagttatattttgctcagaccttacacataggaagctcacacctggctccgccaaatccagacaagcagtttctgatctcccctcccgcctctccgccagtgggatggaaacaagtggaagatgcgaccccagtcataaactatgatctcttatatgccatctccaagctggggccaggggaaaagtatgaattgcacgcagcgactgacaccactcccagcgtggtggtccatgtatgtgagagtgatcaagagaaggaggaagaagaggaaatggaaagaatgaggagacctaagccaaaaattatccagaccaggaggccggagtacacgccgatccacctcagctag"
oksitozin="cccagcgcacccgcaccatggccggccccagcctcgcttgctgtctgctcggcctcctggcgctgacctccgcctgctacatccagaactgccccctgggaggcaagagggccgcgccggacctcgacgtgcgcaagtgcctcccctgcggccccgggggcaaaggccgctgcttcgggcccaatatctgctgcgcggaagagctgggctgcttcgtgggcaccgccgaagcgctgcgctgccaggaggagaactacctgccgtcgccctgccagtccggccagaaggcgtgcgggagcgggggccgctgcgcggtcttgggcctctgctgcagcccggacggctgccacgccgaccctgcctgcgacgcggaagccaccttctcccagcgctgaaacttgatggctccgaacaccctcgaagcgcgccactcgcttcccccatagccaccccagaaatggtgaaaataaaataaagcaggtttttctcctct"
buyumehormonu="gaattcaggactgaatcgtgctcacaacccccacaatctattggctgtgcttggccccttttcccaacacacacattctgtctggtgggtggaggttaaacatgcggggaggaggaaagggataggatagagaatgggatgtggtcggtagggggtctcaaggactggcctatcctgacatccttcgcccgcgtgcaggttggccaccatggcctgcggccagagggcacccacgtgacccttaaagagaggacaagttgggtggtatctctggctgacactctgtgcacaaccctcacaacactggtgacggtgggaagggaaagatgacaagccagggggcatgatcccagcatgtgtgggaggagcttctaaattatccattagcacaagcccgtcagtggccccatgcataaatgtagcacagaaacaggtggggtcaacagtgggagagaaggggccagggtataaaaagggcccacaagagaccagctcaaggatcccaaggcccaactccccgaaccactcagggtcctgtggacagctcacctagctgcaatggctacaggtaagcgcccctaaaatccctttggcacaatgtgtcctgaggggagaggcagcgacctgtagatgggacgggggcactaaccctcagggtttggggttctgaatgtgagtatcgccatctaagcccagtatttggccaatctcagaaagctcctggctccctggaggatggagagagaaaaacaaacagctcctggagcagggagagtgttggcctcttgctctccggctccctctgttgccctctggtttctccccaggctcccggacgtccctgctcctggcttttggcctgctctgcctgccctggcttcaagagggcagtgccttcccaaccattcccttatccaggctttttgacaacgctatgctccgcgcccatcgtctgcaccagctggcctttgacacctaccaggagtttgtaagctcttggggaatgggtgcgcatcaggggtggcaggaaggggtgactttcccccgctggaaataagaggaggagactaaggagctcagggtttttcccgaccgcgaaaatgcaggcagatgagcacacgctgagctaggttcccagaaaagtaaaatgggagcaggtctcagctcagaccttggtgggcggtccttctcctaggaagaagcctatatcccaaaggaacagaagtattcattcctgcagaacccccagacctccctctgtttctcagagtctattccgacaccctccaacagggaggaaacacaacagaaatccgtgagtggatgccttctccccaggcggggatgggggagacctgtagtcagagcccccgggcagcacagccaatgcccgtccttgcccctgcagaacctagagctgctccgcatctccctgctgctcatccagtcgtggctggagcccgtgcagttcctcaggagtgtcttcgccaacagcctggtgtacggcgcctctgacagcaacgtctatgacctcctaaaggacctagaggaaggcatccaaacgctgatgggggtgagggtggcgccaggggtccccaatcctggagccccactgactttgagagactgtgttagagaaacactggctgccctctttttagcagtcaggccctgacccaagagaactcaccttattcttcatttcccctcgtgaatcctccaggcctttctctacactgaaggggagggaggaaaatgaatgaatgagaaagggagggaacagtacccaagcgcttggcctctccttctcttccttcactttgcagaggctggaagatggcagcccccggactgggcagatcttcaagcagacctacagcaagttcgacacaaactcacacaacgatgacgcactactcaagaactacgggctgctctactgcttcaggaaggacatggacaaggtcgagacattcctgcgcatcgtgcagtgccgctctgtggagggcagctgtggcttctagctgcccgggtggcatccctgtgacccctccccagtgcctctcctggccctggaagttgccactccagtgcccaccagccttgtcctaataaaattaagttgcatcattttgtctgactaggtgtccttctataatattatggggtggaggggggtggtatggagcaaggggcccaagttgggaagacaacctgtagggcctgcggggtctattcgggaaccaagctggagtgcagtggcacaatcttggctcactgcaatctccgcctcctgggttcaagcgattctcctgcctcagcctcccgagttgttgggattccaggcatgcatgaccaggctcagctaatttttgtttttttggtagagacggggtttcaccatattggccaggctggtctccaactcctaatctcaggtgatctacccaccttggcctcccaaattgctgggattacaggcgtgaaccactgctcccttccctgtccttctgattttaaaataactataccagcaggaggacgtccagacacagcataggctacctgccatggcccaaccggtgggacatttgagttgcttgcttggcactgtcctctcatgcgttgggtccactcagtagatgcctgttgaattc"

while True:
    x = 0
    y = 0
    z = 0
    bingen=[]
    bingen2 = []
    notalar=[]
    ritim=[]
    aciknanahtar = []
    acikranahtar = []

    # Genleri ikili gruplandırıp bingen listesine aktarma

    secim = input("Gen Seçiniz (1-5) \n1.p53ekzon\n2.downsendromu\n3.oksitozin\n4.buyumehormonu\n5.exit\n>")
    match secim:
        case '1':
            genayir(p53ekzon)
        case '2':
            genayir(downsendromu)
        case '3':
            genayir(oksitozin)
        case '4':
            genayir(buyumehormonu)
        case '5':
            exit(0)
        case default:
            print("Geçersiz seçim, çıkış yapılıyor.")
            exit(0)


    e = len(bingen)

    # Nota anahtarını çözzme
    nanahtar = "tgcatatcgtctacgaatttagcggcaaggcc-P53"

    while x < len(nanahtar):
            if x < nanahtar.index("-"):
                aciknanahtar.append(nanahtar[x:x+2])
                x += 2
            elif nanahtar.index("-") == x:
                x += 1
            elif nanahtar.index("-") < x:
                genname = nanahtar[x:]
                break

    # Ritim anahtarını çözme
    ranahtar = "actatggtggtccggaaaatcactaggcttcc-P53"

    while y < len(ranahtar):
            if y < ranahtar.index("-"):
                acikranahtar.append(ranahtar[y:y+2])
                y += 2
            elif ranahtar.index("-") == y:
                y += 1
            elif ranahtar.index("-") < y:
                genname = ranahtar[y:]
                break


    shuffle(aciknanahtar)
    shuffle(acikranahtar)

    # İkililer listesindeki gen parçalarını notalara dönüstürüp notalar listesine aktarma
    for z in range(len(bingen)):
        if bingen[z] == aciknanahtar[0]: notalar.append("do")
        elif bingen[z] == aciknanahtar[1]: notalar.append("re")
        elif bingen[z] == aciknanahtar[2]: notalar.append("mi")
        elif bingen[z] == aciknanahtar[3]: notalar.append("fa")
        elif bingen[z] == aciknanahtar[4]: notalar.append("sol")
        elif bingen[z] == aciknanahtar[5]: notalar.append("la")
        elif bingen[z] == aciknanahtar[6]: notalar.append("si")
        elif bingen[z] == aciknanahtar[7]: notalar.append("DO")
        elif bingen[z] == aciknanahtar[8]: notalar.append("reb")
        elif bingen[z] == aciknanahtar[9]: notalar.append("mib")
        elif bingen[z] == aciknanahtar[10]: notalar.append("solb")
        elif bingen[z] == aciknanahtar[11]: notalar.append("lab")
        elif bingen[z] == aciknanahtar[12]: notalar.append("sib")
        elif bingen[z] == aciknanahtar[13]: notalar.append("dod")
        elif bingen[z] == aciknanahtar[14]: notalar.append("DOd")
        elif bingen[z] == aciknanahtar[15]: notalar.append("fad")
        else: notalar.append("Bos Nota")

    # Gen listesinden ritim elemanları olusturup ritim listesine kaydetme
    ritimrange = len(bingen)
    for z in range((ritimrange)):
            try:
                if bingen[z] == acikranahtar[0]: ritim.append("onaltilik es")

                elif bingen[z] == acikranahtar[1]:
                    ritim.append("iz")
                    ritim.append("mir")
                    delete(1)

                elif bingen[z] == acikranahtar[2]:
                    ritim.append("an")
                    ritim.append("ka")
                    ritim.append("ra")
                    delete(2)

                elif bingen[z] == acikranahtar[3]:
                    ritim.append("ka")
                    ritim.append("ra")
                    ritim.append("man")
                    delete(2)

                elif bingen[z] == acikranahtar[4]:
                    ritim.append("ge")
                    ritim.append("li")
                    ritim.append("bo")
                    ritim.append("lu")
                    delete(3)

                elif bingen[z] == acikranahtar[5]:
                    ritim.append("te")
                    ritim.append("ra")
                    ritim.append("zi")
                    delete(2)

                elif bingen[z] == acikranahtar[6]:
                    ritim.append("bur")
                    ritim.append("sa")
                    delete(1)

                elif bingen[z] == acikranahtar[7]:
                    ritim.append("si")
                    ritim.append("vas")
                    delete(1)

                elif bingen[z] == acikranahtar[8]:
                    ritim.append("uc")
                    ritim.append("le")
                    ritim.append("me")
                    delete(2)

                elif bingen[z] == acikranahtar[9]:
                    ritim.append("on1")
                    ritim.append("on2")
                    ritim.append("on3")
                    delete(2)

                elif bingen[z] == acikranahtar[10]: ritim.append("2 vurus")
                elif bingen[z] == acikranahtar[11]: ritim.append("1 vurus")
                elif bingen[z] == acikranahtar[12]: ritim.append("birlik es")
                elif bingen[z] == acikranahtar[13]: ritim.append("ikilik es")
                elif bingen[z] == acikranahtar[14]: ritim.append("dortluk es")
                elif bingen[z] == acikranahtar[15]: ritim.append("sekizlik es")
                else: ritim.append("Bos ritim")


                if z >= (len(bingen))-1:
                    break
            except IndexError:
                break

    while len(ritim) > e:
        del ritim[len(ritim) - 1]


    # Test için bazı verilerin ekrana yazdırma
    print("Notalar: ", notalar)
    print("Nota anahtari: ", aciknanahtar)
    print("Nota sayisi: ",len(notalar))

    print("Ritimler: ", ritim)
    print("Ritim anahtari: ", acikranahtar)
    print("Ritim sayisi: ",len(ritim))

   
    exitkey = input("Çıkış için 1 yazınız")
    if exitkey == '1':
        exit(0)