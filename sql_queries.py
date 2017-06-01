import functions


def mentors():
    query = """SELECT CONCAT (mentors.first_name, ' ', mentors.last_name) AS full_name ,schools.name, schools.country
            FROM mentors 
            INNER JOIN schools ON mentors.city=schools.city
            ORDER BY mentors.id ASC;"""
    result_list = functions.request_data(query)
    return result_list


def all_school():
    query = """SELECT CONCAT (mentors.first_name, ' ', mentors.last_name) AS full_name, schools.name, schools.country
            FROM mentors 
            RIGHT JOIN schools ON mentors.city=schools.city
            ORDER BY mentors.id ASC;"""
    result_list = functions.request_data(query)
    return result_list


def mentors_by_country():
    query = """Select schools.country, count(mentors.first_name)
            FROM schools
            JOIN mentors ON schools.city=mentors.city
            GROUP BY schools.country;"""
    result_list = functions.request_data(query)
    return result_list


def contacts():
    query = """SELECT schools.name, CONCAT (mentors.first_name, ' ', mentors.last_name) AS full_name
            FROM schools 
            RIGHT JOIN mentors ON schools.contact_person=mentors.id
            WHERE schools.name IS NOT NULL;"""
    result_list = functions.request_data(query)
    return result_list


def applicants():
    query = """SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date
            FROM applicants
            JOIN applicants_mentors ON applicants.id=applicants_mentors.applicant_id
            WHERE applicants_mentors.creation_date >= '2016-01-01'
            ORDER BY applicants_mentors.creation_date DESC;"""
    result_list = functions.request_data(query)
    return result_list


def applicants_and_mentors():
    query = """SELECT applicants.first_name, applicants.application_code, CONCAT (mentors.first_name, ' ', mentors.last_name) AS full_name
            FROM applicants
            LEFT JOIN applicants_mentors ON applicants.id=applicants_mentors.applicant_id
            LEFT JOIN mentors ON applicants_mentors.applicant_id=mentors.id"""
    result_list = functions.request_data(query)
    return result_list
