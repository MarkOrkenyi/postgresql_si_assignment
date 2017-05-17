import os
import sql_queries


def print_result(column1, column2=None, column3=None, column4=None, result_list=None):
    if column4:
        print("{:<17}| {:<15} | {:<26} | {:<12} |".format(column1, column2, column3, column4))
        print("{}".format("-" * 56))
    elif column3:
        print("{:<12}| {:<15} | {:<30} |".format(column1, column2, column3))
        print("{}".format("-" * 42))
    elif column2:
        print("{:<14}| {:<15} |".format(column1, column2))
        print("{}".format("-" * 28))
    else:
        print("{:<12}|".format(column1))
        print("{}".format("-" * 14))
    if type(result_list) == tuple:
        if len(result_list) == 2:
            print("{:<12}| {:<12} |".format(result_list[0], result_list[1]))
        elif len(result_list) == 3:
            print("{:<12}| {:<12} | {:<12} |".format(result_list[0], result_list[1], result_list[2]))
        elif len(result_list) == 4:
            print("{:<12}| {:<12} | {:<12} | {:<16} |".format(
                result_list[0], result_list[1], result_list[2], result_list[3]))
    elif len(result_list[0]) > 1:
        for entry in result_list:
            print("{:<12}| {:<12} |".format(entry[0], entry[1]))
    else:
        for entry in result_list:
            print("{:<12}|".format(entry[0]))
    print()


def start_screen(options):
    print("SQL - SI WEEK ASSIGNMENT")
    print("Select from the following options, then enter it's number")
    for number, option in enumerate(options):
        print("({}) - {}".format(number + 1, option))
    print("(X) - Exit application")
    selected_option = input("")
    return selected_option


def select_query(number, cur):
    if number == 1:
        os.system('clear')
        sql_queries.question1(cur)
    elif number == 2:
        os.system('clear')
        sql_queries.question2(cur)
    elif number == 3:
        os.system('clear')
        sql_queries.question3(cur)
    elif number == 4:
        os.system('clear')
        sql_queries.question4(cur)
    elif number == 5:
        os.system('clear')
        sql_queries.question5(cur)
    elif number == 6:
        os.system('clear')
        sql_queries.question6(cur)
    elif number == 7:
        os.system('clear')
        sql_queries.question7(cur)
