#! /bin/bash
cd ~/Cloudstation/Development/Eve/Analysis/ToBeLoaded/

for f in kor23.csv
do
        mysqlimport -e "USE eve1 LOAD DATA LOCAL INFILE '"$f"'INTO TABLE KLEFMSanalysis"
done

#! chmod u+x ~/Cloudstation/Development/Eve/ProdCode/DailyPull.command