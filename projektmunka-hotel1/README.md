# Projektmunka

## Projekt első indítása
- Klónozd le a github repót a saját gépedre
- Indítsd el a Docker Desktop-ot (vagy az Engine-t, ha linux-ról vagy és nincs Desktop) 
- Nyiss egy terminált a leklónozott repó Sprintnek megfelelő mappájában
- A `docker compose up` parancs kiadásával le lehet tölteni a szükséges image-eket, a docker ebből létrehozza a megfelelő konténereket és el is indítja őket
- Állítsd be az adatbázis kapcsolatot a MySQL Workbenchben.
- Az adatbázis feltöltéséhez futtasd a Sprint mappájában található sql fájlt 

## Projekt indítása a továbbiakban
- Konténerek indítása: `docker compose start`
- Konténerek leállítása: `docker compose stop`

## Elérhetőségek
- A frontend böngészőn keresztül a http://localhost:4200 címen elérhető 
- A backend postman-en keresztül a http://localhost:8080 címen elérhető 
- Adatbázis csatlakozási adatok:
  - Hostname: localhost
  - Port: 3306
  - Username: root
  - Password: test1234 

## Projekt törlése
- Konténerek törlése: `docker compose down`
- Vigyázz! Ha törölted a database konténert, elvesznek a benne lévő adatok is!