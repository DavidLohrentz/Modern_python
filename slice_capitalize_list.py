# Practice slicing and Capitalizing words in a list
from random import choice
PunkinHeadAdvisers = ['russian stooge', 'orange jump suit', 'wife-beater', 'traitor', 'asshole', 'dimwit', 'turd']
RandomPunkinHeadFool = choice(PunkinHeadAdvisers)
print(f"Trump's favorite adviser is a {RandomPunkinHeadFool}.")
# Slice the list
print(PunkinHeadAdvisers[::3])
# Use slicing to capitalize words in list
print([TrumpTurds[:1].upper() + TrumpTurds[1:] for TrumpTurds in PunkinHeadAdvisers])

numbs = range(1,6)
tenx = [x * 2 for x in numbs]
# for i in numbs:
#     print(i * 100000)
print(tenx)
