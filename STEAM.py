# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

"""
Bar graph to compare between the search frequency of topics in STEM/STEAM
(Training courses and programs Vrs. Competitions)
Globally and in the gulf region

"""

# Globaly: Create lists from data
countries = ["India", "United States", "China", "Singapore", "Philippines", "Indonesia", "Malaysia", "Vietnam", "Thailand", "South Korea"]
monthly_searches_stem_steam_programs = [26100, 12100, 10100, 8100, 6100, 4100, 2100, 1100, 500, 300]
monthly_searches_stem_steam_competitions = [14100, 12100, 10100, 8100, 6100, 4100, 2100, 1100, 500, 300]

# Globaly: Create DataFrame from lists
df = pd.DataFrame(list(zip(countries, monthly_searches_stem_steam_programs, monthly_searches_stem_steam_competitions)), columns = ['Country', 'Training', 'Competitions'])

# Globaly: Create a bar chart to compare monthly searches for STEM/STEAM Training programs/courses and STEM/STEAM competitions
plt.figure(figsize=(10, 6))
df.plot(x='Country', kind='bar', stacked=False, title='Globally: Monthly Avrg. online search for STEM/STEAM (Training vs. Competitions)')
plt.xlabel('Country')
plt.ylabel('Monthly Searches')
plt.legend(title='Search in STEAM about')
plt.grid(axis='y')
plt.xticks(rotation=45)
plt.tight_layout()
# Save the figure image
plt.savefig('GlobFreqTrainingVrCompetition.jpg')

# Region: Create lists from data
countries = ["Kuwait", "KSA", "UAE", "Qatar", "Bahrain", "Oman"]
monthly_searches_stem_steam_programs = [6060, 25014, 27839, 7721, 3016, 4444]
monthly_searches_stem_steam_competitions = [4315, 15811, 20700, 5276, 2452, 3392]

# Region: Create DataFrame from lists
df = pd.DataFrame(list(zip(countries, monthly_searches_stem_steam_programs, monthly_searches_stem_steam_competitions)), columns = ['Country', 'Training', 'Competitions'])

# Region: Create a bar chart to compare monthly searches for STEM/STEAM Training programs/courses and STEM/STEAM competitions
plt.figure(figsize=(10, 6))
df.plot(x='Country', kind='bar', stacked=False, title='Gulf Region: Monthly Avrg. online search for STEM/STEAM (Training vs. Competitions)')
plt.xlabel('Country')
plt.ylabel('Monthly Searches')
plt.legend(title='Search in STEAM about')
plt.grid(axis='y')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the figure image
plt.savefig('GulfFreqTrainingVrCompetition.jpg')

# Display the figure
plt.show()


"""
Bar graph to compare between the growth rate in search of topics in STEM/STEAM
(Training courses and programs Vrs. Competitions)
Globally and in the gulf region
in the past 3 years 
2021-2022-2023

"""

# Globaly: Create lists from data
countries = ["India", "United States", "China", "Singapore", "Philippines", "Indonesia", "Malaysia", "Vietnam", "Thailand", "South Korea"]
growth_rates_programs = [22.3, 18.4, 15.2, 12.1, 9.3, 6.2, 3.4, 0.9, -1.2, -2.3]
growth_rates_competitions = [27, 22, 25, 22, 20, 18, 16, 14, 12, 10]

# Globaly: Create DataFrame from lists
df = pd.DataFrame(list(zip(countries, growth_rates_programs, growth_rates_competitions)), columns = ['Country', 'Training', 'Competitions'])

# Globaly: Create a bar chart to compare growth in searches for STEM/STEAM Training programs/courses and STEM/STEAM competitions
plt.figure(figsize=(10, 6))
df.plot(x='Country', kind='bar', stacked=False, title='Globally: Search growth rate in STEM/STEAM (Training vs. Competitions) in the past 3 years')
plt.xlabel('Country')
plt.ylabel('Growth Rate')
plt.legend(title='Search in STEAM about')
plt.grid(axis='y')
plt.xticks(rotation=45)
plt.tight_layout()
# Save the figure image
plt.savefig('GlobGrowthTrainingVrCompetition.jpg')

# Region: Create lists from data
countries = ["Kuwait", "KSA", "UAE", "Qatar", "Bahrain", "Oman"]
growth_rates_stem_steam_programs = [16.03, 17.13, 15.47, 13.14, 14.38, 11.23]
growth_rates_stem_steam_competitions = [24.04, 26.29, 25.12, 22.27, 23.34, 20.12]

# Region: Create DataFrame from lists
df = pd.DataFrame(list(zip(countries, growth_rates_stem_steam_programs, growth_rates_stem_steam_competitions)), columns = ['Country', 'Training', 'Competitions'])

# Region: Create a bar chart to Growth in the searches for STEM/STEAM Training programs/courses and STEM/STEAM competitions
plt.figure(figsize=(10, 6))
df.plot(x='Country', kind='bar', stacked=False, title='Gulf Region: Search growth in STEM/STEAM (Training vs. Competitions) in the past 3 years')
plt.xlabel('Country')
plt.ylabel('Monthly Searches')
plt.legend(title='Search in STEAM about')
plt.grid(axis='y')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the figure image
plt.savefig('GulfGrowthTrainingVrCompetition.jpg')

# Display the figure
plt.show()

