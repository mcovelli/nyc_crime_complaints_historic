# nyc_crime_complaints_historic
Analysis of NYC Crime trends, Borough comparisons and offense types

### Work in progress...

## Data Cleaning Log  
**Project:** NYPD Crime Complaints  
**Dataset:** NYPD Complaint Data Historic (NYC Open Date)  
**Tool:** Python/Pandas  
**Date:** March 2026  
**Analyst:** Michael Covelli  
  
1. ### Dataset Overview  
   | Attribute  | Detail  |
   | ---------  | ------- |
   | Source | NYPD Complaint Data Historic (NYC Open Data) |
   | Original Format | CSV |
   | Imported Format | CSV |
   | Total Rows | 9.5M |
   | Total Columns | 35 |
   | Date Range | January 1, 1989 - December 31, 2024 |
   
2. ### Data Dictionary  

   | # | Column  | Type  | Description |
   | --- | ---------  | ------- | -------- |
   | 1 | CMPLNT_FR_DT | text | Exact date of occurence (if CMPLNT_TO_DT exists) |
   | 2 | CMPLNT_FR_TM | text | exact time of occurence (if CMPLNT_TO_TM exists) |
   | 3 | RPT_DT | text | Date the incident was reported to the police |
   | 4 | OFNS_DESC |	text | Description of offense corresponding with KY_CD  |
   | 5 | LAW_CAT_CD | text | Level of Offense (felony, misdemeanor, violation) |
   | 6 | BORO_NM | text | Name of the borough in which the incident occurred |
   | 7 | SUSP_AGE_GROUP | text | Suspect's Age Group |
   | 8 | SUSP_RACE | text | Suspect's Race Description |
   | 9 | SUSP_SEX | text | Suspect's Sex Desciption |
   | 10 | VIC_AGE_GROUP	| text | Victim's Age Group |	
   | 11 | VIC_RACE |	text | Victim's Race Desciption |
   | 12 | VIC_SEX |	text | Victim's Sex Description |

   The original table contained 35 rows, 12 of which were chosen for this analysis. Columns like latitude, longitude, station_nm, etc. were too granular for a borough based analysis

4. ### Number of Null values in each column
  | Column | # of Nulls | Resolution |
  | ----- | ------ | ------ |
  | CMPLNT_FR_DT | 655 | dropped |
  | CMPLNT_FR_TM | 48 | dropped |
  | RPT_DT | 0 | n/a  |
  | OFNS_DESC | 18894 | dropped |
  | LAW_CAT_CD | 0 |  n/a |
  | BORO_NM | 8719 | dropped |
  | SUSP_AGE_GROUP | 4649568 | kept, filtered out during analysis  |
  | SUSP_RACE | 3753075 | kept, filtered out during analysis |
  | SUSP_SEX | 3886446 | kept, filtered out during analysis |
  | VIC_AGE_GROUP | 1623568 | kept, filtered out during analysis |
  | VIC_RACE | 760 | dropped  |
  | VIC_SEX | 308 | dropped |  

  *Approximately 40 - 49% of suspect information such as age, sex and race is missing which indicates the suspect wasn't found or no arrests had been made.  
  
6. ### Important Issues and Resolutions  
   | # | Issue  | Resolution  |   Outcome |
   | --- | ---------  | ------- | -------- |
  
7. ### Data Type Corrections
   
   | Column | Original Type  | Corrected Type  |   Reason |
   | --- | ---------  | ------- | -------- |
   | CMPLNT_FR_DT | text | Date | Required for incident date analysis |
   | RPT_DT | text | date | Required for report delay analysis |
   | CMPLNT_FR_TM | text | time | Required for time based analysis |
   
    
9. ### Data Verification Checks  
     
   5.1  
   **Question:**  
   **Risk:**  
    
   ``` {sql}

   ```    
    
   **Result:** 
   
  
10. ### Notable Data Observations  
   | Observation | Detail | Action Taken |
   | --- | ---------  | ------- |
   |   |   |   |  
     
11. ### Final Dataset Summary  
   | Metric | Value |
   | --- | ---------  |
   | Total Rows | 9.5M |
   | Date Range | January 1, 1989 - December 31 - 2024 |
   | Validation Checks Passed |  |
   | Import Issues resolved |  |  
  
11. ### Known Limitations  
   - Dataset covers January 1, 1989 - December 31, 2024. Data my not reflect current crime statistics.
   - Analysis does not include precise location information such as longitude, latitude, station_nm.
   - Approximately 40 - 49% of suspect information such as age, sex and race is missing

*This code is MIT licensed and the dataset is CC BY-SA 4.0*  

[NYC Dataset](https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i/about_data)
