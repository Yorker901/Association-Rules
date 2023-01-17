@author: Anshu Pyasi
"""
# Import the data
import pandas as pd
df = pd.read_csv("my_movies.csv")  
df
df.shape

df.head()

# Appliying Apriori using the below parameters gives 6 rules as result
from apyori import apriori
rules = apriori(transactions = df, 
                min_support = 0.001, 
                min_confidence = 0.2, 
                min_lift = 2, min_length = 2, max_length = 2)

rules
results = list(rules)
len(results)

# Accessing the data in results

#RelationRecord(items = frozenset({'Harry Potter1', 'Green Mile'}), 
#support = 0.2, 
#ordered_statistics=[OrderedStatistic(items_base = frozenset({'Green Mile'}), 
                                  #items_add = frozenset({'Harry Potter1'}), 
                                  #confidence = 1.0, 
                                  #lift = 5.0)

results[0]
results[0][0]
results[0][1] # support
results[0][2] 
results[0][2][1]
results[0][2][0][1] # base item
results[0][2][0][0] # add item
results[0][2][0][2] # confidence
results[0][2][0][3] # lift

# Creating empty library to save the data
b = []
a = []
s = []
c = []
l = []
y=["Base Item", "Add Item", "Support", "Confidence", "lift"]

for i in range(0,102):
    b.append(results[i][2][0][1]) # base item
    a.append(results[i][2][0][0]) # add item
    s.append(results[i][1]) # support
    c.append(results[i][2][0][2]) # confidence
    l.append(results[i][2][0][3]) # lift

df_new = pd.concat([pd.DataFrame(b),
           pd.DataFrame(a),
           pd.DataFrame(s),
           pd.DataFrame(c),
           pd.DataFrame(l)],axis=1)

df_new.columns=y
df_new

# Appliying Apriori using the below parameters gives 1 rule as result, 
# here we changed support to 0.005 and lift = 3
from apyori import apriori
rules = apriori(transactions = df, 
                min_support = 0.002, 
                min_confidence = 0.5, 
                min_lift = 3, min_length = 2, max_length = 2)

rules
results = list(rules)
len(results)

results[0]
results[0][0]
results[0][1] # support
results[0][2] 
results[0][2][1]
results[0][2][0][1] # base item
results[0][2][0][0] # add item
results[0][2][0][2] # confidence
results[0][2][0][3] # lift

b = []
a = []
s = []
c = []
l = []
y = ["Base Item", "Add Item", "Support", "Confidence", "lift"]

for i in range(0,1):
    b.append(results[i][2][0][1]) # base item
    a.append(results[i][2][0][0]) # add item
    s.append(results[i][1]) # support
    c.append(results[i][2][0][2]) # confidence
    l.append(results[i][2][0][3]) # lift

df_new = pd.concat([pd.DataFrame(b),
           pd.DataFrame(a),
           pd.DataFrame(s),
           pd.DataFrame(c),
           pd.DataFrame(l)],axis=1)

df_new.columns=y
df_new

# Appliying Apriori using the below parameters gives 6 rules as result, 
# here we changed support to 0.008 and lift = 2 and confidence = 0.06
from apyori import apriori
rules = apriori(transactions = trans, 
                min_support = 0.08, 
                min_confidence = 0.06, 
                min_lift = 2, min_length = 2, max_length = 2)

rules
results = list(rules)
len(results)

results[0]
results[0][0]
results[0][1] # support
results[0][2] 
results[0][2][1]
results[0][2][0][1] # base item
results[0][2][0][0] # add item
results[0][2][0][2] # confidence
results[0][2][0][3] # lift

b = []
a = []
s = []
c = []
l = []
y = ["Base Item", "Add Item", "Support", "Confidence", "lift"]

for i in range(0,1):
    b.append(results[i][2][0][1]) # base item
    a.append(results[i][2][0][0]) # add item
    s.append(results[i][1]) # support
    c.append(results[i][2][0][2]) # confidence
    l.append(results[i][2][0][3]) # lift

df_new = pd.concat([pd.DataFrame(b),
           pd.DataFrame(a),
           pd.DataFrame(s),
           pd.DataFrame(c),
           pd.DataFrame(l)],axis=1)

df_new.columns = y
df_new

# Appliying Apriori using the below parameters gives 1 rule as result, 
# here we changed support to 0.3
from apyori import apriori
rules = apriori(transactions = df, 
                min_support = 0.3, 
                min_confidence = 0.06, 
                min_lift = 2, min_length = 2, max_length = 2)

rules
results = list(rules)
len(results)

results[0]
results[0][1] # support
results[0][2][0][1] # base item
results[0][2][0][0] # add item
results[0][2][0][2] # confidence
results[0][2][0][3] # lift

b = []
a = []
s = []
c = []
l = []
y=["Base Item", "Add Item", "Support", "Confidence", "lift"]

for i in range(0,1):
    b.append(results[i][2][0][1]) # base item
    a.append(results[i][2][0][0]) # add item
    s.append(results[i][1]) # support
    c.append(results[i][2][0][2]) # confidence
    l.append(results[i][2][0][3]) # lift

df_new = pd.concat([pd.DataFrame(b),
           pd.DataFrame(a),
           pd.DataFrame(s),
           pd.DataFrame(c),
           pd.DataFrame(l)],axis=1)

df_new.columns=y
df_new

#=============================================================================
#                           EDA
#=============================================================================

# Data Visvualization using Histogram, Scatterplot etc.

# Boxplot
df_new.boxplot(column="Support",vert=False)
df_new.boxplot(column="Confidence",vert=False) 
df_new.boxplot(column="lift",vert=False) 

# Histogram
df_new["Support"].hist() 
df_new["Confidence"].hist() 
df_new["lift"].hist() 
 
# Scatterplot for base Item and Support
df_new.plot.scatter("Base Item","Support") 

# Bar graph and Pie chart

t1=df_new["lift"].value_counts()

# Bar graph
t1.plot(kind="bar")

# Pie chart
t1.plot(kind='pie')

#====================================================================================
