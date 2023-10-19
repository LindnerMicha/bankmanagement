import xlsxwriter

workbook = xlsxwriter.Workbook("testMappe.xlsx")
worksheet1 = workbook.add_worksheet("Datenbank_test")

worksheet1.write("A1", "E-Mail"), worksheet1.write("B1", "Vorname"), worksheet1.write("C1", "Nachname"), worksheet1.write("D1", "Strasse"), worksheet1.write("E1", "Postcode"), worksheet1.write("F1", "Geb-Datum"), worksheet1.write("G1", "I-BAN")

workbook.close()
