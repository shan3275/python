import time
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

@scheduler.scheduled_job('cron', minute='*/1')
def request_update_status():
    print time.strftime('%Y-%m-%d %H:%M:%S') + ' Doing job'

@scheduler.scheduled_job('cron', minute='1', hour='*/1')
def rrequest_update_status():
    print time.strftime('%Y-%m-%d %H:%M:%S') + ' Doing  another job'
scheduler.start()

