# %%
import pandas as pd

# %%
hero_powers = pd.read_csv("superhero_powers.csv")
hero_powers

# %%
s = pd.Series([1,2,3,4,5,6,7])
s

# %%
index_day = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
data = [1,2,3,4,5,6,7]

# %%
s = pd.Series(data,index = index_day)
s

# %%
s.mean()

# %%
4*s

# %%
df = pd.DataFrame({"first":s,"second":s*2,"third":s*5})
df

# %%
column_names = ['city','population']
index_country = ['japan','india','china','brazil','mexico']

# %%
row1 = ['tokyo',37.4]
row2 = ['delhi',28.5]
row3 = ['shangai',27.5]
row4 = ['sau palio',21.5]
row5 = ['mexico city',21.6]
data = [row1,row2,row3,row4,row5]

# %%
df = pd.DataFrame(data,index = index_country,columns = column_names)
df

# %%
cities = ['tokyo','mumbai','shangai','rio','mexico city']
population = [28.5,25.6,45.5,23.5,54.2]
popu_dict = {'city':cities,"population":population}

# %%
df = pd.DataFrame(popu_dict,index = index_country)
df

# %%
hero_dc = pd.read_excel('superhero_info.xlsx',sheet_name = 'DC Comics')
hero_marvel = pd.read_excel('superhero_info.xlsx',sheet_name = 'Marvel Comics')

# %%
hero_marvel.head()

# %%
df = pd.read_csv('weather.csv')
df

# %%
df.info()

# %%
df['temperature_high'] = df['temperature_high'].astype('int8')

# %%
df.info()

# %%
df['rained'] = df['rained'].astype('bool')
df['rained']

# %%
df.info()

# %%
df['overcast']

# %%
df['temperature_low'] = pd.to_numeric(df['temperature_low'],errors = 'coerce')

# %%
df['temperature_low']

# %%
df['date'] = pd.to_datetime(df['date'])

# %%
df['date']

# %%
df.info()

# %%
hero_powers.info()

# %%
hero_powers.head()

# %%
hero_powers['hero_names'] = hero_powers['hero_names'].astype('string')

# %%
hero_dc.dtypes

# %%
hero_dc.head()

# %%
hero_dtype = {'name':'string','Gender':'category','Eye colour':'string','Race':'string','Hair color':'string','Publisher':'string','Alignment':'category'}


# %%
hero_dc = pd.read_excel('superhero_info.xlsx',sheet_name = 'DC Comics',dtype = hero_dtype)
hero_marvel = pd.read_excel('superhero_info.xlsx',sheet_name = 'Marvel Comics',dtype = hero_dtype)


# %%



