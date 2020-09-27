
import threading
from win10toast import ToastNotifier
from followskeleton2 import * 
for i in range(5):
	
	# if (i==0):
	# 	id='be.shayar'
	# 	passw='bhaktishakti'
	# 	people=['gulzar.ki.shayari']
	# 	print('starting HB')
	# 	z1=threading.Thread(target=login,args=(id,passw,people))
	# 	z1.start()	


	# if (i==1):
	# 	id='kriaa_18'
	# 	passw='bhaktishakti'
	# 	people=['surabhi.samriddhi']
	# 	print('starting mihira ')	
	# 	z2=threading.Thread(target=login,args=(id,passw,people))
	# 	z2.start()

	if (i==2):
		id='book_spot_'
		passw='booksnbooks'
		people=['booknerdnative']
		print('starting bookspot')
		z3=threading.Thread(target=login,args=(id,passw,people))
		z3.start()

	if (i==3):
		id='_art.af_'
		passw='bhaktishakti'
		people=['hantograph']
		print('starting Art af')
		z4=threading.Thread(target=login,args=(id,passw,people))
		z4.start()

	# if (i==4):	
	# 	id='samaira_._18' 
	# 	passw='bhaktishakti'
	# 	people=['memesnse']
	# 	print('starting sammy')
	# 	z5=threading.Thread(target=login,args=(id,passw,people))
	# 	z5.start()

	

	

# z1.join()
# z2.join()
z3.join()	
z4.join()
# z5.join()
print('done following')
toaster = ToastNotifier()
toaster.show_toast("Python Notification","Done following ",duration=360)



