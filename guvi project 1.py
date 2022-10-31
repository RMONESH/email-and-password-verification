import os
import re

A = input("Login or Register :")
file = open("monesh.txt", "a")

if A == "Login":
    Email = input("Enter email id:")
    password= input("Enter password:")
    file = open("monesh.txt", "r")
    read = file.readlines()
    for x in read:
        temp = x.split()
        if Email and password in temp:
            print("valid")
            break
    else:
        print("Register or Forgot password or provide new password")
        B = input()
        if B == "Forgot password":
            re_enter_email = input("Enter email id:")
            for i in read:
                temp = i.split()
                if re_enter_email in temp:
                    d = temp[1:]
                    print("your password :", *d)
                    break
            else:
                print("your email not found please register")
        if B == "provide new password":
            file = open("monesh.txt", "r")
            file_a = open("temp.txt", "a")
            C = input("Enter email id:")
            s = file.readlines()
            for n in s:
                L = n.split()
                if L[0] == C:
                    password = "not valid"
                    for Z in password:
                        password = input("enter password:")
                        if re.search("[a-z]", password):
                            if re.search("[A-Z]", password):
                                if re.search("[0-9]", password):
                                    if re.search("[!@#$%^&*]", password):
                                        if len(password) > 5:
                                            file_a.write(C)
                                            file_a.write(" ")
                                            file_a.write(password)
                                            file_a.write("\n")
                                            print("successfully Register")
                                            break
                                        else:
                                            print("at least use")
                                    else:
                                        print("use special characters")
                                else:
                                    print("use digit")
                            else:
                                print("use upper")
                        else:
                            print("use lower")
                else:
                    file_a.write(L[0]+" "+L[1]+ "\n")
            file.close()
            file_a.close()
            os.remove("monesh.txt")
            os.rename("temp.txt","monesh.txt")
        elif B == "Register":
            condition = "[^0-9A-Z][a-z0-9]{2,15}@[a-z]{2,10}[+.][a-z]{2,5}"
            condition_1 = '[!#$%^&*]'

            def check(email):
                if (re.fullmatch(condition, email)):
                    if not (re.search(condition_1, email)):
                        return True
                    else:
                        return
                else:
                    return
            email = "not valid"
            if __name__ == '__main__':
                for F in email:
                    email = input("enter id:")
                    check(email)
                    if check(email):
                        print("valid")
                        file = open("monesh.txt", "a")
                        break
                    else:
                        print("invalid")
            password = "not valid"
            for Z in password:
               password = input("enter password:")
               if re.search("[a-z]", password):
                   if re.search("[A-Z]", password):
                        if re.search("[0-9]", password):
                            if re.search("[!@#$%^&*]", password):
                                if len(password) > 5:
                                    file = open("monesh.txt", "a")
                                    file.write(email)
                                    file.write(" ")
                                    file.write(password)
                                    file.write("\n")
                                    file.close()
                                    print("successfully Register")
                                    break
                                else:
                                    print("at least use")
                            else:
                                print("use special characters")
                        else:
                            print("use digit")
                   else:
                       print("use upper")
               else:
                    print("use lower")

elif A == "Register":
    condition = "[^0-9A-Z][a-z0-9]{2,15}@[a-z]{2,10}[+.][a-z]{2,5}"
    condition_1 = '[!#$%^&*]'
    def check(email):
        if (re.fullmatch(condition, email)):
            if not (re.search(condition_1, email)):
                return True
            else:
                return
        else:
            return
    email = "not valid"
    if __name__ == '__main__':
        for F in email:
            email = input("enter id:")
            check(email)
            if check(email):
                print("valid")
                break
            else:
                print("invalid")
    password = "not valid"
    for Z in password:
        password = input("enter password:")
        if re.search("[a-z]", password):
            if re.search("[A-Z]", password):
                if re.search("[0-9]", password):
                    if re.search("[!@#$%^&*]", password):
                        if len(password) > 5:
                            file = open("monesh.txt", "a")
                            file.write(email)
                            file.write(" ")
                            file.write(password)
                            file.write("\n")
                            file.close()
                            print("successfully Register")
                            break
                        else:
                            print("at least use")
                    else:
                        print("use special characters")
                else:
                    print("use digits")
            else:
                print("use upper")
        else:
            print("use lower")





