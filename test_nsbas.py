import nsbas
import numpy as np 

# Extracted info for a random pixel.
pixel_value = np.array([1.6787422, np.nan, 0.63776565, 8.9154243, -5.5445247, 5.3991389, 4.024384, -1.2127494, -1.3101652, -6.7393432, -6.0843148, 0.74427611, 1.2428262, 0.53327626, 3.066505, 2.0696607, 2.3495839, 0.55888182, 1.0304395, 7.0070472, np.nan, 2.8901145, np.nan, 8.1926308, 0.35018942, -6.855248, -1.6475339, -0.85152066, 7.8289495, 2.742965, -13.100082, -15.758694, -9.1002159, 6.7630491, 3.6848667, -3.1546376, np.nan, 12.299849, -6.307229, -18.175419, -3.6914065, 13.868797, 14.271556, -3.4113064, 4.9759355, 1.8947219, -1.2857001, -8.4657831, -8.763217, -6.7877431, np.nan, 6.6413355, 12.686193, 12.327196, 2.965524, -9.3228235, -7.6308813, 1.9115051, -3.3419585, -4.955997, -17.411396, -12.019952])
dates = ['2017022', '2017262', '2017298', '2017250', '2017106', '2016364', '2017226', '2017190', '2017166', '2017334', '2017238', '2017094', '2017358', '2016292', '2017178', '2018017', '2017046', '2018029', '2017202', '2017286', '2017274', '2017154', '2016316', '2016340', '2017346', '2017058', '2017082', '2018005', '2017130', '2017322', '2017310', '2017070', '2017118', '2017142', '2017214']
date_pairs = ['2016292_2016316', '2016316_2016340', '2016340_2016364', '2016364_2017022', '2017022_2017046', '2017046_2017058', '2017046_2017070', '2017058_2017070', '2017058_2017082', '2017070_2017082', '2017070_2017094', '2017082_2017094', '2017082_2017106', '2017094_2017106', '2017094_2017118', '2017106_2017118', '2017106_2017130', '2017118_2017130', '2017118_2017142', '2017130_2017142', '2017130_2017154', '2017142_2017154', '2017142_2017166', '2017154_2017166', '2017154_2017178', '2017166_2017178', '2017166_2017190', '2017178_2017190', '2017178_2017202', '2017190_2017202', '2017190_2017214', '2017202_2017214', '2017202_2017226', '2017214_2017226', '2017214_2017238', '2017226_2017238', '2017226_2017250', '2017238_2017250', '2017238_2017262', '2017250_2017262', '2017250_2017274', '2017262_2017274', '2017262_2017286', '2017274_2017286', '2017274_2017298', '2017286_2017298', '2017286_2017310', '2017298_2017310', '2017298_2017322', '2017310_2017322', '2017310_2017334', '2017322_2017334', '2017322_2017346', '2017334_2017346', '2017334_2017358', '2017346_2017358', '2017346_2018005', '2017358_2018005', '2017358_2018017', '2018005_2018017', '2018005_2018029', '2018017_2018029'];
smoothing = 1;
wavelength=56;  # in mm


vel = nsbas.do_nsbas_pixel(pixel_value, dates, date_pairs, smoothing, wavelength);


