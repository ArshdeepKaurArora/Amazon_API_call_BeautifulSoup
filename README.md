# Amazon_API_call_BeautifulSoup

This is an automation project to collect the data(price of product) from the Amazon website using BeautifulSoup.

## What does the project do?

`BeautifulSoup` and `requests` package helps to collect data on Amazon products from the Amazon website(I have looked for an electric pressure cooker).

If the price of an Amazon product is lower than my limit of expenditure on the same, then using `smptlib` package an email is dropped on my email account with the price information and link to the Amazon page with the product.

## How this project is useful?

The following facts make it useful -

+ Due to its simple sorted program, it is easy to understand for beginner programmers.
+ `BeautifulSoup` package in [amazon.py file](https://github.com/ArshdeepKaurArora/Amazon_API_call_BeautifulSoup/blob/main/amazon.py) for data scraping decrease time complexity.
+ `smptlib` package in [drop_email.py file](https://github.com/ArshdeepKaurArora/Amazon_API_call_BeautifulSoup/blob/main/drop_mail.py) makes a free-of-cost process to drop an email with the information regarding the product.

## How anyone can use the code of this project?

Perform the following steps after downloading and opening this project in your editor.

+ Use the command `pip install -r requirements.txt` on the terminal to install all the required packages.
+ Use the latest version of Python (I have used Python 3.11.1).
+ Google your `User-Agent` and `Accept-language` to assign the corresponding variables a correct value in the amazon.py file.
+ Change the URL of Amazon products unless you are also interested in buying an electric pressure cooker 😅.
+ Get your app password from your Gmail account and use it as a password to drop an email.
+ Finally, run main.py

There you go. You have got your own automated Amazon data scraping program.


