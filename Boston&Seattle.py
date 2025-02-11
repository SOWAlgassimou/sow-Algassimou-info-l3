BOS = [ 2.67, 1.00, 1.21, 3.09, 3.43, 4.71, 3.88, 3.08, 4.10, 2.62, 1.01, 5.93]
SEA = [ 6.83, 3.63, 7.20, 2.68, 2.05, 2.96, 1.04, 0.00, 0.03, 6.71, 8.28, 6.85]

total_bos = sum(BOS)
total_sea = sum(SEA)
avg_bos = total_bos / len(BOS)
avg_sea = total_sea / len(SEA)
print(f"Précipitations totales pour Boston: {total_bos:.2f} pouces")
print(f"Précipitations totales pour Seattle: {total_sea:.2f} pouces")
print(f"Précipitations moyennes mensuelles pour Boston: {avg_bos:.2f} pouces ")
print(f"Précipitations moyennes mensuelles pour Seattle: {avg_sea:.2f} pouces ")

above_avg_bos = [ month for month in BOS if month > avg_bos]
above_avg_sea = [ month for month in SEA if month > avg_sea]
print(f"Nombre de mois avec précipitation supérieurs à la moyenne à Boston: {len(above_avg_bos)}")
print(f"Nombre de mois avec précipitation supérieurs à la moyenne à Seattle: {len(above_avg_sea)}")

month_bos_less_sea = [ i + 1 for i in range(len(BOS)) if BOS[i] < SEA[i]]
num_month_bos_less_sea = len(month_bos_less_sea)
print(f"Nombre de mois ou les précipitations à Boston sont inférieurs à celles de seattle: {num_month_bos_less_sea}")
print(f"Mois correspondants: {month_bos_less_sea}")
