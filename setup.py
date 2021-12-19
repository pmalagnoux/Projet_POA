from setuptools import setup
from Cython.Build import cythonize
import os

setup(
    ext_modules=cythonize([ #(c)
                            "/Users/hugoreinhardt/PycharmProjects/testProject/Factoriel/factoriel_cy.pyx",
                            "/Users/hugoreinhardt/PycharmProjects/testProject/Finonacci/fibonacci_cy.pyx",
                            "/Users/hugoreinhardt/PycharmProjects/testProject/Tableaux/tableaux_cy.pyx",
                            "/Users/hugoreinhardt/PycharmProjects/testProject/Premier/premier_cy.pyx",
                            "/Users/hugoreinhardt/PycharmProjects/testProject/Print/print_cy.pyx",
                            "/Users/hugoreinhardt/PycharmProjects/testProject/Quicksort/Quicksort_cy.pyx",
                            "/Users/hugoreinhardt/PycharmProjects/testProject/TriFusion/Trifusion_cy.pyx",
                            "/Users/hugoreinhardt/PycharmProjects/testProject/TriInsertion/TriInsertion_cy.pyx",
                           #(py)
                            "/Users/hugoreinhardt/PycharmProjects/testProject/Factoriel/Factorielle.pyx",
                            "/Users/hugoreinhardt/PycharmProjects/testProject/Finonacci/Fibonacci.pyx",
                            "/Users/hugoreinhardt/PycharmProjects/testProject/Tableaux/Tableau.pyx",
                            "/Users/hugoreinhardt/PycharmProjects/testProject/Premier/Premier.pyx",
                            "/Users/hugoreinhardt/PycharmProjects/testProject/Print/Print.pyx",
                            "/Users/hugoreinhardt/PycharmProjects/testProject/Quicksort/Quicksort.pyx",
                            "/Users/hugoreinhardt/PycharmProjects/testProject/TriFusion/Trifusion.pyx",
                            "/Users/hugoreinhardt/PycharmProjects/testProject/TriInsertion/TriInsertion.pyx",])
)

#os.system("rm /Users/hugoreinhardt/PycharmProjects/testProject/*.so")