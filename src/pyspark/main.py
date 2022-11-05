import os

from pyspark.sql import SparkSession
from pyspark.sql.types import *

from jobs.chapter01 import Chapter01
from jobs.chapter02 import Chapter02
from jobs.chapter03 import Chapter03
from jobs.chapter04 import Chapter04
from jobs.chapter05 import Chapter05
from jobs.chapter06 import Chapter06
from jobs.chapter07 import Chapter07
from jobs.chapter08 import Chapter08

spark = SparkSession.builder.appName('data_processing').getOrCreate()

chapterNames = ["", "Chapter 01", "Chapter 02", "Chapter 03", "Chapter 04", "Chapter 05", "Chapter 06", "Chapter 07", "Chapter 08"]

def printFillLine(lineSize):
    print(lineSize*"*")


def printTabLine(leftSpace, rightSpace, someText):
    print("*", leftSpace*"\t", someText, rightSpace*"\t", "*")

def showMenu():
    print("")
    printFillLine(114)
    printTabLine(1, 0,  "                                                                                                      ")
    printTabLine(5, 6,  "Pyspark pour le Big Data")                    
    printTabLine(2, 5,  "Veuillez choisir le chapitre que vous souhaitez executer")
    printTabLine(1, 0,  "                                                                                                      ")
    printFillLine(114)
    printTabLine(1, 0, "                                                                                                      ")
    printTabLine(1, 10,  "Liste des chapitre dispo...")
    printTabLine(1, 10,  "===========================")
    printTabLine(1, 0, "                                                                                                      ")
    printTabLine(1, 0, "                                                                                                      ")
    printTabLine(2, 9,  "Chapitre 01: Scala Language")
    printTabLine(2, 8,  "Chapitre 02: Data Processing       ")
    printTabLine(2, 7,  "Chapitre 03: Spark Structured Streaming")
    printTabLine(2, 9,  "Chapitre 04: Airflow       ")
    printTabLine(2, 7,  "Chapitre 05: MLlib: Machine Learning Library")
    printTabLine(2, 7,  "Chapitre 06: Supervised Machine Learning")
    printTabLine(2, 7,  "Chapitre 07: Unsupervised Machine Learning")
    printTabLine(2, 7,  "Chapitre 08: Deep Learning Using PySpark")
    printTabLine(1, 0, "                                                                                                      ")
    printFillLine(114)

def continueEvaluation(): 
    try:
        continuer = 1
        print("""Souhaitez-vous continuer les tests : 
            -1- pour rentrez au menu principal
            -0- Pour arreter l'utilitaire de test \n""")
        continuer = int(input())
        return continuer
    except ValueError:
        
        print("Invalide Choice")
        continueEvaluation()


def caseChapter(chapter):
    try:
        switcher = {
            1: Chapter01(chapterNames[1], spark, StructType),
            2: Chapter02(chapterNames[2], spark, StructType),
            3: Chapter03(chapterNames[3], spark, StructType),
            4: Chapter04(chapterNames[4], spark, StructType),
            5: Chapter05(chapterNames[5], spark, StructType),
            6: Chapter06(chapterNames[6], spark, StructType),
            7: Chapter07(chapterNames[7], spark, StructType),
            8: Chapter08(chapterNames[8], spark, StructType),
        }
        selected = switcher.get(chapter, None)
        if selected  != None: 
            selected.run()
    except ValueError:
          
          print("Invalide Choice")
          caseChapter(chapter)

def begin():
    continuer = chapter =  1 
    while continuer == 1:
        
        showMenu()
        try:
          print("\n Veuillez entrez le numero du chapitre que vous souhaitez interroger, Ex: 3")
          chapter = int(input())
          print("\n--------------------  START OF CHAPTER ", chapter, "-----------------\n")
          caseChapter(chapter)
          print("\n--------------------  END OF CHAPTER ", chapter, "-----------------\n")
          continuer = continueEvaluation()
        except ValueError:
            
            print("Invalide Choice")
            begin()


## Lancement du programme principal
begin() 