from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess

def run_start_script():
    try:
        subprocess.run(["python3", "app/StockBasicData.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running StockBasicData.py: {e}")

def run_end_script():
    try:
        subprocess.run(["python3", "app/StockFinaceDate.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running StockFinaceDate.py: {e}")

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    # 毎日午前0時にrun_start_script関数を実行する
    scheduler.add_job(run_start_script, 'cron', hour=0, minute=0)
    # 毎日午前0時15分にrun_end_script関数を実行する
    scheduler.add_job(run_end_script, 'cron', hour=0, minute=15)
    print("Scheduler started. The scripts will run once every day at midnight and 12:15 AM.")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
