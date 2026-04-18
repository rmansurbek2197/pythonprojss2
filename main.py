def matn_analiz():
    matn = input("Matnni kiriting: ")
    harflar_soni = 0
    raqamlar_soni = 0
    maxsus_belmalar_soni = 0

    for belgi in matn:
        if belgi.isalpha():
            harflar_soni += 1
        elif belgi.isdigit():
            raqamlar_soni += 1
        elif not belgi.isspace():
            maxsus_belmalar_soni += 1

    print("Harflar soni:", harflar_soni)
    print("Raqamlar soni:", raqamlar_soni)
    print("Maxsus belgilar soni:", maxsus_belmalar_soni)

    def matn_haqqida_malumot():
        katta_harflar_soni = 0
        kichik_harflar_soni = 0
        for belgi in matn:
            if belgi.isupper():
                katta_harflar_soni += 1
            elif belgi.islower():
                kichik_harflar_soni += 1
        print("Katta harflar soni:", katta_harflar_soni)
        print("Kichik harflar soni:", kichik_harflar_soni)

    def raqamlar_haqqida_malumot():
        juft_raqamlar_soni = 0
        toq_raqamlar_soni = 0
        for belgi in matn:
            if belgi.isdigit():
                if int(belgi) % 2 == 0:
                    juft_raqamlar_soni += 1
                else:
                    toq_raqamlar_soni += 1
        print("Juft raqamlar soni:", juft_raqamlar_soni)
        print("Toq raqamlar soni:", toq_raqamlar_soni)

    matn_haqqida_malumot()
    raqamlar_haqqida_malumot()

def bosh_menu():
    print("1. Matn analiz qilish")
    print("2. Chiqish")
    tanlov = input("Tanlovni kiriting: ")
    if tanlov == "1":
        matn_analiz()
        bosh_menu()
    elif tanlov == "2":
        print("Dasturdan chiqildi")
    else:
        print("Noto'g'ri tanlov")
        bosh_menu()

bosh_menu()