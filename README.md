# Pyspark pour le Big Data
Test pour la formation en Big Data


*LES DOSSIER DU PROJET*
# Le dossier: `deployment`

Le dossier deployement permet de faire toutes des ocnfiguration de déployement du projet avec docker ou Kubernates, mais pour notre cas c'est un deployement docker.

`deployment/`
`deployment/docker`
`deployment/kubernetes`

# Le dossier: `ressources`

C'est un dossier qui contient des ressources supplémentaires utilisées dans le projet et des description complementaire.

`resources/`
`resources/CodeManagementPolicy.txt`

# Le dossier: `src`

Il contient les source de code qui ont été realisées dans le cadre de ce test pour py-spark.

`src`
`src/BigData`
`src/BigData/py-spark`

## Demarrer le projet

## Structure du projet PYSPARK_POUR_BIG_DATA

## LE Big Data avec Pyspark Project Structure

La structure complete du projet est la suivante:

```bash
root/
 |-- deployment/
 |   |-- docker/
 |   |-- | -- custom-images/
 |   |-- | -- |-- python/
 |   |-- | -- |-- |-- Dockerfile
 |   |-- | -- |-- scala/
 |   |-- | -- volumes/
 |   |-- | -- docker-compose.yml
 |   |-- | -- run.sh
 |   |-- kubernetes/
 |-- resources/
 |   |-- CodeManagementPolicy.txt
 |-- src/
 |   |-- pyspark/
 |   |-- | -- configs/
 |   |-- | -- dependencies/
 |   |-- | -- jobs/
 |   |-- | -- ressources/
 |   |-- | -- tests/
 |   |-- | -- main.py
 |   |-- scala/
 |   docker-run.sh
 |   README.md
```

![Architecture du projet](./resources/images/architecture.png)


*Deployement docker*

[1] Cloner le projet:
    `git clone https://github.com/TemateuRoslyn/Pyspark_pour_big_data.git`

[2] Se deplacer dans le projet:
    `cd Pyspark_pour_big_data`

[3] Lancer le déployement docker: Ouvrir un terminal et executer
    `sh docker-run.sh`
[4] Ouvrer un navigateur et allez a l'addresse suivante pour voir spark en action
    `http://localhost:7070/`
[5] Pour acceder a l'interface de Airflow:
    `http://localhost:8191/`
    Identifiant de coneion a Airflow
    username: `user`
    password: `bitnami`


*Deployement de py-spark*