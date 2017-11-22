import math

sales = ((-3./11.)*math.log2(3/11.)-(8./11)*math.log2(8/11.)) * (110/165.)
systems = ((-8./31)*math.log2(8./31)-(23./31.)*math.log2(23/31.))*(31./165.)
marketing = ((-5/7.) * math.log2(5./7) - (2./7)*math.log2(2./7)) * (14./165.)
secretary = ((-2./5)*math.log2(2./5) - (3./5)*math.log2(3./5))*(10./165)

x = sales + systems + marketing + secretary
print(x) # 0.8504239852462385