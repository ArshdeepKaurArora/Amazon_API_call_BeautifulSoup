import smtplib

def dropping_email(from_email,password,to_email,price_value,link):
    if price_value < 100:
        with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
            connection.starttls()
            connection.login(user=from_email,password=password)
            connection.sendmail(
                from_addr= from_email,
                to_addrs= to_email,
                msg="Subject: Price Drop!\n\n"
                    "Hey, the price of 'Slow Cooker' is dropped below your target price ($100).\n"
                    f"Now you can buy it at {price_value}.\n"
                    f"To buy - Click on the link below \n"
                    f"{link}"
            )