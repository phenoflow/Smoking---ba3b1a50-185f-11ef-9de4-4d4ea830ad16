# Matthew J Carr, Darren M Ashcroft, Evangelos Kontopantelis, David While, Yvonne Awenat, Jayne Cooper, Carolyn Chew-Graham, Nav Kapur, Roger T Webb, 2024.

import sys, csv, re

codes = [{"code":"137P.00","system":"readv2"},{"code":"137N.00","system":"readv2"},{"code":"1372.00","system":"readv2"},{"code":"137O.00","system":"readv2"},{"code":"1372.11","system":"readv2"},{"code":"137R.00","system":"readv2"},{"code":"137S.00","system":"readv2"},{"code":"137j.00","system":"readv2"},{"code":"137A.00","system":"readv2"},{"code":"1375.00","system":"readv2"},{"code":"9ko..11","system":"readv2"},{"code":"1378.00","system":"readv2"},{"code":"9km..11","system":"readv2"},{"code":"1377.00","system":"readv2"},{"code":"137H.00","system":"readv2"},{"code":"137J.00","system":"readv2"},{"code":"137l.00","system":"readv2"},{"code":"1379.00","system":"readv2"},{"code":"137P.11","system":"readv2"},{"code":"1373.00","system":"readv2"},{"code":"137B.00","system":"readv2"},{"code":"1374.00","system":"readv2"},{"code":"1376.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('smoking-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["smoking-exsmoker---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["smoking-exsmoker---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["smoking-exsmoker---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
