#threading in python


import threading, time
#print('start of program')

""""def takeANap():
  time.sleep(0)
  print('wakeup')

threadObj= threading.Thread(target=takeANap)
threadObj.start()

print('end of program')
threadObj= threading.Thread(target=print, args=['cat','dogs','frogs'],kwargs={'sep':'&'})
threadObj.start()
"""
#python multithreading
import sys,os,bs4
os.makedirs('xkcd',exist_ok=True)

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
     #downloading the pagep
     print("downloading page http://xkcd.com/%s..." %(urlNumber))
     res= requests.get('http://xkcd.com/%s' %(urlNumber))
     res.raise_for_status()
     soup =bs4.BeautifulSoup(res.text)

     #find the url of the cominc image
     comicElem= soup.select('#comic img')
     if comicElem==[]:
          print('Could not find cominc image')
     else:

        comicUrl= comicElem[0].get('src')
        #download the image
        print('downlaoding image %s...' %(comicUrl))
        res= requests.get(comicUrl)
        res.raise_for_status()
        #save the image to ./xkcd.

        imageFile= open(os.path.join('xkcd', os.path.basename(comicUrl),'wb'))
        for chunk in res.iter_content(100000):
             imageFile.write(chunk)

        imageFile.close()
     #create and start the Thread Object
     downloadThreads=[]
     for i in range(0,1400, 100):
      downloadThread= threading.Thread(target=downloadXkcd, args=(i, i+99))
      downloadThreads.append(downloadThread)
      downloadThread.start()

      #wait for all thrads to end.

      for downloadingThread in downoadingThreads:
          downloadThread.join()
      print('done')
