import collections
from collections import Counter
import ast

file=open("a.txt","r")
contents=file.read()
dictionary=ast.literal_eval(contents)
file.close()
lst= []
#Φτιάχνω μία συνάρτηση που ελέγχει αν μέσα στο λεξικό υπάρχουν εμφωλευμένα λεξικά ή λίστες και
#προσθέτει σε μία λίστα όλα τα κλειδιά
def get_keys(dl, lst):
    #Αν είναι λεξικό
    #Με τη συνάρτηση insistance ελέγχω αν το αντικείμενό μου είναι στην προκειμένη περίπτωση λεξικό ή λίστα
    if isinstance(dl, dict):
        for k, v in dl.items():
            if isinstance(v, list):
                get_keys(v, lst)
            elif isinstance(v, dict):
                get_keys(v, lst)
            lst.append(k)
    #Αν είναι λίστα
    elif isinstance(dl, list):
        for i in dl:
            if isinstance(i, list):
                get_keys(i, lst)
            elif isinstance(i, dict):
                get_keys(i, lst)
    return lst
#Καλώ τη συνάρτηση για το λεξικό που έχω
get_keys(dictionary, lst)
#Με τον Counter μετράω τις εμφανίσεις των κλειδιών στη λίστα
counter=collections.Counter(lst)
print(counter.most_common())
