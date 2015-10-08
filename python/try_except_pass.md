```
def sanitize_year(year):
    try:   # try except error
        cleaned_year = int(year)
    except ValueError:
    	pass   # this is equivalent to:  return none OR return "Joe" OR return "9999
    else:
    # cool, it's an integer, but is it > 1950 ?
        if cleaned_year > 1950:
            return cleaned_year


sanitize_year("1081")

for row in rows:
    row["Sanitized Year"] = sanitize_year(row["Release Year"])
    
less1984 = [row for row in rows if row["Sanitized Year"] < 1984]
print less1984[0:5]
print len(less1984)

```