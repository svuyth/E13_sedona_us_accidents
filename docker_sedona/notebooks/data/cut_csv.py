import csv

input_file = r"C:\Users\svenu\Documents\FHNW\MSE\S1\GEO_AdvSpatM\E11_Aproach_Sedona\docker_sedona\US_Accidents_March23.csv"
output_file = r"C:\Users\svenu\Documents\FHNW\MSE\S1\GEO_AdvSpatM\E11_Aproach_Sedona\docker_sedona\US_Accidents_March23_100rows.csv"

max_rows = 100

with open(input_file, "r", newline="", encoding="utf-8") as infile, \
     open(output_file, "w", newline="", encoding="utf-8") as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for i, row in enumerate(reader):
        if i == 0:
            # Write header
            writer.writerow(row)
            continue

        if i <= max_rows:
            writer.writerow(row)
        else:
            break

print("Done! Saved first 100 rows to:", output_file)
