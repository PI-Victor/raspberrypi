#!/usr/bin/env python

import MySQLdb

class SqlHandler:
    
    def __init__(self, user, password, hostname):
        self.user=user
        self.paswd=password
        self.host=hostname
        self.handler= MySQLdb.connect(hostname,username,password,db='app')
        return self.handler
