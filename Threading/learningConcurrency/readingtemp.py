

import urllib.request
def downloadImage(imagePath,fileName):
	print("Downloading Image from ", imagePath)
	urllib.request.urlretrieve(imagePath,fileName)

def main():
	for i in range(10):
		imageName="temp/image-" +str(i)+ ".jpg"
		downloadImage("https://www.shutterstock.com/search/houses",imageName)


if __name__ == '__main__':
  main()		