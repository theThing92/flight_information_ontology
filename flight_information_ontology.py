from owlready2 import *

if __name__ == "__main__":
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


        class Sehenswürdigkeit(Startort, Zielort):
            namespace = onto


        # define realations between concepts/classes
        class hat_einen_zielort(ObjectProperty, FunctionalProperty):
            domain = [Flugreise]
            range = [Zielort]
            inverse_property = onto.ist_zielort_von


        class ist_zielort_von(ObjectProperty, FunctionalProperty):
            domain = [Zielort]
            range = [Flugreise]
            inverse_property = onto.hat_einen_zielort


        class hat_einen_startort(ObjectProperty, FunctionalProperty):
            domain = [Flugreise]
            range = [Startort]
            inverse_property = onto.ist_startort_von


        class ist_startort_von(ObjectProperty, FunctionalProperty):
            domain = [Startort]
            range = [Flugreise]
            inverse_property = onto.hat_einen_startort


        class ist_gültiger_startflughafen_für_flugreise(DataProperty, FunctionalProperty):
            domain = [Stadt, Flughafen, Land, Bundesstaat, Bundesland, Sonderverwaltungszone, Sehenswürdigkeit]
            range = [bool]


        class ist_gültiger_zielflughafen_für_flugreise(DataProperty, FunctionalProperty):
            domain = [Stadt, Flughafen, Land, Bundesstaat, Bundesland, Sonderverwaltungszone, Sehenswürdigkeit]
            range = [bool]


        class hat_synonyme(DataProperty):
            domain = [Stadt, Flughafen, Land, Bundesstaat, Bundesland, Sonderverwaltungszone, Sehenswürdigkeit]
            range = [str]


        class hat_flughäfen(ObjectProperty):
            domain = [Stadt, Flughafen, Land, Bundesstaat, Bundesland, Sonderverwaltungszone, Sehenswürdigkeit]
            range = [Flughafen]
            inverse_property = onto.ist_flughafen_von


        class ist_flughafen_von(ObjectProperty):
            domain = [Flughafen]
            range = [Stadt, Flughafen, Land, Bundesstaat, Bundesland, Sonderverwaltungszone, Sehenswürdigkeit]
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


        class ist_sehenswürdigkeit_von_stadt(ObjectProperty, FunctionalProperty):
            domain = [Sehenswürdigkeit]
            range = [Stadt]


        class hat_sehenswürdigkeiten(ObjectProperty):
            domain = [Stadt]
            range = [Sehenswürdigkeit]


        # define individuals within the given ontology
        reise1 = Flugreise(name="Flugreise1")
        reise2 = Flugreise(name="Flugreise2")

        # start / end
        start = Stadt(name="Düsseldorf", hat_synonyme=["DUS", "D-Dorf", "Ddorf"])
        ziel1 = Stadt(name="New York", hat_synonyme=["NY", "NYC"])
        ziel2 = Stadt(name="Hongkong", hat_synonyme=["HK", "Hong Kong"])

        # countries
        amerika = Land(name="Amerika", hat_synonyme=["USA", "Vereinigte Staaten von Amerika"])
        deutschland = Land(name="Deutschland", hat_synonyme=["Bundesrepublik Deutschland"])
        china = Land(name="China",
                     hat_synonyme=["Volksrepublik China", "Chinesische Repubrik", "Land der aufgehenden Sonne"])

        # federal staates
        düsseldorf_bundesland = Bundesland(name="Nord-Rhein-Westphalen", hat_synonyme=["NRW"])
        new_york_bundesstaat = Bundesstaat(name="New York", hat_synonyme=["NY"])
        hongkong_sovezone = Sonderverwaltungszone(name="Hongkong", hat_synonyme=["HK", "Hong Kong"])

        # airports
        düsseldorf_flughafen = Flughafen(name="Flughafen Düsseldorf",
                                         hat_synonyme=["Düsseldorf Flughafen", "Düsseldorf Airport", "DUS"])

        new_york_jfk = Flughafen(name="John F. Kennedy Airport", hat_synonyme=["JFK", "John F. Kennedy"])
        new_york_ewr = Flughafen(name="Newark Liberty International Airport",
                                 hat_synonyme=["EWR", " KEWR", "New York-Newark International Airport"])
        new_york_lga = Flughafen(name="LaGuarda Airport", hat_synonyme=["LGA"])

        hk_chep = Flughafen(name="Chek Lap Kok Hong Kong International Airport", hat_synonyme=["HKG", "Chek Lap Kok"])
        hk_shek = Flughafen(name="Shek Kong Airfield", hat_synonyme=["Shek Kong", "VHSK"])

        # sights
        düsseldorf_altstadt = Sehenswürdigkeit(name="Altstadt", hat_synonyme=["Düsseldorfer Altstadt"])
        düsseldorf_königsallee = Sehenswürdigkeit(name="Königsallee", hat_synonyme=["KÖ", "Düsseldorfer Königsallee",
                                                                                    "Königsallee Düsseldorf"])
        düsseldorf_rheinturm = Sehenswürdigkeit(name="Rheinturm",
                                                hat_synonyme=["Düsseldorfer Rheinturm", "Rheinturm Düsseldorf"])
        düsseldorf_schloss_benrath = Sehenswürdigkeit(name="Schloss Benrath",
                                                      hat_synonyme=["Schloss Benrath Düsseldorf"])

        new_york_freiheitsstatue = Sehenswürdigkeit(name="Freiheitsstatue",
                                                    hat_synonyme=["Statue of Liberty", "Statue of Liberty New York",
                                                                  "Statue of Liberty NYC", "Statue of Liberty NY",
                                                                  "Freiheitsstatue New York", "Freiheitsstatue NYC",
                                                                  "Freiheitsstatue NY"])
        new_york_central_park = Sehenswürdigkeit(name="Central Park", hat_synonyme=["Central Park New York"])
        new_york_times_square = Sehenswürdigkeit(name="Times Square", hat_synonyme=["Times Square New York"])
        new_york_rockefeller_center = Sehenswürdigkeit(name="Rockefeller Center",
                                                       hat_synonyme=["Rockefeller Center New York"])

        hongkong_victoria_peak = Sehenswürdigkeit(name="Victoria Peak",
                                                  hat_synonyme=["Victoria Peak Hongkong", "Victoria Peak Hong Kong"])
        hongkong_disney_land = Sehenswürdigkeit(name="Hong Kong Disneyland",
                                                hat_synonyme=["Hongkong Disneyland", "Hongkong Disney Land"])
        hongkong_ocean_park = Sehenswürdigkeit(name="Ocean Park Hong Kong", hat_synonyme=["Ocean Park Hongkong"])
        hongkong_victoria_harbour = Sehenswürdigkeit(name="Victoria Harbour", hat_synonyme=["Victoria Harbour Hongkong",
                                                                                            "Victoria Harbour Hong Kong",
                                                                                            "Victoria Hafen Hongkong",
                                                                                            "Victoria Hafen Hong Kong"])

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

        new_york_freiheitsstatue.ist_gültiger_startflughafen_für_flugreise = False
        new_york_freiheitsstatue.ist_gültiger_zielflughafen_für_flugreise = False

        new_york_central_park.ist_gültiger_startflughafen_für_flugreise = False
        new_york_central_park.ist_gültiger_zielflughafen_für_flugreise = False

        new_york_times_square.ist_gültiger_startflughafen_für_flugreise = False
        new_york_times_square.ist_gültiger_zielflughafen_für_flugreise = False

        new_york_rockefeller_center.ist_gültiger_startflughafen_für_flugreise = False
        new_york_rockefeller_center.ist_gültiger_zielflughafen_für_flugreise = False

        hongkong_disney_land.ist_gültiger_startflughafen_für_flugreise = False
        hongkong_disney_land.ist_gültiger_zielflughafen_für_flugreise = False

        hongkong_ocean_park.ist_gültiger_startflughafen_für_flugreise = False
        hongkong_ocean_park.ist_gültiger_zielflughafen_für_flugreise = False

        hongkong_victoria_harbour.ist_gültiger_startflughafen_für_flugreise = False
        hongkong_victoria_harbour.ist_gültiger_zielflughafen_für_flugreise = False

        hongkong_victoria_peak.ist_gültiger_startflughafen_für_flugreise = False
        hongkong_victoria_peak.ist_gültiger_zielflughafen_für_flugreise = False

        düsseldorf_altstadt.ist_gültiger_startflughafen_für_flugreise = False
        düsseldorf_altstadt.ist_gültiger_zielflughafen_für_flugreise = False

        düsseldorf_königsallee.ist_gültiger_startflughafen_für_flugreise = False
        düsseldorf_königsallee.ist_gültiger_zielflughafen_für_flugreise = False

        düsseldorf_rheinturm.ist_gültiger_startflughafen_für_flugreise = False
        düsseldorf_rheinturm.ist_gültiger_zielflughafen_für_flugreise = False

        düsseldorf_schloss_benrath.ist_gültiger_startflughafen_für_flugreise = False
        düsseldorf_schloss_benrath.ist_gültiger_zielflughafen_für_flugreise = False

        amerika.besteht_aus_bundesstaaten.append(new_york_bundesstaat)
        deutschland.besteht_aus_bundesländern.append(düsseldorf_bundesland)
        china.besteht_aus_sonderverwaltungszonen.append(hongkong_sovezone)

        düsseldorf_flughafen.ist_flughafen_von.append(start)
        new_york_lga.ist_flughafen_von.append(ziel1)
        new_york_ewr.ist_flughafen_von.append(ziel1)
        new_york_jfk.ist_flughafen_von.append(ziel1)

        hk_chep.ist_flughafen_von.append(ziel2)
        hk_shek.ist_flughafen_von.append(ziel2)

        start.hat_sehenswürdigkeiten.append(düsseldorf_schloss_benrath)
        start.hat_sehenswürdigkeiten.append(düsseldorf_rheinturm)
        start.hat_sehenswürdigkeiten.append(düsseldorf_königsallee)
        start.hat_sehenswürdigkeiten.append(düsseldorf_altstadt)

        ziel1.hat_sehenswürdigkeiten.append(new_york_rockefeller_center)
        ziel1.hat_sehenswürdigkeiten.append(new_york_freiheitsstatue)
        ziel1.hat_sehenswürdigkeiten.append(new_york_times_square)
        ziel1.hat_sehenswürdigkeiten.append(new_york_central_park)

        ziel2.hat_sehenswürdigkeiten.append(hongkong_victoria_peak)
        ziel2.hat_sehenswürdigkeiten.append(hongkong_victoria_harbour)
        ziel2.hat_sehenswürdigkeiten.append(hongkong_ocean_park)
        ziel2.hat_sehenswürdigkeiten.append(hongkong_disney_land)

        hongkong_ocean_park.ist_sehenswürdigkeit_von_stadt = ziel2
        hongkong_disney_land.ist_sehenswürdigkeit_von_stadt = ziel2
        hongkong_victoria_harbour.ist_sehenswürdigkeit_von_stadt = ziel2
        hongkong_victoria_peak.ist_sehenswürdigkeit_von_stadt = ziel2

        new_york_central_park.ist_sehenswürdigkeit_von_stadt = ziel1
        new_york_times_square.ist_sehenswürdigkeit_von_stadt = ziel1
        new_york_freiheitsstatue.ist_sehenswürdigkeit_von_stadt = ziel1
        new_york_rockefeller_center.ist_sehenswürdigkeit_von_stadt = ziel1

        düsseldorf_altstadt.ist_sehenswürdigkeit_von_stadt = start
        düsseldorf_königsallee.ist_sehenswürdigkeit_von_stadt = start
        düsseldorf_rheinturm.ist_sehenswürdigkeit_von_stadt = start
        düsseldorf_schloss_benrath.ist_sehenswürdigkeit_von_stadt = start
