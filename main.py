# Tackle Box Calculator

# Item drop rate equation

x = 2000 # Let x be the number of tackle boxes

fishingfly_equation = (121/600) * x
megapellet_equation = (31/600) * x
salmon_equation = (151/600) * x
shiny_equation = (211/600) * x
shrimp_equation = (47/600) * x
uranium_equation = (19/600) * x
wiggly_equation = (93/200) * x

total_drops = fishingfly_equation + megapellet_equation + salmon_equation + shiny_equation + shrimp_equation + uranium_equation +  wiggly_equation

print(str(x) + " tackle boxes drop " + str(fishingfly_equation) + " Fishing Fly, " + str(megapellet_equation) + " Mega-Pellet Bait, " + str(salmon_equation) + " Salmon Eggs, " + str(shiny_equation) + " Shiny Flashy Thing, " + str(shrimp_equation) + " Shrimp Lure, " + str(uranium_equation) + " Uranium Glowing Lure and " + str(wiggly_equation) + " Wiggly Worm, " + str(total_drops) + " drops in total per harvest.")

# Item price rate

fishingfly_rate = fishingfly_equation / 100
megapellet_rate = megapellet_equation / 30
salmon_rate = salmon_equation / 200
shiny_rate = shiny_equation / 200
shrimp_rate = shrimp_equation / 8
uranium_rate = uranium_equation / 30
wiggly_rate = wiggly_equation / 500

total_earned = fishingfly_rate + megapellet_rate + salmon_rate + shiny_rate + shrimp_rate + uranium_rate + wiggly_rate

print("I will earn " + str(total_earned) + " WLS in total for every harvest (2 days)")

# Tackle box price rate

tackle_rate = 3.33 * x
earn_wls = tackle_rate / (total_earned / 2)

print("It will take me " + str(earn_wls) + " days to earn back the amount of wls I spent on " + str(x) + " tackle boxes in which I paid " + str(tackle_rate) + "WLS")