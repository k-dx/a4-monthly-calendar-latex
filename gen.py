from math import floor

############# BEGIN CONFIG ############# 

# change 28 to 29 if necessary
days_per_month = [ 31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30 ]
year = "2023"
month_names = [
    "Styczeń",
    "Luty",
    "Marzec",
    "Kwiecień",
    "Maj",
    "Czerwiec",
    "Lipiec",
    "Sierpień",
    "Wrzesień",
    "Październik",
    "Listopad",
    "Grudzień",
]
weekday_names = "poniedziałek & wtorek & środa & czwartek & piątek & sobota & niedziela"
# start is on which weekday starts January of given year,
# where 0 = Monday, 1 = Tuesday, etc.
start = 6

############# END CONFIG ############# 

pos_in_week = 0

for month in range(0, 12):
    days = days_per_month[month]
    print("\\begin{landscape}")
    print("    \\begin{center}")
    print(f"        \\textbf{{\\huge{{{month_names[month]} {year}}}}}")
    print("    \\end{center}")
    print("")
    print("    \\vspace{-3mm}")
    print("")

    # tabela z dniami tygodnia
    # this is a separate table because it didn't work as one for me
    print("    \\thispagestyle{empty}")
    print("    \\noindent")
    print("    \\begin{tabularx}{28.7cm}{|Y|Y|Y|Y|Y|Y|Y|}")
    print("        \\hline")
    print(f"{weekday_names} \\\\ [-0.5mm]")
    print("        \\hline")
    print("    \\end{tabularx}")
    print("")
    print("    \\vspace{-0.5mm}")
    print("")

    # faktyczny kalendarz
    print("    \\noindent")
    print("    \\begin{tabularx}{28.7cm}{|X|X|X|X|X|X|X|}")
    print("        \\hline")
    row_count = (int)((days + start + 6) / 7)
    # print(f"row_count = {row_count}")
    row_height = floor(155/row_count)
    for i in range(0, start):
        print("& ", end="")
        pos_in_week += 1

    for i in range(1, days+1):
        # print(f"\\textbf{{{i}}} ", end="")
        print(f"{i} ", end="")
        if pos_in_week != 6:
            print("& ", end="")

        if pos_in_week == 6:
            print(f"\\\\ [{row_height:.1f}mm]")
            print("\hline")
            pos_in_week = 0
        else:
            pos_in_week += 1
    start = pos_in_week
    if pos_in_week != 0:
        for i in range(0, 6-pos_in_week):
            print("& ", end="")
        print(f"\\\\ [{row_height:.1f}mm]")
        print("\hline")
        pos_in_week = 0
    print("")
    print("    \\end{tabularx}")
    print("\\end{landscape}")
    print("")
    print("\\clearpage")
    print("")
