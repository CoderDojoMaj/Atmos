CREATE DATABASE Atmos;

USE Atmos;

CREATE TABLE MeteoData (
fecha DATETIME NOT NULL,
temp INTEGER NOT NULL DEFAULT 0,
hum INTEGER NOT NULL DEFAULT 0,
luz INTEGER NOT NULL DEFAULT 0,
pres INTEGER NOT NULL DEFAULT 0
);

CREATE INDEX idx_MeteoData_Fecha ON MeteoData (fecha);

CREATE TABLE Lang (
ID VARCHAR(100) NOT NULL UNIQUE,  /* code for the word/phrase  */
EN VARCHAR(100) NOT NULL,         /* english translation       */
ES VARCHAR(100) NOT NULL,         /* spanish translation       */
PRIMARY KEY(ID)
);

/*      Fill the language table with translations and codes    */
INSERT INTO Lang(ID, EN, ES) VALUES('main_menu', 'Main menu', 'Menú principal');
INSERT INTO Lang(ID, EN, ES) VALUES('tmp_menu', 'Temperature menu', 'Menú temperatura');
INSERT INTO Lang(ID, EN, ES) VALUES('hum_menu', 'Humidity menu', 'Menú humedad');
INSERT INTO Lang(ID, EN, ES) VALUES('lig_menu', 'Light menu', 'Menú luz');
INSERT INTO Lang(ID, EN, ES) VALUES('prs_menu', 'Pressure menu', 'Menú presión');

INSERT INTO Lang(ID, EN, ES) VALUES('max_tmp', 'Max. temp.', 'Temp. máx.');
INSERT INTO Lang(ID, EN, ES) VALUES('min_tmp', 'Min. temp.', 'Temp. mín.');
INSERT INTO Lang(ID, EN, ES) VALUES('avg_tmp', 'Avg. temp.', 'Temp. media');
INSERT INTO Lang(ID, EN, ES) VALUES('cur_tmp', 'Current temp.', 'Temp. actual');

INSERT INTO Lang(ID, EN, ES) VALUES('max_hum', 'Max. humidity', 'Humedad máx.');
INSERT INTO Lang(ID, EN, ES) VALUES('min_hum', 'Min. humidity', 'Humedad mín.');
INSERT INTO Lang(ID, EN, ES) VALUES('avg_hum', 'Avg. humidity', 'Humedad media');
INSERT INTO Lang(ID, EN, ES) VALUES('cur_hum', 'Current humidity', 'Humedad actual');

INSERT INTO Lang(ID, EN, ES) VALUES('max_hum', 'Max. humidity', 'Humedad máx.');
INSERT INTO Lang(ID, EN, ES) VALUES('min_hum', 'Min. humidity', 'Humedad mín.');
INSERT INTO Lang(ID, EN, ES) VALUES('avg_hum', 'Avg. humidity', 'Humedad media');
INSERT INTO Lang(ID, EN, ES) VALUES('cur_hum', 'Current humidity', 'Humedad actual');

INSERT INTO Lang(ID, EN, ES) VALUES('max_prs', 'Max. pressure', 'Presión máx.');
INSERT INTO Lang(ID, EN, ES) VALUES('min_prs', 'Min. pressure', 'Presión mín.');
INSERT INTO Lang(ID, EN, ES) VALUES('avg_prs', 'Avg. pressure', 'Presión media');
INSERT INTO Lang(ID, EN, ES) VALUES('cur_prs', 'Current pressure', 'Presión actual');

INSERT INTO Lang(ID, EN, ES) VALUES('max_lig', 'Max. light', 'Luz máx.');
INSERT INTO Lang(ID, EN, ES) VALUES('min_lig', 'Min. light', 'Luz mín.');
INSERT INTO Lang(ID, EN, ES) VALUES('avg_lig', 'Avg. light', 'Luz media');
INSERT INTO Lang(ID, EN, ES) VALUES('cur_lig', 'Current light', 'Luz actual');

INSERT INTO Lang(ID, EN, ES) VALUES('back', 'Go back', 'Volver');
