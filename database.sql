CREATE DATABASE cr;


CREATE TABLE c_sta(
       id_c INT,
       ocu CHAR,
       ont DATETIME,
       oft DATETIME,
       inco FLOAT,
       CONSTRAINT bookkey PRIMARY KEY(id_c)
);

CREATE TABLE stu(
       id_s INT,
       name VARCHAR(40),
       cls VARCHAR(40),
       psw VARCHAR(20),
       sx VARCHAR(10),
       sno CHAR(12),
       PRIMARY KEY(id_s,sno)
);

CREATE TABLE d_total(
       ic_da VARCHAR(17),
       inco FLOAT,
       id_c INT
);

CREATE TABLE rate(
       netfee FLOAT);


INSERT INTO c_sta VALUES
(1,'N',NULL,NULL,0);
INSERT INTO c_sta VALUES
(2,'N',NULL,NULL,0);
--....

INSERT INTO stu VALUES
(1,'User1','class1','password1','man','201507040319');
INSERT INTO stu VALUES
(2,'User2','class2','password2','woman','201507040318');
INSERT INTO stu VALUES
(3,'User3','class2','1','woman','0');
--....

INSERT INTO rate VALUES
(1);--yuan/persec


UPDATE rate SET netfee =2;
UPDATE rate SET netfee =31.01;
--UPDATE...
