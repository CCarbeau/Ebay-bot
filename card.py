class card():
    def __init__(self, title, condition, auto):
        self.name = title
        self.cond = condition
        self.auto = auto
        
def createCards(condition):
    cards = [
        # Anthony Volpe: 
            card("2023 Topps Chrome Anthony-Volpe Refractor PSA 10",condition["Graded"], False),
            card("2023 Topps Chrome Anthony-Volpe X-fractor PSA 10",condition["Graded"], False),
            card("2023 Topps Chrome Anthony-Volpe Prism Refractor 4 PSA 10",condition["Graded"], False),
            card("2023 Topps Chrome Sapphire Anthony-Volpe 460 PSA 10",condition["Graded"], False),
            card("2023 Topps Chrome Anthony-Volpe auto PSA 10", condition["Graded"], True),
            card("2020 Bowman Chrome Anthony-Volpe 1st auto PSA 10", condition["Graded"], True),
            card("2020 Bowman Chrome Anthony-Volpe 1st auto PSA 9", condition["Graded"], True),
            card("2020 Bowman Chrome Anthony-Volpe 1st PSA 10", condition["Graded"], False),
            card("2020 Bowman Chrome Anthony-Volpe 1st Refractor PSA 10", condition["Graded"], False),
        
        # Adley Rutschman:
            card("2023 Topps Chrome Adley-Rutschman Refractor PSA 10",condition["Graded"], False),
            card("2023 Topps Chrome Adley-Rutschman X-fractor PSA 10",condition["Graded"], False),
            card("2023 Topps Chrome Adley-Rutschman Prism Refractor PSA 10",condition["Graded"], False),
            card("2023 Topps Chrome Adley-Rutschman auto PSA 10",condition["Graded"], True),
            card("2023 Topps Chrome Sapphire Adley-Rutschman 250 PSA 10",condition["Graded"], False),
            card("2019 Bowman Chrome Adley-Rutschman 1st auto PSA 10",condition["Graded"], True),
            card("2019 Bowman Chrome Adley-Rutschman 1st auto",condition["Ungraded"], True),
        
        # Gunnar Henderson: 
            card("2023 Topps Chrome Gunnar-Henderson 2 Refractor PSA 10",condition["Graded"], False),
            card("2023 Topps Chrome Gunnar-Henderson X-fractor PSA 10",condition["Graded"], False),
            card("2023 Topps Chrome Gunnar-Henderson Prism Refractor PSA 10",condition["Graded"], False),
            card("2023 Topps Chrome Gunnar-Henderson auto PSA 10",condition["Graded"], True),
            card("2023 Topps Chrome Sapphire Gunnar-Henderson 206 PSA 10",condition["Graded"], False),
            card("2019 Bowman Chrome Draft Gunnar-Henderson 1st auto PSA 10",condition["Graded"], True),
            card("2019 Bowman Chrome Draft Gunnar-Henderson 1st PSA 10",condition["Graded"], True),
            card("2019 Bowman Chrome Draft Refractor Gunnar-Henderson 1st PSA 10",condition["Graded"], True),
        
        # Julio Rodriguez: 
            card("2022 Topps Chrome Update Julio-Rodriguez USC150 PSA 10",condition["Graded"], False),
            
        # Bobby Witt Jr:    
            card("2022 Topps Update Bobby-Witt-Jr USC35 PSA 10",condition["Graded"], False),
        
        # Max Clark:
            card("2023 Bowman Draft Max-Clark 1st auto PSA 10",condition["Graded"], True),
            card("2023 Bowman Draft Max-Clark 1st auto",condition["Ungraded"], True),
            card("2023 Bowman Draft Max-Clark BDC76 PSA 10",condition["Graded"], False),
        
        # Luisangel Acuna
            card("2020 Bowman Chrome 1st Luisangel-Acuna auto PSA 10",condition["Graded"], True),
            card("2020 Bowman Chrome 1st Luisangel-Acuna auto",condition["Ungraded"], True),
        
        # Chase DeLauter:
            card("2022 Bowman Draft Chase-DeLauter 1st auto PSA 10",condition["Graded"], True),
            card("2022 Bowman Draft Chase-DeLauter 1st auto",condition["Ungraded"], True),
        
        # Jackson Merrill: 
            card("2022 Bowman Chrome Jackson-Merrill 1st auto PSA 10",condition["Graded"], True),
            card("2022 Bowman Chrome Jackson-Merrill 1st auto",condition["Ungraded"], True),
        
        # Adael Amador:
            card("2021 Bowman Chrome Adael-Amador 1st auto PSA 10",condition["Graded"], True),
            card("2021 Bowman Chrome Adael-Amador 1st auto",condition["Ungraded"], True),
        
        # Carson Williams: 
            card("2021 Bowman Draft Carson-Williams 1st auto PSA 10",condition["Graded"], True),
            card("2021 Bowman Draft Carson-Williams 1st auto",condition["Ungraded"], True),
        
        # Colt Emerson:
            card("2023 Bowman Draft Colt-Emerson 1st auto PSA 10",condition["Graded"], True),
            card("2023 Bowman Draft Colt-Emerson 1st auto",condition["Ungraded"], True),
        
        # Colson Montgomery:
            card("2022 Bowman Chrome Colson-Montgomery 1st auto PSA 10",condition["Graded"], True),
            card("2022 Bowman Chrome Colson-Montgomery 1st auto",condition["Ungraded"], True),
        
        # Curtis Mead:
            card("2022 Bowman Chrome Curtis-Mead 1st auto PSA 10",condition["Graded"], True),
            card("2022 Bowman Chrome Curtis-Mead 1st auto", condition["Ungraded"], True),
        
        # Jett Williams:
            card("2022 Bowman Draft Jett-Williams 1st auto PSA 10", condition["Graded"], True),
            card("2022 Bowman Draft Jett-Williams 1st auto",condition["Ungraded"], True),
        
        # Jordan Lawlar:
            card("2021 Bowman Draft Jordan-Lawlar 1st auto BD-194 PSA 10",condition["Graded"], True),
        
        # James Wood:
            card("2022 Bowman Chrome James-Wood 1st auto PSA 10",condition["Graded"], True),
        
        # Jasson Dominguez: 
            card("2020 Bowman Chrome Jasson-Dominguez 1st CPA-JDO PSA 10",condition["Graded"], True),
        
        # Matt Shaw: 
            card("2023 Bowman Draft Matt-Shaw 1st auto PSA 10",condition["Graded"], True),
            card("2023 Bowman Draft Matt-Shaw 1st auto",condition["Ungraded"], True),
        
        # Roman Anthony: 
            card("2023 Bowman Chrome Roman-Anthony 1st auto PSA 10",condition["Graded"], True),
            card("2023 Bowman Chrome Roman-Anthony 1st auto",condition["Ungraded"], True),
        
        # Coby Mayo:
            card("2021 Bowman Chrome Coby-Mayo 1st auto PSA 10",condition["Graded"], True),
            card("2021 Bowman Chrome Coby-Mayo 1st auto",condition["Ungraded"], True),
        
        # Colt Keith:
            card("2020 Bowman Draft Colt-Keith 1st auto PSA 10",condition["Graded"], True),
            card("2020 Bowman Draft Colt-Keith 1st auto",condition["Ungraded"], True),
        
        # Noelvi Marte:
            card("2019 Bowman Chrome Noelvi-Marte 1st auto PSA 10",condition["Graded"], True),
        
        # Pete Crow Armstrong: 
            card("2020 Bowman Chrome Draft Pete-Crow-Armstrong 1st auto PSA 10",condition["Graded"], True), 
            card("2020 Bowman Draft Pete-Crow-Armstrong 1st auto",condition["Ungraded"], True), 
        
        # Samuel Basallo: 
            card("2023 Bowman Chrome Samuel-Basallo 1st auto PSA 10",condition["Graded"], True),
            card("2023 Bowman Chrome Samuel-Basallo 1st auto",condition["Ungraded"], True),
        
        # Evan Carter: 
            card("2020 Bowman Draft Evan-Carter 1st auto PSA 10",condition["Graded"], True),
            card("2020 Bowman Draft Evan-Carter 1st auto",condition["Ungraded"], True),
        
        # Ethan Salas:
            card("2023 Bowman Chrome Ethan-Salas 1st auto PSA 10",condition["Graded"], True),
            card("2023 Bowman Chrome Ethan-Salas 1st auto",condition["Ungraded"], True),
        
        # Junior Caminero:
            card("2023 Bowman Chrome Junior-Caminero 1st auto PSA 10",condition["Graded"], True),
            card("2023 Bowman Chrome Junior-Caminero 1st auto",condition["Ungraded"], True),
        
        # Wyatt Langford:
            card("2023 Bowman Draft Wyatt-Langford 1st auto PSA 10",condition["Graded"], True),
            card("2023 Bowman Draft Wyatt-Langford 1st auto",condition["Ungraded"], True),
            card("2023 Bowman Draft Wyatt-Langford BDC 1st PSA 10",condition["Graded"], False),
        
        # Jackson Chourio:
            card("2022 Bowman Chrome Jackson-Chourio 1st auto PSA 10",condition["Graded"], True),
            card("2022 Bowman Chrome Jackson-Chourio 1st BCP PSA 10",condition["Graded"], False),
        
        # Jackson Holliday:
            card("2022 Bowman Draft Jackson-Holliday 1st auto PSA 10",condition["Graded"], True),
            card("2022 Bowman Draft Jackson-Holliday 1st auto",condition["Ungraded"], True),
            card("2022 Bowman Draft Jackson-Holliday 1st BDC PSA 10",condition["Graded"], False),
            card("2022 Bowman Draft Jackson-Holliday 1st Paper PSA 10",condition["Graded"], False),
        
        # Elly De La Cruz: 
            card("2022 Bowman Chrome Elly-de-la-Cruz 1st BCP PSA 10", condition["Graded"], False),
            card("2022 Bowman Chrome Elly-de-la-Cruz 1st BCP Mojo PSA 10", condition["Graded"], False),
            card("2024 Topps Series 1 Elly-de-la-Cruz Rainbow Foil 141", condition["Ungraded"], False),
            card("2024 Topps Series 1 Elly-de-la-Cruz Gold Foil 141", condition["Ungraded"], False),
        
        # O'neil Cruz:
            card("2022 Topps Chrome Oneil-Cruz Pink Refractor 128 PSA 10", condition["Graded"], False),
        
        # Corbin Carroll:
            card("2023 Topps Chrome Refractor Corbin-Carroll 95 PSA 10", condition["Graded"],False),
            card("2023 Topps Chrome Corbin-Carroll Auto RACCA PSA 10", condition["Graded"],True),
            card("2023 Topps Chrome Corbin-Carroll Auto RACCA", condition["Ungraded"],True),
            card("2019 Bowman Draft Chrome Corbin-Carroll 1st PSA 10", condition["Graded"],False),
            card("2019 Bowman Draft Chrome Corbin-Carroll 1st PSA 10 auto", condition["Graded"],True),
        
        # Paul Skenes:
            card("2023 Bowman Draft Chrome Paul Skenes 1st BDC PSA 10", condition["Graded"],False),
            card("2023 Bowman Draft Chrome Paul Skenes 1st PSA 10 auto", condition["Graded"],True),
            card("2023 Bowman Draft Chrome Paul Skenes 1st auto", condition["Ungraded"],True),
        
        # Aaron Judge:
            card("2017 Topps Chrome Aaron-Judge 169 PSA 10", condition["Graded"],False),
        
        # Ronald Acuna Jr:
            card("2017 Bowman Ronald-Acuna-Jr Chrome 1st 127 PSA 10", condition["Graded"],False),
            card("2018 Topps Update Ronald-Acuna-Jr 250 PSA 10", condition["Graded"],False),
            card("2018 Topps Chrome Ronald-Acuna-Jr 193 PSA 10", condition["Graded"],False),
        
        # Shohei Ohtani:
            card("2018 Topps Chrome Shohei-Ohtani 150 PSA 10", condition["Graded"],False),
            card("2018 Topps Chrome Update Shohei-Ohtani 32 PSA 10", condition["Graded"],False),
            card("2018 Topps Chrome Update Shohei-Ohtani HMT1 PSA 10", condition["Graded"],False),
            card("2018 Bowman Shohei-Ohtani 49 PSA 10", condition["Graded"],False),
            card("2018 Bowman Chrome Shohei-Ohtani 1 batting PSA 10", condition["Graded"],False),
        
        # Juan Soto: 
            card("2018 Topps Chrome Update Juan-Soto 55 PSA 10", condition["Graded"],False),
            card("2018 Topps Update Juan-Soto 300 PSA 10", condition["Graded"],False),
        
        # Mookie Betts:
            card("2014 Bowman Chrome BCP Mookie-Betts PSA 10", condition["Graded"], False),
            card("2014 Topps Update Mookie-Betts 26 PSA 10", condition["Graded"], False),
        
        # Victor Wembanyama:
            card("2023 Prizm Draft Victor-Wembanyama PSA 10", condition["Graded"], False),
            card("2023 Prizm Victor-Wembanyama 136 PSA 10", condition["Graded"], False),
        
        # CJ Stroud:
            card("2023 Panini Donruss C.J.-Stroud 339 PSA 10", condition["Graded"], False),
            card("2023 Panini Prizm 339 CJ-Stroud PSA 10", condition["Graded"],False),
            card("2023 Panini Prizm CJ-Stroud-339", condition["Ungraded"],False),
            
            # yamamoto, 
            # mike trout, jram, yordan, harper, lindor, tatis, verlander, scherzer, kershaw,
            # bedard, paolo, puka, purdy, anthony edwards, haliburton 
            ]
    return cards