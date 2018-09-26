from threading import Timer

# threaded timer
class ThreadedTimer():
    def __init__(self, seconds, target, name):
        self._should_continue = False
        self.is_running = False
        self.seconds = seconds
        self.target = target
        self.thread = None
        self.PAUSED = False
        self.clockTimer = 0
        self.name = name

    def _handle_target(self):
        self.is_running = True
        self.target()
        self.is_running = False
        self._start_timer()

    def _start_timer(self):
        if self._should_continue: # Code could have been running when cancel was called.
            self.thread = Timer(self.seconds, self._handle_target)
            self.thread.start()

    def setPause(self):
        print("pausing timer")
        self.PAUSED = True

    def setUnPause(self):
        print("un-pausing timer")
        self.PAUSED = False

    def getPaused(self):
        return self.PAUSED

    def getTimer(self):
        return self.clockTimer

    def start(self):
        if not self._should_continue and not self.is_running:
            self._should_continue = True
            self._start_timer()
            print("started timer." + self.name)
        else:
            print("Timer already started or running, please wait if you're restarting.")

    def cancel(self):
        if self.thread is not None:
            self._should_continue = False # Just in case thread is running and cancel fails.
            self.thread.cancel()

            self.seconds = 0
            print("canceling timer.")
        else:
            print("Timer never started or failed to initialize.")