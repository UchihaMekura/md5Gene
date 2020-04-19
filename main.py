import sys,os
import hashlib
import time 

def getFileMd5(file_path):
	
	file_size = os.path.getsize(file_path)

	loop_count = int(file_size/4096)+1

	m = hashlib.md5() 

	with open(file_path,'rb') as f:

		count = 0

		for i in range(loop_count):

			percent = int((i+1)/loop_count*100/2)
			if percent != count:
				sys.stdout.write('\r'+'Process: ['+'#'*percent+ ' '*(50-percent)+']  '+str(int((i+1)/loop_count*100))+' %')
				sys.stdout.flush()
				count += 1

			data = f.read(4096)

			if not data:
				break

			m.update(data) 

	return m.hexdigest()    


if __name__ == '__main__':

	file_path = sys.argv[1]
	
	file_name = file_path.split(os.sep)[-1]
	
	md5 = getFileMd5(file_path)
	
	with open(file_name+'.md5','w') as f: 
		f.write(md5)

	sys.stdout.write("\n\n")
	sys.stdout.flush()

	for i in range(5):
		sys.stdout.write("\rClose in %d seconds" %(5-i))
		sys.stdout.flush()
		time.sleep(1)


