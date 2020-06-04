#!/usr/bin/env zsh
cd ~/Documents/GitHub/Task_Tracker
python TaskTracker.py


cd ~/Documents/GitHub/COVID-19

git pull

cd ~/Documents/GitHub/Covid-Dashboard/

python COVID_KPI_Scraper.py

R -e "knitr::purl('Update_COVID_Data.RMD')"
Rscript Update_COVID_Data.R
rm Update_COVID_Data.R

git add Tableau_Data
git add Update_COVID_Data.Rmd
git add csse_covid_19_data/csse_covid_19_time_series
git commit -m "changes made on $(date +%d.%m.%y)"
git push

open COVID-19\ by\ Analytica\ Consulting.twbx
