Make sure that you have installed google appengine on localmachine. 
Step 1:
    download your all entitie from appengine datastore using followning command 
        appcfg.py download_data --url=http://APP_ID.appspot.com/_ah/remote_api --batch_size=500 --num_threads=50 --bandwidth_limit=500000 --rps_limit=1000 --filename=PATH_ON_LOCAL_MACHINE
Step 2:
    run followng command to extract all entities into separate files:
        python export_sql3.py PATH_ON_LOCAL_MACHINE
