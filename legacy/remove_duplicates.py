#!/usr/bin/python
'''
Created on 1 Jun 2010

@author: kreczko

Email: kreczko@cern.ch
'''

from optparse import OptionParser
import os
import copy

duplicates = []
duplicateFiles = {}

def getUniqueFiles(files):
    if listContainsDuplicates(files):
        findDuplicates(files)
    else:
        return files
    uniqueFiles = copy.copy(files)
    for values in duplicateFiles.itervalues():
        for value in values:
            if value in uniqueFiles:
                uniqueFiles.remove(value)
        values.sort()
        uniqueFiles.append(values[-1])
    return uniqueFiles

def listContainsDuplicates(list):
    seen = []
    for item in list:
        jobnumber = extractJobnumber(item)
        if jobnumber in seen:
            duplicates.append(jobnumber)
        else:
            seen.append(jobnumber)
    return len(duplicates) >0

def findDuplicates(files):
    for file in files:
        for job in duplicates:
            if job == extractJobnumber(file):
                addDuplicate(job, file)
        
def extractJobnumber(file):
    jobnumber = file.split('_')[-3]
    return int(jobnumber)

def addDuplicate(jobnumber, file):
    if not duplicateFiles.has_key(jobnumber):
        duplicateFiles[jobnumber] = []
    duplicateFiles[jobnumber].append(file)

def removeDuplicates(path, files):
    print 'Number of file in path:', len(files)
    files.sort()
    uniqueFiles = getUniqueFiles(files)
    uniqueFiles.sort()
    print 'Number of unique files', len(uniqueFiles)
    filesToRemove = [file for file in files if not file in uniqueFiles]
    print 'Number of duplicate files:', len(filesToRemove)
    [remove(path + file) for file in filesToRemove]

def remove(file):
    print 'removing',file
    os.remove(file)

if __name__ == "__main__":
    parser = OptionParser()
    (options, args) = parser.parse_args()
    if len(args) >0:
        path = args[0]
        files = os.listdir(path)
        removeDuplicates(path, files)
    else:
        print 'File path was not specified. Use script "./remove_duplicates path"'