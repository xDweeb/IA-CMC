
use efmrevision;

create table produit_SCD (
id_historique int primary key, 
id_produit int,  
nom varchar(25),  
categorie varchar(50),  
sous_categorie varchar(50),
date_debut date ,
date_fin date );



insert into produit_SCD (id_historique,
id_produit,nom,
categorie,sous_categorie,
date_debut,
date_fin)
select row_number() over (order by id_produit) as id_historique,
id_produit,nom,categorie,sous_categorie,"2024-02-01" ,null from produit 
;



update produit_SCD 
SET date_fin = "2024-02-20"
where id_produit = 5 ;


insert into produit_SCD (id_historique,
id_produit,
nom,
categorie,sous_categorie,
date_debut,
date_fin)
values (6,5,
"Chips",
"Aliments apéritifs","",curdate(),null);



insert into produit_SCD (id_historique,
id_produit,
nom,
categorie,sous_categorie,
date_debut,
date_fin)
values (7,5,
"Chips",
"Aliments apéritifs2","",curdate(),null);


update produit_SCD 
SET date_fin = "2024-03-10"
where id_historique = 6;



select * from produit_scd 
where date_fin is  null and  id_produit=5;


CREATE TABLE  date_dim (
      Date_PK INT NOT NULL,
      DATTE DATE NOT NULL ,
      jour_semaine VARCHAR(10) NOT NULL,
      Jour_mois INT NOT NULL,
      Mois_num INT NOT NULL, 
      Mois_nom VARCHAR(15) NOT NULL,
      Annee INT NOT NULL,
      PRIMARY KEY (Date_PK),
      INDEX (DATTE)
);

CREATE TABLE  nombres (
       id INT 
       );
      
DELIMITER //
CREATE PROCEDURE genererNomber(IN idDepart INT, IN idFin INT)
BEGIN
	DECLARE i INT;
    SET i = idDepart;
    WHILE i <= idFin DO
         INSERT INTO nombres (id) VALUES (i);
         SET i = i + 1;
	END WHILE;
END//


CALL genererNomber(0, 400);


SELECT id, DATE_ADD('2024-01-01', INTERVAL id DAY) 
AS dateGeneree FROM nombres
WHERE DATE_ADD('2024-01-01', INTERVAL id DAY) <= '2024-12-31';



SELECT r.id , r.dateGeneree, DAYNAME(r.dateGeneree) AS Jour_Semaine 
FROM (
	SELECT id, DATE_ADD('2024-01-01', INTERVAL id DAY) 
	AS dateGeneree FROM nombres
	WHERE DATE_ADD('2024-01-01', INTERVAL id DAY) <= '2024-12-31'
) AS r;




SELECT r.id , r.dateGeneree, DAYNAME(r.dateGeneree) AS Jour_Semaine ,
		DAYOFMONTH(r.dateGeneree) as Jour_Mois,
        MONTH(r.dateGeneree) AS Mois_num,
        MONTHNAME(r.dateGeneree) AS Mois_nom ,
        YEAR(r.dateGeneree) AS Annee 
FROM (
	SELECT id, DATE_ADD('2024-01-01', INTERVAL id DAY) 
	AS dateGeneree FROM nombres
	WHERE DATE_ADD('2024-01-01', INTERVAL id DAY) <= '2024-12-31'
) AS r;



INSERT INTO date_dim (Date_Pk, DATTE, Jour_semaine, Jour_mois, Mois_num, Mois_nom, Annee)
SELECT DATE_FORMAT(r.dateGeneree, '%Y%m%d') AS Date_Pk , r.dateGeneree, DAYNAME(r.dateGeneree) ,
		DAYOFMONTH(r.dateGeneree) , MONTH(r.dateGeneree),
        MONTHNAME(r.dateGeneree),
        YEAR(r.dateGeneree) AS Annee 
FROM (
	SELECT id, DATE_ADD('2024-01-01', INTERVAL id DAY) 
	AS dateGeneree FROM nombres
	WHERE DATE_ADD('2024-01-01', INTERVAL id DAY) <= '2024-12-31'
) AS r;








SELECT id, DATE_ADD('2024-01-01', INTERVAL id DAY) AS dateGeneree
FROM nombres
WHERE DATE_ADD('2024-01-01', INTERVAL id DAY) <= '2024-12-31';



SELECT r.id, r.dateGeneree, DAYNAME(r.dateGeneree) AS Jour_Semaine
FROM (
    SELECT id, DATE_ADD('2024-01-01', INTERVAL id DAY) AS dateGeneree
    FROM nombres
    WHERE DATE_ADD('2024-01-01', INTERVAL id DAY) <= '2024-12-31'
) AS r;



SELECT r.id, r.dateGeneree, DAYNAME(r.dateGeneree) AS Jour_Semaine,
    DAYOFMONTH(r.dateGeneree) AS Jour_Mois,
    MONTH(r.dateGeneree) AS Mois_num,
    MONTHNAME(r.dateGeneree) AS Mois_nom,
    YEAR(r.dateGeneree) AS Annee
FROM (
    SELECT id, DATE_ADD('2024-01-01', INTERVAL id DAY) AS dateGeneree
    FROM nombres
    WHERE DATE_ADD('2024-01-01', INTERVAL id DAY) <= '2024-12-31'
) AS r;


INSERT INTO date_dim (Date_Pk, DATTE, Jour_semaine, Jour_mois, Mois_num, Mois_nom, Annee)
SELECT DATE_FORMAT(r.dateGeneree, '%Y%m%d') AS Date_Pk, r.dateGeneree, DAYNAME(r.dateGeneree),
    DAYOFMONTH(r.dateGeneree), MONTH(r.dateGeneree),
    MONTHNAME(r.dateGeneree), YEAR(r.dateGeneree)
FROM (
    SELECT id, DATE_ADD('2024-01-01', INTERVAL id DAY) AS dateGeneree
    FROM nombres
    WHERE DATE_ADD('2024-01-01', INTERVAL id DAY) <= '2024-12-31'
) AS r;