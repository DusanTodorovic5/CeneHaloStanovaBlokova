# CeneHaloStanovaBlokova
Python skripta za scrappovanje stanova koji se prodaju na Novom Beogradu

# Kako koristiti

```console
python main.py {broj_bloka}
```

## Ispis izgleda ovako :

```txt
['LINK PRETRAGE CE SE ISPISATI OVODE \\NIJE NAPISAN ZBOG MOZDA PROBLEMA S SAJTOM']

##############################

STAN : NAZIV OGLASA
LINK : LINK DO TOG OGLASA
CENA : 110.000
CENA KVADRATA : 1.864 
KVADRATURA : 59 m
BROJ SOBA : 2.0 
SPRATNOST : XVIII/20 

##############################

.
.OVDE SU DRUGI STANOVI
.

##############################

STAN : NAZIV OGLASA
LINK : LINK DO TOG OGLASA
CENA : 126.000
CENA KVADRATA : 1.881 
KVADRATURA : 67 m
BROJ SOBA : 2.0 
SPRATNOST : V/20 

##############################

PROSECNA CENA STANA : 
1885.4
```

# Preporuka

Ja koristim sledeću komandu u bash-u
```console
broj_bloka={broj_bloka_koji_vas_interesuje};python main.py $broj_bloka > "$broj_bloka" ; cat "$broj_bloka"
```
{broj_bloka_koji_vas_interesuje} zamenite sa nekim brojem, na primer za blok 45 komanda izgleda :
```console
broj_bloka=45;python main.py $broj_bloka > "$broj_bloka" ; cat "$broj_bloka"
```
Izlaz ovakve komande je otvoren fajl po imenu bloka, u slučaju bloka 45 je fajl po imenu 45 bez ekstenzije i nalazi se u folderu gde ste i pokrenuli komandu
