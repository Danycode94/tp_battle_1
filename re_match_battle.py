
antre_po = input("Antre adres IP an separe pa yon pwen foma (111.1.1.1): ")
# premye_digi = 0

if antre_po:
    sp = antre_po.split(".")

    total = (int(sp[0][0]) + int(sp[0][1]) + int(sp[0][2]) + int(sp[1][0]) + int(sp[2][0]) + int(sp[3][0]) ) * int(sp[0][0])
        
        
    print(f"Total {total}")
else:
    print("Antre yon Adres IP")