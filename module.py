def gepjarmuado(gyev:int, le:int) -> int:
    kw:int = round(le/1.36)
    kor:int = 2023 - gyev
    aa:int = 0
    if kor <= 3: aa = 345
    elif kor <= 7: aa = 300
    elif kor <= 11: aa = 230
    elif kor <= 15: aa = 185
    else: aa = 140
    return kw * aa


class Horcsog:
    def __init__(self, sor:str) -> None:
        v:list[str] = sor.strip().split(';')
        self.nev:str = v[0]
        self.szin:str = v[1]
        self.kor:int = int(v[2])
        self.suly:int = int(v[3])
        self.nem:bool = 'hím' == v[4]