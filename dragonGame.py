import random
class Dragon:
    blood_value=100000
    def fighting(self):
        hurt_value = random.randint(1,15000)
        return hurt_value
    @staticmethod
    def dragon_indignation():
        print("Who are you, hurt my son, take down")
        return 500000
class QiuNiu(Dragon):
    def __init__(self,name):
        self.name=name
    def fighting(self):
        hurt_value=super().fighting()
        print("QiuNiu is irritated, the harmness is{}".format(hurt_value))
        return hurt_value
class YaZi(Dragon):
    def __init__(self, name):
        self.name = name
    def fighting(self):
        hurt_value=super().fighting()
        print("The fatal battle, the harmness is {}".format(hurt_value))
        return hurt_value
class ChaoFeng(Dragon):
    def __init__(self, name):
        self.name=name
    def fighting(self):
        hurt_value=super().fighting()
        print("Chaofeng starts to fight, the harmness is{}".format(hurt_value))
        return hurt_value
class PuLao(Dragon):
    def __init__(self, name):
        self.name=name
    def fighting(self):
        hurt_value=super().fighting()
        print("Pulao starts to fight, the harmness is{}".format(hurt_value))
        return hurt_value
class SuanNi(Dragon):
    def __init__(self, name):
        self.name=name
    def fighting(self):
        hurt_value=super().fighting()
        print("SuanNi starts to fight, the harmness is{}".format(hurt_value))
        return hurt_value
class BiXi(Dragon):
    def __init__(self, name):
        self.name=name
    def fighting(self):
        hurt_value=super().fighting()
        print("BiXi starts to fight, the harmness is{}".format(hurt_value))
        return hurt_value
class BiAn(Dragon):
    def __init__(self, name):
        self.name=name
    def fighting(self):
        hurt_value=super().fighting()
        print("BiAn starts to fight, the harmness is{}".format(hurt_value))
        return hurt_value
class FuXi(Dragon):
    def __init__(self, name):
        self.name=name
    def fighting(self):
        hurt_value=super().fighting()
        print("FuXi starts to fight, the harmness is{}".format(hurt_value))
        return hurt_value
class ChiWen(Dragon):
    def __init__(self, name):
        self.name=name
    def fighting(self):
        hurt_value=super().fighting()
        print("ChiWen starts to fight, the harmness is{}".format(hurt_value))
        return hurt_value
class Villain:
    blood_value = 1000000
    def __init__(self, name):
        self.name=name
def add_blood_value(self):
    value=random.randint(100000,200000)
    print("{}Recover the blood, Add blood{}".format(slef.name,value))
    self.blood_value += value
    print("The current blood valumn is {}".format(self.blood_value))

def one_strike(self):
    hurt_value = random.randint(1,8000)
    return hurt_value
qiuniu = QiuNiu("Dragon1")
yazi = YaZi("Dragon2")
chaofeng = ChaoFeng("Dragon3")
pulao = PuLao("Dragon4")
suanni = SuanNi("Dragon5")
bixi = BiXi("Dragon6")
bian = BiAn("Dragon7")
fuxi = FuXi("Dragon8")
chiwen = ChiWen("Dragon9")

brother_nine_list =[qiuniu, yazi, chaofeng, pulao, suanni, bixi, bian, fuxi, chiwen]
villain = Villain("BraveKnight")

def brother_fighting(obj):
    hurt_value = obj.fighting()
    villain.blood_value -= hurt_value
    return hurt_value

who_strike = "villain"
while True:
    if who_strike =="villain":
        if villain.blood_value<100000:
            add_blood_status = input("The blood is lower than 100000, add blood(Y/N)?")
            if add_blood_status.upper()=="Y":
                villain.add_blood_value()

                who_strike == "Nine dragons"
                continue
        strike_type = input("please{}will fight,1 is single fight, 2 is a group fighting, please choose")
        if strike_type == "1":
            villain_one_strike_hurt_value=villain.one_strike()
            one_of_nine = brother_nine_list[random.randint(0,len(brother_nine_list)-1)]
            one_of_nine.blood_value -= villain_one_strike_hurt_value
            print("{}is under strike, the rest blood volumn{}".formet(one_of_nine.name,one_of_nine.blood_value))
            
            if one_of_nine.blood_value <1:
                print("{}Failed, out".format(one_of_nine.name))
                brother_nine_list.remove(one_of_nine)
                print("The brothers left from 9 is {}".format(len(brother_nine_list)))
            elif strike_type == "2":
                villain_group_hurt_value = villain.group_strike()
                for i in brother_nine_list:
                    i.blood_value -= villain_group_hurt_value
                    print("{} is under group strike, the left blood is{}".format(i.name,i.blood_value))
                    if i.blood_value<1:
                        print("{} failed, out".format(i.name))
                        brother_nine_list.remove(i)
                        print("The brothers left from 9 is {}".format(len(brother_nine_list)))
            if len(brother_nine_list)==1:
                print("Only one left from 9, request for dragon strike")
                if random.randint(0,5)==1:
                    hurt_value = Dragon.dragon_indignation()
                    villain.blood_value -= hurt_value
                    if villain.blood_value<1:
                        print("9 brothers win")
                else:
                    print("Request Failed")
            if len(brother_nine_list)==0:
                print("All brothers killed,{} win".format(villain.name))
                break
            who_strike ="nine brothers"
        elif who_strike=="nine brothers":
            for i in brother_nine_list:
                hurt_value = brother_fighting(i)
                print("The villain killed, nine brothers win")
                break










