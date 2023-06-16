# Amazon_API_call_BeautifulSoup

This is an automation project in which I have a call to Amazon webpage and collected the data(price of product) using BeautifulSoup.

## What the project does?

Using the package `BeautifulSoup` and `requests` it collects data from amazon product from amazon website(I have looked for electric pressure cooker).

If the price of amazon product is lower than my limit of expenditure on the same, then using `smptlib` package an email is dropped on my email account with the price information and link of the amazon page with the product.

## How this project is useful?

Following facts makes it useful -

+ Due to its simple sorted program, it is easy to understand for beginner programmer.
+ `BeautifulSoup` package in [amazon.py file](https://github.com/ArshdeepKaurArora/Amazon_API_call_BeautifulSoup/blob/main/amazon.py) for data scraping decrease time complexity.
+ `smptlib` package in [drop_email.py file](https://github.com/ArshdeepKaurArora/Amazon_API_call_BeautifulSoup/blob/main/drop_mail.py) makes a free of cost process to drop an email with the information regarding the product.

## How anyone can use the code of this project?

Perform the following steps after your download and open this project files in your editor.

+ Use the command `pip instal -r requirements.txt` on the terminal to install all the required packages.
+ Use the latest version of python (I have used python 3.11.1).
+ Change the url of amazon product unless you are also interested in buying electric pressure cooker 😅.
+ Get your app password from your gmail account and use it as a password to drop and email.
+ Finally, run main.py

There you go. You have got your own automated Amazon data scraping program.


