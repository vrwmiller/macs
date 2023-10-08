# macs

sqlite3 database and Python management script for tracking MAC addresses. sqlcipher is used for encryption.

## sqlite table

```sql
sqlite> PRAGMA key = 'key';
sqlite> .import /tmp/f.csv macs --csv
sqlite> pragma table_info(macs);
0|user|TEXT|0||0
1|device|TEXT|0||0
2|mac|TEXT|0||0
3|description|TEXT|0||0
4|five|TEXT|0||0
5|six|TEXT|0||0
sqlite> .quit
```

## grepmacs.py

search the sqlite3 database
