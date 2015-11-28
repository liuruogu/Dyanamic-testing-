import os
import subprocess

test = open('universe.txt', 'r')
lines = test.read().splitlines()

# file_name = input("Please input the program name e.g. tcas, totinfo :")
file_name = "tcas"
print("1.Statement random 2.Statement_total 3.Statement_add 4.Branch_random")
test_name = input("5.Branch_total 6.Branch_add 7.Combine_random.txt 8.Combine_total 9.Combine_add ")
if test_name == "1":
    var = "Statement_random.txt"
elif test_name == "2":
    var = "Statement_total.txt"
elif test_name == "3":
    var = "Statement_add.txt"
elif test_name == "4":
    var = "Branch_random.txt"
elif test_name == "5":
    var = "Branch_total.txt"
elif test_name == "6":
    var = "Branch_add.txt"
elif test_name == "7":
    var = "Combine_random.txt"
elif test_name == "8":
    var = "Combine_total.txt"
elif test_name == "9":
    var = "Combine_add.txt"

test_process = open(var, 'r')
test_lines = test_process.read().split(',')

current = os.getcwd()
print(current)
# os.chdir("v0")
os.system("ls")
command_remove = "rm "+file_name
os.system(command_remove)

origin_set = []
compare_set = []

command_compile = "gcc -g -fprofile-arcs -ftest-coverage "+file_name+".c -o "+file_name
os.system(command_compile)
i = 0

''''go through every fault version'''
f = 1

for each in test_lines:
    command_execute = "./"+file_name+" "+lines[int(each)]
    os.system(command_execute)
    p = subprocess.Popen(command_execute, universal_newlines=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    test_output = p.stdout.read()
    retcode = p.wait()
    i+=1
    '''Get the V0 test set output'''
    origin_set.append(test_output)
    print(test_output)
    print(command_execute)
    print()
print("----", i)
print(origin_set)

fault_revel = 0
while f <= 41:
    os.chdir("/home/liu/"+file_name)
    current = os.getcwd()
    os.chdir("v"+str(f))
    command_compile = "gcc -g -fprofile-arcs -ftest-coverage "+file_name+".c -o "+file_name
    os.system(command_compile)
    current = os.getcwd()
    f+=1
    for each in test_lines:
        command_execute = "./"+file_name+" "+lines[int(each)]
        os.system(command_execute)
        p = subprocess.Popen(command_execute, universal_newlines=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test_output = p.stdout.read()
        retcode = p.wait()
        compare_set.append(test_output)
    print(compare_set)
    print(origin_set)
    if compare_set !=  origin_set:
        fault_revel += 1
    print("------------", fault_revel)
    compare_set = []