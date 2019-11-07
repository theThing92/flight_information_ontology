from owlready2 import *


if __name__ == "__main__":


    #### TODO: sehenswürdigkeiten ergänzen

    # create empty ontology with some iri (internationalized ressource identifier)
    onto = get_ontology("flight_information_ontology.owl")

    # define the flight information ontolgy
    with onto:
        class Domänenkonzept(Thing):
            namespace = onto

        # define concepts/classes within the given flight domain
        class Flugreise(Domänenkonzept):
            namespace = onto

        class Startort(Thing):
            namespace = onto

        class Zielort(Thing):
            namespace = onto

        class Land(Startort, Zielort):
            namespace = onto

        class Stadt(Startort, Zielort):
            namespace = onto

        class Flughafen(Startort, Zielort):
            namespace = onto

        class Bundesland(Startort, Zielort):
            namespace = onto

        class Bundesstaat(Startort, Zielort):
            namespace = onto

        class Sonderverwaltungszone(Startort, Zielort):
            namespace = onto

        # define realations between concepts/classes
        class hat_einen_zielort(ObjectProperty, FunctionalProperty):
            domain = [Flugreise]
            range = [Zielort]
            inverse_property = onto.ist_zielort_von

        class ist_zielort_von(ObjectProperty, FunctionalProperty):
            domain = [Zielort]
            range = [Flugreise]
            inverse_property =  onto.hat_einen_zielort

        class hat_einen_startort(ObjectProperty, FunctionalProperty):
            domain = [Flugreise]
            range = [Startort]
            inverse_property = onto.ist_startort_von

        class ist_startort_von(ObjectProperty, FunctionalProperty):
            domain = [Startort]
            range = [Flugreise]
            inverse_property = onto.hat_einen_startort

        class ist_gültiger_startflughafen_für_flugreise(DataProperty, FunctionalProperty):
            domain = [Stadt, Flughafen, Land, Bundesstaat, Bundesland, Sonderverwaltungszone]
            range = [bool]

        class ist_gültiger_zielflughafen_für_flugreise(DataProperty, FunctionalProperty):
            domain = [Stadt, Flughafen, Land, Bundesstaat, Bundesland, Sonderverwaltungszone]
            range = [bool]

        class hat_synonyme(DataProperty):
            domain = [Stadt, Flughafen, Land, Bundesstaat, Bundesland, Sonderverwaltungszone]
            range = [str]

        class hat_flughäfen(ObjectProperty):
            domain = [Stadt, Flughafen, Land, Bundesstaat, Bundesland, Sonderverwaltungszone]
            range = [Flughafen]
            inverse_property  = onto.ist_flughafen_von

        class ist_flughafen_von(ObjectProperty):
            domain = [Flughafen]
            range = [Stadt, Flughafen, Land, Bundesstaat, Bundesland, Sonderverwaltungszone]
            inverse_property = onto.hat_flughäfen

        class besteht_aus_bundesländern(ObjectProperty):
            domain = [Land]
            range = [Bundesland]

        class besteht_aus_bundesstaaten(ObjectProperty):
            domain = [Land]
            range = [Bundesstaat]

        class ist_teil_von_land(ObjectProperty):
            domain = [Bundesland, Bundesstaat]
            range = [Land]

        class besteht_aus_städten(ObjectProperty):
            domain = [Bundesstaat, Bundesland, Sonderverwaltungszone]
            range = [Stadt]

        class besteht_aus_sonderverwaltungszonen(ObjectProperty):
            domain = [Land]
            range = [Sonderverwaltungszone]

        class ist_stadt_von_bundesland(ObjectProperty):
            domain = [Stadt]
            range = [Bundesland]

        class ist_stadt_von_bundesstaat(ObjectProperty):
            domain = [Stadt]
            range = [Bundesstaat]

        class ist_stadt_von_sonderverwaltungszone(ObjectProperty):
            domain = [Stadt]
            range = [Sonderverwaltungszone]


        # define individuals within the given ontology
        reise1 = Flugreise(name="Flugreise1")
        reise2 = Flugreise(name="Flugreise2")

        # start / end
        start = Stadt(name="Düsseldorf", hat_synonyme=["DUS", "D-Dorf", "Ddorf"])
        ziel1 = Stadt(name="New York", hat_synonyme=["NY", "NYC"])
        ziel2 = Stadt(name="Hongkong", hat_synonyme=["HK", "Hong Kong"])

        # countries
        amerika = Land(name="Amerika", hat_synonyme=["USA", "Vereinigte Staaten von Amerika"])
        deutschland =  Land(name="Deutschland", hat_synonyme=["Bundesrepublik Deutschland"])
        china = Land(name="China", hat_synonyme=["Volksrepublik China", "Chinesische Repubrik", "Land der aufgehenden Sonne"])

        # federal staates
        düsseldorf_bundesland = Bundesland(name="Nord-Rhein-Westphalen", hat_synonyme=["NRW"])
        new_york_bundesstaat = Bundesstaat(name="New York", hat_synonyme=["NY"])
        hongkong_sovezone = Sonderverwaltungszone(name="Hongkong", hat_synonyme = ["HK", "Hong Kong"])

        # airports
        düsseldorf_flughafen = Flughafen(name="Flughafen Düsseldorf", hat_synonyme=["Düsseldorf Flughafen", "Düsseldorf Airport","DUS"])

        new_york_jfk = Flughafen(name="John F. Kennedy Airport", hat_synonyme=["JFK", "John F. Kennedy"])
        new_york_ewr = Flughafen(name="Newark Liberty International Airport", hat_synonyme = ["EWR", " KEWR",  "New York-Newark International Airport"])
        new_york_lga = Flughafen(name="LaGuarda Airport", hat_synonyme=["LGA"])

        hk_chep = Flughafen(name="Chek Lap Kok Hong Kong International Airport", hat_synonyme=["HKG", "Chek Lap Kok"])
        hk_shek = Flughafen(name="Shek Kong Airfield", hat_synonyme=["Shek Kong", "VHSK"])

        # define relations between individuals
        reise1.hat_einen_startort = start
        reise1.hat_einen_zielort = ziel1

        reise2.hat_einen_startort = start
        reise2.hat_einen_zielort = ziel2

        start.ist_gültiger_startflughafen_für_flugreise = False
        start.ist_gültiger_zielflughafen_für_flugreise = False

        ziel1.ist_gültiger_startflughafen_für_flugreise = False
        ziel1.ist_gültiger_zielflughafen_für_flugreise = False

        ziel2.ist_gültiger_startflughafen_für_flugreise = False
        ziel2.ist_gültiger_zielflughafen_für_flugreise = False

        new_york_jfk.ist_gültiger_startflughafen_für_flugreise = False
        new_york_jfk.ist_gültiger_zielflughafen_für_flugreise = True

        düsseldorf_flughafen.ist_gültiger_startflughafen_für_flugreise = True
        düsseldorf_flughafen.ist_gültiger_zielflughafen_für_flugreise = False

        # no internationl airport
        new_york_ewr.ist_gültiger_startflughafen_für_flugreise = False
        new_york_ewr.ist_gültiger_zielflughafen_für_flugreise = False

        new_york_lga.ist_gültiger_startflughafen_für_flugreise = False
        new_york_lga.ist_gültiger_zielflughafen_für_flugreise = True

        hk_chep.ist_gültiger_startflughafen_für_flugreise = False
        hk_chep.ist_gültiger_zielflughafen_für_flugreise = True

        hk_shek.ist_gültiger_startflughafen_für_flugreise = False
        hk_shek.ist_gültiger_zielflughafen_für_flugreise = True

        amerika.besteht_aus_bundesstaaten.append(new_york_bundesstaat)
        deutschland.besteht_aus_bundesländern.append(düsseldorf_bundesland)
        china.besteht_aus_sonderverwaltungszonen.append(hongkong_sovezone)

        düsseldorf_flughafen.ist_flughafen_von.append(start)
        new_york_lga.ist_flughafen_von.append(ziel1)
        new_york_ewr.ist_flughafen_von.append(ziel1)
        new_york_jfk.ist_flughafen_von.append(ziel1)

        hk_chep.ist_flughafen_von.append(ziel2)
        hk_shek.ist_flughafen_von.append(ziel2)
