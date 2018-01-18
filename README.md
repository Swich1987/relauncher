# relauncher
Script relauncher. Re-run any script automatically, after finish work or any crashes/freezes. Cross-platform.

It's just simple algorithm:
1. Start any script as separate process.
2. Wait some time
3. Check if script finished(normally or crashed), then simply relaunch it.
4. If script not completed it's work, check special file's time of change. If it was more then TIME_TO_UNFREEZE, then kill process and launch it again.

Sometimes planned features:
- adding log possibility
