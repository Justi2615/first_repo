standard_username = 'Kamil'
standard_passwd = '1234'

username = input ('Podaj nazwe:   ')
passwd = input ('Podaj hasło:   ')
while username != standard_username or passwd != standard_passwd:
    print ('Złe dane')
    username = input ('Podaj nazwe:   ')
    passwd = input ('Podaj hasło:   ')
print ('Zalogowano')

standard_username = 'Kamil'
standard_passwd = '1234'
service_passwd = 'service'
a = 0
username = input ('Podaj nazwe:   ')
passwd = input ('Podaj hasło:   ')
while True:
    if username == standard_username and passwd == standard_passwd:
        break
    elif passwd == service_passwd:
        break
    print ('Złe dane')
    username = input ('Podaj nazwe:   ')
    passwd = input ('Podaj hasło:   ')
print ('Zalogowano')
