import random
import xlsxwriter

vornamen = [
    "Max", "Anna", "Paul", "Lena", "Felix", "Sophie", "David", "Emma", "Luca", "Mia",
    "Liam", "Olivia", "Noah", "Isabella", "Ethan", "Ava", "Mason", "Sophia", "Logan", "Harper",
    "Aiden", "Abigail", "Lucas", "Emily", "Jackson", "Madison", "Henry", "Elizabeth", "Jacob", "Amelia",
    "Michael", "Mila", "Ella", "Oliver", "Avery", "Benjamin", "Scarlett", "William", "Grace", "Alexander", "Evelyn",
    "Sebastian", "Chloe", "Elijah", "Sofia", "Matthew", "Hannah", "Joseph", "Lily", "Daniel", "Layla", "Landon", "Zoe",
    "Carter", "Aria", "Joshua", "Nora", "Jayden", "Riley", "Dylan", "Hazel"
    ,"Owen", "Savannah", "Nathan", "Claire", "Caleb", "Penelope", "Cameron", "Luna", "Evan", "Aubrey",
    "Hunter", "Stella", "Levi", "Paisley", "Gabriel", "Skylar", "Samantha", "Leo", "Ellie", "Isaac",
    "Violet", "Mason", "Lillian", "Samuel", "Natalie", "Gavin", "Zara", "Wyatt", "Grace", "Eli", "Liliana",
    "Nicholas", "Bella", "Brandon", "Ivy", "Jordan", "Madeline", "Carson", "Nova", "Nolan", "Layla", "Lucas",
    "Nora", "Eli", "Hannah", "Jack", "Grace", "Andrew", "Lily", "Henry", "Mila",
    "Mason", "Zoe", "Carter", "Aria", "Liam", "Scarlett", "Ethan", "Sofia", "Oliver", "Layla",
    "Aiden", "Chloe", "Elijah", "Madison", "William", "Avery", "James", "Abigail", "Benjamin", "Victoria",
    "Samuel", "Audrey", "Sebastian", "Riley", "Matthew", "Natalie", "Logan", "Evelyn", "Nicholas", "Charlotte",
    "David", "Penelope", "Daniel", "Mackenzie", "John", "Sophie", "Nathan", "Alice", "Adam", "Luna",
    "Michael", "Harper", "Sophia", "Emma", "Luna", "Aiden", "Sophia", "Lucas", "Olivia", "Ethan", "Liam",
    "Olivia", "Noah", "Emma", "Oliver", "Ava", "Isabella", "Sophia", "Mia", "Charlotte",
    "Amelia", "Harper", "Evelyn", "Abigail", "Emily", "Elizabeth", "Sofia", "Mila", "Ella", "Scarlett",
    "Grace", "Aria", "Chloe", "Victoria", "Lily", "Hazel", "Penelope", "Riley", "Nora", "Zoe",
    "Layla", "Leah", "Stella", "Lillian", "Audrey", "Ellie", "Natalie", "Savannah", "Violet", "Alice",
    "Claire", "Lucy", "Luna", "Caroline", "Amara", "Maya", "Ariana", "Samantha", "Madison", "Quinn",
    "Peyton", "Taylor", "Brooklyn", "Naomi", "Zara", "Aurora", "Melanie", "Maria", "Valentina", "Valerie",
    "Ruby", "Rebecca", "Katherine", "Kaitlyn", "Kylie", "Liliana", "Adalyn", "Vivian", "Lyla", "Hannah",
    "Grace", "Ella", "Olivia", "Avery", "Mia", "Emma", "Sophia", "Charlotte", "Amelia", "Harper",
    "Evelyn", "Abigail", "Emily", "Elizabeth", "Sofia", "Mila", "Scarlett", "Victoria", "Zoe", "Nora",
    "Layla", "Stella", "Chloe", "Lily", "Penelope", "Hazel", "Ellie", "Sophia", "Aria", "Ava",
    "Oliver", "Liam", "Noah", "Ethan", "Lucas", "Mason", "Logan", "Elijah", "Aiden", "James", "Aiden", "Sophia",
    "Lucas", "Olivia", "Ethan", "Liam", "Jackson", "Charlotte", "Avery", "Emma",
    "Lucy", "Daniel", "Grace", "Benjamin", "Aria", "Matthew", "Scarlett", "Nicholas", "Zoe", "David",
    "Ella", "Joseph", "Natalie", "Samuel", "Sophie", "Eli", "Mila", "Michael", "Madeline", "James",
    "Amelia", "William", "Aubrey", "Alexander", "Ariana", "Oliver", "Riley", "Sebastian", "Samantha", "Gabriel",
    "Harper", "Jack", "Penelope", "Henry", "Stella", "Elijah", "Chloe", "Caleb", "Luna", "Nathan",
    "Victoria", "Levi", "Alice", "Isaac", "Hannah", "Owen", "Aurora", "Mason", "Lily", "Wyatt",
    "Zara", "Carson", "Ivy", "Andrew", "Layla", "Nicholas", "Paisley", "Eli", "Aria", "Joshua",
    "Nora", "Jayden", "Riley", "Dylan", "Hazel", "Owen", "Savannah", "Nathan", "Claire", "Caleb",
    "Penelope", "Cameron", "Luna", "Evan", "Aubrey", "Hunter", "Stella", "Landon", "Zoe", "Carter",
    "Aria", "Sophia", "Michael", "Mila", "Ella", "Oliver", "Avery", "Benjamin", "Scarlett", "William",
    "Grace", "Alexander", "Evelyn", "Sebastian", "Chloe", "Elijah", "Sofia", "Matthew", "Hannah", "Joseph"
]
nachnamen = [
    "Smith", "Johnson", "Brown", "Taylor", "Miller", "Anderson", "Wilson", "Moore", "Jackson", "White",
    "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee",
    "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Wright", "Lopez", "Hill", "Scott",
    "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner",
    "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins", "Stewart", "Sanchez", "Morris", "Rogers",
    "Reed", "Cook", "Morgan", "Bell", "Murphy", "Bailey", "Rivera", "Cooper", "Richardson", "Cox",
    "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez", "James", "Watson", "Brooks", "Kelly",
    "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross", "Henderson", "Coleman", "Jenkins", "Perry",
    "Powell", "Long", "Patterson", "Hughes", "Flores", "Washington", "Butler", "Simmons", "Foster", "Gonzales",
    "Bryant", "Alexander", "Russell", "Griffin", "Diaz", "Hayes", "Myers", "Ford", "Hamilton", "Graham",
    "Sullivan", "Wallace", "Woods", "Cole", "West", "Jordan", "Owens", "Reynolds", "Fisher", "Ellis",
    "Harrison", "Gibson", "Mcdonald", "Cruz", "Marshall", "Ortiz", "Gomez", "Murray", "Freeman", "Wells",
    "Webb", "Simpson", "Stevens", "Tucker", "Porter", "Hunter", "Hicks", "Crawford", "Henry", "Boyd",
    "Mason", "Morales", "Kennedy", "Warren", "Dixon", "Ramos", "Reyes", "Burns", "Gordon", "Shaw", "Morrison",
    "Austin", "Robbins", "Wagner", "Bowen", "Munoz", "Brewer", "Marshall", "Garza", "Soto",
    "Walters", "Webster", "Newton", "Smith", "Horton", "Reed", "Dunn", "Johnson", "Turner", "Harrison",
    "Keller", "Franklin", "Barrett", "Castillo", "Gibson", "Ward", "Larson", "Kim", "Gomez", "Nelson",
    "Hunt", "Diaz", "Henry", "Schmidt", "Martin", "Chavez", "Weaver", "Henderson", "Lane", "Fernandez",
    "Gardner", "Barnes", "Johnson", "Hernandez", "Garrett", "Bennett", "Hernandez", "Murphy", "Gonzales", "Fleming",
    "Dixon", "Lawrence", "Kennedy", "Coleman", "Gutierrez", "Wells", "Reyes", "Bishop", "Holland", "Griffith",
    "Owens", "Daniels", "Simmons", "Beck", "Rodriguez", "Sullivan", "Walker", "Garcia", "Duncan", "Kemp",
    "Gilbert", "Harrington", "Hayes", "Pierce", "Powell", "Austin", "Moss", "Dunn", "Perez", "Hartman",
    "Ortega", "Jordan", "Stephens", "Graves", "Black", "Mcbride", "Richards", "Ray", "Hodges", "Boone",
    "Ellis", "Parker", "Smith", "Lopez", "Keller", "Washington", "Williams", "Duncan", "Mcbride", "Harrison",
    "Daniels", "Barton", "Collins", "Barnes", "Evans", "Sullivan", "Hawkins", "Brown", "Williams", "Richardson",
    "Ross", "Powell", "Sanchez", "Mitchell", "Hunt", "Marshall", "Mcguire", "Bryant", "Bennett", "Harrison",
    "Ortiz", "Griffin", "Sullivan", "Tucker", "Walters", "Phillips", "Lewis", "Schmidt", "Myers", "Hoffman",
    "Hernandez", "Collins", "Cunningham", "Simpson", "Garcia", "King", "Williams", "Wood", "Holland", "Gardner",
    "Soto", "Lawrence", "Olson", "Ross", "Chapman", "Barton", "Thomas", "Hartman", "Martin", "Weaver",
    "Jackson", "Bryant", "Daniels", "Ramos", "Jenkins", "Ramirez", "Wright", "Watson", "Wagner", "Hernandez"
]

workbook = xlsxwriter.Workbook("testMappe.xlsx")
worksheet1 = workbook.add_worksheet("Datenbank_test")
header_format = workbook.add_format()
header_format.set_bold()
worksheet1.set_column(0, 0, 35), worksheet1.set_column(1, 1, 15), worksheet1.set_column(2, 2, 15), worksheet1.set_column(3, 3, 15), worksheet1.set_column(4, 4, 20), worksheet1.set_column(5, 5, 10), worksheet1.set_column(6, 6, 15), worksheet1.set_column(7, 7, 30)

worksheet1.write("A1", "E-Mail"), worksheet1.write("B1", "Passwort"), worksheet1.write("C1", "Vorname"), worksheet1.write("D1", "Nachname"), worksheet1.write("E1", "Strasse"), worksheet1.write("F1", "Postcode"), worksheet1.write("G1", "Geb-Datum"), worksheet1.write("H1", "I-BAN")

erg = ""
name = ""
line = 2

stuck = int(input("Wie viele Datensätze werden benötigt ? -> "))
pw_len = int(input("Wie land soll das random Passwort sein ? -> "))

def gen_pw(pw_len):
    zahlen = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    ABC = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    sond_zei = ["@", "_", "-", "#", "+", "-"]
    pw_temp = ""
    while pw_len-1 >= 0:
        ran_type = random.randint(0, 3)
        if ran_type == 0:
            pw_temp += zahlen[random.randint(0, len(zahlen)-1)]
        elif ran_type == 1:
            pw_temp += abc[random.randint(0, len(abc)-1)]
        elif ran_type == 2:
            pw_temp += ABC[random.randint(0, len(ABC)-1)]
        elif ran_type == 3:
            pw_temp += sond_zei[random.randint(0, len(sond_zei)-1)]

        pw_len -= 1

    return pw_temp
def gen_street():
    strassen_erg = ""
    strassen_vornamen = ["Smith", "Johnson", "Brown", "Williams", "Jones", "Davis", "Wilson", "Miller", "Moore", "Taylor",
                         "Jackson", "Harris", "White", "Martin", "Clark", "Lee", "Robinson", "Walker", "Hall", "Young",
                         "Wright", "Scott", "Lewis", "King", "Baker", "Adams", "Nelson", "Harrison", "Garcia", "Martinez",
                         "Roberts", "Turner", "Cook", "Perez", "Morris", "Hill", "Watson", "Evans", "Reed", "Gonzalez",
                         "Carter", "Parker", "Bell", "Bailey", "Rivera", "Cooper", "Howard", "Ward", "Torres", "Peterson",
                         "Gray", "Barnes", "Ross", "Henderson", "Coleman", "Jenkins", "Perry", "Powell", "Long", "Patterson",
                         "Hughes", "Fisher", "Gomez", "Murray", "Webb", "Simpson", "Stevens", "Tucker", "Porter", "Hunter",
                         "Hicks", "Crawford", "Boyd", "Mason", "Morales", "Kennedy", "Warren", "Dixon", "Ramos", "Reyes",
                         "Burns", "Gordon", "Shaw", "Holmes", "Rice", "Robertson", "Hunt", "Black", "Daniels", "Palmer",
                         "Mills", "Nichols", "Grant", "Knight", "Ferguson", "Rose", "Stone", "Hawkins", "Dunn", "Perkins",
                         "Hudson", "Spencer", "Gardner", "Stephens", "Payne", "Pierce", "Berry", "Matthews", "Arnold", "Wagner",
                         "Willis", "Ray", "Watkins", "Olson", "Carroll", "Duncan", "Snyder", "Hart", "Cunningham", "Bradley",
                         "Lane", "Andrews", "Ruiz", "Harper", "Fox", "Riley", "Armstrong", "Carpenter", "Weaver", "Greene",
                         "Lawrence", "Elliott", "Chavez", "Sims", "Austin", "Peters", "Kelley", "Franklin", "Lawson", "Fields",
                         "Patterson", "Matthews", "Arnold", "Wagner", "Willis", "Ray", "Watkins", "Olson", "Carroll", "Duncan",
                         "Snyder", "Hart", "Cunningham", "Bradley", "Lane", "Andrews", "Ruiz", "Harper", "Fox", "Riley",
                         "Armstrong", "Carpenter", "Weaver", "Greene", "Lawrence", "Elliott", "Chavez", "Sims", "Austin", "Peters",
                         "Kelley", "Franklin", "Lawson", "Fields", "Gutierrez", "Ryan", "Schmidt", "Vasquez", "Castillo", "Wheeler",
                         "Bradley", "Simmons", "Ferguson", "Ellis", "Hartman", "Morton", "Salazar", "Mendoza", "Roth", "Griffith",
                         "Gaines", "Shaw", "Stevens", "Hicks", "Pierce", "Joseph", "Perkins", "Wheeler", "Nicholson", "Rogers",
                         "Carr", "Holmes", "Jones", "Freeman", "Hunt", "Lynch", "Porter", "Baldwin", "Sullivan", "Powell",
                         "Thornton", "Gardner", "Davidson", "Clarke", "Patterson", "Bryant", "Hudson", "Spencer", "Henderson", "Knight",
                         "Ross", "Barrett", "Matthews", "Stone", "Lawson", "Fields", "Dunn", "Olson", "Cunningham", "Riley",
                         "Fox", "Simmons", "Ryan", "Snyder", "Hartman", "Griffith", "Hicks", "Pierce", "Joseph", "Freeman",
                         "Mendoza", "Hunt", "Gutierrez", "Gaines", "Rogers", "Nicholson", "Morton", "Salazar", "Bradley", "Wagner",
                         "Jones", "Baldwin", "Carr", "Thornton", "Lynch", "Sullivan", "Clarke", "Davidson", "Knight", "Hudson"]
    strassen_enden = [" Street", "-Straße", "-Gasse", "-Weg"]

    strassen_erg += strassen_vornamen[random.randint(0, len(strassen_vornamen)-1)]
    strassen_erg += strassen_enden[random.randint(0, len(strassen_enden)-1)]

    return strassen_erg
def gen_postcode():
    postcode_len = 4
    zahlen = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    postcode_erg = ""
    while postcode_len >= 0:
        postcode_erg += zahlen[random.randint(0, 9)]
        postcode_len -= 1
    return postcode_erg
def gen_birth():
    birth_day = random.randint(1, 31)
    birth_month = random.randint(1,12)
    birth_year = random.randint(1950, 2023)
    return str(f"{birth_day}.{birth_month}.{birth_year}")
def gen_iban():
    laender_num = random.randint(10, 99)
    blz_num = random.randint(10000000, 99999999)
    knt_nummer = random.randint(1000000000, 9999999999)
    return f"DE{laender_num} {blz_num} {knt_nummer}"

while stuck >= 1:
    pw_temp = 0

    var_vorname = random.randint(0, len(vornamen)-1)
    var_nachname = random.randint(0, len(nachnamen)-1)

    worksheet1.write(f"A{line}", f"{vornamen[var_vorname]}.{nachnamen[var_nachname]}@test-mail.de")
    worksheet1.write(f"B{line}", f"{gen_pw(pw_len)}")
    worksheet1.write(f"C{line}", f"{vornamen[var_vorname]}")
    worksheet1.write(f"D{line}", f"{nachnamen[var_nachname]}")
    worksheet1.write(f"E{line}", f"{gen_street()}")
    worksheet1.write(f"F{line}", f"{gen_postcode()}")
    worksheet1.write(f"G{line}", f"{gen_birth()}")
    worksheet1.write(f"H{line}", f"{gen_iban()}")


    line += 1
    stuck -= 1

workbook.close()