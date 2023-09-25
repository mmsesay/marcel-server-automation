import time
from app.platforms.marcel import MarcelServer


if __name__ == "__main__":
    marcel_server = MarcelServer()
    marcel_server.login()

    time.sleep(1000)

