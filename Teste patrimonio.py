princ = []
mai = men = 0

while True:
    temp = []
    temp.append(str(input("Nome: ")))
    temp.append(int(input("Fortuna: ")))
    princ.append(temp[:])

    if len(princ) == 1:
        men = mai = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    quer_mais = input("Quer continuar? (S/N): ")
    if quer_mais in "Nn":
        break
    
print(F"A quantidade de pessoas cadastradas foi de {len(princ)}")
print(f'A maior fortuna foi de {mai}')
for p in princ:
    if p[1] == mai:
        print(p[0])
print(f"A menor fortuna foi de {men}")
for p in princ:
    if p[1] == men:
        print(p[0])


