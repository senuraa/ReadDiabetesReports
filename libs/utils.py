import time
import os


def get_current_time():
    current_milli = int(round(time.time() * 1000))
    return str(current_milli)


def calc_result_box(text_loc=None, img_width=None):
    """
    input
    text_loc : dict of all text bbox coordinates
    {'fasting': (287, 1329, 483, 1364), 'blood': (506, 1330, 664, 1366), 'sugar': (685, 1332, 846, 1368)}

    img_width: maximum width to check
    output
    calc_loc: tuple of the calculated box
    """
    # TODO:Need to check whether the words are in the same line

    for key, val in text_loc.items():
        el_one_loc = val
        break
    calc_loc = (el_one_loc[0] - 10, el_one_loc[1] - 10, el_one_loc[2] + (img_width * 0.4), el_one_loc[3] + 10);
    return calc_loc


def create_dir(dirname):
    if not os.path.isdir(os.path.join(os.path.abspath('..'), "reader", dirname)) == True:
        os.makedirs(os.path.join(os.path.abspath('..'), "reader", dirname))
