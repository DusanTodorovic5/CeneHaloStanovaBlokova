# CeneHaloStanovaBlokova
Python skripta za scrappovanje stanova koji se prodaju na novom beogradu

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

Ja koristim sledecu komandu u bash-u
```console
python main.py {broj_bloka} > broj_bloka ; nano broj_bloka
```
