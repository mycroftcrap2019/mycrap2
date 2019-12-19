# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:52:06 2019

@author: johan
"""
# Importing IntentBuilder
from adapt.intent import IntentBuilder
# Importing MycroftSkill class
from mycroft.skills.core import MycroftSkill

#create class
class ListenToCommandSkill(MycroftSkill):
    
    def _init_(self):
        super(ListenToCommandSkill, self)._init_("ListenToCommandSkill")
        
    def initialize(self):
        listen = IntentBuilder("test_inputIntent").require("test_input").build()
        # associate callback
        self.register_intent(listen, self.handle_listen)
        
    def handle_listen(self):
        #reaction
        self.speak_dialog("test_response")
        
    def stop(self):
        pass
    
    
    def create_skill():
        return ListenToCommandSkill()