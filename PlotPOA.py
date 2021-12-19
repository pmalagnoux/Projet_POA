from matplotlib import pyplot as plt

	
dataPremier = [('Jython (-jar)', 1.693,'sec'),
 ('Python (py)', 0.321, 'sec'),
 ('Cython (py)', 0.292, 'sec'),
 ('Cython (c)', 0.036, 'sec')]


labels, data, _ = zip(*dataPremier)
plt.bar(labels,data)
plt.xlabel("Python Interpeter / Platform")
plt.ylabel("Time (sec)")
plt.title("Calcul des 10 000 premiers nombres premeirs")
plt.show()

dataFacto = [('Jython (-jar)', 1.571, 'sec'),
 ('Python (py)', 0.035, 'sec'),
  ('Cython (c)', 0.034, 'sec'),
   ('Cython (py)', 0.032, 'sec')]   

labels, data, _ = zip(*dataFacto)
plt.bar(labels,data)
plt.xlabel("Python Interpeter / Platform")
plt.ylabel("Time (sec)")
plt.title("Calcul de factorielle 100 en récursif")
plt.show()

dataFibo = [('Jython (-jar)', 7.914, 'sec'),
 ('Python (py)', 6.037, 'sec'),
  ('Cython (py)', 5.907, 'sec'),
   ('Cython (c)', 2.082, 'sec')]

labels, data, _ = zip(*dataFibo)
plt.bar(labels,data)
plt.xlabel("Python Interpeter / Platform")
plt.ylabel("Time (sec)")
plt.title("Calcul de 1 000 000 de fois la fonction de Fibonacci itéarif avec n = 92")
plt.show()

dataPrint = [('Jython (-jar)', 1.578, 'sec'),
 ('Cython (py)', 0.287, 'sec'),
  ('Python (py)', 0.277, 'sec'),
   ('Cython (c)', 0.266, 'sec')]

labels, data, _ = zip(*dataPrint)
plt.bar(labels,data)
plt.xlabel("Python Interpeter / Platform")
plt.ylabel("Time (sec)")
plt.title("Affichage de la chaine "'8INF957'" 10 000 fois")
plt.show()

dataTableau = [('Python (py)', 2.736, 'sec'),
 ('Cython (py)', 2.595, 'sec'),
  ('Jython (-jar)', 2.425, 'sec'),
   ('Cython (c)', 0.567, 'sec')]

labels, data, _ = zip(*dataTableau)
plt.bar(labels,data)
plt.xlabel("Python Interpeter / Platform")
plt.ylabel("Time (sec)")
plt.title("Allocation d'un tableau à 1 000 000 décimales entre 0 et 1")
plt.show()

dataTriFusion = [('jython (-jar)', 1.950, 'sec'),
 ('Cython (py)', 0.297, 'sec'),
 ('Python (py)', 0.290, 'sec'),
 ('Cython (c)', 0.124, 'sec')]


labels, data, _ = zip(*dataTriFusion)
plt.bar(labels,data)
plt.xlabel("Python Interpeter / Platform")
plt.ylabel("Time (sec)")
plt.title("Tri de 1000 tableau de 100 valeurs par le tri Fusion")
plt.show()

dataTriInsertion = [('jython (-jar)', 1.978, 'sec'),
 ('Cython (py)', 0.303, 'sec'),
  ('Python (py)', 0.286, 'sec'),
   ('Cython (c)', 0.071, 'sec')]

labels, data, _ = zip(*dataTriInsertion)
plt.bar(labels,data)
plt.xlabel("Python Interpeter / Platform")
plt.ylabel("Time (sec)")
plt.title("Tri de 1000 tableau de 100 valeurs par le tri par Insertion")
plt.show()

dataQuickSort = [('Jython (-jar)', 2.000, 'sec'),
 ('Python (py)', 0.249, 'sec'),
  ('Cython (py)', 0.186, 'sec'),
   ('Cython (c)', 0.087, 'sec')]
labels, data, _ = zip(*dataQuickSort)
plt.bar(labels,data)
plt.xlabel("Python Interpeter / Platform")
plt.ylabel("Time (sec)")
plt.title("Tri de 1000 tableau de 100 valeurs par le tri Rapide")
plt.show()


