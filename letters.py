import argparse
import matplotlib.pyplot as plt
import time

parser = argparse.ArgumentParser(description='This program calculates the relative frequence of each letter of the alphabet in a given text.')
parser.add_argument('path', help='insert the path to the file')
parser.add_argument("--hist", help="display the histogram of the frequencies", action='store_true')
parser.add_argument('-s', '--stats', help='display some text stats', action='store_true')
args = parser.parse_args()

# Apro il file di testo e loggo come una stringa
testo = []
with open(args.path, 'r', encoding="utf8") as t:
    testo = t.read()
letters = testo.lower()

# Faccio partire il timer
start = time.time()

# Creo una lista che contiene le lettere dell'alfabeto
a_z = []
for i in range(ord('a'), ord('z')+1):
    a_z.append(chr(i))  

# Stampo le frequenze relative delle lettere
print('\nRelative frequencies:')
for i in a_z:
    print(f'   {i} -> {(letters.count(i)/len(letters))*100:.2f}%')


# Istogramma delle frequenze relative
if args.hist:
    counter = []
    for i in a_z:
        counter.append(letters.count(i)*100/len(letters))

    plt.figure()
    plt.bar(range(len(a_z)), counter, tick_label=a_z)
    plt.ylabel('Relative frequence (%)')

# Statistiche del testo
if args.stats:
    print(f'\nBasic stats of the text:\n   -The number of letters in the text is: {len(letters)}')
    lines = []
    with open(args.path, 'r', encoding="utf8") as l:
        lines = l.readlines()
    print(f'   -The number of lines in the text is: {len(lines)}')
    words = []
    for i in a_z:
        w = letters.count(f' {i}')
        words.append(w)
    print(f'   -The number of words in the text is: {sum(words)}')

# Fermo il timer e vedo il tempo impiegato
end = time.time()
print(f'\n\nTotal elapsed time: {end - start:.2f}s')

plt.show()
