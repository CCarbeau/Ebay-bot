class card():
    def __init__(self, title, condition, auto):
        self.name = title
        self.cond = condition
        self.auto = auto
        
def createCards(condition):
    cards = [
        # # BASEBALL:
        # # Anthony Volpe: 
        #     card("2023 Topps Chrome Anthony-Volpe Refractor 4 PSA 10",condition["Graded"], False),
        #     card("2023 Topps Chrome Anthony-Volpe X-fractor PSA 10",condition["Graded"], False),
        #     card("2023 Topps Chrome Anthony-Volpe Prism Refractor 4 PSA 10",condition["Graded"], False),
        #     card("2023 Topps Chrome Sapphire Anthony-Volpe 460 PSA 10",condition["Graded"], False),
        #     card("2023 Topps Chrome Anthony-Volpe auto PSA 10", condition["Graded"], True),
        #     card("2020 Bowman Chrome Anthony-Volpe 1st auto PSA 10", condition["Graded"], True),
        #     card("2020 Bowman Chrome Anthony-Volpe 1st auto PSA 9", condition["Graded"], True),
        #     card("2020 Bowman Chrome Anthony-Volpe 1st PSA 10", condition["Graded"], False),
        #     card("2020 Bowman Chrome Anthony-Volpe 1st Refractor PSA 10", condition["Graded"], False),
        
        # # Adley Rutschman:
        #     card("2023 Topps Chrome Adley-Rutschman Refractor PSA 10",condition["Graded"], False),
        #     card("2023 Topps Chrome Adley-Rutschman X-fractor PSA 10",condition["Graded"], False),
        #     card("2023 Topps Chrome Adley-Rutschman Prism Refractor PSA 10",condition["Graded"], False),
        #     card("2023 Topps Chrome Adley-Rutschman auto PSA 10",condition["Graded"], True),
        #     card("2023 Topps Chrome Sapphire Adley-Rutschman 250 PSA 10",condition["Graded"], False),
        #     card("2019 Bowman Chrome Adley-Rutschman 1st auto PSA 10",condition["Graded"], True),
        #     card("2019 Bowman Chrome Adley-Rutschman 1st auto",condition["Ungraded"], True),
        
        # # Gunnar Henderson: 
        #     card("2023 Topps Chrome Gunnar-Henderson 2 Refractor PSA 10",condition["Graded"], False),
        #     card("2023 Topps Chrome Gunnar-Henderson X-fractor PSA 10",condition["Graded"], False),
        #     card("2023 Topps Chrome Gunnar-Henderson Prism Refractor PSA 10",condition["Graded"], False),
        #     card("2023 Topps Chrome Gunnar-Henderson auto PSA 10",condition["Graded"], True),
        #     card("2023 Topps Chrome Sapphire Gunnar-Henderson 206 PSA 10",condition["Graded"], False),
        #     card("2019 Bowman Chrome Draft Gunnar-Henderson 1st auto PSA 10",condition["Graded"], True),
        #     card("2019 Bowman Chrome Draft Gunnar-Henderson 1st PSA 10",condition["Graded"], True),
        #     card("2019 Bowman Chrome Draft Refractor Gunnar-Henderson 1st PSA 10",condition["Graded"], True),
        
        # # Julio Rodriguez: 
        #     card("2022 Topps Chrome Update Julio-Rodriguez USC150 PSA 10",condition["Graded"], False),
            
        # # Bobby Witt Jr:    
        #     card("2022 Topps Update Bobby-Witt-Jr USC35 PSA 10",condition["Graded"], False),
        
        # # Max Clark:
        #     card("2023 Bowman Draft Max-Clark 1st auto PSA 10",condition["Graded"], True),
        #     card("2023 Bowman Draft Max-Clark 1st auto",condition["Ungraded"], True),
        #     card("2023 Bowman Draft Max-Clark BDC76 PSA 10",condition["Graded"], False),
        
        # # Luisangel Acuna
        #     card("2020 Bowman Chrome 1st Luisangel-Acuna auto PSA 10",condition["Graded"], True),
        #     card("2020 Bowman Chrome 1st Luisangel-Acuna auto",condition["Ungraded"], True),
        
        # # Chase DeLauter:
        #     card("2022 Bowman Draft Chase-DeLauter 1st auto PSA 10",condition["Graded"], True),
        #     card("2022 Bowman Draft Chase-DeLauter 1st auto",condition["Ungraded"], True),
        
        # # Jackson Merrill: 
        #     card("2022 Bowman Chrome Jackson-Merrill 1st auto PSA 10",condition["Graded"], True),
        #     card("2022 Bowman Chrome Jackson-Merrill 1st auto",condition["Ungraded"], True),
        
        # # Adael Amador:
        #     card("2021 Bowman Chrome Adael-Amador 1st auto PSA 10",condition["Graded"], True),
        #     card("2021 Bowman Chrome Adael-Amador 1st auto",condition["Ungraded"], True),
        
        # # Carson Williams: 
        #     card("2021 Bowman Draft Carson-Williams 1st auto PSA 10",condition["Graded"], True),
        #     card("2021 Bowman Draft Carson-Williams 1st auto",condition["Ungraded"], True),
        
        # # Colt Emerson:
        #     card("2023 Bowman Draft Colt-Emerson 1st auto PSA 10",condition["Graded"], True),
        #     card("2023 Bowman Draft Colt-Emerson 1st auto",condition["Ungraded"], True),
        
        # # Colson Montgomery:
        #     card("2022 Bowman Chrome Colson-Montgomery 1st auto PSA 10",condition["Graded"], True),
        #     card("2022 Bowman Chrome Colson-Montgomery 1st auto",condition["Ungraded"], True),
        
        # # Curtis Mead:
        #     card("2022 Bowman Chrome Curtis-Mead 1st auto PSA 10",condition["Graded"], True),
        #     card("2022 Bowman Chrome Curtis-Mead 1st auto", condition["Ungraded"], True),
        
        # # Jett Williams:
        #     card("2022 Bowman Draft Jett-Williams 1st auto PSA 10", condition["Graded"], True),
        #     card("2022 Bowman Draft Jett-Williams 1st auto",condition["Ungraded"], True),
        
        # # Jordan Lawlar:
        #     card("2021 Bowman Draft Jordan-Lawlar 1st auto BD-194 PSA 10",condition["Graded"], True),
        
        # # James Wood:
        #     card("2022 Bowman Chrome James-Wood 1st auto PSA 10",condition["Graded"], True),
        
        # # Jasson Dominguez: 
        #     card("2020 Bowman Chrome Jasson-Dominguez 1st CPA-JDO PSA 10",condition["Graded"], True),
        
        # # Matt Shaw: 
        #     card("2023 Bowman Draft Matt-Shaw 1st auto PSA 10",condition["Graded"], True),
        #     card("2023 Bowman Draft Matt-Shaw 1st auto",condition["Ungraded"], True),
        
        # # Roman Anthony: 
        #     card("2023 Bowman Chrome Roman-Anthony 1st auto PSA 10",condition["Graded"], True),
        #     card("2023 Bowman Chrome Roman-Anthony 1st auto",condition["Ungraded"], True),
        
        # # Coby Mayo:
        #     card("2021 Bowman Chrome Coby-Mayo 1st auto PSA 10",condition["Graded"], True),
        #     card("2021 Bowman Chrome Coby-Mayo 1st auto",condition["Ungraded"], True),
        
        # # Colt Keith:
        #     card("2020 Bowman Draft Colt-Keith 1st auto PSA 10",condition["Graded"], True),
        #     card("2020 Bowman Draft Colt-Keith 1st auto",condition["Ungraded"], True),
        
        # # Pete Crow Armstrong: 
        #     card("2020 Bowman Chrome Draft Pete-Crow-Armstrong 1st auto PSA 10",condition["Graded"], True), 
        #     card("2020 Bowman Draft Pete-Crow-Armstrong 1st auto",condition["Ungraded"], True), 
        
        # # Samuel Basallo: 
        #     card("2023 Bowman Chrome Samuel-Basallo 1st auto PSA 10",condition["Graded"], True),
        #     card("2023 Bowman Chrome Samuel-Basallo 1st Refractor auto PSA 10",condition["Graded"], True),
        #     card("2023 Bowman Chrome Samuel-Basallo 1st auto",condition["Ungraded"], True),
        
        # # Evan Carter: 
        #     card("2020 Bowman Draft Evan-Carter 1st auto PSA 10",condition["Graded"], True),
        #     card("2020 Bowman Draft Evan-Carter 1st auto",condition["Ungraded"], True),
        
        # # Ethan Salas:
        #     card("2023 Bowman Chrome Ethan-Salas 1st auto PSA 10",condition["Graded"], True),
        #     card("2023 Bowman Chrome Ethan-Salas 1st auto",condition["Ungraded"], True),
        
        # # Junior Caminero:
        #     card("2023 Bowman Chrome Junior-Caminero 1st auto PSA 10",condition["Graded"], True),
        #     card("2023 Bowman Chrome Junior-Caminero 1st auto",condition["Ungraded"], True),
        
        # # Wyatt Langford:
        #     card("2023 Bowman Draft Wyatt-Langford 1st auto PSA 10",condition["Graded"], True),
        #     card("2023 Bowman Draft Wyatt-Langford 1st auto",condition["Ungraded"], True),
        #     card("2023 Bowman Draft Wyatt-Langford BDC 1st PSA 10",condition["Graded"], False),
        
        # # Jackson Chourio:
        #     card("2022 Bowman Chrome Jackson-Chourio 1st auto PSA 10",condition["Graded"], True),
        #     card("2022 Bowman Chrome Jackson-Chourio 1st BCP PSA 10",condition["Graded"], False),
        
        # # Jackson Holliday:
        #     card("2022 Bowman Draft Jackson-Holliday 1st auto PSA 10",condition["Graded"], True),
        #     card("2022 Bowman Draft Jackson-Holliday 1st auto",condition["Ungraded"], True),
        #     card("2022 Bowman Draft Jackson-Holliday 1st BDC PSA 10",condition["Graded"], False),
        #     card("2022 Bowman Draft Jackson-Holliday 1st Paper PSA 10",condition["Graded"], False),
        
        # # Elly De La Cruz: 
        #     card("2022 Bowman Chrome Elly-de-la-Cruz 1st BCP PSA 10", condition["Graded"], False),
        #     card("2022 Bowman Chrome Elly-de-la-Cruz 1st BCP Mojo PSA 10", condition["Graded"], False),
        #     card("2024 Topps Series 1 Elly-de-la-Cruz Rainbow Foil 141", condition["Ungraded"], False),
        #     card("2024 Topps Series 1 Elly-de-la-Cruz Gold Foil 141", condition["Ungraded"], False),
        
        # # O'neil Cruz:
        #     card("2022 Topps Chrome Oneil-Cruz Pink Refractor 128 PSA 10", condition["Graded"], False),
        
        # # Corbin Carroll:
        #     card("2023 Topps Chrome Refractor Corbin-Carroll 95 PSA 10", condition["Graded"],False),
        #     card("2023 Topps Chrome Corbin-Carroll Auto RACCA PSA 10", condition["Graded"],True),
        #     card("2023 Topps Chrome Corbin-Carroll Auto RACCA", condition["Ungraded"],True),
        #     card("2019 Bowman Draft Chrome Corbin-Carroll 1st PSA 10", condition["Graded"],False),
        #     card("2019 Bowman Draft Chrome Corbin-Carroll 1st PSA 10 auto", condition["Graded"],True),
        
        # # Paul Skenes:
        #     card("2023 Bowman Draft Chrome Paul Skenes 1st BDC PSA 10", condition["Graded"],False),
        #     card("2023 Bowman Draft Chrome Paul Skenes 1st PSA 10 auto", condition["Graded"],True),
        #     card("2023 Bowman Draft Chrome Paul Skenes 1st auto", condition["Ungraded"],True),
        
        # # Aaron Judge:
        #     card("2017 Topps Chrome Aaron-Judge 169 PSA 10", condition["Graded"],False),
        
        # # Ronald Acuna Jr:
        #     card("2017 Bowman Ronald-Acuna-Jr Chrome 1st 127 PSA 10", condition["Graded"],False),
        #     card("2018 Topps Update Ronald-Acuna-Jr 250 PSA 10", condition["Graded"],False),
        #     card("2018 Topps Chrome Ronald-Acuna-Jr 193 PSA 10", condition["Graded"],False),
        
        # # Shohei Ohtani:
        #     card("2018 Topps Chrome Shohei-Ohtani 150 PSA 10", condition["Graded"],False),
        #     card("2018 Topps Chrome Update Shohei-Ohtani 32 PSA 10", condition["Graded"],False),
        #     card("2018 Topps Chrome Update Shohei-Ohtani HMT1 PSA 10", condition["Graded"],False),
        #     card("2018 Bowman Shohei-Ohtani 49 PSA 10", condition["Graded"],False),
        #     card("2018 Bowman Chrome Shohei-Ohtani 1 batting PSA 10", condition["Graded"],False),
        
        # # Juan Soto: 
        #     card("2018 Topps Chrome Update Juan-Soto 55 PSA 10", condition["Graded"],False),
        #     card("2018 Topps Update Juan-Soto 300 PSA 10", condition["Graded"],False),
        
        # # Mookie Betts:
        #     card("2014 Bowman Chrome BCP Mookie-Betts PSA 10", condition["Graded"], False),
        #     card("2014 Topps Update Mookie-Betts 26 PSA 10", condition["Graded"], False),

        # # Mike Trout:
        #     card("2011 Topps Update Mike-Trout PSA 10", condition["Graded"], False),
        #     card("2011 Topps Update Mike-Trout", condition["Ungraded"], False),

        # # Cheap Autos
        #     card("2023 Bowman Draft 1st Auto PSA 10", condition["Graded"], True),
        #     card("2023 Bowman Chrome 1st Auto PSA 10", condition["Graded"], True),
        #     card("2022 Bowman Draft 1st Auto PSA 10", condition["Graded"], True),
        #     card("2022 Bowman Chrome 1st Auto PSA 10", condition["Graded"], True),
        #     card("2021 Bowman Draft 1st Auto PSA 10", condition["Graded"], True),
        #     card("2021 Bowman Chrome 1st Auto PSA 10", condition["Graded"], True),
        #     card("2020 Bowman Draft 1st Auto PSA 10", condition["Graded"], True),
        #     card("2020 Bowman Chrome 1st Auto PSA 10", condition["Graded"], True),
        #     card("2024 Topps Baseball Auto PSA 10", condition["Graded"], True),
        #     card("2023 Topps Chrome Baseball Auto PSA 10", condition["Graded"], True),
        #     card("2023 Topps Baseball Auto PSA 10", condition["Graded"], True),
        #     card("2022 Topps Chrome Baseball Auto PSA 10", condition["Graded"], True),
        #     card("2022 Topps Baseball Auto PSA 10", condition["Graded"], True),
        #     card("2021 Topps Chrome Baseball Auto PSA 10", condition["Graded"], True),
        #     card("2021 Topps Baseball Auto PSA 10", condition["Graded"], True),
        #     card("2020 Topps Chrome Baseball Auto PSA 10", condition["Graded"], True),
        #     card("2020 Topps Baseball Auto PSA 10", condition["Graded"], True),
        #     card("2019 Topps Chrome Baseball Auto PSA 10", condition["Graded"], True),
        #     card("2019 Topps Baseball Auto PSA 10", condition["Graded"], True),
        #     card("2018 Topps Chrome Baseball Auto PSA 10", condition["Graded"], True),
        #     card("2018 Topps Baseball Auto PSA 10", condition["Graded"], True),

        # # BASKETBALL:
        # # Victor Wembanyama:
        #     card("2023 Prizm Draft Victor-Wembanyama PSA 10", condition["Graded"], False),
        #     card("2023 Prizm Victor-Wembanyama 136 PSA 10", condition["Graded"], False),

        # Steph Curry:
            card("2009 Topps Stephen Curry #321 PSA 9", condition["Graded"],False),
            card("2009 Topps Stephen Curry #321 PSA 8", condition["Graded"],False),
            card("2009 Topps Stephen Curry #321 PSA 7", condition["Graded"],False),
        # Lebron James:
            card("2003-04 Topps 2003 NBA Draft #221 LeBron James PSA 9", condition["Graded"],False),
            card("2003-04 Topps 2003 NBA Draft #221 LeBron James PSA 8", condition["Graded"],False),
            card("2003-04 Topps chrome 111 2003 LeBron James PSA 9", condition["Graded"],False),
            card("2003-04 Topps chrome 111 2003 LeBron James PSA 8", condition["Graded"],False),
            card("2003-04 Topps chrome 111 2003 LeBron James PSA 7", condition["Graded"],False),

        # Luka Doncic:
            card("2018 Panini Prizm Luka-Doncic Rookie RC #280 PSA 10", condition["Graded"], False),
            card("2018-19 Donruss Rated Rookie Luka Doncic PSA 10 ROOKIE CARD RC #177", condition["Graded"], False),
            card("2018 Panini Select Luka Doncic Concourse RC PSA 10 #25", condition["Graded"], False),
            card("2018-19 Panini Select Premier level #122 Luka Doncic PSA 10", condition["Graded"], False),
        
        # Nikola Jokic:
            card("2015-16 Panini Prizm Nikola Jokic #335 PSA 10", condition["Graded"], False),
            card("2015-16 Panini Prizm Nikola Jokic #335 PSA 9", condition["Graded"], False),
            card("2015-16 Panini Select #128 Nikola Jokic PSA 10", condition["Graded"], False),
            card("2015-16 Panini Select Premier #128 Nikola Jokic PSA 9", condition["Graded"], False),

        # Anthony Edwards:
            card("2020-2021 Panini Prizm Anthony Edwards 258 PSA 10", condition["Graded"], False),
            card("2020-2021 Panini Prizm Anthony Edwards 258 Silver PSA 10", condition["Graded"], False),
            card("2020-2021 Panini Prizm Anthony Edwards 258 Silver PSA 9", condition["Graded"], False),

        # Zion Williamson:
            card("2019 Panini Prizm Zion Williamson 248 PSA 10", condition["Graded"], False),
            card("2019 Panini Prizm Zion Williamson Silver 248 PSA 10", condition["Graded"], False),

        # Paolo Banchero:
            card("2022-23 Panini Prizm Paolo Banchero #249 Prizm PSA 10", condition["Graded"], False),
            card("2022-23 Panini Prizm Paolo Banchero #249 Silver Prizm PSA 10", condition["Graded"], False),

        # Jason Tatum:
            card("2017-18 Panini Prizm Jayson Tatum 16 PSA 10",condition["Graded"], False),
            card("2017-18 Panini Prizm Jayson Tatum Silver 16 PSA 10",condition["Graded"], False),
            card("2017-18 Panini Prizm Jayson Tatum Silver 16 PSA 9",condition["Graded"], False),
            
        # Giannis Antetokounmpo:
            card("2013-14 Panini Prizm 290 Giannis Antetokounmpo PSA 10", condition["Graded"], False),
            card("2013-14 Panini Prizm 290 Giannis Antetokounmpo PSA 9", condition["Graded"], False),

        # Michael Jordan:
            card("1986 Fleer #57 Michael Jordan PSA 7", condition["Graded"], False),
            card("1986 Fleer #57 Michael Jordan PSA 6", condition["Graded"], False),
            card("1986 Fleer #57 Michael Jordan PSA 5", condition["Graded"], False),
            card("1986 Fleer #57 Michael Jordan PSA 4", condition["Graded"], False),
            card("1986 Fleer #57 Michael Jordan PSA 3", condition["Graded"], False),

        # Chet Holmgreen:
            card("2022 Panini Prizm 266 Chet Holmgren PSA 10", condition["Graded"], False),
            card("2022 Panini Prizm 266 Chet Holmgren Silver PSA 10", condition["Graded"], False),
            card("2022 Panini Prizm 266 Chet Holmgren Green PSA 10", condition["Graded"], False),

        # Shai Gilgeous-Alexander:
            card("2018-19 Panini Prizm 184 Shai Gilgeous-Alexander PSA 10", condition["Graded"], False),
            card("2018-19 Panini Prizm 184 Shai Gilgeous-Alexander Silver PSA 10", condition["Graded"], False),
            card("2018-19 Panini Prizm 184 Shai Gilgeous-Alexander Green PSA 10", condition["Graded"], False),

        # Kyrie Irving:
            card("2012 Panini Prizm #201 Kyrie Irving PSA 10", condition["Graded"], False),
            card("2012 Panini Prizm #201 Kyrie Irving Silver PSA 10", condition["Graded"], False),

        # Trae Young:
            card("2018-19 Panini Prizm Trae Young 78 PSA 10", condition["Graded"], False),
            card("2018-19 Panini Prizm Trae Young Silver 78 PSA 10", condition["Graded"], False),
            card("2018-19 Panini Prizm Trae Young Green 78 PSA 10", condition["Graded"], False),

        # Damian Lillard:
            card("2012-13 Panini Prizm Damian Lillard 245 PSA 10", condition["Graded"], False),
            card("2012-13 Panini Prizm Damian Lillard Silver 245 PSA 10", condition["Graded"], False),
            card("2012-13 Panini Prizm Damian Lillard Silver 245 PSA 9", condition["Graded"], False),

        # Jimmy Butler:
            card("2012-13 Prizm Jimmy Butler 205 PSA 10", condition["Graded"], False),

        # Devin Booker:
            card("2015-16 Panini Prizm Devin Booker 308 PSA 10", condition["Graded"],False),
            card("2015-16 Panini Prizm Devin Booker Silver 308 PSA 10", condition["Graded"],False),

        # Joel Embid:
            card("2014-15 Panini Prizm Joel Embiid 253 PSA 10", condition["Graded"],False),
            card("2014-15 Panini Prizm Joel Embiid 253 PSA 9", condition["Graded"],False),
            card("2014-15 Panini Prizm Joel Embiid Silver 253 PSA 10", condition["Graded"],False),
            card("2014-15 Panini Prizm Joel Embiid Silver 253 PSA 9", condition["Graded"],False),

        # Kevin Durant:
            card("2007 Topps Kevin Durant 2 PSA 10", condition["Graded"], False),

        # Kobe Bryant:
            card("1996 Topps Kobe Bryant 138 PSA 10", condition["Graded"], False),
            card("1996 Topps Kobe Bryant 138 PSA 9", condition["Graded"], False),
        
        # FOOTBALL:
        # # CJ Stroud:
        #     card("2023 Panini Donruss C.J.-Stroud 339 PSA 10", condition["Graded"], False),
        #     card("2023 Panini Prizm 339 CJ-Stroud PSA 10", condition["Graded"],False),
        #     card("2023 Panini Prizm CJ-Stroud-339", condition["Ungraded"],False),
        # Brock Purdy:
            card("2022 Prizm Brock Purdy 353 PSA 10", condition["Graded"], False),
            card("2022 Chronicles PB8 Brock Purdy Prizm Black Silver PSA 10", condition["Graded"], False),

        # Josh Allen:
            card("2018 Panini Donruss Josh Allen Rated Rookie 304 PSA 10", condition["Graded"], False),
            card("2018 Panini Prizm Josh Allen 205 PSA 10", condition["Graded"], False),

        # Patrick Mahomes:
            card("2017 Donruss Optic Patrick Mahomes Rated Rookie PSA 10 177", condition["Graded"], False),
            card("2017 Donruss Optic Patrick Mahomes Rated Rookie PSA 9 177", condition["Graded"], False),
            card("2017 Panini Prizm Patrick Mahomes Silver 269 PSA 10", condition["Graded"], False),
            card("2017 Panini Prizm Patrick Mahomes Silver 269 PSA 9", condition["Graded"], False),

        # Tom Brady:
            card("2000 Bowman 236 Tom Brady PSA 9", condition["Graded"], False),
            card("2000 Bowman 236 Tom Brady PSA 8", condition["Graded"], False),
            card("2000 Bowman 236 Tom Brady PSA 7", condition["Graded"], False),

        # Aaron Rodgers: 
            card("2005 Topps Aaron Rodgers 431 PSA 10", condition["Graded"], False),
            card("2005 Topps Aaron Rodgers 431 PSA 9", condition["Graded"], False),

        # Lamar Jackson:
            card("2018 Panini Donruss Optic Lamar Jackson Rated Rookie 167 PSA 10", condition["Graded"], False),
            card("2018 Panini Prizm 212 Lamar Jackson PSA 10", condition["Graded"], False),

        # Joe Burrow:
            card("2020 Panini Prizm 307 Joe Burrow PSA 10", condition["Graded"], False),
            card("2020 Panini Donruss Optic Joe Burrow Rated Rookie 151 PSA 10", condition["Graded"], False),

        # Jordan Love:
            card("2020 Panini Donruss Jordan Love 304 Rated Rookie PSA 10", condition["Graded"], False),
            card("2020 Panini Prizm Jordan Love 363 PSA 10", condition["Graded"], False),

        # Anthony Richardson:
            card("2023 Panini Prizm Anthony Richardson 343 PSA 10", condition["Graded"], False),
            
        # Justin Herbert:
            card("2020 Panini Prizm Justin Herbert 325 Chargers PSA 10", condition["Graded"], False),
            card("2020 Panini Donruss Justin Herbert Rated Rookie 303 PSA 10", condition["Graded"], False),

        # Ben Roethlisburger:

        # Jalen Hurts:

        # HOCKEY: 
        # Connor Bedard:

        # Connor McDavid:

        # Nathan Mackinnon:

        # Nikita Kucherov:

        # Leon Draisaitl:

        # Auston Matthews: 

        # Cale Makar:

        # Jack Hughes:

        # Sidney Crosby:

        # Alexander Ovechkin:

        # Tim Stutzle:
            
            ]

    return cards

if __name__ =="__main__":
    condition = {"Graded":"2750", "Ungraded":"4000"}
    print(len(createCards(condition)))
    