from sqlite3 import connect

from re import match


def vaildation_check(reg_no):
    re_pattern = r"^(PIET|PGI|PCE)(\d{2})([A-Z]{2})(\d{3,})"
    match_reg_no = match(re_pattern, reg_no)
    if(match_reg_no):
        if(match_reg_no.group(1) == "PIET"):
            piet_conn = connect("PIET.db")
            piet_cur = piet_conn.cursor()
            if(match_reg_no.group(2)) =='19':
                check = piet_cur.execute("SELECT * FROM FIRSTYEAR WHERE registration_number = ?;", (reg_no, )).fetchall()
                if(check):
                    return True
                else:
                    return False
            elif(match_reg_no.group(2)) =='18':
                check = piet_cur.execute("SELECT * FROM SECONDYEAR WHERE registration_number = ?;", (reg_no, )).fetchall()
                if(check):
                    return True
                else:
                    return False
            elif(match_reg_no.group(2)) =='17':
                check = piet_cur.execute("SELECT * FROM THIRDYEAR WHERE registration_number = ?;", (reg_no, )).fetchall()
                if(check):
                    return True
                else:
                    return False
            else:
                check = piet_cur.execute("SELECT * FROM FOURTHYEAR WHERE registration_number = ?;", (reg_no, )).fetchall()
                if(check):
                    return True
                else:
                    return False
        else:
            pgi_conn = connect("PGI.db")
            pgi_cur = pgi_conn.cursor()
            if(match_reg_no.group(2)) =='19':
                check = pgi_cur.execute("SELECT * FROM FIRSTYEAR WHERE registration_number = ?;", (reg_no, )).fetchall()
                if(check):
                    return True
                else:
                    return False
            elif(match_reg_no.group(2)) =='18':
                check = pgi_cur.execute("SELECT * FROM SECONDYEAR WHERE registration_number = ?;", (reg_no, )).fetchall()
                if(check):
                    return True
                else:
                    return False
            elif(match_reg_no.group(2)) =='17':
                check = pgi_cur.execute("SELECT * FROM THIRDYEAR WHERE registration_number = ?;", (reg_no, )).fetchall()
                if(check):
                    return True
                else:
                    return False
            else:
                check = pgi_cur.execute("SELECT * FROM FOURTHYEAR WHERE registration_number = ?;", (reg_no, )).fetchall()
                if(check):
                    return True
                else:
                    return False
    else:
        return False

if __name__ == '__main__':
    reg_no = input("Enter reg_no.: ")
    print(vaildation_check(reg_no))