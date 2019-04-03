prodotti =[['Carne','Pesce','Latte','Biscotti','Nutella','Uova'],[10.00,20.00,1.00,3.00,2.50,1.80]]
carrello = [[],[],[]]
totale =[]
somma=0

print'Benvenuto nel nostro supermercato on-line\n'
print'Questa è la nostra scheda prodotti che puoi trovare all\'interno del nostro punto vendita:\n'
#STAMPA LISTA PRODOTTI 
for x in range (len(prodotti[0])):
    print '- ',x,prodotti[0][x],'\t','€ ',prodotti[1][x],'\n'

s_acquisto = raw_input('Vuoi iniziare ad acquistare i nostri prodotti ? S/N\t')

if s_acquisto =='S' or s_acquisto =='s' :
    print'Bene Iniziamo...\n'

#CICLO CHE FA SCEGLIERE I PRODOTTI DA STAMPARE E LI AGGIUNGE ALLA MATRICE CARRELLO              
    while True:
            
        n = raw_input('Quale Prodotto vuoi Acquistare ? (premi E per uscire)\t')
        if n=='E' or n=='e':
            break

        print'Hai scelto\t',prodotti[0][int(n)],'\t','€ ',prodotti[1][int(n)],'\n\n'
        a_carrello = raw_input('Vuoi Aggiungerlo nel Carrello ? S/N\t')
        if a_carrello =='S' or a_carrello =='s' :
            q = raw_input('Quantità ?\t')

            carrello[0].append(prodotti[0][int(n)])
            carrello[1].append(prodotti[1][int(n)])
            carrello[2].append(int(q))
#FA STAMPARE IL CARRELLO CON RELATIVI PREZZI E QUANTITA E FA LA SOMMA TOTALE DELLA SPESA
print ' Il tuo carrello :\n'
for y in range (len(carrello[0])):
    print '- ',carrello[0][y],'\t','€ ',carrello[1][y],'\tQuantita:',carrello[2][y]
conferma = raw_input('Vuoi Confermare l\'acquisto ? S/N\t')
if conferma =='S' or conferma =='s':
    for z in range (len(carrello[0])):
        
        totale.append(float(carrello[1][z])*int(carrello[2][z]))
    for e in range (len(totale)):
        somma=int(somma) + float(totale[e])

    print'Hai speso un totale di € ',somma

#CREA UN FILE E SCRIVE LO SCONTRINO FISCALE CON LA RELATIVA SOMMA DELLA SPESA TOTALE
    scontrino_fiscale = raw_input('Vuoi Stampare lo Scontrino Fiscale ? S/N\t')
    
    if scontrino_fiscale == 'S' or scontrino_fiscale =='s':
        file_scontrino = open("SCONTRINO FISCALE.txt","a")
        file_scontrino.write('SCONTRINO FISCALE\n\n\nLista:\n\n')
        for n in range(len(carrello[0])):
            file_scontrino.write('- ')
            file_scontrino.write(carrello[0][n])
            file_scontrino.write('\tQuantita:')
            file_scontrino.write(str(carrello[2][n]))
            file_scontrino.write('\tPrezzo: €')
            file_scontrino.write(str(carrello[1][n]))
            file_scontrino.write('\n\n')
        file_scontrino.write('Totale: € ')
        file_scontrino.write(str(somma))
        file_scontrino.close()
        print('Lo Scontrino è Stato Stampato')
        
                            
            
    print'Grazie per Aver visitato il nostro negozio'

   

                       
                        
    

    
