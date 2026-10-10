from apscheduler.schedulers.background import BackgroundScheduler

from .knowledge_updater import update_knowledge_base


scheduler = BackgroundScheduler()


def start_scheduler():
    """
    Start the automatic knowledge-base updater.
    """

    from apscheduler.schedulers.background import BackgroundScheduler

from .knowledge_updater import update_knowledge_base


scheduler = BackgroundScheduler()


def start_scheduler():

    if not scheduler.running:

        scheduler.add_job(
            update_knowledge_base,
            "interval",
            minutes=30,
            id="knowledge_base_update",
            replace_existing=True
        )

        scheduler.start()

        print("Knowledge-base scheduler started.")
        print("Next update will run in 30 minutes.")

        print("Knowledge-base scheduler started.")
        print("Knowledge base updated immediately.")
        print("Next automatic update will run in 30 minutes.")