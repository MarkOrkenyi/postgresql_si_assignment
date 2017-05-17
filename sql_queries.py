import console


def question1(cur):
    try:
        cur.execute("""SELECT first_name, last_name FROM mentors""")
    except:
        print("Failed")
    column1 = cur.description[0][0]
    column2 = cur.description[1][0]
    result_list = []
    rows = cur.fetchall()
    for entry in rows:
        result_list.append(entry)
    console.print_result(column1=column1, column2=column2, result_list=result_list)
    return result_list


def question2(cur):
    try:
        cur.execute("""SELECT nick_name FROM mentors""")
    except:
        print("Failed")
    column1 = cur.description[0][0]
    result_list = []
    rows = cur.fetchall()
    for entry in rows:
        result_list.append(entry)
    console.print_result(column1=column1, result_list=result_list)
    return result_list


def question3(cur):
    try:
        cur.execute("""SELECT first_name, last_name, phone_number FROM applicants WHERE first_name LIKE 'Carol';""")
    except:
        print("Failed")
    result = cur.fetchall()
    column1 = "full_name"
    column2 = cur.description[2][0]
    full_name = (result[0][0] + " " + result[0][1])
    phone_number = result[0][2]
    result_list = (full_name, phone_number)
    console.print_result(column1=column1, column2=column2, result_list=result_list)
    return result_list


def question4(cur):
    try:
        cur.execute(
            """SELECT first_name, last_name, phone_number, email FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu';""")
    except:
        print("Failed")
    column1 = "full_name"
    column2 = cur.description[2][0]
    column3 = cur.description[3][0]
    result = cur.fetchall()
    full_name = (result[0][0] + " " + result[0][1])
    phone_number = result[0][2]
    email = result[0][3]
    result_list = (full_name, phone_number, email)
    console.print_result(column1=column1, column2=column2, column3=column3, result_list=result_list)
    return result_list


def question5(cur):
    try:
        cur.execute("""INSERT INTO applicants (first_name, last_name, phone_number, email, application_code) VALUES ('Markus', 'Scaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823);""")
        print("Entries inserted")
    except:
        print("Failed to insert, possibly already inserted")
    cur.execute("""SELECT * FROM applicants WHERE application_code='54823';""")
    column1 = "full_name"
    column2 = cur.description[3][0]
    column3 = cur.description[4][0]
    column4 = cur.description[5][0]
    result = cur.fetchall()
    full_name = "{} {}".format(result[0][1], result[0][2])
    phone_number = result[0][3]
    email = result[0][4]
    application_code = result[0][5]
    result_list = (full_name, phone_number, email, application_code)
    console.print_result(column1=column1, column2=column2, column3=column3, column4=column4, result_list=result_list)
    return result_list


def question6(cur):
    try:
        cur.execute("""UPDATE applicants SET phone_number='003670/223-7459' WHERE first_name='Jemima' AND last_name='Foreman';""")
        print("Entries updated")
    except:
        print("Failed")
    cur.execute("""SELECT * FROM applicants WHERE first_name='Jemima' AND last_name='Foreman';""")
    column1 = "full_name"
    column2 = cur.description[3][0]
    result = cur.fetchall()
    full_name = "{} {}".format(result[0][1], result[0][2])
    phone_number = result[0][3]
    result_list = (full_name, phone_number)
    console.print_result(column1=column1, column2=column2, result_list=result_list)
    return result_list


def question7(cur):
    try:
        cur.execute("""DELETE FROM applicants WHERE email LIKE '%mauriseu.net';""")
        print("Entries deleted")
    except:
        print("Failed")
