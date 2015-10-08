```
# Functions are largely used in Pandas to apply data transformations to each row:
def saw_ad_many_times(x):
    return 1 if x >= 6 else 0

nyt['Impressions_categorical']= nyt['Impressions'].apply(saw_ad_many_times).head()

```