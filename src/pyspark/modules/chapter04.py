from modules.chapter import ChapterParent
from dags.custom_dag import CustomDag


class Chapter04(ChapterParent):

    def run(self):
        print("Run chapter 04")
        CustomDag().run()