import pandas as p
import matplotlib.pyplot as m
import seaborn as s
df=p.read_csv('C:\\Users\\win10\\Downloads\\mtcars (1).csv')

mpg=df['mpg']
m.hist(mpg,color='b',bins='auto')
m.xlabel('miles')
m.ylabel('frequency')
m.show()

wt=df['wt']
iv=range(len(df))
m.scatter(iv,mpg,color='k',label='mpg')
m.scatter(iv,wt,color='g',label='wt')
m.title("Weigth and MPG")
m.legend()
m.show()

c=df['am'].value_counts()
co=['k','g']
m.bar(c.index,c.values,color=co,width=0.3)
m.xticks([0,1],['0-automatic','1-manual'])
m.ylabel("number of count")
m.title("frequency distribution")
m.show()
h