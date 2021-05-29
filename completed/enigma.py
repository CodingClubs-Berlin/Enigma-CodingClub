from typing import List

class Drum:
    def __init__(self, newdrumnString: List):
        self.Rechts = newdrumnString
        self.Counter = 0
        self.Links = [c for c in (chr(i) for i in range(32,127))]

    def rotate(self):
        self.Rechts.insert(0, self.Rechts[-1])
        self.Rechts.pop()
        self.Links.insert(0, self.Links[-1])
        self.Links.pop()
        self.Counter += 1
        
drum1 =       Drum(list('''`z-<;7BsG?jx"|ofUF369w]S4MVqvQ&Y+*Kr2=)8'>kZ0pO$mL/T!_bHidXgAWcyu\PCn.1D:al(%J5RN Ie,@[~^{h#Et}'''))
drum2 =       Drum(list('''SN7{Pq+:ixm w%4Kf>"tRYQuCI&*;D,5J)AWp$96U8~z`F}o\Mn1aly#!cBXZHsd'?g0_[VL2/j(bTG^|v=eEk<-r.hO@]3'''))
drum3 =       Drum(list('''S34#}oq!uRlF(0)*,?yMeH@"p|]B+KZ[9'Ii<UgX2tzwh;mYv5nVC>{L6A$T^:-~cbf_./k1&G\D%7=sJaxNOr `jEd8PWQ'''))
startdrum =   Drum(list('''\g9#zr&:^UJHKYnjLE2);F0>[w!-+M`a6q4BTS8(Q<pAi5d/~ls3}mtoZ"XhxeIv{$'VuPk7@%y]? f1._DN=|WGCc,bOR*'''))
reversedrum = Drum(list(''' W+A3br6Z'{N5,G"7#:<qHidQ^KVI-SRn@ku=|m_ot]\le`9YCzg1XD$}c~y(*UFvwaEpj%Ph2&J;B!x04sM)[OT/L>.f?8'''))


def rotate():
    global drum1
    global drum2
    global drum3

    if drum1.Counter != 95:
        drum1.rotate()
    elif drum2.Counter != 95:
        drum1.Counter = 0
        drum2.rotate()
    elif drum3.Counte != 95:
        drum1.Counter = 0
        drum2.Counter = 0
        drum3.rotate()
    else:
        drum2.Counter = 0
        drum3.Counter = 0
        drum1.rotate()
        drum1.Counter = 0
    
def changedrumToStartPosition(drum: Drum, pos: str):
    while(drum.Links[0] != pos):
        drum.rotate()

def letThroughdrum(drum: Drum, i: int):
    newCharacter = drum.Rechts[i]
    position = drum.Links.index(newCharacter)
    return position

def letThroughDrumBack(drum: Drum, i: int):
    newCharacter = drum.Links[i]
    position = drum.Rechts.index(newCharacter)
    return position

def letToStartdrum(c: str):
    position = startdrum.Rechts.index(c)
    return position

def letToStartdrumBack(c: str):
    position = startdrum.Rechts[c]
    return position

def enigma(encode: bool, text: str, begin1: str, begin2: str, begin3: str):
    changedrumToStartPosition(drum1, begin1)
    changedrumToStartPosition(drum2, begin2)
    changedrumToStartPosition(drum3, begin3)
    fin = []
    for character in text:
        rotate()
        position = letToStartdrum(character)
        position = letThroughdrum(drum1, position)
        position = letThroughdrum(drum2, position) 
        position = letThroughdrum(drum3, position) 

        if (encode):
            position = letThroughdrum(reversedrum, position)
        else:
            position =  letThroughDrumBack(reversedrum, position)

        position = letThroughDrumBack(drum3, position)
        position = letThroughDrumBack(drum2, position)
        position = letThroughDrumBack(drum1, position)
        c = letToStartdrumBack(position)
        fin.append(c)
    print("".join(fin))

# enigma(True, "hallo ich bins", "a", "a", "a")
# enigma(False, "B@EDU h'/!cI))", "a", "a", "a")
