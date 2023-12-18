#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request
IDX = 6

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
	"""Returns a list of the puzzle urls from the given log file,
	extracting the hostname from the filename itself.
	Screens out duplicate urls and returns the urls sorted into
	increasing order."""
	urls = []
	with open(filename, "r") as file:
		parseFile = filename.split("_")
		for line in file:
		  lineParse = line.split(" ")
		  jpgFile = "http://" + parseFile[1] + lineParse[IDX]
		  if ".jpg" in jpgFile:
		  	urls.append(jpgFile)

		urls = sorted(set(urls))

	return urls


  

def download_images(img_urls, dest_dir):
	"""Given the urls already in the correct order, downloads
	each image into the given directory.
	Gives the images local filenames img0, img1, and so on.
	Creates an index.html in the directory
	with an img tag to show each local image file.
	Creates the directory if necessary.
	"""
	i = 0
	htmlStart = """
<verbatim>
<html>
<body>
	"""
	htmlEnd = """
</body>
</html>
"""

	if not os.path.exists(dest_dir):
	  os.makedirs(dest_dir)

	htmlPath = os.path.join(dest_dir, "index.html")
	with open(htmlPath, 'w') as htmlFile:
		htmlFile.write(htmlStart)

		for img in img_urls:
			with urllib.request.urlopen(img) as response:
				image = response.read()
				imgFile = f"img{i}"
				imgPath = os.path.join(dest_dir, imgFile)
				i += 1

				with open(imgPath, 'wb') as output_file:
					output_file.write(image)
					htmlFile.write(f'<img src="{imgFile}">')

		htmlFile.write(htmlEnd)




def main():
	args = sys.argv[1:3]

	if not args:
		print('usage: [--todir dir] logfile ')
		sys.exit(1)

	img_urls = read_urls(args[0])

	try:
		download_images(img_urls, sys.argv[3])
	except Exception as e:
		print("Error! {}".format(e) +'\n'.join(img_urls))
	finally:
		print("\n \t\t<< No smile! Only compile ಠ_ಠ >>")


if __name__ == '__main__':
  main()
