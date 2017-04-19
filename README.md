# njuskalo-nekretnine
Collecting  realestate listings from [njuškalo](http://www.njuskalo.hr/), most popular Croatian listing website

## Built With
* [Scrapy](https://scrapy.org/) - Python scraping framework
* [peewee](http://docs.peewee-orm.com/en/latest/) - simple and small ORM

## Database schema
Easily modified using the OglasModel.py and then execute the setup_database.py script (or use the console) to create the database schema
![Database schema](baza.png)

## Running the scraper
There are two spiders, depending on the type you want to scrape. Both types get stored into the same database with different oglas.tip fields. Run with:
```
scrapy crawl rent_stan
scrapy crawl prodaja_stan
```
You can cron these commands but it would be better to make a [script](https://doc.scrapy.org/en/latest/topics/practices.html)

## In progress
This project is still in progress, the current todos are:
* adding spiders for houses (rent/sale)
* duplicate checker for database (the link is unique for each listing so it can be used for this purpose)
* scrape&persist authors (users) of the listings
* parse more information from the listings


## Warning!
Whatever you scrape, scrape responsibly by obeying robots.txt and throttle your requests! If you publish the information, make links back to the source!
