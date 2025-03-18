import random
from time import sleep

from lib.hangman_gui import HangmanGui


# TODO: Wie unterer Kommentar beim Kapseln der Built-In Funktion.
#       Weiß nicht, ob es hier sinnvoll ist zu kapseln, wenn das eigentlich eine 1 Zeilen Operation ist...

# gekapselte Funktionen
def verringere_um_eins(zahl):  # grundlegende Funktion
    return zahl - 1


def kündige_spieleröffnung_an():
# Nutzung bereits gegebener Funktionen wie input
    print("Willkommen beim Hangman-Spiel")
    name = input("Bitte gib deinen Namen ein: ")
    print("Hallo " + name + "! Schön dich kennenzulernen.")
    print("-------------------------------------------------")
    print("Let's Play Hangman! Du kannst dir 10 Fehlversuche leisten.")


def ist_das_spiel_noch_am_laufen(erratenes_teilwort, erlaubte_fehlversuche):  # if else Funktion
    if (not ("_" in erratenes_teilwort)):
        print("CONGRATULATIONS! - YOU WON")
        return False

    if (erlaubte_fehlversuche == 0):
        print("GAME OVER - YOU LOST")
        return False

    else:
        return True

#
def erhalte_großbuchstaben():
    eingabebuchstabe = input("Gib einen Großbuchstaben ein: ")
    while (not (len(eingabebuchstabe) == 1 and eingabebuchstabe.isalpha())):
        print("Das war kein einzelner Buchstabe: ")
        eingabebuchstabe = input("Gib einen Großbuchstaben ein: ")

    return eingabebuchstabe.upper()


# TODO: Hier ne eigene Funktion zu machen bietet iwie keinen Mehrwert.
#       Ich denke, dass verwirrt eher und bläht den Code auf.
def erweitere_fehlgeschlagene_BuchstabenListe(eingabebuchstabe, fehlgeschlagene_buchstaben):  # Listen Funktion 1
    fehlgeschlagene_buchstaben.append(eingabebuchstabe)


# Spacing entfernen?
# Liste-Konzept vor for-Konzept
def gib_verdecktes_wort(geheimwort):  # For Funktion
    verschleiertesWort = []
    for buchstabe in geheimwort:
        verschleiertesWort.append("_")

    return verschleiertesWort

# im Spielcode vorgeben
def wähle_ein_zufälliges_wort(wörter_liste):  # Listen Funktion 4
    wort = random.choice(wörter_liste)
    # TODO: for unified representation i changed that here.
    #   I'm considering to force upper case for user inputs as well to un-bloat the code for the students...
    return wort.upper()


# for i in range ?
# Buchstabenposition * 2 -> Buchstaben ?
# -> einfache Funktion
def buchstaben_aufdecken(eingabebuchstabe, geheimwort, erratenes_teilwort):  # For
    for buchstabenposition, buchstabe in enumerate(geheimwort):
        if (eingabebuchstabe == buchstabe):
            erratenes_teilwort[buchstabenposition] = eingabebuchstabe


# Eigentliches Spiel
def starte_hangmanspiel(wörter_liste):

    #kündige_spieleröffnung_an()
    geheimwort = wähle_ein_zufälliges_wort(wörter_liste)
    erratenesTeilwort = gib_verdecktes_wort(geheimwort)
    fehlgeschlageneBuchstaben = []
    erlaubteFehlversuche = 10

    sleep(0.5)

    gui = HangmanGui(geheimwort, erratenesTeilwort, erlaubteFehlversuche)

    #zeige_Zustand(erratenesTeilwort, fehlgeschlageneBuchstaben, erlaubteFehlversuche)

    # TODO: Vielleicht würde hier ein einfacher Boolean Abgleich leichter zu verstehen sein.
    #       Weiß nicht, ob das für den Anfang zu verkapselt ist.
    while (ist_das_spiel_noch_am_laufen(erratenesTeilwort, erlaubteFehlversuche)):
        eingabebuchstabe = erhalte_großbuchstaben()

        if (eingabebuchstabe in erratenesTeilwort):
            nachricht ="Der Buchstabe ist bereits erraten.\nVersuche einen anderen Buchstaben."

        if (eingabebuchstabe in geheimwort):
            nachricht = "Glückwunsch, der Buchstabe ist im Wort enthalten"
            buchstaben_aufdecken(eingabebuchstabe, geheimwort, erratenesTeilwort)

        if (eingabebuchstabe in fehlgeschlageneBuchstaben):
            nachricht="Der Buchstabe ist bereits fehlgeschlagenen.\nVersuche einen anderen Buchstaben!"

        if (not (eingabebuchstabe in geheimwort)):
            erlaubteFehlversuche = verringere_um_eins(erlaubteFehlversuche)
            erweitere_fehlgeschlagene_BuchstabenListe(eingabebuchstabe, fehlgeschlageneBuchstaben)
            nachricht="Leider ist der Buchstabe nicht im Wort enthalten.\nDu hast nun ein Leben weniger!"

        gui.cycle(erratenesTeilwort, erlaubteFehlversuche, fehlgeschlageneBuchstaben, message=nachricht)

