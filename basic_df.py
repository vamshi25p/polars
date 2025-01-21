import polars as pl 
import datetime as dt 

df=pl.DataFrame(
    {
    "name":["Vamshi","Ajay","Mahesh","Yatish"],
    "birthdate":[
        dt.date(2003,10,14),
        dt.date(2003,1,1),
        dt.date(2003,1,1),
        dt.date(2003,1,1),
    ],
    "weight":[50,60,70,80],
    "height":[6.1,6.0,5.9,5.8]
    }
)

print(df)