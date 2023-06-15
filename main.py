from amazon import AmazonPrice
from drop_mail import dropping_email

# from email to email
from_email = "YOUR EMAIL"
password = 'YOUR APP PASSWORD'
to_email = 'OTHER EMAIL'

# objects from the related class
price = AmazonPrice()

# Current price
price_value = float(price.show_data().replace("$",""))

# dropping an email of low price.
dropping_email(from_email,password,to_email,price_value,price.url)
