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
				sys.stdout.write('\r'+'    Process: ['+'#'*percent+ ' '*(50-percent)+']  '+str(int((i+1)/loop_count*100))+' %')
				sys.stdout.flush()
				count += 1

			data = f.read(4096)

			if not data:
				break

			m.update(data) 

	return m.hexdigest()    


def getAndSave_single(file_path):

	if file_path.split('.')[-1] != 'md5':

		sys.stdout.write(file_path+'\n')
		sys.stdout.flush()

		md5 = getFileMd5(file_path)
		
		with open(file_path+'.md5','w') as f: 
			f.write(md5)

		sys.stdout.write('\n\n')
		sys.stdout.flush()

if __name__ == '__main__':

	input_package = sys.argv[1:]

	for each in input_package:
		if os.path.isdir(each):
			#fileInside_list = []
			for root, dirs, files in os.walk(each):
				for name in files:
					#fileInside_list.append()
					getAndSave_single(os.path.join(root, name))
		else:
			getAndSave_single(each)

	for i in range(10):
		sys.stdout.write("\rClose in %d seconds" %(10-i))
		sys.stdout.flush()
		time.sleep(1)

