import matplotlib.pyplot
import pylab
import csv
import pandas as pd

dataSet_1 = pd.read_csv('data_news_hillary.csv')
dataSet_2 = pd.read_csv('data_news_Trump.csv')
#source_name	desc_subjectivity	desc_polarity	titl_subjectivity	titl_polarity

y = dataSet_2.source
y2  = dataSet_1.source

#data_1 = dataSet_1.desc_polarity
data_2 = dataSet_2.desc_polarity
data_1 = dataSet_1.desc_polarity

#matplotlib.pyplot.scatter(x,y)


matplotlib.pyplot.scatter(y2, data_1 , color='red')
#matplotlib.pyplot.scatter(y, data_2, color='blue')

matplotlib.pyplot.show()

