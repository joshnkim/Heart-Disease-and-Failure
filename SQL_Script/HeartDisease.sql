create database Heart_Disease;
use Heart_Disease;

select * from heartdisease;

alter table heartdisease
add column PatientID int not null auto_increment primary key first;


set SQL_SAFE_UPDATES = 0;
set @id :=0;
update heartdisease
set PatientID = (@id := @id + 1); 
set SQL_SAFE_UPDATES = 1;

select * from heartdisease;
-- is heart disease more prevalent in males or females? 
select Sex, HeartDisease from heartdisease;

-- what age does heart disease frequency start ot increase? 
select Age, HeartDisease from heartdisease;

-- do younger people or older people tend to be asymptomatic with heart disease?
select Age, ChestPainType, HeartDisease from heartdisease;

-- number of people in each blood pressure class
select 
	case 
		when RestingBP < 131 then 'lower blood pressure'
        else 'higher blood pressure'
	end as `blood pressure categories`,
    count(*) as `number of people`, 
    round(avg(HeartDisease) * 100, 2) as `heart disease rate`
from heartdisease 
group by `blood pressure categories`;

select RestingBP, count(*) as 'number of people' from heartdisease group by RestingBP order by RestingBP;

-- bp vs heart disease
select  
	PatientID, 
    RestingBP, 
    HeartDisease
from heartdisease 
where RestingBP is not null 
order by RestingBP; 

-- does having certain chest pains correlate to resting ECG patterns?
select ChestPainType, restingECG from heartdisease;

-- chest pain and ecg correlation to heart disease
select 
	ChestPainType, 
	restingECG, 
    round(avg(HeartDisease)*100, 2) as `Heart Disease Rate` 
from heartdisease 
group by ChestPainType, restingECG;


-- which ST slope has the highest percentage of heart disease?
-- normal = upsloping
select ST_Slope, round(avg(HeartDisease) * 100, 2) as 'Heart Disease Rate'
from heartdisease
group by ST_Slope
order by ST_Slope;

select 
	ST_Slope, 
    count(*) as `Number of Patients` 
from heartdisease
group by ST_Slope;


-- oldpeak and st_slope correlation
select 
	ST_Slope, 
    round(avg(Oldpeak), 2),
    round(avg(HeartDisease) * 100, 2)
from heartdisease 
group by ST_Slope;



-- is heart pain on its own enough to determine whether someone is prone to heart disease?
select ChestPainType, ExerciseAngina, HeartDisease from heartdisease;

-- at what point does cholesterol dictate the likelihood of heart disease?
select
    case
        when Cholesterol < 200 THEN 'Desirable (<200)'
        when Cholesterol BETWEEN 200 AND 239 THEN 'Borderline (200-239)'
        else 'High (>=240)'
    end as CholesterolGroup,
    round(avg(HeartDisease)*100, 2) as HeartDiseasePercent,
    count(*) as NumPatients
from heartdisease
group by CholesterolGroup
order by NumPatients;

-- does cholesterol affect presence of exercise angina?
select exerciseAngina from heartdisease;
select 
	case 
		when Cholesterol < 200 THEN 'Desirable (<200)'
        when Cholesterol BETWEEN 200 AND 239 THEN 'Borderline (200-239)'
        else 'High (>=240)'
	end as CholesterolGroup, 
   
round(avg(
	case 
		when exerciseAngina = 'Y' then 1
        else 0
	end ) *100, 2) as averageAngina
from heartdisease
group by CholesterolGroup;

-- fasting blood sugar and hd rates
select 
	FastingBS, 
    round(avg(HeartDisease)*100, 2) as `Heart Disease Percentage` 
from heartdisease
group by FastingBS; 


select FastingBS, count(*) from heartdisease group by FastingBS;

-- normal ecg and no exercise angina vs heart disease? aka hidden condition?
select restingECG, exerciseAngina, ChestPainType, HeartDisease from heartdisease;

-- find hidden condition?
select 
	restingECG,
    case
        when Cholesterol < 200 THEN 'Desirable (<200)'
        when Cholesterol BETWEEN 200 AND 239 THEN 'Borderline (200-239)'
        else 'High (>=240)'
    end as CholesterolGroup,
	exerciseAngina, 
    ChestPainType, 
    HeartDisease 
from heartdisease;

-- more attributes, bs filter = 0
select 
	restingECG,
    case
        when Cholesterol < 200 THEN 'Desirable (<200)'
        when Cholesterol BETWEEN 200 AND 239 THEN 'Borderline (200-239)'
        else 'High (>=240)'
    end as CholesterolGroup,
	exerciseAngina, 
    ChestPainType, 
    FastingBS,
    HeartDisease 
from heartdisease
where FastingBS = 0;

-- more attributes, bs filter = 1
select 
	restingECG,
    case
        when Cholesterol < 200 THEN 'Desirable (<200)'
        when Cholesterol BETWEEN 200 AND 239 THEN 'Borderline (200-239)'
        else 'High (>=240)'
    end as CholesterolGroup,
	exerciseAngina, 
    ChestPainType, 
    FastingBS,
    HeartDisease 
from heartdisease
where FastingBS = 1;










