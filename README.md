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
# Le dossier: `src/BigData`
# Le dossier: `src/BigData/py-spark`

Il contient les source de code qui ont été realisées dans le cadre de ce test pour py-spark.

## Demarrer le projet

*Deployement docker*

[1] Cloner le projet:
    `git clone https://github.com/TemateuRoslyn/Pyspark_pour_big_data.git`

[2] Se deplacer dans le projet:
    `cd Pyspark_pour_big_data`

[3] Lancer le déployement docker: Ouvrir un terminal et executer
    `sh docker-run.sh`

*Deployement de py-spark*