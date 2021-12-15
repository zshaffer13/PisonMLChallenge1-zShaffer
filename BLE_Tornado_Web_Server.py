# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:07:38 2021

@author: zshaf
"""

import tornado.httpserver, tornado.ioloop, tornado.options, tornado.web,tornado.autoreload
from tornado.options import define, options
import time
import asyncio
from bleak import  discover
import os 
from flask import Flask, render_template



devices_dict = {}
devices_list = []
receive_data = []
details_list = []


define("port", default=8888, help="run on the given port", type=int)
start_time = time.time()
reScanTime = int(input("Please input amount of time between BLE Scans:\n"))

__UPLOADS__ = "uploads/"
#app2 = Flask(__name__)

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r"/", HomeHandler)
		]
		tornado.web.Application.__init__(self, handlers)
		
class HomeHandler(tornado.web.RequestHandler):
    async def get(self):
        self.set_status(200)
        self.set_header("Content-type", "text/html")
        self.write(bytes("<body>", "utf-8"))
        self.write(bytes("<p>Server Uptime: %.2f seconds</p>" %(time.time()-start_time), "utf-8" ))
        self.write(bytes("<p>BLE UUIDs:</p>", "utf-8"))
        await self.scan(reScanTime)
        
        self.render('form.html')
        
        
            
    
    async def scan(self,reScanTime):
        numScans = 0
        time.sleep(reScanTime)
        dev = await discover()
        for i in range(0,len(dev)):
            #print("[" + str(i) + "]" + dev[i].address,dev[i].name,dev[i].metadata["uuids"])
            #Put devices information into list
            devices_dict[dev[i].address] = []
            devices_dict[dev[i].address].append(dev[i].name)
            devices_dict[dev[i].address].append(dev[i].metadata["uuids"])
            devices_list.append(dev[i].address)
            details_list.append(dev[i].metadata["uuids"])


        #print(devices_list)
        details_list_remv = [i for i in details_list if i ]
        #print(details_list_remv)
        
        textfile = open("metadata_file.txt",'w')
        for element in details_list_remv:
            textfile.write(str(element) +'\n')
            #self.write(bytes("\n", "utf-8"))
            self.write("<p>")
            self.write(bytes((str(element) + "\n"), "utf-8"))
        self.write("</p>")
            
        self.write(bytes('Number of Refreshes:' + str(numScans),"utf-8"))
        numScans += 1
        textfile.write('\n')
        textfile.close
        #return render_template('metadata_ht.html', details_list_remv=details_list_remv)
        
    
    async def track_refresh(self):
        idx = 0
        self.write(bytes(str(idx), "utf-8"))
        idx +=1
    
    
def main():

    
    
    app = tornado.web.Application( handlers=[
        (r'/', HomeHandler)], 
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        template_path=os.path.join(os.path.dirname(__file__), "templates"))
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)

    tornado.ioloop.IOLoop.instance().start()
	
if __name__ == "__main__":
	main()