# Brands Crawl
This package contains three files: `998brands_crawl.py`, `998Brands_Wiki.py` and `Festival_Walk.py`. They are all crawlers.

## Implementations
All of these two crawlers (except the Wiki crawler which include another package) adopt `selenium` and use `Chrome` as emulator for crawling. Compared with traditional method which only analyze on HTML file, emulating methods make it easier because you will get exactly the same web page as you do a real exploring on the internet. More important, some web pages (like Festival Walk web site) cannot (or are very hard to) be crawled without executing JavaScript. In this case, emulating is the only solution.

## Deployments
Except for the required depended packages, a `Chrome Driver` is also required to run the program. See [chromedriver](http://chromedriver.chromium.org/) to download correspond driver. Then change the driver path in the code.

## Dependencies
### Python Packages
+ requests_html
+ urllib
+ requests
+ selenium
+ re
+ time
### My Own Packages
+ `WikipediaContent`

## Authors
+ **NI Ronghao** - *Initial Work* - [RogerNi](https://github.com/RogerNi)

## Acknowledgments
+ The authors of the packages used here
+ Teachers and friends in Aalborg University who inspire and provide me the chance to write these codes