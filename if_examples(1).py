# grade conversion

studentGrade=int(input("grade? "))


# exclsive if statement
if studentGrade>=90:
    print("A")
elif studentGrade>=80:
    print("B")
elif studentGrade>=70:
    print("C")
elif studentGrade>=60:
    print("D")
elif studentGrade<60:
    print("F")
else: #
    print("wrong value")

print('=============')
# nesting
if studentGrade>=90:
    print("A")
else:
    if studentGrade>=80:
        print("B")
    else:
        if studentGrade>=70:
            print("C")
        else:
            if studentGrade>=60:
                print("D")
            else:
                if studentGrade<60:
                    print("F")
