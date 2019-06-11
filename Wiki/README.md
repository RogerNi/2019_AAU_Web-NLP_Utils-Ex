# Wiki Crawler
This package contains the codes for `Wikipedia` crawling. Two files are utilizations and two are testing programs

## Implementations
### `GoogleRedirect`
It is noticed that directly openning the corresponding page on `Wikipeida` may not give out the page we want (like searching `apple` on `Wikipedia`). However, searching the keyword on `Google` first and open the `Wikipedia` link in searching result will always lead to the wanted one. This program is for the redirecting.

Simple HTTP requests are used to access Google searching results.
#### Known Issues
Sometimes, Google will temperarily ban the IP due to massive access in a short time.

### `WikipediaContent`
This program accepts a list of keywords and return the corresponding `Wikipedia` pages. The keyword will first be sent to `GoogleRedirect` to ensure better result.

#### Known Issues
Even though the keyword is interpreted by `Google Search`, sometimes we still do not get what we want as some keywords have so many meanings.

## Dependencies
+ requests_html
+ wikipedia
+ json
+ pickle

## Authors
+ **NI Ronghao** - *Initial Work* - [RogerNi](https://github.com/RogerNi)

## Acknowledgments
+ The authors of the packages used here
+ Teachers and friends in Aalborg University who inspire and provide me the chance to write these codes