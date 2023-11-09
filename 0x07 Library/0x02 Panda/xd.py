import pandas as xd

population_dict = {'Rabat-Salé-Zemmour-Zaër': 3123595,
'Grand Casablanca' :3631061,
'Tanger-Tétouan': 2470372,
'Marrakech-Tensift-Al Haouz': 3102652,
'Meknès-Tafilalet': 2119000,
'Laâyoune-Boujdour-Sakia el Hamra': 256152}
population = xd.Series(population_dict)