DROP TABLE sentiment_analysis;

CREATE TABLE IF NOT EXISTS sentiment_analysis (
  twitter_name         STRING,
  place         STRING,
  about_author       STRING,
  created_at STRING,
  twitter_interface STRING,
  tweet_text   STRING,
  sentiment      INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

SHOW TABLES;

LOAD DATA LOCAL INPATH '/Users/saiaravindreddymannem/Documents/workspaces/java_workspaces/Project_Big_Data_programming/dataset/sentiment_analysis.txt' INTO TABLE sentiment_analysis;

set hive.groupby.orderby.position.alias=true;

select count(*),case when sentiment < 0 then -1 when sentiment > 0 then 1 else 0 end as analytics from sentiment_analysis 
group by 2;