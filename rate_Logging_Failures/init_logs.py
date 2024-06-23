import logging
import os
import random
import base64

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

# Configure logging
logging.basicConfig(filename='logs/all_logs.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Generate fake logs
for i in range(20):
    # Generate realistic log entries
    if i == 0:
        logging.info("User 'alice' logged in.")
    elif i == 1:
        logging.info("User 'bob' logged in.")
    elif i == 2:
        logging.info("Failed login attempt for user 'charlie' from IP 192.168.1.100.")
    elif i == 3:
        logging.info("User 'admin' changed password.")
    elif i == 4:
        logging.info("User 'eve' accessed sensitive data.")
    elif i == 5:
        logging.info("User 'mallory' attempted to escalate privileges.")
    elif i == 6:
        logging.info("User 'bob' uploaded a file 'document.pdf'.")
    elif i == 7:
        logging.info("User 'alice' deleted file 'report.docx'.")
    else:
        # Generate random fake logs for diversity
        logging.info(f"Random log entry {i}: Random data {random.randint(1, 1000)}")

# Log admin login with credentials
logging.info("Admin logged in with username: admin and password: P@ssw0rd!23.")

# Log admin access to secret_logs
logging.info("Admin accessed the /secret_logs directory.")
