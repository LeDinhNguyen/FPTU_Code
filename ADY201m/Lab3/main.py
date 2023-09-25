import ibm_db
import sqlalchemy


dsn_hostname = "1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud"
dsn_uid = "xkk84284"        # e.g. "abc12345"
dsn_pwd = "QdRxktEwkW0eOMFE"      # e.g. "7dBZ3wWt9XN6$o0J"

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "bludb"            # e.g. "BLUDB"
dsn_port = "32286"                # e.g. "32733"
dsn_protocol = "TCPIP"            # i.e. "TCPIP"
dsn_security = "SSL"    

dsn = f"""DATABASE={dsn_database};
  HOSTNAME={dsn_hostname};
  PORT={dsn_port};
  PROTOCOL={dsn_protocol};
  UID={dsn_uid};
  PWD={dsn_pwd};
"""

ibm_db.connect( dsn, "", "")

question_1 = """
  SELECT
      `Elementary, Middle, or High School`,
      COUNT(*) as total_number_of_students
  FROM chicago
  GROUP BY `Elementary, Middle, or High School`;
"""

question_2 = """"""

question_3 = """
  SELECT ROUND(AVG(CAST(REPLACE(AVERAGE_STUDENT_ATTENDANCE, '%', '') AS DECIMAL(5, 2))),2) AS average_attendance
  FROM (
      SELECT 
        Name_OF_SCHOOL,
        AVERAGE_STUDENT_ATTENDANCE,
        SAFETY_SCORE
      FROM chicago
      ORDER BY SAFETY_SCORE
      LIMIT 10
  ) AS subquery;
"""

question_4 = """
SELECT Name_OF_SCHOOL, CAST(College_Eligibility__ AS FLOAT) AS College_Eligibility_Score
FROM chicago
WHERE COLLEGE_ELIGIBILITY__ NOT LIKE '%NDA%'
ORDER BY College_Eligibility_Score DESC
LIMIT 10;
"""