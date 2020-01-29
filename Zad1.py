

zipCode1 = "79-900"
zipCode2 = "80-155"


def zad1():
    code_generator = []
    zip_code_string_start1: str = zipCode1[0:2]
    zip_code_string_end1: str = zipCode1[3:6]
    zip_code_string_start2: str = zipCode2[0:2]
    zip_code_string_end2: str = zipCode2[3:6]

    zip_code1_string = zip_code_string_start1+zip_code_string_end1
    zip_code2_string = zip_code_string_start2+zip_code_string_end2
    zip_code_int1: int = int(zip_code1_string)
    zip_code_int2: int = int(zip_code2_string)

    print(zip_code_string_start2)
    print(zip_code_string_end2)

    for zipCodeInt in range(zip_code_int1, zip_code_int2, 1):
        zip_code_string = str(zipCodeInt)
        zip_code_start3 = zip_code_string[0:2]
        zip_code_start4 = zip_code_string[2:6]
        zip_code_full = zip_code_start3 + "-" + zip_code_start4
        code_generator.append(zip_code_full)
        print(code_generator)
