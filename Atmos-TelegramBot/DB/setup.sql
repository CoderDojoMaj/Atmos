CREATE DATABASE AtmosData;
USE AtmosData;
CREATE TABLE Readings(
  id int NOT NULL AUTO_INCREMENT,
  datadate datetime NOT NULL,
  temp int,
  hum int,
  water int,
  light int,
  PRIMARY KEY(id)
);

CREATE TABLE Language(
  id varchar(100) not null,
  EN varchar(100),
  ES varchar(100),
  PRIMARY KEY(id)
);

SOURCE 'filllang.sql'; /* FILL THE LANGUAGE TABLE */
