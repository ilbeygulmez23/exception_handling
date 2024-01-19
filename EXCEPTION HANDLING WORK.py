import sys
try:
    f1 = open(sys.argv[1])
except IOError:
    print(f"IOError: cannot open {sys.argv[1]}")
except IndexError:
    print("IndexError: number of input files less than expected.")
try:
    f2 = open(sys.argv[2])
except IOError:
    print(f"IOError: cannot open {sys.argv[2]}")
except IndexError:
    print("IndexError: number of input files less than expected.")
f1_list=[]
f2_list = []
output_list = []
try:
    for line2 in f2:
        f2_list.append(line2.strip("\n") + "\n")
    value=0
    for line in f1:
        number_list = []
        f1_list.append(line.strip("\n")+"\n")
        try:
            div = int(float(line.split()[0]))
            nondiv = int(float(line.split()[1]))
            fromv = int(float(line.split()[2]))
            to = int(float(line.split()[3]))
            for number in range(fromv, to + 1):
                if number % div == 0 and number % nondiv != 0:
                    number_list.append(str(number))
                else:
                    pass
            print("------------")
            print('My results: '+" ".join(number_list) + "\n",end="")
            print('Results to compare: '+ f2_list[value],end="")
            if " ".join(number_list)+"\n"!=f2_list[value]:
                print("AssertionError: results don't match.")
            else:
                print("Goool!!!")
        except IndexError:
            print("------------")
            print("IndexError: number of operands less than expected.\n",end="")
            print("Given input: "+f1_list[value],end="")
        except ValueError:
            print("------------")
            print("ValueError: only numeric input is accepted.\n",end="")
            print("Given input: " + f1_list[value],end="")
        except ZeroDivisionError:
            print("------------")
            print("ZeroDivisionError: You can’t divide by 0.\n",end="")
            print("Given input: " + f1_list[value],end="")
        except:
            print("kaBOOM: run for your life!\n",end="")
        value+=1
except NameError:
    pass
finally:
    print("˜ Game Over ˜")
