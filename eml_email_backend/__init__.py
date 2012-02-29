# -*- coding: utf-8 -*-
from __future__ import absolute_import
import datetime
import os
from django.core.mail.backends import filebased

class EmailBackend(filebased.EmailBackend):
    def _get_filename(self):
        """Return a unique file name."""
        if self._fname is None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            fname = "%s-%s.eml" % (timestamp, abs(id(self)))
            self._fname = os.path.join(self.file_path, fname)
        return self._fname
