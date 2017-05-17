
def question1(cur):
    cur.execute("""SELECT first_name, last_name FROM mentors""")
    rows = cur.fetchall()
    for entry in rows:
        print(entry)


def question2(cur):
    cur.execute("""SELECT nick_name FROM mentors""")
    rows = cur.fetchall()
    for entry in rows:
        print(entry)


def question3(cur):
    cur.execute("""SELECT first_name, last_name, phone_number, email FROM applicants WHERE first_name LIKE 'Carol';""")
    result = cur.fetchall()
    full_name = "{} {}".format(result[0][0], result[0][1])
    phone_number = result[0][2]
    email = result[0][3]
    print(full_name, phone_number, email)


def question4(cur):
    cur.execute("""SELECT first_name, last_name, phone_number, email FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu';""")
    result = cur.fetchall()
    full_name = "{} {}".format(result[0][0], result[0][1])
    phone_number = result[0][2]
    email = result[0][3]
    print(full_name, phone_number, email)


def question5(cur):
    try:
        cur.execute("""INSERT INTO applicants (first_name, last_name, phone_number, email, application_code) VALUES ('Markus', 'Scaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823);""")
        print("success")
    except:
        print("Failed")
    cur.execute("""SELECT * FROM applicants WHERE application_code='54823';""")
    result = cur.fetchall()
    full_name = "{} {}".format(result[0][1], result[0][2])
    phone_number = result[0][3]
    email = result[0][4]
    print(full_name, phone_number, email)


def question6(cur):
    try:
        cur.execute("""UPDATE applicants SET phone_number='003670/223-7459' WHERE first_name='Jemima' AND last_name='Foreman';""")
        print("success")
    except:
        print("Failed")
    cur.execute("""SELECT * FROM applicants WHERE first_name='Jemima' AND last_name='Foreman';""")
    result = cur.fetchall()
    full_name = "{} {}".format(result[0][1], result[0][2])
    phone_number = result[0][3]
    email = result[0][4]
    print(full_name, phone_number, email)


def question7(cur):
    try:
        cur.execute("""DELETE FROM applicants WHERE email LIKE '%mauriseu.net';""")
        print("success")
    except:
        print("Failed")
