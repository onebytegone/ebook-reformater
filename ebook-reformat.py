#!/usr/bin/python

import sys
from os import listdir
from os.path import isfile, splitext, basename
from subprocess import call

# Config
CLI_PATH = '/Applications/calibre.app/Contents/MacOS/'
CONVERTER = 'ebook-convert'

args = sys.argv
if len(args) < 4:
   print "Error: This needs to be input and output folders and target format to process."
   print "Usage: ebook-reformat {input folder} {output folder} {target format}"
   exit()





def process_ebook(source, output):
   print "converting: "+source
   call([CLI_PATH+CONVERTER, source, output])


def generateOutputFilepath(source, output, targetFormat):
   filename = splitext(basename(source))[0]
   return output.rstrip('/')+'/'+filename+'.'+targetFormat

def generateIOFilePairs(source, output, targetFormat):
   fileList = []
   basedir = source.rstrip('/')+'/';
   for f in listdir(basedir):
      fullPath = basedir+f;
      if isfile(fullPath):
         fileList.append({
              'source': fullPath,
              'output': generateOutputFilepath(fullPath, output, targetFormat)
            });
   return fileList


files = generateIOFilePairs(args[1], args[2], args[3])

for info in files:
   process_ebook(info['source'], info['output'])
