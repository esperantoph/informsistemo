# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from uuid import uuid4


def get_upload_path(instance, filename):
    """
    This function gets upload path of the image.
    Returns the image path.
    """
    
    file_name, file_extension = os.path.splitext(filename)
    app = instance._meta.app_label
    model = instance._meta.object_name.lower()
    
    new_file = '{}{}'.format(uuid4().hex, file_extension)
    
    return os.path.join(app, model, new_file)
