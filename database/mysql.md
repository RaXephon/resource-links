

**mysql> show databases;**
```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| tennis             |
+--------------------+
4 rows in set (0.01 sec)
```

**mysql> show tables in tennis;**
```
+------------------+
| Tables_in_tennis |
+------------------+
| aus_ladies_2013  |
+------------------+
1 row in set (0.00 sec)
```

**mysql> use tennis;**
```
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
```
**mysql> describe tennis;**

```How do you view the first 10 lines of u_users?```
**mysql> SELECT * from u_users limit 10;**
