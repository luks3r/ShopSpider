Ordi SQLite WebSpider
---

### Running
```
scrapy crawl ordispider
```

or (if you need a json file)
```
scrapy crawl ordispider -O ORDI.json
```

### Settings
`sql_spider/settings.py`

DATABASE_URL - database connection string, example: 'sqlite:///test.db'
