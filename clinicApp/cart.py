# from django.conf import settings
# from .models import Pharmacy
# from decimal import Decimal
# class Cart:
#     def __init__(self, request):
#         self.session =  request.session
#         cart = self.session.get(settings.CART_SESSION_KEY)
#         if not cart:
#             cart = self.session[settings.CART_SESSION_KEY] = {}

#         self.cart  =  cart
        
    
    
    

#     def add(self, pharmacy):
#         pharmacy_id = pharmacy.id
#         if not pharmacy_id in self.cart:
#             self.cart[pharmacy_id]  = {'price': str(pharmacy.price)}

#         else:
#             self.cart[pharmacy_id] [price] += price
  
#         self.save()

#     def save(self):
#         self.session.modified = True

#     def list(self):
#         carts =[]
              
#         for pharmacy_id in self.cart.keys():
            
#             objs = Pharmacy.objects.get(id=pharmacy_id)
            
#             temp_cart = {
#                 'id':pharmacy_id,
#                 'objs':objs,
#                 'price': objs.price,

#             }
#             carts.append(temp_cart)
        
        
#         return carts
   
    
    