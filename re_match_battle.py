
antre_po = input("Antre adres IP an separe pa yon pwen foma (111.1.1.1): ")
# premye_digi = 0

if antre_po:
    sp = antre_po.split(".")

    total = (sp[0][0] + sp[0][1] + sp[0][2] + sp[1][0] +sp[2][0] + sp[3][0] ) *sp[0][0]
        
        
    print(f"Total {total}")
else:
    print("Antre yon Adres IP")