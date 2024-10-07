import schedule
import time
import os
from dotenv import load_dotenv
from func.checkInToday import check_in_today
from func.dailySpinner import daily_spinner
from func.claimFarming import claim_farming
from func.crushLocker import crush_locker

# Load environment variables
load_dotenv()

# Run the tasks initially
check_in_today()
daily_spinner()
claim_farming()
crush_locker()

# Schedule tasks to run every hour
schedule.every().hour.do(check_in_today)
schedule.every().hour.do(daily_spinner)
schedule.every().hour.do(claim_farming)
schedule.every().hour.do(crush_locker)

# Main loop with a 2-minute interval between checks
while True:
    schedule.run_pending()
    time.sleep(120)  # 2-minute delay to check for pending tasks
