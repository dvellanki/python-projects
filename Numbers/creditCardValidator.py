cc = str(raw_input("Enter a credit card number to validate (Mastercard, Visa, Discover, Amex only): "))

def val_cc(number):
  cc_rev = number[::-1]
  total = 0
  for i in cc_rev[1::2]:
  	x = int(i)*2
  	if len(str(x)) == 2:
  		for a in str(x):
  			total += int(a)
  	else:
  		total += int(x)
  	
  for i in cc_rev[::2]:
  	total += int(i)

  return total

if (int(cc[:2]) >= 51 and int(cc[:2]) <= 55 and len(cc) == 16) or \
	(int(cc[0]) == 4 and (len(cc) == 13 or len(cc) == 16)) or \
	((int(cc[:2]) == 34 or int(cc[:2]) == 37) and len(cc) == 15) or \
	(int(cc[:4]) == 6011 and len(cc) == 16):
  if val_cc(cc) % 10 == 0:
	  print "%s is a valid credit card number" % cc
  else:
	  print "%s is NOT a valid credit card number" % cc
else:
	print "%s is NOT a valid credit card number" % cc
