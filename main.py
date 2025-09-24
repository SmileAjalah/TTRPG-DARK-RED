import time
import random

#VARIABEL
gold = int(50)
HP = int(50)
HP2 = HP
ATK = int(5)
DEF = int(3)
SPD = int(1)
SP = int(0)
EXP = int(0)
NEXP2 = int(100)
level = int(1)
NEXP = NEXP2 * level
potion = int(0)


#STATUS DEF N UPGRADE
def status(name, gold,HP,ATK,DEF,SPD,SP,EXP,NEXP,level):
    time.sleep(0.8)
    while(True):
        print("")
        print("\n === STATUS ===")
        print(f"Name : {name}")
        print(f"Level : {level}")
        print(f"Experience : {EXP}")
        print(f"EXP needed for level up : {NEXP - EXP}")
        print(f"Gold : {gold}")
        print(f"Health[HP] : {HP}")
        print(f"Attack[ATK] : {ATK}")
        print(f"Defense[DEF] : {DEF}")
        print(f"Speed[SPD] : {SPD}")
        print("")
        print(f"Status Point : {SP}")
        print("[A = Stats Upgrade|Enter = Left]")
        a1 = input("ACT : ")
        if a1 == "A":
            while(True):
                print("Masukan nama stats sesuai seperti yang di status bertanda kurung![Enter untuk keluar]")
                sts = input("STATS : ")
                if sts in ["HP","ATK","DEF","SPD"]:
                    if SP >= 0:
                        print("SP MU TAK CUKUP!")
                        break
                    elif SP <= 0:
                        if sts == HP:
                            SP -= 1
                            HP += 5
                            print("SP mu berkurang 1")
                            print(f"Sekarang Health mu adalah {HP}")
                        if sts == ATK:
                            SP -= 1
                            ATK += 1
                            print("SP mu berkurang 1")
                            print(f"Sekarang Attack mu adalah {ATK}")
                        if sts == DEF:
                            SP -= 1
                            DEF += 1
                            print("SP mu berkurang 1")
                            print(f"Sekarang Defense mu adalah {DEF}")
                        if sts == SPD:
                            SP -= 1
                            SPD += 1
                            print("SP mu berkurang 1")
                            print(f"Sekarang Speed mu adalah {SPD}")
                elif sts == "":
                    break
        else:
            break

#INVENTORY DEF
print("\n === INVENTORY ===")
print(f"Potion = {potion}")
print("")
print()

#PROLOG
print("DEMI KENYAMANAN SELAMA BERMAIN DISARANKAN MENYALAKAN CAPSLOCK")
input("Tekan enter untuk memulai")

print("Kamu terbangun dari mimpi panjangmu atau mungkin kehidupan mu sebelumnya?")
time.sleep(1.5)
print("Tidak ada yang tau, yang pasti sekarang kamu berada di dekat sebuah danau yang cukup besar")
time.sleep(1.5)
print("(Hei! akhirnya kamu bangun! aku sudah menunggu mu daritadi!)")
time.sleep(1.5)
print("A.Tanya dia siapa(Tekan A)")
while(True):
    a1 = input("Jawab : ")
    if a1 == "A":
        break
    else:
        print("kiat: tolong ketik A sesuai yang diarahkan")
        a1 = input("Jawab : ")

time.sleep(1.5)
print("(Aku? Aku YV. Peri yang ditakdirkan untuk menuntun mu disini!)")
time.sleep(1.5)
print("(Ekhem, aku belum tau siapa nama mu... jadi siapa nama mu?)")
name = input("Jawab : ")
time.sleep(1)
print(f"(Oh nama yang keren! Haloooo {name}!!!)")
time.sleep(1.5)
print("(Ekhem, coba katakan MENU! kau akan melihat sebuah layar ajaib! ya itu adalah statusmu!)")
a1 = input("Katakan : ")
while(True):
    if a1 == "MENU":
        break
    else:
        print("(Katakan MENU bukan yang lain dan harus berteriak(kapital))")
        a1 = input("Katakan : ")

print("(MENU!!!) kamu mengatakannya dengan sangat lantang")
while(True):
    if EXP == NEXP:
        level += 1
        print("LEVEL UP!!!")
        print(f"Level mu sekarang adalah {level}")
        time.sleep(1.5)

    print("")
    print("\n=== MENU ===")
    print("A.Status")
    print("B.Inventory")
    print("C.Adventure")
    print("D.Story")
    menu = input("ACT(Huruf Kapital Awal) :")
    if menu == "A":
        status(name, gold, HP, ATK, DEF, SPD, SP, EXP, NEXP, level)