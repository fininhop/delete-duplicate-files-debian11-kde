#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class mainWindow:

    def mainWindow_destroy_cb(self, object, data=None):
        Gtk.main_quit()
    
    def chooseFolder_file_set_cb(self, object, data=None):
        #print(self.chooseFolder.get_filename())
        self.pathEntry.set_text(self.chooseFolder.get_filename())
        
    def removeButton_clicked_cb(self, object, data=None):
        #print(self.pathEntry.get_text())
        output_stream = os.popen('rdfind -deleteduplicates true -ignoreempty false '+self.pathEntry.get_text())
        self.textbuffer1.set_text(output_stream.read())

    def __init__(self):
        self.gladefile = "delete-duplicated-files.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("mainWindow")
        self.removeButtom = self.builder.get_object("removeButtom")
        self.resultTextView = self.builder.get_object("resultTextView")
        self.chooseFolder = self.builder.get_object("chooseFolder")
        self.pathEntry = self.builder.get_object("pathEntry")
        self.textbuffer1 = self.builder.get_object("textbuffer1")
        self.window.show()

if __name__ == "__main__":
    main = mainWindow()
    Gtk.main()
