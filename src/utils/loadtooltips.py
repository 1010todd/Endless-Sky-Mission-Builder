""" loadtooltips.py
# Copyright (c) 2019 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
"""

import logging
import json
import os


def load_tooltips():
    logging.debug("\tLoading tooltips...")
    data_folder = os.path.dirname(os.path.dirname(os.path.abspath("ESMB.py")))
    file_path = os.path.join(data_folder, "data", "tooltips.json")
    with open(file_path) as data_file:
        logging.debug("\t\tTooltips JSON file opened...")
        data = json.load(data_file)
    #end with open
    return data
#end load_tooltips
