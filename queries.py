import pymysql.cursors


def getRooms():
    db = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='intelligentsystem',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.Cursor)

    cursor = db.cursor()

    sql = "SELECT * FROM rooms"
    try:

        cursor.execute(sql)
        results = cursor.fetchall()
        return results

    except:
        return None

    db.close()


def getStudents():
    db = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='intelligentsystem',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.Cursor)

    cursor = db.cursor()

    sql = "SELECT * FROM stud"
    try:

        cursor.execute(sql)
        results = cursor.fetchall()
        return results

    except:
        return None

    db.close()




def auth(stdid, pas):
    db = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='intelligentsystem',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.Cursor)

    cursor = db.cursor()

    sql = "SELECT * FROM staff where stid='" + stdid + "' and stpass='" + pas + "'"
    try:

        cursor.execute(sql)
        results = cursor.fetchone()
        return results

    except:
        return None

    db.close()

def readData(val):
    db = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='intelligentsystem',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.Cursor)

    cursor = db.cursor()

    sql = "SELECT * FROM stud where studid='" + str(val) + "'" 
    try:

        cursor.execute(sql)
        results = cursor.fetchone()
        return results

    except:
        return "unknown"

    db.close()


def insertData(stdid, name, degree, semister, status):
    db = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='intelligentsystem',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.Cursor)

    cursor = db.cursor()

    sql = "INSERT INTO stud values('" + stdid + "','" + name + "','" + degree + "','" + semister + "','" + status + "')"
    try:

        cursor.execute(sql)

        db.commit()

    except Exception as e:

        return None

    db.close()

    return "None"