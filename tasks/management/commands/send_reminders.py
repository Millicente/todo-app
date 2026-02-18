from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from tasks.models import Task
from datetime import timedelta

class Command(BaseCommand):
    help = 'Send email reminders for due and overdue tasks'

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
        
        # Get all incomplete tasks that are due today or overdue
        tasks = Task.objects.filter(
            completed=False,
            due_date__lte=today
        ).select_related('user')
        
        # Group tasks by user
        user_tasks = {}
        for task in tasks:
            if task.user.email:  # Only if user has an email
                if task.user not in user_tasks:
                    user_tasks[task.user] = []
                user_tasks[task.user].append(task)
        
        # Send emails
        emails_sent = 0
        for user, task_list in user_tasks.items():
            overdue = [t for t in task_list if t.is_overdue]
            due_today = [t for t in task_list if t.is_due_today]
            
            if overdue or due_today:
                subject = f'Task Reminder - {len(overdue)} overdue, {len(due_today)} due today'
                
                message = f'Hello {user.username},\n\n'
                
                if overdue:
                    message += f'You have {len(overdue)} overdue task(s):\n'
                    for task in overdue:
                        message += f'  - {task.title} (Due: {task.due_date})\n'
                    message += '\n'
                
                if due_today:
                    message += f'You have {len(due_today)} task(s) due today:\n'
                    for task in due_today:
                        message += f'  - {task.title}\n'
                        if task.due_time:
                            message += f'    at {task.due_time.strftime("%I:%M %p")}\n'
                    message += '\n'
                
                message += 'Visit your todo list to manage your tasks.\n'
                message += 'http://127.0.0.1:8000/\n'
                
                try:
                    send_mail(
                        subject,
                        message,
                        None,  # Uses DEFAULT_FROM_EMAIL
                        [user.email],
                        fail_silently=False,
                    )
                    emails_sent += 1
                    self.stdout.write(self.style.SUCCESS(f'Email sent to {user.email}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Failed to send to {user.email}: {str(e)}'))
        
        self.stdout.write(self.style.SUCCESS(f'Total emails sent: {emails_sent}'))