from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess

sched = BlockingScheduler()

@sched.scheduled_job('cron', hour=8, minute=0)
def send_daily_reminders():
    subprocess.run(['python', 'manage.py', 'send_reminders'])

sched.start()
