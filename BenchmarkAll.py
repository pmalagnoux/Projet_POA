from Finonacci.BenchmarkFibonacci import benchFibonacci
from Print.BenchmarkPrint import benchPrint
from Quicksort.BenchmarkQuicksort import benchQuicksort
from Tableaux.BenchmarkTableau import benchTableau
from TriFusion.BenchmarkTriFusion import benchTriFusion
from TriInsertion.BenchmarkTriInsertion import benchTriInsertion
from Factoriel.BenchmarkFactorielle import benchFactorielle
from Premier.BenchmarkPremier import benchPremier

result = []

result.append("Premier")
result.append(benchPremier())
result.append("Factorielle")
result.append(benchFactorielle())
result.append("Fibonacci")
result.append(benchFibonacci())
result.append("Print")
result.append(benchPrint())
result.append("Tableau")
result.append(benchTableau())
result.append("TriFusion")
result.append(benchTriFusion())
result.append("TriInsertion")
result.append(benchTriInsertion())
result.append("Quicksort")
result.append(benchQuicksort())


fichier = open("Resultat.txt", "a")
for ligne in result:
    fichier.write(ligne.__str__() + "\n")
fichier.close()