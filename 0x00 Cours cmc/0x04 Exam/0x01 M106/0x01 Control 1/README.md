### Correction Control 1 ETL

1. **le rôle principal de l'ETL dans la BI :**
- [ ] Gérer les ressources humaines
- [ ] Fournir des informations détaillées sur les activités
- [x] **Faciliter la collecte, la transformation et le chargement des données**

2. **la phase du processus ETL où les données brutes sont nettoyées et converties aux formats appropriés est :**
- [ ] Extraction
- [ ] Chargement
- [x] **Transformation**

3. **Le Data Lifecycle Management (DLM) :**
- [ ] Un processus de fabrication de données
- [x] **Un processus de gestion des données du début à la fin**
- [ ] Un processus de suppression des données

4. **Les composants clés d'un processus ETL :**
- [ ] Extraction, Filtrage, Chargement
- [ ] Stockage, Transformation, Analyse
- [x] **Extraction, Transformation, Chargement**

**5. L'objectif des outils de restitution :**
- [ ] Complexifier l'accès à l'information
- [x] **Générer des rapports et des tableaux de bord**
- [ ] Appliquer des règles de transformation des données

6. **Le fonctionnement de Talend repose sur :**
- [x] **L’installation de JDK et l’utilisation du langage Java**
- [ ] L’installation de JDK et l’utilisation du langage Python
- [ ] L’installation de JDK et l’utilisation du langage C#

7. **L’extraction/chargement incrémental(e) :**
- [x] **ETL ne charge que les données modifiées/ajoutées depuis la dernière exécution.**
- [ ] ETL charge toutes les données à chaque exécution.
- [ ] Elle ne fonctionne que pour les petits ensembles de données.

8. **Où est positionné l’ETL dans la chaîne décisionnelle :**
- [x] **En amont**
- [ ] En aval
- [ ] Au milieu

9. **Que signifie l’acronyme OLAP ?**
- [x] **Online Analytical Processing**
- [ ] Onsite Local Analysis Platform
- [ ] Offline Automated Learning Process


**10. La différence entre un Datamart et un Data Warehouse :**
- [ ] Un Datamart est une version obsolète d'un Data Warehouse
- [x] **Un Data Warehouse contient toutes les données de l'entreprise, tandis qu'un Datamart contient des données spécifiques à un domaine**
- [ ] Il n'y a aucune différence, ce sont des synonymes

### Questions de cours

1. **Donne la définition de BI/Informatique décisionnelle (0.5pts) :**
   La Business Intelligence (BI), ou informatique décisionnelle, est la technologie utilisée pour la collecte, l’analyse et la production d’informations pour soutenir les décisions d’affaires. [M106, page 9](https://myaidrive.com/gGoFsP8V2dB4ArSF/M106.pdf?pdfPage=9).

2. **Donne la définition de Système d’information décisionnel (1pts) :**
   Un système d’information décisionnel est structuré pour transformer les données en informations utiles pour prendre des décisions stratégiques. Il utilise des processus ETL pour intégrer et préparer les données, stockées ensuite dans des entrepôts de données et analysées via des outils de reporting. [M106, page 13](https://myaidrive.com/gGoFsP8V2dB4ArSF/M106.pdf?pdfPage=13).

3. **Donne la définition de Système d’information opérationnel (1pts) :**
   Un système d’information opérationnel gère les opérations quotidiennes d'une organisation, incluant des ERP pour la gestion des ressources, CRM pour la gestion des clients, et autres bases de données pour stocker les données transactionnelles. [M106, page 12](https://myaidrive.com/gGoFsP8V2dB4ArSF/M106.pdf?pdfPage=12).

4. **Qu’est-ce que l’ETL ? (1pts) :**
   L'ETL (Extract, Transform, Load) est un processus en trois étapes permettant d'extraire des données brutes de sources multiples, de les transformer pour les préparer à l'utilisation, et de les charger dans un entrepôt de données. [M106, page 27](https://myaidrive.com/gGoFsP8V2dB4ArSF/M106.pdf?pdfPage=27).

5. **De quelles phases l’ETL est composé ? (0.5pts) :**
   L’ETL est composé de trois phases : Extraction, Transformation, Chargement. [M106, page 31](https://myaidrive.com/gGoFsP8V2dB4ArSF/M106.pdf?pdfPage=31).

6. **Donne quatre types de sources de données ? (1pts) :**
   - Bases de données
   - Fichiers plats
   - Services web
   - ERP/CRM [M106, page 12](https://myaidrive.com/gGoFsP8V2dB4ArSF/M106.pdf?pdfPage=12).

7. **Quelle est la différence entre données structurées et non structurées ? (1pts) :**
   Les données structurées sont organisées selon un modèle prédéfini comme des bases de données relationnelles, tandis que les données non structurées ne suivent pas de modèle spécifique, comme les emails, les vidéos, les fichiers texte. [M106, page 11](https://myaidrive.com/gGoFsP8V2dB4ArSF/M106.pdf?pdfPage=11).

8. **Donne trois composants permettant l’extraction des données dans Talend ? (1.5 pts) :**
   - **tFileInputDelimited** : Permet de lire un fichier texte délimité.
   - **tFileInputExcel** : Permet de lire un fichier Excel.
   - **tMysqlInput** : Permet de lire des données d'une base de données MySQL. [M106, page 31](https://myaidrive.com/gGoFsP8V2dB4ArSF/M106.pdf?pdfPage=31).

9. **Donne trois exemples d’outils ETL populaires ? (1.5 pts) :**
   - Talend Open Studio
   - Informatica PowerCenter
   - Microsoft SSIS [M106, pages 38-48](https://myaidrive.com/gGoFsP8V2dB4ArSF/M106.pdf?pdfPage=38).

10. **Dessine l’architecture détaillée d’une chaîne décisionnelle d’un projet BI et expliquer les rôles des couches de l’architecture ? (1pts) :**
    - **Collecte des données** : Extraction des données des systèmes sources.
    - **Transformation des données** : Nettoyage, standardisation et consolidation des données.
    - **Stockage des données** : Enregistrement des données transformées dans un Data Warehouse.
    - **Restitution des données** : Utilisation des données via des outils de reporting et d'analyse pour soutenir la prise de décision. [M106, pages 13-16](https://myaidrive.com/gGoFsP8V2dB4ArSF/M106.pdf?pdfPage=13).
