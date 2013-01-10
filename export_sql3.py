import re
import sys
import csv
import sqlite3
from google.appengine.datastore import entity_pb
from google.appengine.api import datastore
if len(sys.argv) != 2:
    print "need to provide downloaded datastore file location"
    sys.exit()
datastore_file = sys.argv[1]

ct = 0
p=re.compile("type: \"(.*)\"")
conn = sqlite3.connect(datastore_file, isolation_level=None)
cursor = conn.cursor()
cursor.execute('select id, value from result')
writers = dict()
for unused_entity_id, entity in cursor:
        entity_proto = entity_pb.EntityProto(contents=entity)
        f = datastore.Entity._FromPb(entity_proto)
        entity_type = p.search(str(entity_proto.key().path())).group(1)
        writer_name = 'export_%s.csv' % entity_type
        if writers.has_key(writer_name):
            csvwriter = writers[writer_name]
        else:
            csvwriter = csv.writer(open(writer_name, 'w'))
            writers[writer_name] = csvwriter
        csvwriter.writerow([f])

        ct += 1
        if ct % 20000 == 0:
            print "Ct is %s" % ct
            sys.stdout.flush()

print "done"
