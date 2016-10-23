drop schema if exists 607project3;

CREATE SCHEMA 607project3 ;
USE 607project3;

DROP TABLE IF EXISTS Descriptions;
DROP TABLE IF EXISTS Frequency;

CREATE TABLE 607project3.Descriptions (
    DescriptionsName varchar(125) not null, 
  DescriptionsType varchar(125) not null,
  DescriptionsCategory varchar(125) not null,
  PRIMARY KEY (DescriptionsName));
  
  CREATE TABLE 607project3.Frequency (
   FrequencyName varchar(125) not null, 
  FrequencyTotal int NULL,
    PRIMARY KEY (FrequencyName));
    
    
-- verify correct file location
    LOAD DATA LOCAL INFILE 'C:/Users/OmegaCel/Documents/GitHub/DataAnalyticsProjects/Project3/Frequency.csv' 
INTO TABLE frequency
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
(FrequencyName, FrequencyTotal);

-- verify correct file location

    LOAD DATA LOCAL INFILE 'C:/Users/OmegaCel/Documents/GitHub/DataAnalyticsProjects/Project3/Descriptions.csv' 
INTO TABLE Descriptions
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
(DescriptionsName, DescriptionsType,DescriptionsCategory);

-- The frequency table needed to be alter after loading the data in order to create a relationship.
alter table frequency
add FOREIGN KEY Frequency(FrequencyName) REFERENCES Descriptions(DescriptionsName);

-- This is the final view for the data analysis.

create view reportingdata as
select UPPER(DescriptionsName) as 'skillname' ,DescriptionsType,DescriptionsCategory,FrequencyTotal
from 607project3.Descriptions left join Frequency 
   on DescriptionsName = FrequencyName
   order by FrequencyTotal desc;




