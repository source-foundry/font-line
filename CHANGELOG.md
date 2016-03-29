## Changelog

### v0.5.3

- added [head] yMax to report
- added [head] yMin to report
- added [OS/2] (TypoAscender + TypoDescender + TypoLineGap) / UPM to report
- added [OS/2] (winAsc + winDesc) / UPM to report
- added [OS/2] (hhea Asc + Desc) / UPM to report
- removed [OS/2] TypoLineGap / UPM from the report

### v0.5.2

- percent command: now forces entry of a percent integer value > 0, reports error & exits with attempts to enter values <= 0
- percent command: added standard output warning if there is an attempt to modify to a percent value > 100%
- minor standard output user message updates

### v0.5.1

- fixed implicit string cast / concatenation bug with Python 3.x interpreters
- updated usage message string formatting
- updated in application message string formatting

### v0.5.0

- initial release
