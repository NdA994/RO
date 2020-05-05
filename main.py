import csv
import os

import networkx as nx

#TO DO: Vedere se i punti di articolazione possono aiutare sotto il punto di vista computazionale
#TO DO: Implementazione brutale per individuare tutte le rotte per le commodities senza alcun tipo di controllo sulla banda
#TO DO: Salvataggio dati di precalcolo
#TO DO: Sistemare l'esecuzione del programma. Funzioni e cose varie.

G = nx.DiGraph()
node = []
edge = []
comm = []

#NODI
#Parametro 1: ID nodo
#Parametro 2: Nome nodo
with open('./dati/05_giorno_commodities.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        G.add_node(row[0], name=row[1])
        node.append(row)

#ARCHI
#Parametro 1: ID nodo sorgente
#Parametro 2: ID nodo destinazione
#Parametro 3: Capacità arco
with open('./dati/05_giorno_topology.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        G.add_edge(row[0], row[1], cap=int(row[2]))
        edge.append(row)

#COMMODITIES
#Parametro 1: ID Sorgente
#Parametro 2: ID Destinazione
#Parametro 3: Banda richiesta
#Parametro 4: Priotrità
i = 0
with open('./dati/05_giorno_commodities.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        row[4] = i
        comm.append(row)
        i = i+1

#TO DO: controllare e completare questa parte
#TO DO: correggere errore su file resPath
i = 0
#TO DO: aggiungere try catch
os.remove("./out2/resPath.csv")
#calcolo Lk
for row in comm:
    all_paths = []
    Lk = nx.shortest_path_length(G, source=(row[0]), target=row[1])
    with open('./out2/'+str(i)+'.csv', 'w', newline='') as csvPath:
        resPath = csv.writer(csvPath, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
        if int(row[3]) == 1:
            print("Priorità 1")
            #print(Lk)
            #print(nx.shortest_path(implementazione calcolo path ammissibiliG, source=(row[0]), target=row[1]))
            for path in nx.all_simple_paths(G, source=(row[0]), target=row[1], cutoff=Lk+1):
                resPath.writerow(path)
                all_paths.append(path)
                print(path)
            with open('./out2/resPath.csv', 'a+', newline='') as csvRes:
                csvRes = csv.writer(csvRes, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
                print(len(all_paths))
                csvRes.writerow([i, len(all_paths)])
        if int(row[3]) == 2:
            print("Priorità 2")
            if Lk < 3:
                #print(Lk)
                #print(nx.shortest_path(G, source=(row[0]), target=row[1]))
                for path in nx.all_simple_paths(G, source=(row[0]), target=row[1], cutoff=Lk*2):
                    resPath.writerow(path)
                    all_paths.append(path)
                    print(path)
                with open('./out2/resPath.csv', 'a+', newline='') as csvRes:
                    csvRes = csv.writer(csvRes, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
                    print(len(all_paths))
                    csvRes.writerow([i, len(all_paths)])

            elif Lk < 5:
                #print(Lk)
                #print(nx.shortest_path(G, source=(row[0]), target=row[1]))
                for path in nx.all_simple_paths(G, source=(row[0]), target=row[1], cutoff=Lk*1.5):
                    resPath.writerow(path)
                    all_paths.append(path)
                    print(path)
                with open('./out2/resPath.csv', 'a+', newline='') as csvRes:
                    csvRes = csv.writer(csvRes, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
                    print(len(all_paths))
                    csvRes.writerow([i, len(all_paths)])
            elif Lk < 11:
                #print(Lk)
                #print(nx.shortest_path(G, source=(row[0]), target=row[1]))
                for path in nx.all_simple_paths(G, source=(row[0]), target=row[1], cutoff=int(Lk*1.5)):
                    resPath.writerow(path)
                    all_paths.append(path)
                    print(path)
                with open('./out2/resPath.csv', 'a+', newline='') as csvRes:
                    csvRes = csv.writer(csvRes, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
                    print(len(all_paths))
                    csvRes.writerow([i, len(all_paths)])
            else:
                #print(Lk)
                #print(nx.shortest_path(G, source=(row[0]), target=row[1]))
                for path in nx.all_simple_paths(G, source=(row[0]), target=row[1], cutoff=Lk+2):
                    resPath.writerow(path)
                    all_paths.append(path)
                    print(path)
                with open('./out2/resPath.csv', 'a+', newline='') as csvRes:
                    csvRes = csv.writer(csvRes, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
                    print(len(all_paths))
                    csvRes.writerow([i, len(all_paths)])
        if int(row[3]) == 3:
            print("Priorità 3")
            if Lk < 3:
                #print(Lk)
                #print(nx.shortest_path(G, source=(row[0]), target=row[1]))
                for path in nx.all_simple_paths(G, source=(row[0]), target=row[1], cutoff=Lk*2):
                    resPath.writerow(path)
                    all_paths.append(path)
                    print(path)
                with open('./out2/resPath.csv', 'a+', newline='') as csvRes:
                    csvRes = csv.writer(csvRes, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
                    print(len(all_paths))
                    csvRes.writerow([i, len(all_paths)])
            elif Lk < 5:
                #print(Lk)
                #print(nx.shortest_path(G, source=(row[0]), target=row[1]))
                for path in nx.all_simple_paths(G, source=(row[0]), target=row[1], cutoff=Lk*2):
                    resPath.writerow(path)
                    all_paths.append(path)
                    print(path)
                with open('./out2/resPath.csv', 'a+', newline='') as csvRes:
                    csvRes = csv.writer(csvRes, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
                    print(len(all_paths))
                    csvRes.writerow([i, len(all_paths)])
            elif Lk < 11:
                #print(Lk)
                #print(nx.shortest_path(G, source=(row[0]), target=row[1]))
                for path in nx.all_simple_paths(G, source=(row[0]), target=row[1], cutoff=int(Lk*1.5)):
                    resPath.writerow(path)
                    all_paths.append(path)
                    print(path)
                with open('./out2/resPath.csv', 'a+', newline='') as csvRes:
                    csvRes = csv.writer(csvRes, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
                    print(len(all_paths))
                    csvRes.writerow([i, len(all_paths)])
            else:
                #print(Lk)
                #print(nx.shortest_path(G, source=(row[0]), target=row[1]))
                for path in nx.all_simple_paths(G, source=(row[0]), target=row[1], cutoff=Lk+2):
                    resPath.writerow(path)
                    all_paths.append(path)
                    print(path)
                with open('./out2/resPath.csv', 'a+', newline='') as csvRes:
                    csvRes = csv.writer(csvRes, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
                    print(len(all_paths))
                    csvRes.writerow([i, len(all_paths)])
    i = i+1
