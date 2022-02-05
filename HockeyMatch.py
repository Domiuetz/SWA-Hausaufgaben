
import sys #Dieser eintrag wird verwendet, um das Programm zu beenden wird
import time #noetig, damit die Sekundenschleife funktioniert
import webbrowser #wird gebraucht um eine Website aufrufen zu koennen
import os #brachen wir fuer die Funktion
import this #Easteregg
import platform #wird verwendet um das Betriebsystem zu ermitteln

#Ermitteln, welches Betriebssystem verwendet wird, das muessen wir wissen fuer die Funktion
from sys import platform
if platform == "linux" or platform == "linux2":
    System = "clear"
elif platform == "win32":
    System = "cls"
elif platform == "ios":
    System = "ls"
os.system(System) #das Betriebsystem definieren, cls unter windows, clear in Linux! Muss angegeben werden, fuer den Fliesstext

# Nun definieren wir Spieler als Variablen, welche wir anschliessend einsetzen koennen.
ehcbtor1 = "van Pottelberghe"
ehcbsturm1 = "Haas"
ehcbsturm2 = "Cunti"
ehcbsturm3 = "Brunner"
ehcbdef1 = "Grossmann"
ehcbdef2 = "Forster"

scbtor1 = "Wuethrich"
scbsturm1 = "Kahun"
scbsturm2 = "Gerber"
scbdef1 = "Blum"
scbdef2 = "Untersander"

Leben = 3 #definition der Anzahl Leben
game_start = "ja" #solange ja, bleibt die Whileschlaufe aktiv
schuss = "" #variable schuss muss definiert sein, weil sonst das Script bei einer Fehleingebe hinfaellt
zaehler = 0 #variable zaehler muss definiert sein, weil sonst das Script bei einer Fehleingebe hinfaellt
ende = 0 #variable ende muss definiert sein, weil sonst das Script bei einer Fehleingebe hinfaellt

#Zeilenumbruch
Umbr = "\n"

#Texte definieren, welche sich wiederholen
Ungueltig = "Ungueltige Eingabe, du verlierst ein Leben startest aber neu!"
Wahl = Umbr + "Deine Wahl viel auf "
Abschluss = "Wo fliegt die Scheibe hin? Ins Lattenkreuz oder gibt es einen Abpraller bei "
Tor = "Ins Tor oder gibt es einen Abpraller?"
JorN = "Ja oder Nein?"
Meister1 = "Der EHCB ist SCHWEIZERMEISTER."
Meister2 = "Der SCB ist SCHWEIZERMEISTER."

#URL fuer Webseitenaufruf definieren
url = "https://www.ehcb.ch/de/saison/tabelle/"

#Endtext definieren
endtext = "\n\
\n\
\n\
MEISTER!!! SCHWEIZER MEISTER!!!! LALALALALALALALALALA\n\
\n\
\n\
Vielen dank, dass Sie mit dabei waren! \n\
Die Fans liegen sich in den Armen, Bier Becher fliegen durch die Halle.\n\
Alle stehen, lachen und singen. \n\
\n\
\n\
\n\
\n\
Wir bedanken uns, dass ihr unser Game gezockt habt! \n\
Wenn ihr Spass hattet, folgt uns auf Facebook, Instagramm! \n\
Gebt uns einen Daumen nach oben, lasst uns einen Like da! \n\
Und wenn ihr weitere Erlebnisse aus der FeusiGamingAcademy wuenscht, unterstuetzt uns. \n\
Am liebsten in irgend einer Form von Kryptos, abgesehen von Stellar! \n\
Beteiligt waren:\n\
Story und Marketing: André Gysi\n\
Programmierung: Michael Bommer\n\
Testing und Vertrieb: Dominic Uetz\n\
\n\
\n\
\n\
\n\
Merci, danke und Tschuessikofski"

#hier definieren wir Funktionen, diese werden wir weiter unten aufrufen.
# Super Lernvideo fuer Funktionen: https://www.youtube.com/watch?v=2h8e0tXHfk0
def schreiberling(endtext): 
    for char in endtext: #fuer jedes Zeichen in Endtext machen wir:
        sys.stdout.write(char) #drucken
        sys.stdout.flush() #anzeigen
        if char != "\n": #wenn kein \n (Zeilenumbruch) dann ist 0.1 Sekunde Unterbruch
            time.sleep(0.05) 
        else: #ansonsten eine Sekunde unterbruch
            time.sleep(1)

#Eastereggdaten aufbereiten
Eiderdaus = 1
egg = "".join([this.d.get(c, c) for c in this.s]) #der Import von "this" wird so umgewandelt, im Styl von this.py (um den Stolz von Peters nicht zu treffen)
# moeglich waere auch: egg = this.s.decode('rot13'), umwandel muessen wir es, damit eine Fliesstextausgabe moeglich ist.
def Oster(egg):
    for char in egg:
        sys.stdout.write(char)
        sys.stdout.flush() 
        time.sleep(0.05)

#Hier sind noch Informationen, wenn Text zwischen '''Text''' steht, beeinflusst er das Programm nicht.
'''Erlaeuterungen, was wie funktioniert:
print = Zeigt den gewuenschten Textdruck an
.strip() = Schneidet Leerzeichen bei der Eingabe raus
input() = in der Klammer wird als Bsp. die Frage mitgegeben und was vor dem = ist, beinhaltet die Eingabe
open_new = verwenden wir, um eine Homepage im standard Browser zu oeffnen.
exit = Beendet das Skript auf der Stelle
.sleep definiert die Pause in Sekundne
.zfill(2) sorgr dafuer, dass die Sekunden eine fuehrende Null erhalten
'''

#Fertig mit Variablen und Definitionen, jetzt gehts um die Wurst! Hier startet das Spiel.
while game_start == "ja" and Leben == 3: 
    print("Hallo und Herzlich willkommen zum grossen Finale du wirst Zeuge und Mitgestalter eines Spektakels!! \n\
Wir stehen im Spiel 7 des Playoff Finals EHCB gegen den SCB. Gespielt sind 59 Minuten und 40 Sekunden." + Umbr)
    print("Wir simulieren die letzten 20 Sekunden des Playoff Knuellers EHCB gegen den SCB. In der Serie steht es 3 zu 3.\n\
Dies ist daher das entscheidende Spiel. Der EHCB ist vor 2 Minuten mit 4:3 in Fuehrung gegangen.\n\
Es wird wohl die letzte Szene in diesem spannenden Spiel sein. Du kanns ueber die letzen 20 Sekunden entscheiden, Faceoff im Berner Drittel.." + Umbr) 
    while game_start == "ja" and Leben >0:
        #Zeit wird hier definiert, damit sie immer wieder zurueck gesetzt wird.
        Zeit = 3581
        if Leben == 1:
            print("Letztes Leben, bist du ein Zocker?" + Umbr)
            Eiderdaus = 0
        elif Leben != 3:
            print("Willst du weiterspielen?" + Umbr)
        else:
            print("Willst du ueber den Ausgang entscheiden?" + Umbr)
        antwort_1 = input(JorN + Umbr).strip()
#--------------------------------------------------------------------------------
        if antwort_1 == "ja" or antwort_1 == "Ja" or antwort_1 == "JA":
            print(Umbr + "Du hast " + str(Leben) + " Leben")
            Leben -= 1 
            print(Umbr + ehcbsturm1 + " gegen " + scbsturm1 + " beim Faceoff, wer gewinnt?" + Umbr)
            Faceoff = input(scbsturm1 + " oder " + ehcbsturm1 + "?" + Umbr).strip()
            if Faceoff == "Kahun" or Faceoff == "kahun":
                print(Umbr + Wahl + scbsturm1 + Umbr)
                while Zeit <= 3585:
                    Min = Zeit//60
                    Sec = Zeit%60
                    Sec = (str(Sec).zfill(2))
                    time.sleep(1)
                    print("%d:%s" % (Min , Sec ))
                    Zeit += 1 
                print(Umbr + "Die Scheibe wird zurueck gelegt auf " + scbsturm2 + ", diese verspringt ihm jedoch, " + ehcbsturm2 + " ueberlaeuft ihn und kommt an den Puck. \n\
" + ehcbsturm2 + " laeuft mit dem Puck aus der Angriffszone, daher muessen alle Bieler Spieler die Zone verlassen. \n\
Wie kehren die Bieler in die Angriffszone zurueck, per Pass oder " + ehcbsturm2 + " zieht alleine rein?" + Umbr)
                oZone = input("Pass oder alleine ?" + Umbr).strip()
                if oZone == "Pass" or oZone == "pass" or oZone == "PASS":
                    print(Umbr + "Du hast dich fuer den Pass entschieden" + Umbr)
                    while Zeit <= 3590:
                        Min = Zeit//60
                        Sec = Zeit%60
                        Sec = (str(Sec).zfill(2))
                        time.sleep(1)
                        print("%d:%s" % (Min , Sec ))
                        Zeit += 1 
                    print(Umbr + ehcbsturm2 + " spielt den Pass in das Angriffsdrittel. " + ehcbsturm1 + " spielt einen Querpass und " + ehcbsturm3 + " nimmt den Direktschuss. " + Abschluss + scbtor1 + "?" + Umbr)
                    schuss = input("Tor oder Abpraller?" + Umbr).strip()
                elif oZone == "Alleine" or oZone == "alleine" or oZone == "ALLEINE":
                    print(Umbr + Wahl + oZone + Umbr)
                    while Zeit <= 3590:
                        Min = Zeit//60
                        Sec = Zeit%60
                        Sec = (str(Sec).zfill(2))
                        time.sleep(1)
                        print("%d:%s" % (Min , Sec ))
                        Zeit += 1 
                    print(Umbr + ehcbsturm2 + " zieht alleine rein und zur Ueberraschung aller, kann er sich gegen die Verteidiger " + scbdef1 + " & " + scbdef2 + " durchsetzten.")
                    print(ehcbsturm2 + " schiesst mit voller Wucht auf das Tor, " + scbtor1 + " kann einem richtig leidtun. Wo fliegt die Scheibe hin? " + Tor + Umbr)
                    schuss = input("Tor oder Abpraller?" + Umbr).strip()
                else:
                    print(Umbr + Ungueltig + Umbr)
            elif Faceoff == "Haas" or Faceoff == "haas":
                print(Umbr + Wahl + ehcbsturm1 + Umbr)
                while Zeit <= 3585:
                    Min = Zeit//60
                    Sec = Zeit%60
                    Sec = (str(Sec).zfill(2))
                    time.sleep(1)
                    print("%d:%s" % (Min , Sec ))
                    Zeit += 1 
                print(Umbr + "Das Faceoff wurde duch " + ehcbsturm1 + " gwonnen. Auf wen soll er passen?")
                if Eiderdaus == 0:
                    ehcbsturm2 = "Peters"
                    zuspiel = input(ehcbdef1 + " oder " + ehcbsturm2 + "?" + Umbr).strip()
                else:
                    zuspiel = input(ehcbdef1 + " oder " + ehcbsturm2 + "?" + Umbr).strip()
                if zuspiel == "Cunti" or zuspiel == "cunti":
                    print(Umbr + Wahl + ehcbsturm2 + Umbr)
                    while Zeit <= 3590:
                        Min = Zeit//60
                        Sec = Zeit%60
                        Sec = (str(Sec).zfill(2))
                        time.sleep(1)
                        print("%d:%s" % (Min , Sec ))
                        Zeit += 1 
                    print(Umbr + ehcbsturm2 + " passt auf " + ehcbdef1 + " und dieser wiederum auf " + ehcbsturm3 + "."
                    + " Ein ansehnliches TicTacToe, Abschluss! " + Abschluss + scbtor1 + "?" + Umbr)
                    schuss = input("Tor oder Abpraller?" + Umbr).strip()
                elif zuspiel == "Grossmann" or zuspiel == "grossmann":
                    print(Umbr + Wahl + ehcbdef1 + Umbr)
                    while Zeit <= 3590:
                        Min = Zeit//60
                        Sec = Zeit%60
                        Sec = (str(Sec).zfill(2))
                        time.sleep(1)
                        print("%d:%s" % (Min , Sec ))
                        Zeit += 1 
                    print(Umbr + ehcbdef1 + " nimmt die Scheibe und wird hart von " + scbsturm2 + " gegen die Bande gecheckt!")
                    print(scbtor1 + " verlaesst sein Gehaeuse und " + scbsturm2 + " schickt " + scbsturm1 + " mit einem langen Pass in Richtung " + ehcbtor1 + "." + Umbr)
                    print("Kann " + ehcbtor1 + " die Chance zu nichte machen?")
                    save = input(JorN + Umbr).strip()
                    if save == "ja" or save == "Ja" or save == "JA": 
                        print(Umbr + Wahl + save + Umbr)
                        while Zeit <= 3595:
                            Min = Zeit//60
                            Sec = Zeit%60
                            Sec = (str(Sec).zfill(2))
                            time.sleep(1)
                            print("%d:%s" % (Min , Sec ))
                            Zeit += 1 
                        print(Umbr + ehcbtor1 + " macht eine Glanzparade." + Umbr)
                        while Zeit <= 3600:
                            Min = Zeit//60
                            Sec = Zeit%60
                            Sec = (str(Sec).zfill(2))
                            time.sleep(1)
                            print("%d:%s" % (Min , Sec ))
                            Zeit += 1 
                        print(Umbr + "Sekunden spaeter ertoent die Sirene und " + Meister1)
                        ende = "real"
                    elif save == "nein" or save == "Nein" or save == "NEIN": 
                        print(Umbr + Wahl + save + Umbr)
                        while Zeit <= 3595:
                            Min = Zeit//60
                            Sec = Zeit%60
                            Sec = (str(Sec).zfill(2))
                            time.sleep(1)
                            print("%d:%s" % (Min , Sec ))
                            Zeit += 1                  
                        print(Umbr + "Korrekt, der Schuss verfehlt haarscharf das Gehaeuse." + Umbr)
                        while Zeit <= 3600:
                            Min = Zeit//60
                            Sec = Zeit%60
                            Sec = (str(Sec).zfill(2))
                            time.sleep(1)
                            print("%d:%s" % (Min , Sec ))
                            Zeit += 1 
                        print(Umbr + "Die Sirene ertoent und " + ehcbtor1 + " muss gar nicht mehr eingreifen. " + Meister1 + Umbr)
                        ende = "real"
                    else:
                        print(Umbr + Ungueltig + Umbr)
                elif zuspiel == "Peters" or zuspiel == "peters":
                    print(Umbr + Wahl + ehcbsturm2 + Umbr)
                    print(Umbr + "Gratuliere, du hast unser Osterei gefunden!" +Umbr)
                    Oster(egg + Umbr + Umbr)
                    Leben += 3
                    ehcbsturm2 = "Cunti"
                    Eiderdaus = 1
                else:
                   print(Umbr + Ungueltig + Umbr)
            else:
                print(Umbr + Ungueltig + Umbr)
        elif antwort_1 == "nein" or antwort_1 == "Nein" or antwort_1 == "NEIN":
            Leben = 0
        else:
            print(Umbr + "Ungueltige Eingabe, damit gibst du auf und steigst aus dem Spiel aus!" + Umbr)
            Ausgang = input("Fortsetzen oder Abbrechen?" + Umbr).strip()
            Leben -= 1
            if Ausgang == "Fortsetzen" or Ausgang == "fortsetzen":
                print(Umbr)
                game_start = "ja"
            elif Ausgang == "Abbrechen" or Ausgang == "abbrechen":
                print(Umbr)
                game_start = "nein"
                Leben = 0
            else:
                print(Ungueltig + Umbr)
#--------------------------------------------------------------------------------
        if schuss == "Tor" or schuss == "tor" or schuss == "TOR":
            print(Umbr + "Du hast dich fuer einen Treffer entschieden." + Umbr)
            while Zeit <= 3595:
                Min = Zeit//60
                Sec = Zeit%60
                Sec = (str(Sec).zfill(2))
                time.sleep(1)
                print("%d:%s" % (Min , Sec ))
                Zeit += 1  
            print(Umbr + "Der EHCB geht somit mit 5:3 in Fuehrung. Es stehen noch 5 Sekunden auf der Matchuhr. Es gibt ein Faceoff in der Mitte des Eisstadions." + Umbr)
            print("Was denkst du, kann der SCB nochmals ins Spiel finden?" + Umbr) 
            comeback = input(JorN + Umbr).strip()
            if comeback == "ja" or comeback == "Ja" or comeback == "JA":
                print(Umbr + "Du hast dich fuer " + comeback + " entschieden." + Umbr)
                while Zeit <= 3600:
                    Min = Zeit//60
                    Sec = Zeit%60
                    Sec = (str(Sec).zfill(2))
                    time.sleep(1)
                    print("%d:%s" % (Min , Sec ))
                    Zeit += 1 
                print(Umbr + "Dies ist nicht mehr das Fall. " + Meister1 + Umbr)
                ende = "real"
            elif comeback == "nein" or comeback == "Nein" or comeback == "NEIN":
                print(Umbr + "Du hast dich fuer " + comeback + " entschieden." + Umbr)
                while Zeit <= 3600:
                    Min = Zeit//60
                    Sec = Zeit%60
                    Sec = (str(Sec).zfill(2))
                    time.sleep(1)
                    print("%d:%s" % (Min , Sec ))
                    Zeit += 1 
                ende = "real"
                print(Umbr + "Korrekt, dies ist nicht mehr das Fall. " + Meister1 + Umbr)
            else:
                print(Umbr + Ungueltig + Umbr)
        elif schuss == "Abpraller" or schuss == "abpraller" or schuss == "ABPRALLER":
            print("Du hast dich fuer den Abpraller entschieden" + Umbr)
            while Zeit <= 3595:
                Min = Zeit//60
                Sec = Zeit%60
                Sec = (str(Sec).zfill(2))
                time.sleep(1)
                print("%d:%s" % (Min , Sec ))
                Zeit += 1 
            print(Umbr + "Es gibt ein Gewuehl vor " + scbtor1 + "..." + Umbr)
            while Zeit <= 3600:
                Min = Zeit//60
                Sec = Zeit%60
                Sec = (str(Sec).zfill(2))
                time.sleep(1)
                print("%d:%s" % (Min , Sec ))
                Zeit += 1 
            print(Umbr + "...und schon ertoent die Sirene und das Spiel ist beendet. " + Meister1 + Umbr)
            ende = "real"
        else:
            if schuss != "":
                print(Ungueltig + Umbr)
#--------------------------------------------------------------------------------
        if ende == "real":
            time.sleep(5)
            schreiberling(endtext)
            webbrowser.open_new(url)
            sys.exit()
        #end if ist hier, aber wenn wir hier hin kommen, ist das Spiel fertig und es wird per sys.exit ausgestiegen, desswegen ist kein else nicht definiert
#--------------------------------------------------------------------------------
        if Leben >= 1 and game_start != "ja":
            print(Umbr + "Willst du weiter spielen? Du musst von vorne beginnen, verlierst aber ein Leben!" + Umbr)
            fertig = input(JorN + Umbr).strip()
            if fertig == "ja" or fertig == "Ja" or fertig == "JA":
                game_start = "ja"
            elif antwort_1 == "nein" or antwort_1 == "Nein" or antwort_1 == "NEIN":
                print(Umbr + "Du hast leider aufgegeben! Ich wuensche dir ein schoenes Leben." + Umbr)
                game_start = "nein" 
            else:
                game_start = "nein" 
                print(Umbr + "Fehleingabe = GameOver" + Umbr) 
        elif Leben < 1 or game_start != "ja":
            print(Umbr + "Game Over, du bist zu mies fuer den EHCB!" + Umbr)
            webbrowser.open_new(url)
            game_start = "nein"
            sys.exit()
        else:
            "" #hier hin wollen wir nicht! ;) 