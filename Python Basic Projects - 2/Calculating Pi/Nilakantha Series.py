the_pi = 0.0
the_num = 2.0

for i in range(500000):
    the_pi = the_pi + 4.0 /(the_num* (the_num+1.0)* (the_num+2.0)) - 4.0 /((the_num+2.0)* (the_num+3.0)* (the_num+4.0))
    the_num += 4.0 
    
print(the_pi + 3 ) 