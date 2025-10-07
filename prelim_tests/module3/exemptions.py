#x = int(input(('Enter data: ')))
#print (5/x)

## ValueError, ZeroDivisionError error and more ... Index Error Key Error from base class exemptions
## Exemption class зловить всі помилки.
## можна робити свої

try: 
## execute and run code -  де може бути помилка
    x = input('Input integer: ')
    x = int(x)
    x = 100/x
except ValueError: # or (except: - ловить все)
    # execute this code when exemption occured. 
    print('INTEGER!!')
except ZeroDivisionError :
    print('Zerro devision! ') #except with different outcome

else:
# код що виконається коли неамє ЖОДНОЇ помилки - транзакція $

finally:
# Always run this code 