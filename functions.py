import psycopg2


def request_data(query):
    try:
        connect_str = "dbname='markorkenyi' user='markorkenyi' host='localhost' password='shadow123'"
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
    except:
        print("I am unable to connect to the database")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result


'''options = ["Question 1", "Question 2", "Question 3", "Question 4", "Question 5", "Question 6", "Question 7"]
valid_options = [1, 2, 3, 4, 5, 6, 7, "x"]
selected_option = 0
while selected_option != "x":
    selected_option = console.start_screen(options)
    if selected_option == "x":
        break
    elif selected_option.isalpha() or int(selected_option) not in valid_options:
        print("Not a valid option!")
        continue
    console.select_query(int(selected_option), cur)
    back_to_start = input("Press enter to return to the main menu")
    os.system('clear')'''
