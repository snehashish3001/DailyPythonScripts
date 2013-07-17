'''
Created on 9 Dec 2012

@author: kreczko
'''
from optparse import OptionParser
import os
from rootpy.io import File
from array import array
from tools.Unfolding import Unfolding
from config import RooUnfold
from tools.hist_utilities import hist_to_value_error_tuplelist
from tools.file_utilities import write_data_to_JSON
from time import clock, time
    
def check_multiple_data_multiple_unfolding(input_file, method, channel):
    global nbins, use_N_toy, output_folder, offset_toy_mc, offset_toy_data
    # same unfolding input, different data
    get_folder = input_file.Get
    pulls = []
    add_pull = pulls.append
    histograms = []
    add_histograms = histograms.append
    
    print 'Reading toy MC'
    start1 = time()
    mc_range = range(offset_toy_mc + 1, offset_toy_mc + use_N_toy + 1)
    data_range = range(offset_toy_data + 1, offset_toy_data + use_N_toy + 1)
    for nth_toy_mc in range(1, 10000 + 1):  # read all of them (easier)
        if nth_toy_mc in mc_range or nth_toy_mc in data_range:
            folder_mc = get_folder(channel + '/toy_%d' % nth_toy_mc)
            add_histograms(get_histograms(folder_mc))
        else:
            add_histograms((0, 0, 0))
    print 'Done reading toy MC in', time() - start1, 's'       
    
    for nth_toy_mc in range(offset_toy_mc + 1, offset_toy_mc + use_N_toy + 1):
        print 'Doing MC no', nth_toy_mc
        h_truth, h_measured, h_response = histograms[nth_toy_mc - 1]
        unfolding_obj = Unfolding(h_truth, h_measured, h_response, method=method)
        unfold, get_pull, reset = unfolding_obj.unfold, unfolding_obj.pull, unfolding_obj.Reset
        
        for nth_toy_data in range(offset_toy_data + 1, offset_toy_data + use_N_toy + 1):
            if nth_toy_data == nth_toy_mc:
                continue
            print 'Doing MC no, ' + str(nth_toy_mc) + ', data no', nth_toy_data
            h_data = histograms[nth_toy_data - 1][1]
            unfold(h_data)
            pull = get_pull()
            diff = unfolding_obj.unfolded_data - unfolding_obj.truth
            diff_tuple = hist_to_value_error_tuplelist(diff)
            unfolded = unfolding_obj.unfolded_data
            unfolded_tuple = hist_to_value_error_tuplelist(unfolded)
            all_data = {'unfolded': unfolded_tuple,
                        'difference' : diff_tuple,
                        'pull': pull,
                        'nth_toy_mc': nth_toy_mc,
                        'nth_toy_data':nth_toy_data
                        }
            
            add_pull(all_data)
            reset()
    save_pulls(pulls, test='multiple_data_multiple_unfolding', method=method, channel=channel)


def save_pulls(pulls, test, method, channel):    
    global use_N_toy, offset_toy_mc, offset_toy_data
    file_template = 'Pulls_%s_%s_%s_toy_MC_%d_to_%d_MC_%d_to_%d_data.txt'
    output_file = output_folder + file_template % (test, method, channel, offset_toy_mc + 1, use_N_toy + offset_toy_mc, offset_toy_data + 1, use_N_toy + offset_toy_data)
    write_data_to_JSON(pulls, output_file)
    
    
def get_histograms(folder):
    h_truth = folder.truth.Clone()
    h_measured = folder.measured.Clone()
    h_response = folder.response_withoutFakes_AsymBins.Clone()
    
    return h_truth, h_measured, h_response

if __name__ == "__main__":
    from ROOT import gROOT
    gROOT.SetBatch(True)
    gROOT.ProcessLine("gErrorIgnoreLevel = 3001;");
    bins = array('d', [0, 25, 45, 70, 100, 1000])
    nbins = len(bins) - 1
    parser = OptionParser()
    parser.add_option("-n", "--n_input_mc", type='int',
                      dest="n_input_mc", default=100,
                      help="number of toy MC used for the tests")
    parser.add_option("-e", "--error_toy_MC", type='int',
                      dest="error_toy_MC", default=1000,
                      help="number of toy MC used for the error calculation in SVD unfolding")
    parser.add_option("-k", "--k_value", type='int',
                      dest="k_value", default=6,
                      help="k-value for SVD unfolding")
    parser.add_option("-m", "--method", type='string',
                      dest="method", default='RooUnfoldSvd',
                      help="unfolding method")
    parser.add_option("-f", "--file", type='string',
                      dest="file", default='../../data/unfolding_toy_mc.root',
                      help="file with toy MC")
    parser.add_option("-c", "--channel", type='string',
                      dest="channel", default='both',
                      help="channel to be analysed: electron|muon|both")
    
    parser.add_option("--offset_toy_mc", type='int',
                      dest="offset_toy_mc", default=0,
                      help="offset of the toy MC used to response matrix")
    parser.add_option("--offset_toy_data", type='int',
                      dest="offset_toy_data", default=0,
                      help="offset of the toy MC used as data for unfolding")
    (options, args) = parser.parse_args()
    
    # set the number of toy MC for error calculation
    RooUnfold.SVD_n_toy = options.error_toy_MC
    RooUnfold.SVD_k_value = options.k_value
    use_N_toy = options.n_input_mc
    offset_toy_mc = options.offset_toy_mc
    offset_toy_data = options.offset_toy_data
    method = options.method
    
    output_folder = 'plots/%d_input_toy_mc/k_value_%d/%d_error_toy_MC/' % (use_N_toy, RooUnfold.SVD_k_value, RooUnfold.SVD_n_toy)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    input_file = input_file = File(options.file, 'read')
    
    start1, start2 = clock(), time()
    if options.channel == 'electron':
        check_multiple_data_multiple_unfolding(input_file, method, 'electron')
    elif options.channel == 'muon':
        check_multiple_data_multiple_unfolding(input_file, method, 'muon')
    else:
        check_multiple_data_multiple_unfolding(input_file, method, 'electron')
        check_multiple_data_multiple_unfolding(input_file, method, 'muon')
    end1, end2 = clock(), time()
    
    print 'Runtime', end1 - start1
    print 'Runtime', end2 - start2
    