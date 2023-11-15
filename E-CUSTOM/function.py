def PLD(PreferredLoginDevice):
  if PreferredLoginDevice == 'Mobile Phone':
    result = 0
  elif PreferredLoginDevice == 'Phone':
    result = 1
  elif PreferredLoginDevice == 'Computer':
    result = 2
  return result

def PPM(PreferredPaymentMode):
  if PreferredPaymentMode == 'Debit Card' :
    result = 0
  elif PreferredPaymentMode == 'UPI' :
    result = 1
  elif PreferredPaymentMode == 'CC' :
    result = 2
  elif PreferredPaymentMode == 'Cash on Delivery' :
    result = 3
  elif PreferredPaymentMode == 'E wallet' :
    result = 4
  elif PreferredPaymentMode ==  'COD' :
    result = 5
  elif PreferredPaymentMode ==  'Credit Card' :
    result = 6
  return result

def Gen(Gender):
  if Gender == 'Female':
    result = 0
  elif Gender == 'Male':
    result = 1
  return result

def POC(PreferedOrderCat):
  if PreferedOrderCat == 'Laptop & Accessory':
    result = 0
  elif PreferedOrderCat =='Mobile':
    result = 1
  elif PreferedOrderCat =='Mobile Phone':
    result = 2
  elif PreferedOrderCat =='Fashion':
    result = 3
  elif PreferedOrderCat =='Others':
    result = 4
  elif PreferedOrderCat =='Grocery':
    result = 5
  return result

def MS(MaritalStatus):
  if MaritalStatus ==  'Single':
    result = 0
  elif MaritalStatus ==  'Divorced':
    result = 1
  elif MaritalStatus ==  'Married':
    result = 2
  return result