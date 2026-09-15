#IN THE NAME OF GOD
# MADE IN AMIRABAS KHAJEH FOR MR HAJAVI
# CLASS3.1

##Smart Shopping Cart

class Shopping:

    def __init__(self, point, items, code):
        self.point = point
        self.items = items
        self.code = code

    def __str__(self):
        return f'({self.point},\n {self.items},\n {self.code})'

    def point_and_items(self):
        al = self.point * self.items
        return al

    def al_and_code(self, al):
        match self.code:
            case 'SAVE20':   return f"'gold'    \t~${al * 0.9}"
            case 'SAVE10':   return f"'silver'  \t~${al * 1}"
            case 'SAVE50':   return f"'platinum'\t~${al * 0.5}"
            case 'FREESHIP': return f"'bronze'  \t~${al} " 
            case 'INVALID':  return f"'gold'    \t~${al}"
            case _:
                return 'not found!!!'


#informatoin.
poi = input('Enter the point: ')
po = int(poi)
item = input('Enter the items: ')
it = int(item)
cod = input('Enter the code: ')
co = cod.upper()

if po < 0 or it < 0:
    print('please Enter the + point and item!!!')

else:
    #Tell Sopping...
    shop = Shopping(po, it, co) 
    main = shop.point_and_items()
    al_co = shop.al_and_code(main)
    print('Items \t Discount Code \t User Tier \t Expected')
    print('=' * 60)
    print(f'{it}x${po}items\t{co}\t{al_co} total ') 


print('The end.')
#AMIRABAS KHAJEH    
