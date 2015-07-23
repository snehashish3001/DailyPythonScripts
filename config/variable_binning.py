fit_variable_bin_edges = {
                          'absolute_eta' : [round( i * 0.2, 2 ) for i in range ( int( 3 / 0.2 ) + 1 )],
                          'M3' : [i * 25 for i in range ( int( 1000 / 25 ) + 1 )],
                          'M_bl' : [i * 10 for i in range ( int( 1000 / 20 ) + 1 )],
                          'angle_bl' : [round( i * 0.2, 2 ) for i in range ( int( 4 / 0.2 ) + 1 )],
                          'Mjj' : [i * 25 for i in range ( int( 500 / 25 ) + 1 )],
                          }
bin_edges = {
# # 'leptonPt' : [30, 35, 40, 42., 45, 47, 51, 55, 60, 80, 90, 100, 120, 150, 200, 250, 300, 400],
# 'leptonPt' : [0.0, 33.00789348240006, 35.008371875272786, 37.008850268145515, 39.00932866101825, 41.00980705389098, 43.01028544676371, 45.01076383963644, 48.01148142894554, 51.012199018254634, 54.012916607563724, 57.01363419687282, 60.01435178618192, 63.01506937549102, 66.01578696480011, 69.0165045541092, 72.01722214341831, 75.0179397327274, 78.01865732203649, 82.01961410778196, 86.02057089352742, 90.02152767927288, 94.02248446501834, 99.02368044720016, 104.02487642938199, 109.02607241156382, 115.02750759018201, 121.0289427688002, 128.03061714385476, 136.03253071534567, 144.0344442868366, 153.0365970547639, 165.03946741200025, 178.04257696567302, 193.04616491221847, 209.04999205520033, 230.055015180364, 249.05955991265495, 274.0655398235641, 309.07391169883687, 358.0856323242188],
# # 'leptonEta' : [-2.5, -2.09, -2.08, -2.0700000000000003, -2.06, -2.0500000000000003, -2.04, -2.0300000000000002, -2.02, -2.0100000000000002, -2.0, -1.9900000000000002, -1.98, -1.9700000000000002, -1.96, -1.9500000000000002, -1.94, -1.9300000000000002, -1.92, -1.9100000000000001, -1.9050000000000002, -1.895, -1.8850000000000002, -1.875, -1.87, -1.8650000000000002, -1.855, -1.8450000000000002, -1.84, -1.83, -1.82, -1.81, -1.8, -1.79, -1.7850000000000001, -1.7800000000000002, -1.7750000000000001, -1.77, -1.7650000000000001, -1.7600000000000002, -1.7550000000000001, -1.75, -1.7400000000000002, -1.735, -1.725, -1.715, -1.71, -1.705, -1.7000000000000002, -1.695, -1.69, -1.685, -1.6800000000000002, -1.675, -1.67, -1.665, -1.6600000000000001, -1.6550000000000002, -1.6500000000000001, -1.645, -1.6400000000000001, -1.6350000000000002, -1.6300000000000001, -1.625, -1.62, -1.6150000000000002, -1.61, -1.605, -1.6, -1.5950000000000002, -1.59, -1.585, -1.58, -1.5750000000000002, -1.565, -1.5550000000000002, -1.465, -1.4500000000000002, -1.4400000000000002, -1.435, -1.4300000000000002, -1.425, -1.4200000000000002, -1.415, -1.4100000000000001, -1.405, -1.4000000000000001, -1.395, -1.3900000000000001, -1.385, -1.3800000000000001, -1.375, -1.37, -1.365, -1.36, -1.355, -1.35, -1.345, -1.34, -1.3350000000000002, -1.33, -1.3250000000000002, -1.32, -1.3150000000000002, -1.31, -1.3050000000000002, -1.3, -1.2950000000000002, -1.29, -1.2850000000000001, -1.28, -1.2750000000000001, -1.27, -1.2650000000000001, -1.26, -1.2550000000000001, -1.25, -1.245, -1.24, -1.235, -1.23, -1.225, -1.22, -1.215, -1.2100000000000002, -1.205, -1.2000000000000002, -1.195, -1.1900000000000002, -1.185, -1.1800000000000002, -1.175, -1.1700000000000002, -1.165, -1.1600000000000001, -1.155, -1.1500000000000001, -1.145, -1.1400000000000001, -1.135, -1.1300000000000001, -1.125, -1.12, -1.115, -1.11, -1.105, -1.1, -1.095, -1.09, -1.0850000000000002, -1.08, -1.0750000000000002, -1.07, -1.0650000000000002, -1.06, -1.0550000000000002, -1.05, -1.0450000000000002, -1.04, -1.0350000000000001, -1.03, -1.0250000000000001, -1.02, -1.0150000000000001, -1.01, -1.0050000000000001, -0.9999999999999999, -0.995, -0.9899999999999999, -0.985, -0.9799999999999999, -0.975, -0.9699999999999999, -0.965, -0.9599999999999999, -0.955, -0.9500000000000001, -0.945, -0.9400000000000001, -0.9349999999999999, -0.93, -0.9249999999999999, -0.92, -0.9149999999999999, -0.91, -0.9049999999999999, -0.9, -0.8949999999999999, -0.89, -0.8849999999999999, -0.88, -0.8749999999999999, -0.87, -0.8649999999999999, -0.86, -0.8549999999999999, -0.85, -0.8449999999999999, -0.84, -0.8349999999999999, -0.83, -0.8250000000000001, -0.82, -0.8150000000000001, -0.8099999999999999, -0.805, -0.7999999999999999, -0.795, -0.7899999999999999, -0.785, -0.7799999999999999, -0.775, -0.7699999999999999, -0.765, -0.7599999999999999, -0.755, -0.7499999999999999, -0.745, -0.7399999999999999, -0.735, -0.7299999999999999, -0.725, -0.7199999999999999, -0.715, -0.7099999999999999, -0.705, -0.7000000000000001, -0.695, -0.6900000000000001, -0.6849999999999999, -0.68, -0.6749999999999999, -0.67, -0.6649999999999999, -0.66, -0.6549999999999999, -0.65, -0.6449999999999999, -0.64, -0.6349999999999999, -0.63, -0.6249999999999999, -0.62, -0.6149999999999999, -0.61, -0.6049999999999999, -0.6, -0.5949999999999999, -0.59, -0.5849999999999999, -0.58, -0.5750000000000001, -0.57, -0.5650000000000001, -0.5599999999999999, -0.555, -0.5499999999999999, -0.545, -0.5399999999999999, -0.535, -0.5299999999999999, -0.525, -0.5199999999999999, -0.515, -0.5099999999999999, -0.505, -0.4999999999999999, -0.495, -0.4900000000000001, -0.48499999999999976, -0.47999999999999987, -0.475, -0.4700000000000001, -0.46499999999999975, -0.45999999999999985, -0.45499999999999996, -0.45000000000000007, -0.4450000000000002, -0.43999999999999984, -0.43499999999999994, -0.43000000000000005, -0.42500000000000016, -0.4199999999999998, -0.4149999999999999, -0.41000000000000003, -0.40500000000000014, -0.3999999999999998, -0.3949999999999999, -0.39, -0.3850000000000001, -0.3799999999999998, -0.3749999999999999, -0.37, -0.3650000000000001, -0.35999999999999976, -0.35499999999999987, -0.35, -0.3450000000000001, -0.33999999999999975, -0.33499999999999985, -0.32999999999999996, -0.32500000000000007, -0.31999999999999973, -0.31499999999999984, -0.30999999999999994, -0.30500000000000005, -0.30000000000000016, -0.2949999999999998, -0.2899999999999999, -0.28500000000000003, -0.28000000000000014, -0.2749999999999998, -0.2699999999999999, -0.265, -0.2600000000000001, -0.2549999999999998, -0.2499999999999999, -0.245, -0.2400000000000001, -0.23499999999999976, -0.22999999999999987, -0.22499999999999998, -0.22000000000000008, -0.21499999999999975, -0.20999999999999985, -0.20499999999999996, -0.20000000000000007, -0.19499999999999973, -0.18999999999999984, -0.18499999999999994, -0.18000000000000005, -0.17500000000000016, -0.16999999999999982, -0.16499999999999992, -0.16000000000000003, -0.15500000000000014, -0.1499999999999998, -0.1449999999999999, -0.14, -0.13500000000000012, -0.12999999999999978, -0.12499999999999989, -0.12, -0.1150000000000001, -0.10999999999999976, -0.10499999999999987, -0.09999999999999998, -0.09500000000000008, -0.08999999999999975, -0.08499999999999985, -0.07999999999999996, -0.07500000000000007, -0.06999999999999973, -0.06499999999999984, -0.05999999999999995, -0.055000000000000056, -0.05000000000000016, -0.044999999999999825, -0.03999999999999993, -0.03500000000000004, -0.03000000000000014, -0.024999999999999804, -0.01999999999999991, -0.015000000000000017, -0.010000000000000123, -0.004999999999999787, 1.0668549377257364e-16, 0.005, 0.009999999999999894, 0.015000000000000232, 0.020000000000000125, 0.02500000000000002, 0.029999999999999912, 0.035000000000000246, 0.04000000000000014, 0.04500000000000003, 0.049999999999999926, 0.055000000000000264, 0.06000000000000016, 0.06500000000000006, 0.06999999999999995, 0.07499999999999984, 0.08000000000000018, 0.08500000000000008, 0.08999999999999997, 0.09499999999999986, 0.1000000000000002, 0.1050000000000001, 0.10999999999999999, 0.11499999999999988, 0.12000000000000022, 0.1250000000000001, 0.13, 0.1349999999999999, 0.14000000000000024, 0.14500000000000013, 0.15000000000000002, 0.15499999999999992, 0.16000000000000025, 0.16500000000000015, 0.17000000000000004, 0.17499999999999993, 0.18000000000000027, 0.18500000000000016, 0.19000000000000006, 0.19499999999999995, 0.19999999999999984, 0.20500000000000018, 0.21000000000000008, 0.21499999999999997, 0.21999999999999986, 0.2250000000000002, 0.2300000000000001, 0.235, 0.23999999999999988, 0.24500000000000022, 0.2500000000000001, 0.255, 0.2599999999999999, 0.26500000000000024, 0.27000000000000013, 0.275, 0.2799999999999999, 0.28500000000000025, 0.29000000000000015, 0.29500000000000004, 0.29999999999999993, 0.30500000000000027, 0.31000000000000016, 0.31500000000000006, 0.31999999999999995, 0.32499999999999984, 0.3300000000000002, 0.3350000000000001, 0.33999999999999997, 0.34499999999999986, 0.3500000000000002, 0.3550000000000001, 0.36, 0.3649999999999999, 0.3700000000000002, 0.3750000000000001, 0.38, 0.3849999999999999, 0.39000000000000024, 0.39500000000000013, 0.4, 0.4049999999999999, 0.41000000000000025, 0.41500000000000015, 0.42000000000000004, 0.42499999999999993, 0.43000000000000027, 0.43500000000000016, 0.44000000000000006, 0.44499999999999995, 0.44999999999999984, 0.4550000000000002, 0.4600000000000001, 0.46499999999999997, 0.46999999999999986, 0.4750000000000002, 0.4800000000000001, 0.485, 0.4899999999999999, 0.4950000000000002, 0.5000000000000001, 0.505, 0.5099999999999999, 0.5150000000000002, 0.5200000000000001, 0.525, 0.5299999999999999, 0.5350000000000003, 0.5400000000000001, 0.545, 0.5499999999999999, 0.5550000000000003, 0.5600000000000002, 0.5650000000000001, 0.57, 0.5750000000000003, 0.5800000000000002, 0.5850000000000001, 0.59, 0.5949999999999999, 0.6000000000000002, 0.6050000000000001, 0.61, 0.6149999999999999, 0.6200000000000002, 0.6250000000000001, 0.63, 0.6349999999999999, 0.6400000000000002, 0.6450000000000001, 0.65, 0.6549999999999999, 0.6600000000000003, 0.6650000000000001, 0.67, 0.6749999999999999, 0.6800000000000003, 0.6850000000000002, 0.6900000000000001, 0.695, 0.7000000000000003, 0.7050000000000002, 0.7100000000000001, 0.715, 0.7199999999999999, 0.7250000000000002, 0.7300000000000001, 0.735, 0.7399999999999999, 0.7450000000000002, 0.7500000000000001, 0.755, 0.7599999999999999, 0.7650000000000002, 0.7700000000000001, 0.775, 0.7799999999999999, 0.7850000000000003, 0.7900000000000001, 0.795, 0.7999999999999999, 0.8050000000000003, 0.8100000000000002, 0.8150000000000001, 0.82, 0.8250000000000003, 0.8300000000000002, 0.8350000000000001, 0.84, 0.8449999999999999, 0.8500000000000002, 0.8550000000000001, 0.86, 0.8649999999999999, 0.8700000000000002, 0.8750000000000001, 0.88, 0.8849999999999999, 0.8900000000000002, 0.8950000000000001, 0.9, 0.9049999999999999, 0.9100000000000003, 0.9150000000000001, 0.92, 0.9249999999999999, 0.9300000000000003, 0.9350000000000002, 0.9400000000000001, 0.945, 0.9500000000000003, 0.9550000000000002, 0.9600000000000001, 0.965, 0.9699999999999999, 0.9750000000000002, 0.9800000000000001, 0.985, 0.9899999999999999, 0.9950000000000002, 1.0, 1.005, 1.0099999999999998, 1.0150000000000001, 1.02, 1.025, 1.0299999999999998, 1.0350000000000001, 1.04, 1.045, 1.0499999999999998, 1.0550000000000002, 1.06, 1.065, 1.0699999999999998, 1.0750000000000002, 1.08, 1.085, 1.0899999999999999, 1.0949999999999998, 1.1, 1.105, 1.1099999999999999, 1.1149999999999998, 1.12, 1.125, 1.13, 1.1349999999999998, 1.1400000000000001, 1.145, 1.15, 1.1549999999999998, 1.1600000000000001, 1.165, 1.17, 1.1749999999999998, 1.1800000000000002, 1.185, 1.19, 1.1949999999999998, 1.2000000000000002, 1.205, 1.21, 1.2149999999999999, 1.2199999999999998, 1.225, 1.23, 1.2349999999999999, 1.2399999999999998, 1.245, 1.25, 1.255, 1.2599999999999998, 1.2650000000000001, 1.27, 1.275, 1.2799999999999998, 1.2850000000000001, 1.29, 1.295, 1.2999999999999998, 1.3050000000000002, 1.31, 1.315, 1.3199999999999998, 1.3250000000000002, 1.33, 1.335, 1.3399999999999999, 1.3449999999999998, 1.35, 1.355, 1.3599999999999999, 1.3649999999999998, 1.37, 1.375, 1.38, 1.3849999999999998, 1.3900000000000001, 1.395, 1.4, 1.4049999999999998, 1.4100000000000001, 1.415, 1.42, 1.4249999999999998, 1.4300000000000002, 1.44, 1.4500000000000002, 1.4649999999999999, 1.5499999999999998, 1.5650000000000004, 1.5750000000000002, 1.58, 1.585, 1.5899999999999999, 1.5949999999999998, 1.5999999999999996, 1.6049999999999995, 1.6100000000000003, 1.6150000000000002, 1.62, 1.625, 1.63, 1.6349999999999998, 1.6399999999999997, 1.6449999999999996, 1.6500000000000004, 1.6550000000000002, 1.6600000000000001, 1.665, 1.67, 1.6749999999999998, 1.6799999999999997, 1.6849999999999996, 1.6900000000000004, 1.7000000000000002, 1.705, 1.71, 1.7149999999999999, 1.7199999999999998, 1.7249999999999996, 1.7299999999999995, 1.7350000000000003, 1.745, 1.755, 1.7599999999999998, 1.7649999999999997, 1.7699999999999996, 1.7750000000000004, 1.7800000000000002, 1.79, 1.7999999999999998, 1.8099999999999996, 1.8200000000000003, 1.83, 1.8399999999999999, 1.8499999999999996, 1.8600000000000003, 1.8650000000000002, 1.875, 1.8849999999999998, 1.8949999999999996, 1.9050000000000002, 1.915, 1.9249999999999998, 1.9349999999999996, 1.9450000000000003, 1.955, 1.9649999999999999, 1.9749999999999996, 1.9850000000000003, 1.995, 2.005, 2.0149999999999997, 2.0250000000000004, 2.035, 2.045, 2.0549999999999997, 2.0650000000000004, 2.075, 2.085, 2.5],
# # 'bEta' : [-2.5, -2.265, -2.1750000000000003, -2.085, -2.0, -1.925, -1.86, -1.79, -1.725, -1.665, -1.605, -1.545, -1.485, -1.4300000000000002, -1.37, -1.3150000000000002, -1.26, -1.2100000000000002, -1.1600000000000001, -1.115, -1.07, -1.03, -0.9899999999999999, -0.9500000000000001, -0.91, -0.87, -0.8250000000000001, -0.785, -0.7499999999999999, -0.7099999999999999, -0.67, -0.63, -0.59, -0.5499999999999999, -0.515, -0.475, -0.43499999999999994, -0.3949999999999999, -0.35499999999999987, -0.31999999999999973, -0.28500000000000003, -0.245, -0.20999999999999985, -0.16999999999999982, -0.13500000000000012, -0.09999999999999998, -0.05999999999999995, -0.024999999999999804, 0.015000000000000232, 0.055000000000000264, 0.09499999999999986, 0.1349999999999999, 0.17000000000000004, 0.20500000000000018, 0.24500000000000022, 0.2799999999999999, 0.31500000000000006, 0.3550000000000001, 0.39000000000000024, 0.42499999999999993, 0.46499999999999997, 0.505, 0.545, 0.5800000000000002, 0.6200000000000002, 0.6600000000000003, 0.7000000000000003, 0.7399999999999999, 0.7850000000000003, 0.8250000000000003, 0.8649999999999999, 0.9049999999999999, 0.945, 0.985, 1.0299999999999998, 1.0750000000000002, 1.12, 1.17, 1.2199999999999998, 1.27, 1.3199999999999998, 1.375, 1.4300000000000002, 1.4899999999999998, 1.5549999999999997, 1.6150000000000002, 1.6749999999999998, 1.7350000000000003, 1.7999999999999998, 1.8650000000000002, 1.9349999999999996, 2.005, 2.08, 2.175, 2.5],
# # 'bPt' : [0.0, 39.03763886272605, 54.05211534838991, 71.06852203214228, 91.08782401302743, 114.11002129104536, 140.13511386619606, 169.16310173847953, 203.19591510598428, 247.23837946393164, 788.760498046875],

# 'hadTopRap' : [-3.0, -0.47100000000000003, 0.0, 0.47100000000000003, 3.0],
# 'lepTopPt' : [0.0, 78.00582296558886, 156.01164593117775, 262.0195591921062, 400.0298613619942, 865.0645751953126],
# 'MT' : [0.0, 76.16660841248876, 278.60943603515625],
# 'hadTopPt' : [0.0, 82.01796010578649, 167.03657728861393, 836.1831054687499],
# 'ttbarPt' : [0.0, 73.08446987841735, 791.915283203125],
# 'ttbarM' : [250.0, 467.0353802977426, 740.0798909949027, 2267.328857421875],
# 'lepTopRap' : [-3.0, -0.441, 0.0, 0.441, 3.0],
# 'ttbarRap' : [-3.0, -1.452, -0.771, -0.264, 0.0, 0.264, 0.771, 1.452, 3.0],

# 'WPT' : [0.0, 50.0125104430094, 100.0250208860188, 163.04078404421062, 242.06055054416547, 333.0833195504425, 433.10834043646133, 1038.2597167968752],
# 'MET' : [0.0, 49.046597178131194, 225.21396663427586, 1009.9595214843749],
# 'HT' : [0.0, 214.03944895398095, 274.05050940836816, 339.06249156728757, 417.0768701579909, 509.0938295213846, 615.1133696574686, 740.1364122707753, 888.1636947249303, 1059.1952170199336, 1265.233191246663, 1503.2770643823987, 3231.5956054687495],
# 'ST' : [0.0, 310.0171244550445, 379.02093602729633, 459.02535524150136, 546.0301611369492, 642.0354641939953, 748.0413196528169, 868.0479484741245, 997.0550744570302, 1146.063305243487, 1309.0723093924298, 1508.0833021877647, 1750.096670310735, 3541.1956054687503],

# 'WPT' : [0.0, 500. ],
# 'MET' : [0.0, 400.0],
# 'HT' : [0.0,  1500.],
# 'ST' : [0.0,  2000.],

'WPT' : [0.0, 50, 100, 160, 240, 840, 1000],
'MET' : [0.0, 50, 170, 680, 1000],
'HT' : [0.0, 210, 270, 330, 410, 500, 600, 720, 860, 2900],
'ST' : [0.0, 300, 370, 450, 530, 630, 730, 850, 970, 3020],
}

bin_edges_vis = {
# 'hadTopRap' : [-3.0, -0.47400000000000003, 0.0, 0.47400000000000003, 3.0],
# 'lepTopPt' : [0.0, 79.00589761899386, 156.01164593117775, 256.0191112716763, 388.0289655211344, 865.0645751953126],
#'MT' : [0.0, 59.12934074127417, 278.60943603515625],
# 'hadTopPt' : [0.0, 80.01752205442584, 162.0354821602123, 836.1831054687499],
# 'ttbarPt' : [0.0, 45.052070472997, 123.14232595952514, 791.915283203125],
# 'ttbarM' : [250.0, 428.0290216267198, 576.0531519680375, 882.1030430791399, 2267.328857421875],
# 'lepTopRap' : [-3.0, -1.0979999999999999, -0.438, 0.0, 0.438, 1.0979999999999999, 3.0],
# 'ttbarRap' : [-3.0, -1.3679999999999999, -0.93, -0.54, -0.195, 0.0, 0.195, 0.54, 0.93, 1.3679999999999999, 3.0],

'WPT' : [0.0, 47.04255762419633, 96.0869262111244, 151.13672768624778, 222.20101686322522, 836.7569824218751],
'MET' : [0.0, 57.036686558006075, 154.09911806899888, 678.436376953125],
'HT' : [0.0, 220.06912820904645, 274.086096042176, 339.10652028575794, 418.1313435971882, 512.160880195599, 618.1941874235941, 742.2331505959658, 2863.899609375],
'ST' : [0.0, 327.10380272724444, 396.1257060550116, 476.1511012176402, 567.1799882151303, 670.2126844870146, 787.2498249123589, 919.2917269306961, 3013.9564453125],
}

control_plots_bins = {
  'NJets' : [i + 0.5 for i in range ( 3, 13 + 1 )],
  # 'NJets' : [i*0.25 for i in range ( 0, 40 + 1 )],
  'JetPt' : [i * 5  for i in range ( 5, 40 )],  
  'LeptonPt' : [i * 10 for i in range ( 3, 20 )],  
  'LeptonEta' : [-2.5, -2.0, -1.5, 1.0, 0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5],  
  'NBJets' : [i + 0.5 for i in range ( 1, 6 + 1 )],
  'NVertex' : [i*2 for i in range ( 0,20 + 1 )],
  'relIso_03_deltaBeta' : [i for i in range ( 0,2 + 1 )],
  'relIso_04_deltaBeta' : [i for i in range ( 0,2 + 1 )],
}


# should we want separate binning for different centre of mass energies
# we can put the logic here, maybe as a function:
# get_variable_binning(centre_of_mass_energy, combined = False)
# where combined gives you the best bins across the different
# centre of mass energies

bin_widths = {}
variable_bins_ROOT = {}
variable_bins_latex = {}
# calculate all the other variables
for variable in bin_edges.keys():
    bin_widths[variable] = []
    variable_bins_ROOT[variable] = []
    number_of_edges = len( bin_edges[variable] )
    for i in range( number_of_edges - 1 ):
        lower_edge = bin_edges[variable][i]
        upper_edge = bin_edges[variable][i + 1]
        bin_widths[variable].append( upper_edge - lower_edge )
        bin_name = '%d-%d' % ( int( lower_edge ), int( upper_edge ) )
        bin_name_latex = '%d--%d~\GeV' % ( int( lower_edge ), int( upper_edge ) )
        if ( i + 1 ) == number_of_edges - 1:
            bin_name = '%d-inf' % int( lower_edge )
            bin_name_latex = '$\\geq %d$~\GeV' % int( lower_edge )
        variable_bins_ROOT[variable].append( bin_name )
        variable_bins_latex[bin_name] = bin_name_latex
