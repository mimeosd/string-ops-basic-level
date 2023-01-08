
ulazni_string = """REG_OZNAKA   BOJA    TIP_VOZILA
NI-543-MM   siva    automobil
LE-345-KM   plava   kamion
BG-345-TT   bela    automobil
KG-365-KG   plava   automobil
SU-475-GM   bela    automobil
KG-845-YB   crna    autobus
NI-345-XD   bela    automobil
UE-134-NF   crna    automobil
AL-226-DF   bela    kamion"""


def pravljenje_izlaza(neki_string:str):
    glavni_dikt = {}
    tip_vozila = []
    gradovi = []
    
    # Tipovi vozila
    for i in neki_string.split()[5::3]:
        if i in glavni_dikt:
            glavni_dikt[i] += 1
            tip_vozila.append(i)
        else:
            glavni_dikt[i] = 1
            tip_vozila.append(i)
    
    for i in glavni_dikt:
        glavni_dikt[i] = round((glavni_dikt[i] / len(tip_vozila)) * 100, 2)

    # Dobijanje registracija pa splitovanje
    for i in neki_string.split()[3::3]:
        for j in i.split('-')[0::3]:
            gradovi.append(j)

    result = {"tip_vozila": glavni_dikt, "gradovi": list(set(gradovi)), "boje_po_tipu": {}}

    boje = [i for i in ulazni_string.split()[4::3]]

    for i in zip(tip_vozila, boje):
        
        if i[0] in result["boje_po_tipu"]:
            if i[1] in result["boje_po_tipu"][i[0]]:
                
                result["boje_po_tipu"][i[0]][i[1]] += 1
            else:
                result["boje_po_tipu"][i[0]][i[1]] = 1
        else:
            result["boje_po_tipu"][i[0]] =  {i[1] : 1}
    # Ovo je bukvalno najkompleksnija provera koju sam ikad radio
    
    return result



    
print(pravljenje_izlaza(ulazni_string))