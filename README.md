# nyc_crime_complaints_historic
analysis of historic nypd crime complaints

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
   | 1 | CMPLNT_NUM | text | randomly generated unique id |
   | 2 | CMPLNT_FR_DT | date | Exact date of occurence (if CMPLNT_TO_DT exists) |
   | 3 | CMPLNT_FR_TM | time (hh:mm:ss) | exact time of occurence (if CMPLNT_TO_TM exists) |
   | 4 | CMPLNT_TO_DT | date | Ending Date of occurence (if the exact time of occurence is unknown) |
   | 5 | CMPLNT_TO_TM | time (hh:mm:ss) | Ending Time of occurence (if exact time of occurence is unknown) |
   | 6 | ADDR_PCT_CD | number | The precent in wich the incident occured |
   | 7 | RPT_DT | text | Date the incident was reported to the police |
   | 8 | KY_CD	| int | Three digit offense classification code |	
   | 9 | OFNS_DESC |	text | Description of offense corresponding with KY_CD  |
   | 10 | PD_CD |	number | Three digit internal classification code (more granular than KY_CD) |
   | 11 | PD_DESC | text | Description of internal classification corresponding with PD_CD |
   | 12 | CRM_ATPT_CPTD_CD | text | Indicator of whether the crime as successfully completed or attempted, but failed or was interrupted prematurely |
   | 13 | LAW_CAT_CD | text | Level of Offense (felony, misdemeanor, violation) |
   | 14 | BORO_NM | text | Name of the borough in which the incident occurred |
   | 15 | LOC_OF_OCCUR_DESC | text | Specific location of occurrence in or around the premises (inside, opposite of, front of, rear of_ |
   | 16 | PREM_TYP_DESC | text | Specific description of the premises (grocery store, residence, street, etc.) |
   | 17 | JURIS_DESC | text | Desciption of the jurisdiction code |
   | 18 | JURISDICTION_CODE	| number | Jurisdiction responsible for incident; internal: Police(0), Transit(1) and Housing(2); or eternal(3) like Correction, Port Authorty, etc. |	
   | 19 | PARKS_NM |	text | Name of NYC park, playground or greenspace of occurence, if applicable (state parks excluded) |
   | 20 | HADEVELOPT |	text | Name of the NYCHA housing development of occurrence, if applicable) |
   | 21 | HOUSING_PSA | text | Development Level Code |
   | 22 | X_COORD_CD | number | X-coordinate for New York State Plane Coordinate System, Long Island Zone, NAD 83, units, feet (FIPS 3104) |
   | 23 | Y_COORD_CD | text | Y-coordinate for New York State Plane Coordinate System, Long Island Zone, NAD 83, units, feet (FIPS 3104) |
   | 24 | SUSP_AGE_GROUP | text | Suspect's Age Group |
   | 25 | SUSP_RACE | text | Suspect's Race Description |
   | 26 | SUSP_SEX | text | Suspect's Sex Desciption |
   | 27 | TRANSIT_DISTRICT | number | Transit District in which offense occurred |
   | 28 | Latitude	| number | Midblock Latitude coordinate for Global Coordinate System, WGS 1984, decimal degrees (EPSG 4326) |	
   | 29 | Longitude |	number | Midblock Longitutde coordinate for Global Coordinate System WGS 1984, decimal degrees (EPSG 4326) |
   | 30 | Lat_Lon |	Location | Geospatial Location Point (latitude and Longitude combined) |
   | 31 | PATROL_BORO | text | The name of the patrol borough in which the incident occurred |
   | 32 | STATION_NAME | text | Transit station name |
   | 33 | VIC_AGE_GROUP	| text | Victim's Age Group |	
   | 34 | VIC_RACE |	text | Victim's Race Desciption |
   | 35 | VIC_SEX |	text | Victim's Sex Description |  
     
4. ### Important Issues and Resolutions  
   | # | Issue  | Resolution  |   Outcome |
   | --- | ---------  | ------- | -------- |
  
4. ### Data Type Corrections
   
   |Table | Column | Original Type  | Corrected Type  |   Reason |
   | ---- | --- | ---------  | ------- | -------- |
    
5. ### Data Verification Checks  
     
   5.1  
   **Question:**  
   **Risk:**  
    
   ``` {sql}

   ```    
    
   **Result:** 
   
  
6. ### Notable Data Observations  
   | Observation | Detail | Action Taken |
   | --- | ---------  | ------- |
   |   |   |   |  
     
7. ### Final Dataset Summary  
   | Metric | Value |
   | --- | ---------  |
   | Total Rows | 9.5M |
   | Date Range | January 1, 1989 - December 31 - 2024 |
   | Validation Checks Passed |  |
   | Import Issues resolved |  |  
  
8. ### Known Limitations  
   - Dataset covers February 16, 2026 – March 9, 2026 only — findings may not reflect current oil prices.
   - Dataset does not consider other economic and political factors such as the Russia-Ukraine War.  

*This code is MIT licensed and the dataset is CC BY-SA 4.0*  

[Kaggle Dataset](https://www.kaggle.com/datasets/zkskhurram/global-petrol-prices-impact-of-2026-us-iran-war)
