import sqlite3
import json

DATABASE = "test.db"

def init_database():
    conn = sqlite3.connect(DATABASE)
    conn.executescript("""
CREATE TABLE IF NOT EXISTS awards (
    fiscal_year TEXT,
    project_num TEXT,
    org_name TEXT,
    city TEXT,
    country TEXT,
    org_city TEXT,
    org_country TEXT,
    org_state TEXT,
    org_state_name TEXT,
    dept_type TEXT,
    fips_country_code TEXT,
    primary_duns TEXT,
    primary_uei TEXT,
    org_fips TEXT,
    org_ipf_code TEXT,
    org_zipcode TEXT,
    external_org_id TEXT,
    award_type TEXT,
    activity_code TEXT,
    abstract_text TEXT,
    award_amount TEXT
);
CREATE TABLE IF NOT EXISTS org_duns (
    external_org_id TEXT,
    dun TEXT);
CREATE TABLE IF NOT EXISTS org_ueis (
    external_org_id TEXT,
    uei TEXT);""")
    conn.commit()

def add_result_to_db(json_dict):
    """Add individual record to database"""
    conn = sqlite3.connect(DATABASE)
    sql1 = """
INSERT INTO awards
    (fiscal_year,
    project_num,
    org_name,
    city,
    country,
    org_city,
    org_country,
    org_state,
    org_state_name,
    dept_type,
    fips_country_code,
    primary_duns,
    primary_uei,
    org_fips,
    org_ipf_code,
    org_zipcode,
    external_org_id,
    award_type,
    activity_code,
    abstract_text,
    award_amount) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?); """
    conn.execute(sql1, (json_dict["fiscal_year"],
    json_dict["project_num"],
    json_dict["organization"]["org_name"],
    json_dict["organization"]["city"],
    json_dict["organization"]["country"],
    json_dict["organization"]["org_city"],
    json_dict["organization"]["org_country"],
    json_dict["organization"]["org_state"],
    json_dict["organization"]["org_state_name"],
    json_dict["organization"]["dept_type"],
    json_dict["organization"]["fips_country_code"],
    json_dict["organization"]["primary_duns"],
    json_dict["organization"]["primary_uei"],
    json_dict["organization"]["org_fips"],
    json_dict["organization"]["org_ipf_code"],
    json_dict["organization"]["org_zipcode"],
    json_dict["organization"]["external_org_id"],
    json_dict["award_type"],
    json_dict["activity_code"],
    json_dict["abstract_text"],
    json_dict["award_amount"]))

    sql2 = """INSERT INTO org_duns
    (external_org_id,
    dun) VALUES (?, ?);"""

    sql3 = """INSERT INTO org_ueis
    (external_org_id,
    uei) VALUES (?, ?);"""

    if json_dict["organization"]["org_duns"]:
        for dun in json_dict["organization"]["org_duns"]:
            conn.execute(sql2, (json_dict["organization"]["external_org_id"], dun))
    if json_dict["organization"]["org_ueis"]:
        for uei in json_dict["organization"]["org_ueis"]:
            conn.execute(sql3, (json_dict["organization"]["external_org_id"], uei))
    conn.commit()

def main():
    with open('full_output.json', 'r') as file:
        data = json.load(file)
    #print(data[0]['results'][0])   # it's a list of 2-dicts, each dict is meta and results, each results is like 500 items???
    #add_result_to_db(data[0]['results'][0])
    init_database()
    for tranche in data:
        for result in tranche["results"]:
            add_result_to_db(result)



main()
