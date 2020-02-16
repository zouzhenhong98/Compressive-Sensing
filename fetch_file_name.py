# -*- coding: utf-8 -*-   
      
import os  

def file_name(file_dir):
	for root, dirs, files in os.walk(file_dir):
		print('-'*100)
		print(root)
		print(dirs)
		for name in files:
			print('- '+name)

if __name__ == '__main__':
	path = ['./complex-compressive-sensing','./paper','./codes','./my-codes']
	for p in path:	
		file_name(p)
