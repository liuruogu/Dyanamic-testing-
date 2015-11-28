import os
import random
# -g -fprofile-arcs -ftest-coverage tcas.c -o tcas

def CombineTotalPri(program_name, test_cases):
    Branch_coverage_info = CombineTraverse(test_cases, program_name)
    Biggest_index = 0
    Biggest_so_far = 0
    Biggest_so_far_coverage = 0
    test_cases_collect = []
    gcov_name = program_name+".c.gcov"
    command_delete = "rm "+program_name+".gcda"
    os.system(command_delete)
    Biggest_so_far_coverage = CombineAddPri(program_name, test_cases)
    test_cases_collect = []
    print("----------------------", Biggest_so_far_coverage)
    os.system(command_delete)
    for each in Branch_coverage_info:
        Biggest_so_far = max(Branch_coverage_info)
        Biggest_index = Branch_coverage_info.index(Biggest_so_far)
        test_cases_collect.append(Biggest_index)
        print("The biggest coverage information is at the", Biggest_index, "which is", Branch_coverage_info[Biggest_index])
        Branch_coverage_info[Biggest_index] = 0

        command = "./"+program_name+" "+test_cases[Biggest_index]
        command_gcov = "gcov -b -c "+program_name+".c"
        os.system(command)
        os.system(command_gcov)
        gcov_read = open(gcov_name, 'r')

        line_number = 0
        branch_count = 0
        branch_count_infeasible = 0
        branch_coverage = 0
        Statement_count_infeasible = 0
        Statement_meanless = 0
        Statement_coverage = 0

        lines = gcov_read.read().splitlines()
        for each in lines:
            line_number += 1
            if each[0:6] == 'branch':
                branch_count += 1
                if each[16:17] == '0' or each[16:17] == 'e':
                    branch_count_infeasible += 1
                else:
                    branch_coverage += 1
            elif each[0:4]!='call' and each[0:8]!='function'and each[8:9]!='_':
                if each[8:9] == '#':
                    Statement_count_infeasible += 1
                elif each[8:9] == '-':
                    Statement_meanless += 1
                else:
                    Statement_coverage += 1
        if branch_coverage+Statement_coverage == Biggest_so_far_coverage:
            break
        print(line_number, branch_count, branch_coverage, Statement_coverage)
        print("-------------------", test_cases_collect)

    return 0

def CombineAddPri(program_name, test_cases):
    Branch_coverage_info = CombineTraverse(test_cases, program_name)
    Biggest_index = 0
    Biggest_so_far = 0
    Biggest_coverage = 0
    test_cases_collect = []
    gcov_name = program_name+".c.gcov"
    command_delete = "rm "+program_name+".gcda"
    os.system(command_delete)

    '''count the number of the every test cases'''
    for each in test_cases:
        Biggest_so_far = max(Branch_coverage_info)
        Biggest_index = Branch_coverage_info.index(Biggest_so_far)
        Branch_coverage_info[Biggest_index] = 0

        command = "./"+program_name+" "+test_cases[Biggest_index]
        command_gcov = "gcov -b -c "+program_name+".c"
        os.system(command)
        os.system(command_gcov)
        gcov_read = open(gcov_name, 'r')
        lines = gcov_read.read().splitlines()
        '''record the line number of each statement'''
        line_number = 0
        branch_count = 0
        branch_count_infeasible = 0
        branch_coverage = 0
        Statement_count_infeasible = 0
        Statement_meanless = 0
        Statement_coverage = 0

        for each in lines:
            line_number += 1
            if each[0:6] == 'branch':
                branch_count += 1
                if each[16:17] == '0' or each[16:17] == 'e':
                    branch_count_infeasible += 1
                else:
                    branch_coverage += 1
            elif each[0:4]!='call' and each[0:8]!='function'and each[8:9]!='_':
                if each[8:9] == '#':
                    Statement_count_infeasible += 1
                elif each[8:9] == '-':
                    Statement_meanless += 1
                else:
                    Statement_coverage += 1

        if branch_coverage+Statement_coverage > Biggest_coverage:
            Biggest_coverage = branch_coverage+Statement_coverage
            test_cases_collect.append(Biggest_index)
        print(line_number, branch_count, branch_coverage, Statement_coverage)
        print("-------------------", test_cases_collect)

    return Biggest_coverage

'''AC For Random Prioritization of Branch'''
def CombineRandomPri(program_name, test_cases):
    test_cases_collect = []
    gcov_name = program_name+".c.gcov"
    command_delete = "rm "+program_name+".gcda"
    os.system(command_delete)
    Biggest_so_far_Coverage = 0
    '''count the number of the every test cases'''
    for each in test_cases:
        '''Should be match line number after+1'''
        Random_case = random.randrange(0, len(test_cases))
        print("This is the", Random_case, ":",test_cases[Random_case])
        command = "./"+program_name+" "+test_cases[Random_case]
        command_gcov = "gcov -b -c "+program_name+".c"
        os.system(command)
        os.system(command_gcov)
        gcov_read = open(gcov_name, 'r')
        lines = gcov_read.read().splitlines()
        '''record the line number of each statement'''
        line_number = 0
        branch_count = 0
        branch_count_infeasible = 0
        branch_coverage = 0
        Statement_count_infeasible = 0
        Statement_meanless = 0
        Statement_coverage = 0

        for each in lines:
            line_number += 1
            if each[0:6] == 'branch':
                branch_count += 1
                if each[16:17] == '0' or each[16:17] == 'e':
                    branch_count_infeasible += 1
                else:
                    branch_coverage += 1
            elif each[0:4]!='call' and each[0:8]!='function'and each[8:9]!='_':
                if each[8:9] == '#':
                    Statement_count_infeasible += 1
                elif each[8:9] == '-':
                    Statement_meanless += 1
                else:
                    Statement_coverage += 1

        if branch_coverage+Statement_coverage > Biggest_so_far_Coverage:
            Biggest_so_far_Coverage = branch_coverage+Statement_coverage
            test_cases_collect.append(Random_case)
        print(line_number, branch_count, branch_coverage, Statement_coverage)
        print("-------------------", test_cases_collect)

def BranchRandomPri(program_name, test_cases):
    test_cases_collect = []
    gcov_name = program_name+".c.gcov"
    command_delete = "rm "+program_name+".gcda"
    os.system(command_delete)
    Biggest_so_far_Coverage = 0
    '''count the number of the every test cases'''
    for each in test_cases:
        '''Should be match line number after+1'''
        Random_case = random.randrange(0, len(test_cases))
        print("This is the", Random_case, ":",test_cases[Random_case])
        command = "./"+program_name+" "+test_cases[Random_case]
        command_gcov = "gcov -b -c "+program_name+".c"
        os.system(command)
        os.system(command_gcov)
        gcov_read = open(gcov_name, 'r')
        lines = gcov_read.read().splitlines()
        '''record the line number of each statement'''
        branch_count = 0
        branch_count_infeasible = 0
        branch_coverage = 0

        for each in lines:

            if each[0:6] == 'branch':
                branch_count += 1
                # print("Branch number ", branch_count)
                # print(each[0:6])
                if each[16:17] == '0' or each[16:17] == 'e':
                    # print(each[16:17])
                    branch_count_infeasible += 1
                    # print("Infeasible branch ", branch_count_infeasible)
                else:
                    branch_coverage += 1
                    # print("Feasible branch", branch_coverage)
        if branch_coverage > Biggest_so_far_Coverage:
            Biggest_so_far_Coverage = branch_coverage
            test_cases_collect.append(Random_case)
        print(branch_count, branch_count_infeasible, branch_coverage)
        print("-------------------", test_cases_collect)

    return 0

'''AC For Random Prioritization of Statement'''
def StatementRandomPri(program_name, test_cases):
    print(test_cases)
    original_test_cases = test_cases
    test_cases_collect = []
    gcov_name = program_name+".c.gcov"
    command_delete = "rm "+program_name+".gcda"
    os.system(command_delete)
    Biggest_so_far_Coverage = 0
    '''count the number of the every test cases'''
    for each in test_cases:
        '''Should be match line number after+1'''
        Random_case = random.randrange(0, len(test_cases))
        print("This is the", Random_case, ":",test_cases[Random_case])
        command = "./"+program_name+" "+test_cases[Random_case]
        command_gcov = "gcov "+program_name+".c"
        os.system(command)
        os.system(command_gcov)
        gcov_read = open(gcov_name, 'r')
        lines = gcov_read.read().splitlines()
        '''record the line number of each statement'''
        lines_num = 0
        Statement_meanless = 0
        Statement_count_infeasible = 0
        Statement_coverage = 0

        for each in lines:
            lines_num += 1
            if each[8:9] == '#':
                Statement_count_infeasible += 1
            elif each[8:9] == '-':
                Statement_meanless += 1
            else:
                Statement_coverage += 1
        if Statement_coverage > Biggest_so_far_Coverage:
            Biggest_so_far_Coverage = Statement_coverage
            test_cases_collect.append(Random_case)
        print(lines_num, Statement_meanless, Statement_count_infeasible, Statement_coverage)
        print("-------------------", test_cases_collect)


'''AC For Total Branch coverage prioritization '''
def Add_branch_coverage(program_name, test_cases):
    Branch_coverage_info = BranchTraverse(test_cases, program_name)
    Biggest_index = 0
    Biggest_so_far = 0
    Biggest_so_far_coverage = 0
    test_cases_collect = []
    gcov_name = program_name+".c.gcov"
    command_delete = "rm "+program_name+".gcda"
    os.system(command_delete)

    '''count the number of the every test cases'''
    for each in test_cases:
        Biggest_so_far = max(Branch_coverage_info)
        Biggest_index = Branch_coverage_info.index(Biggest_so_far)
        Branch_coverage_info[Biggest_index] = 0

        command = "./"+program_name+" "+test_cases[Biggest_index]
        command_gcov = "gcov -b -c "+program_name+".c"
        os.system(command)
        os.system(command_gcov)
        gcov_read = open(gcov_name, 'r')
        lines = gcov_read.read().splitlines()
        '''record the line number of each statement'''
        branch_count = 0
        branch_count_infeasible = 0
        branch_coverage = 0

        for each in lines:
            if each[0:6] == 'branch':
                branch_count += 1
                if each[16:17] == '0' or each[16:17] == 'e':
                    branch_count_infeasible += 1
                else:
                    branch_coverage += 1
        if branch_coverage > Biggest_so_far_coverage:
            Biggest_so_far_coverage = branch_coverage
            test_cases_collect.append(Biggest_index)
        print(branch_count, branch_count_infeasible, branch_coverage)
        print("-------------------", test_cases_collect)

    return branch_coverage

'''AC for total statement coverage prioritization'''
def Add_statement_coverage(program_name, test_cases):
    Statement_coverage_info = StatementTraverse(test_cases, program_name)
    Biggest_index = 0
    Biggest_so_far = 0
    Biggest_so_far_coverage = 0
    test_cases_collect = []
    gcov_name = program_name+".c.gcov"
    command_delete = "rm "+program_name+".gcda"
    os.system(command_delete)

    for each in Statement_coverage_info:
        Biggest_so_far = max(Statement_coverage_info)
        Biggest_index = Statement_coverage_info.index(Biggest_so_far)
        Statement_coverage_info[Biggest_index] = 0

        command = "./"+program_name+" "+test_cases[Biggest_index]
        command_gcov = "gcov "+program_name+".c"
        os.system(command)
        os.system(command_gcov)
        gcov_read = open(gcov_name, 'r')

        lines_num = 0
        Statement_count_infeasible = 0
        Statement_meanless = 0
        Statement_coverage = 0

        lines = gcov_read.read().splitlines()
        for each in lines:
            lines_num += 1
            if each[8:9] == '#':
                Statement_count_infeasible += 1
            elif each[8:9] == '-':
                Statement_meanless += 1
            else:
                Statement_coverage += 1
        if Statement_coverage > Biggest_so_far_coverage:
            Biggest_so_far_coverage = Statement_coverage
            test_cases_collect.append(Biggest_index)
        # print(lines_num, Statement_meanless, Statement_count_infeasible, Statement_coverage)
        # print("-------------------", test_cases_collect)

    return Statement_coverage

'''AC for total statement coverage prioritization'''
def TotalStatementPri(program_name, test_cases):
    Statement_coverage_info = StatementTraverse(test_cases, program_name)
    Biggest_index = 0
    Biggest_so_far = 0
    Biggest_so_far_coverage = 0
    test_cases_collect = []
    gcov_name = program_name+".c.gcov"
    command_delete = "rm "+program_name+".gcda"
    os.system(command_delete)
    Biggest_so_far_coverage = Add_statement_coverage(program_name, test_cases)
    test_cases_collect = []
    print("----------------------", Biggest_so_far_coverage)
    os.system(command_delete)
    for each in Statement_coverage_info:
        Biggest_so_far = max(Statement_coverage_info)
        Biggest_index = Statement_coverage_info.index(Biggest_so_far)
        test_cases_collect.append(Biggest_index)
        # print("The biggest coverage information is at the", Biggest_index, "which is",Statement_coverage_info[Biggest_index])
        Statement_coverage_info[Biggest_index] = 0

        command = "./"+program_name+" "+test_cases[Biggest_index]
        command_gcov = "gcov "+program_name+".c"
        os.system(command)
        os.system(command_gcov)
        gcov_read = open(gcov_name, 'r')

        lines_num = 0
        Statement_count_infeasible = 0
        Statement_meanless = 0
        Statement_coverage = 0

        lines = gcov_read.read().splitlines()
        for each in lines:
            lines_num += 1
            if each[8:9] == '#':
                Statement_count_infeasible += 1
            elif each[8:9] == '-':
                Statement_meanless += 1
            else:
                Statement_coverage += 1

        if Statement_coverage == Biggest_so_far_coverage:
            break
        print(lines_num, Statement_meanless, Statement_count_infeasible, Statement_coverage)
        print("-------------------", test_cases_collect)

    '''AC For Total Branch coverage prioritization'''
def TotalBranchPri(program_name, test_cases):
    Branch_coverage_info = BranchTraverse(test_cases, program_name)
    Biggest_index = 0
    Biggest_so_far = 0
    Biggest_so_far_coverage = 0
    test_cases_collect = []
    gcov_name = program_name+".c.gcov"
    command_delete = "rm "+program_name+".gcda"
    os.system(command_delete)
    Biggest_so_far_coverage = Add_branch_coverage(program_name, test_cases)
    test_cases_collect = []
    print("----------------------", Biggest_so_far_coverage)
    os.system(command_delete)
    for each in Branch_coverage_info:
        Biggest_so_far = max(Branch_coverage_info)
        Biggest_index = Branch_coverage_info.index(Biggest_so_far)
        test_cases_collect.append(Biggest_index)
        print("The biggest coverage information is at the", Biggest_index, "which is", Branch_coverage_info[Biggest_index])
        Branch_coverage_info[Biggest_index] = 0

        command = "./"+program_name+" "+test_cases[Biggest_index]
        command_gcov = "gcov -b -c "+program_name+".c"
        os.system(command)
        os.system(command_gcov)
        gcov_read = open(gcov_name, 'r')

        branch_count = 0
        branch_count_infeasible = 0
        branch_coverage = 0

        lines = gcov_read.read().splitlines()
        for each in lines:
            if each[0:6] == 'branch':
                branch_count += 1
                if each[16:17] == '0' or each[16:17] == 'e':
                    branch_count_infeasible += 1
                else:
                    branch_coverage += 1
        if branch_coverage == Biggest_so_far_coverage:
            break
        print(branch_count, branch_count_infeasible, branch_coverage)
        print("###############", test_cases_collect)


'''!!!Collect all information for branch coverage'''
def gcov_branch(program):
    gcov_name = program+".c.gcov"
    '''record the line number of each branch'''
    lines_num = 0
    branch_count = 0
    branch_count_infeasible = 0
    branch_coverage = 0
    gcov_read = open(gcov_name, 'r')
    lines = gcov_read.read().splitlines()
    for each in lines:
        if each[0:6] == 'branch':
            branch_count += 1
            # print("Branch number ", branch_count)
            # print(each[0:6])
            if each[16:17] == '0' or each[16:17] == 'e':
                # print(each[16:17])
                branch_count_infeasible += 1
                # print("Infeasible branch ", branch_count_infeasible)
            else:
                branch_coverage += 1
                # print("Feasible branch", branch_coverage)
        lines_num += 1
        # print(lines_num)
    # print(branch_count, branch_count_infeasible, branch_coverage)
    return branch_coverage

'''!!!!!!! Collect information for each test cases in terms of statement coverage'''
def gcov_statement(program):
    gcov_name = program+".c.gcov"
    '''record the line number of each statement'''
    lines_num = 0
    Statement_meanless = 0
    Statement_count_infeasible = 0
    Statement_coverage = 0
    gcov_read = open(gcov_name, 'r')
    lines = gcov_read.read().splitlines()
    for each in lines:
        lines_num += 1
        if each[8:9] == '#':
            Statement_count_infeasible += 1
        elif each[8:9] == '-':
            Statement_meanless += 1
        else:
            Statement_coverage += 1
    # print(lines_num, Statement_meanless, Statement_count_infeasible, Statement_coverage)
    return Statement_coverage

    '''Traverse the universe file and collect date gcov of every test cases'''

def gcov_total(program):
    gcov_name = program+".c.gcov"
    '''record the line number of each branch'''
    lines_num = 0
    branch_count = 0
    branch_count_infeasible = 0
    branch_coverage = 0
    Statement_count_infeasible = 0
    Statement_meanless = 0
    Statement_coverage = 0
    Coverage_total = 0
    gcov_read = open(gcov_name, 'r')
    lines = gcov_read.read().splitlines()

    for each in lines:
        lines_num += 1
        if each[0:6] == 'branch':
            branch_count += 1
            if each[16:17] == '0' or each[16:17] == 'e':
                branch_count_infeasible += 1
            else:
                branch_coverage += 1
        elif each[0:4]!='call' and each[0:8]!='function'and each[8:9]!='_':
            if each[8:9] == '#':
                Statement_count_infeasible += 1
            elif each[8:9] == '-':
                Statement_meanless += 1
            else:
                Statement_coverage += 1
        Coverage_total = branch_coverage+Statement_coverage
    return Coverage_total

def CombineTraverse(test_cases, program_name):
    i = 0
    print(program_name)
    Total_count = []
    '''count the number of the test case'''
    for each in test_cases:
        command = "./"+program_name+" "+each
        command_gcov = "gcov -b -c "+program_name+".c"
        Total_count.append(gcov_total(program_name))
        command_delete = "rm "+program_name+".gcda"
        os.system(command)
        os.system(command_gcov)
        os.system(command_delete)
        i=i+1
    print(Total_count)
    return Total_count

def BranchTraverse(test_cases, program_name):
    i = 0
    print(program_name)
    Branch_count = []
    '''count the number of the test case'''
    for each in test_cases:
        # print(each)
        # print(i)
        command = "./"+program_name+" "+each
        command_gcov = "gcov -b -c "+program_name+".c"
        Branch_count.append(gcov_branch(program_name))
        command_delete = "rm "+program_name+".gcda"
        os.system(command)
        os.system(command_gcov)
        os.system(command_delete)
        i=i+1
    # print(Branch_count)
    return Branch_count


'''Traverse the universe file and collect date gcov of every test cases'''
def StatementTraverse(test_cases, program_name):
    i = 0
    # print(program_name)
    Statement_count = []
    '''count the number of the every test cases'''
    for each in test_cases:
        # print(each)
        # print(i)
        command = "./"+program_name+" "+each
        command_gcov = "gcov "+program_name+".c"
        Statement_count.append(gcov_statement(program_name))
        command_delete = "rm "+program_name+".gcda"
        os.system(command)
        os.system(command_gcov)
        os.system(command_delete)
        i=i+1

    return Statement_count

'''For coverage criteria'''
'''Every statement has to be executed at least once'''
def StatementCoverage(program_name):
    test = open('universe.txt', 'r')
    lines = test.read().splitlines()
    # StatementTraverse(lines, program_name)
    '''using Random prioritization to generate test cases'''
    aa = input("1. Random Pripritization 2. Total Prioritization 3. Additional Prioritization ")
    if aa == '1':StatementRandomPri(program_name, lines)
    elif aa == '2':TotalStatementPri(program_name, lines)
    elif aa =='3': Add_statement_coverage(program_name, lines)

    return 0

'''For every branch every true or false must be execute at least once'''
def BranchCoverage(program_name):
    test = open('universe.txt', 'r')
    lines = test.read().splitlines()
    # BranchTraverse(lines, program_name)
    '''using Random prioritization to generate test cases'''
    aa = input("1. Random Pripritization 2. Total Prioritization 3. Additional Prioritization , 4.Branch Traverse")
    if aa == '1': BranchRandomPri(program_name, lines)
    elif aa == '2':TotalBranchPri(program_name, lines)
    elif aa =='3':Add_branch_coverage(program_name, lines)
    elif aa == '4':BranchTraverse(lines, program_name)

    return 0

'''Combine Coverage Criteria'''
def CombineCoverage(program_name):
    test = open('universe.txt', 'r')
    lines = test.read().splitlines()
    aa = input("1. Random Pripritization 2. Total Prioritization 3. Additional Prioritization  4.Combine traverse  ")
    if aa == '1':CombineRandomPri(program_name, lines)
    elif aa == '2':CombineTotalPri(program_name, lines)
    elif aa =='3': CombineAddPri(program_name, lines)
    elif aa =='4': CombineTraverse(lines, program_name)

    return 0

def main():
    # file_name = input("Please input the program name e.g. tcas, totinfo :")
    file_name = 'tcas'
    cc = input("1. Statement Coverage Criteria 2. Branch Coverage Criteria 3. Combine Coverage Criteria:")
    if cc == "1":
        StatementCoverage(file_name)
    elif cc == "2":
        BranchCoverage(file_name)
    elif cc == "3":
        CombineCoverage(file_name);

if __name__ == '__main__':
    main()