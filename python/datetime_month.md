

```
#bin Release Dates by month
movies['RD_month']=pd.DatetimeIndex(movies['ReleaseDate']).month
```

```
# extract month from datetime64
mv_df['month'] =  pd.DatetimeIndex(mv_df['reldate']).month
print mv_df[:2] 
```
