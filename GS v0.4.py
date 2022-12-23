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
# Yenilikler : P53 geninin bazı mRNA varyantları eklendi

# Bazı modüllerin eklenmesi
from random import shuffle

# Gen listesini tutan değişken
P53 = "attcgtgaggggtttgtaatgcagggctgaggagtgtccgaagagaatgggcaggtgagcggtgagacagttgttcttccagaagctttgcagtgaaaggaatcaaagaaatggagccgtgtatcagccagactgccttccgggtcactgccatggaggagccgcagtcagatcctagcgtcgagccccctctgagtcaggaaacattttcagacctatggaaactacttcctgaaaacaacgttctgtcccccttgccgtcccaagcaatggatgatttgatgctgtccccggacgatattgaacaatggttcactgaagacccaggtccagatgaagctcccagaatgccagaggctgctccccccgtggcccctgcaccagcagctcctacaccggcggcccctgcaccagccccctcctggcccctgtcatcttctgtcccttcccagaaaacctaccagggcagctacggtttccgtctgggcttcttgcattctgggacagccaagtctgtgacttgcacgtactcccctgccctcaacaagatgttttgccaactggccaagacctgccctgtgcagctgtgggttgattccacacccccgcccggcacccgcgtccgcgccatggccatctacaagcagtcacagcacatgacggaggttgtgaggcgctgcccccaccatgagcgctgctcagatagcgatggtctggcccctcctcagcatcttatccgagtggaaggaaatttgcgtgtggagtatttggatgacagaaacacttttcgacatagtgtggtggtgccctatgagccgcctgaggttggctctgactgtaccaccatccactacaactacatgtgtaacagttcctgcatgggcggcatgaaccggaggcccatcctcaccatcatcacactggaagactccagtggtaatctactgggacggaacagctttgaggtgcgtgtttgtgcctgtcctgggagagaccggcgcacagaggaagagaatctccgcaagaaaggggagcctcaccacgagctgcccccagggagcactaagcgagcactgcccaacaacaccagctcctctccccagccaaagaagaaaccactggatggagaatatttcacccttcagatccgtgggcgtgagcgcttcgagatgttccgagagctgaatgaggccttggaactcaaggatgcccaggctgggaaggagccaggggggagcagggctcactccagccacctgaagtccaaaaagggtcagtctacctcccgccataaaaaactcatgttcaagacagaagggcctgactcagactgacattctccacttcttgttccccactgacagcctcccacccccatctctccctcccctgccattttgggttttgggtctttgaacccttgcttgcaataggtgtgcgtcagaagcacccaggacttccatttgctttgtcccggggctccactgaacaagttggcctgcactggtgttttgttgtggggaggaggatggggagtaggacataccagcttagattttaaggtttttactgtgagggatgtttgggagatgtaagaaatgttcttgcagttaagggttagtttacaatcagccacattctaggtaggggcccacttcaccgtactaaccagggaagctgtccctcactgttgaattttctctaacttcaaggcccatatctgtgaaatgctggcatttgcacctacctcacagagtgcattgtgagggttaatgaaataatgtacatctggccttgaaaccaccttttattacatggggtctagaacttgacccccttgagggtgcttgttccctctccctgttggtcggtgggttggtagtttctacagttgggcagctggttaggtagagggagttgtcaagtctctgctggcccagccaaaccctgtctgacaacctcttggtgaaccttagtacctaaaaggaaatctcaccccatcccacaccctggaggatttcatctcttgtatatgatgatctggatccaccaagacttgttttatgctcagggtcaatttcttttttcttttttttttttttttttctttttctttgagactgggtctcgctttgttgcccaggctggagtggagtggcgtgatcttggcttactgcagcctttgcctccccggctcgagcagtcctgcctcagcctccggagtagctggaccacaggttcatgccaccatggccagccaacttttgcatgttttgtagagatggggtctcacagtgttgcccaggctggtctcaaactcctgggctcaggcgatccacctgtctcagcctcccagagtgctgggattacaattgtgagccaccacgtccagctggaagggtcaacatcttttacattctgcaagcacatctgcattttcaccccacccttcccctccttctccctttttatatcccatttttatatcgatctcttattttacaataaaactttgctgcca"
P53mrna="ctcaaaagtctagagccaccgtccagggagcaggtagctgctgggctccggggacactttgcgttcgggctgggagcgtgctttccacgacggtgacacgcttccctggattggcagccagactgccttccgggtcactgccatggaggagccgcagtcagatcctagcgtcgagccccctctgagtcaggaaacattttcagacctatggaaactacttcctgaaaacaacgttctgtcccccttgccgtcccaagcaatggatgatttgatgctgtccccggacgatattgaacaatggttcactgaagacccaggtccagatgaagctcccagaatgccagaggctgctccccccgtggcccctgcaccagcagctcctacaccggcggcccctgcaccagccccctcctggcccctgtcatcttctgtcccttcccagaaaacctaccagggcagctacggtttccgtctgggcttcttgcattctgggacagccaagtctgtgacttgcacgtactcccctgccctcaacaagatgttttgccaactggccaagacctgccctgtgcagctgtgggttgattccacacccccgcccggcacccgcgtccgcgccatggccatctacaagcagtcacagcacatgacggaggttgtgaggcgctgcccccaccatgagcgctgctcagatagcgatggtctggcccctcctcagcatcttatccgagtggaaggaaatttgcgtgtggagtatttggatgacagaaacacttttcgacatagtgtggtggtgccctatgagccgcctgaggttggctctgactgtaccaccatccactacaactacatgtgtaacagttcctgcatgggcggcatgaaccggaggcccatcctcaccatcatcacactggaagactccagtggtaatctactgggacggaacagctttgaggtgcgtgtttgtgcctgtcctgggagagaccggcgcacagaggaagagaatctccgcaagaaaggggagcctcaccacgagctgcccccagggagcactaagcgagcactgcccaacaacaccagctcctctccccagccaaagaagaaaccactggatggagaatatttcacccttcagatccgtgggcgtgagcgcttcgagatgttccgagagctgaatgaggccttggaactcaaggatgcccaggctgggaaggagccaggggggagcagggctcactccagccacctgaagtccaaaaagggtcagtctacctcccgccataaaaaactcatgttcaagacagaagggcctgactcagactgacattctccacttcttgttccccactgacagcctcccacccccatctctccctcccctgccattttgggttttgggtctttgaacccttgcttgcaataggtgtgcgtcagaagcacccaggacttccatttgctttgtcccggggctccactgaacaagttggcctgcactggtgttttgttgtggggaggaggatggggagtaggacataccagcttagattttaaggtttttactgtgagggatgtttgggagatgtaagaaatgttcttgcagttaagggttagtttacaatcagccacattctaggtaggggcccacttcaccgtactaaccagggaagctgtccctcactgttgaattttctctaacttcaaggcccatatctgtgaaatgctggcatttgcacctacctcacagagtgcattgtgagggttaatgaaataatgtacatctggccttgaaaccaccttttattacatggggtctagaacttgacccccttgagggtgcttgttccctctccctgttggtcggtgggttggtagtttctacagttgggcagctggttaggtagagggagttgtcaagtctctgctggcccagccaaaccctgtctgacaacctcttggtgaaccttagtacctaaaaggaaatctcaccccatcccacaccctggaggatttcatctcttgtatatgatgatctggatccaccaagacttgttttatgctcagggtcaatttcttttttcttttttttttttttttttctttttctttgagactgggtctcgctttgttgcccaggctggagtggagtggcgtgatcttggcttactgcagcctttgcctccccggctcgagcagtcctgcctcagcctccggagtagctgggaccacaggttcatgccaccatggccagccaacttttgcatgttttgtagagatggggtctcacagtgttgcccaggctggtctcaaactcctgggctcaggcgatccacctgtctcagcctcccagagtgctgggattacaattgtgagccaccacgtccagctggaagggtcaacatcttttacattctgcaagcacatctgcattttcaccccacccttcccctccttctccctttttatatcccatttttatatcgatctcttattttacaataaaactttgctgcca"
P53mrna2="tcccccttgccgtcccaagcaatggatgatttgatgctgtccccggacgatattgaacaatggttcactgaagacccaggtccagatgaagctcccagaatgccagaggctgctccccccgtggcccctgcaccagcagctcctacaccggcggcccctgcaccagccccctcctggcccctgtcatcttctgtcccttcccagaaaacctaccagggcagctacggtttccgtctgggcttcttgcattctgggacagccaagtctgtgacttgcacg"

# Gerekli değişkenler (4 liste 2 tamsayı 1 metin 2 bool)
i = 0
x = 0
y = 0
bingen=[]
notalar=[]
ritim=[]
aciknanahtar = []
acikranahtar = []
genname = ""
factor1 = True
factor2 = True
müzik = dict()

# Nota anahtarını çözzme
nanahtar = "agtttgccggcgtcaaatacgagtgccttaca-P53"

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
ranahtar = "agtttgccggcgtcaaatacgagtgccttaca-P53"
while y < len(ranahtar):
        if y < ranahtar.index("-"):
            acikranahtar.append(ranahtar[y:y+2])
            y += 2
        elif ranahtar.index("-") == y:
            y += 1
        elif ranahtar.index("-") < y:
            genname = ranahtar[y:]
            break


# Genleri ikili gruplandırıp bingen listesine aktarma
while i < len(P53mrna2) :
    bingen.append(P53mrna2[i:i+2]) 
    i += 2

# İkililer listesindeki gen parçalarını notalara dönüştürüp notalar listesine aktarma
for a in range(len(bingen)):
    if bingen[a] == aciknanahtar[0]:
        notalar.append("do")            
    elif bingen[a] == aciknanahtar[1]:
        notalar.append("re")            
    elif bingen[a] == aciknanahtar[2]:
        notalar.append("mi")            
    elif bingen[a] == aciknanahtar[3]:
        notalar.append("fa")            
    elif bingen[a] == aciknanahtar[4]:
        notalar.append("sol")   
    elif bingen[a] == aciknanahtar[5]:
        notalar.append("la")            
    elif bingen[a] == aciknanahtar[6]:
        notalar.append("si")            
    elif bingen[a] == aciknanahtar[7]:
        notalar.append("DO")        
    elif bingen[a] == aciknanahtar[8]:
        notalar.append("reb")
    elif bingen[a] == aciknanahtar[9]:
        notalar.append("mib")
    elif bingen[a] == aciknanahtar[10]:
        notalar.append("solb")
    elif bingen[a] == aciknanahtar[11]:
        notalar.append("lab")        
    elif bingen[a] == aciknanahtar[12]:
        notalar.append("sib")
    elif bingen[a] == aciknanahtar[13]:
        notalar.append("dod")
    elif bingen[a] == aciknanahtar[14]:
        notalar.append("DOd")
    elif bingen[a] == aciknanahtar[15]:
        notalar.append("fad")    
    else:
        notalar.append("Bos Nota")

print(bingen)
# Gen listesinden ritim elemanları oluşturup ritim listesine kaydetme
ritimrange = len(bingen)
for a in range((ritimrange)):

        if bingen[a] == acikranahtar[0]:
            ritim.append("van")

        elif bingen[a] == acikranahtar[1]:
            ritim.append("iz")
            ritim.append("mir")
            del bingen[a+1]
            

        elif bingen[a] == acikranahtar[2]:
            ritim.append("an")
            ritim.append("ka")
            ritim.append("ra")
            del bingen[a+1]
            del bingen[a+2]


        elif bingen[a] == acikranahtar[3]:
            ritim.append("ka")
            ritim.append("ra")
            ritim.append("man")
            del bingen[a+1]
            del bingen[a+2]


        elif bingen[a] == acikranahtar[4]:
            ritim.append("ge")
            ritim.append("li")
            ritim.append("bo")
            ritim.append("lu")

            del bingen[a+1]
            del bingen[a+2]
            del bingen[a+3]


        elif bingen[a] == acikranahtar[5]:
            ritim.append("şi")
            ritim.append("ra")
            ritim.append("z")
            del bingen[a+1]
            del bingen[a+2]


        elif bingen[a] == acikranahtar[6]:
            ritim.append("bur")
            ritim.append("sa")
            del bingen[a+1]

        elif bingen[a] == acikranahtar[7]:
            ritim.append("si")
            ritim.append("vas")
            del bingen[a+1]

        elif bingen[a] == acikranahtar[8]:
            ritim.append("üç")
            ritim.append("me")
            ritim.append("le")
            del bingen[a+1]
            del bingen[a+2]


        elif bingen[a] == acikranahtar[9]:
            ritim.append("on")

        elif bingen[a] == acikranahtar[10]:
            ritim.append("2 vuruş")

        elif bingen[a] == acikranahtar[11]:
            ritim.append("1 vuruş")

        elif bingen[a] == acikranahtar[12]:
           ritim.append("es")

        elif bingen[a] == acikranahtar[13]:
           ritim.append("2es")

        elif bingen[a] == acikranahtar[14]:
           ritim.append("4es")

        elif bingen[a] == acikranahtar[15]:
           ritim.append("8es")
        else:
            ritim.append("Boş ritim")
        
        ritimrange = len(bingen)

        if a >= (ritimrange)-1:
            break
        

# Test için bazı verilerin ekrana yazdırma

print(notalar)
print(ritim)