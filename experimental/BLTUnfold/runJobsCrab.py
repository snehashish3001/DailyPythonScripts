from optparse import OptionParser
import os

jobs = [
        # 13 TeV
        # '--centreOfMassEnergy 13 -f',

        # '--centreOfMassEnergy 13 -s central',
        # '--centreOfMassEnergy 13 -s amcatnlo',
        # '--centreOfMassEnergy 13 -s madgraph',

        # # PS scale samples
        # '--centreOfMassEnergy 13 -s scaleup',
        # '--centreOfMassEnergy 13 -s scaledown',
        # ME scale weights
        '--centreOfMassEnergy 13 --generatorWeight 4',
        '--centreOfMassEnergy 13 --generatorWeight 8',

        # '--centreOfMassEnergy 13 -s massup',
        # '--centreOfMassEnergy 13 -s massdown',


        ]

# # #  Add pdf variations to list of jobs
# for variation in range(9,110):
#     jobs.append('--centreOfMassEnergy 13 --generatorWeight %i' % variation)
#     pass

# print len(jobs)
parser = OptionParser()
parser.add_option('-j','--job_number',type='int',dest='jobNumber',default=0)
(options, _) = parser.parse_args()
      
print 'Running job :',jobs[options.jobNumber-1]
os.system('python experimental/BLTUnfold/produceUnfoldingHistograms.py %s ' % jobs[options.jobNumber-1] )
