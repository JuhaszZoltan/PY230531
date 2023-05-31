from module import *

horcsogok:list[Horcsog] = []
file = open('horcsogok.txt', 'r', encoding='utf8')
for s in file: horcsogok.append(Horcsog(s))

print(f'horcsogok szama: {len(horcsogok)}')

sum_suly:int = 0
for h in horcsogok:
    sum_suly += h.suly
avg_suly = round(sum_suly / len(horcsogok), 2)
print(f'atlagos testsuly: {avg_suly}')

cnt_nosteny:int = 0
for h in horcsogok:
    if not h.nem:
        cnt_nosteny += 1
print(f'nostenyek szama: {cnt_nosteny}')

ind_minkor:int = 0
for i in range(1, len(horcsogok)):
    if horcsogok[i].kor < horcsogok[ind_minkor].kor:
        ind_minkor = i
print(f'legfiatalabb: {horcsogok[ind_minkor].nev}')
print(f'\téletkora: {horcsogok[ind_minkor].kor} hónap')

nevek:list[str] = []
ker_szin:str = input('irj be egy szint: ')
for h in horcsogok:
    if h.szin == ker_szin:
        nevek.append(h.nev)

if len(nevek) == 0: print('nincs ilyen szinu horcsog')
else:
    print(f'{ker_szin} szinu horcsogok ({len(nevek)} db):')
    for n in nevek:
        print(f'\t- {n}')