import sqlite3

def printProfile(lmbcDB):
    conn = sqlite3.connect(lmbcDB)
    c = conn.cursor()
    c.execute("SELECT fname, lname, username, mID FROM User;")
    for row in c:
        print '[*] -- User Found --'
        print '[+] User: ' + str(row[0]) + " " + str(row[1])
        print '[+] Username: ' + str(row[2])
        print '[+] mID: ' + str(row[3])
        print ''
def main():
    lmbcDB = '/root/Code/flasklm/app.db'
    printProfile(lmbcDB)

if __name__ == '__main__':
    main()