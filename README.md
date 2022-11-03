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

## ETL Project Structure

La structure basic du projet est la suivante:

```bash
root/
 |-- configs/
 |   |-- etl_config.json
 |-- dependencies/
 |   |-- logging.py
 |   |-- spark.py
 |-- jobs/
 |   |-- etl_job.py
 |-- tests/
 |   |-- test_data/
 |   |-- | -- employees/
 |   |-- | -- employees_report/
 |   |-- test_etl_job.py
 |   build_dependencies.sh
 |   packages.zip
 |   Pipfile
 |   Pipfile.lock
```

*Deployement docker*

[1] Cloner le projet:
    `git clone https://github.com/TemateuRoslyn/Pyspark_pour_big_data.git`

[2] Se deplacer dans le projet:
    `cd Pyspark_pour_big_data`

[3] Lancer le déployement docker: Ouvrir un terminal et executer
    `sh docker-run.sh`
[4] Ouvrer un navigateur et allez a l'addresse suivante pour voir spark en action
    `http://localhost:7070/`
[5] Pour voir le worker qui a été configuré aller à l'adresse suivnate:
    `http://172.22.0.2:8081/`

*Deployement de py-spark*