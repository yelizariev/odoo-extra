# -*- coding: utf-8 -*-

def migrate(cr, version):
    cr.execute("UPDATE runbot_build SET job = concat('_', job) WHERE job IS NOT NULL")
