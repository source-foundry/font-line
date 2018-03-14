## Changelog

### v1.0.0

- initial stable/production release

### v0.7.1

- bug fix for report failures when the xHeight and CapHeight values are missing from OpenType OS/2 tables in some fonts

### v0.7.0

- added [OS/2] CapHeight metric to report table
- added [OS/2] xHeight metric to report table
- modified version string parsing for report to support fonts that do not contain langID=0 tables
- added release.sh shell script
- updated Travis CI testing settings
- updated Appveyor CI testing settings
- updated tox.ini Python tox testing settings

### v0.6.1

- minor Python style fixes (PR #8 by @moyogo)

### v0.6.0

- modified percent command calculations to maintain vertical metrics approaches in the original font design
- added vertical metrics modification support for fonts designed with the following vertical metrics approaches:
    - Google style metrics where TypoLinegap = hhea linegap = 0, internal leading is present in [OS/2] TypoAsc/TypoDesc, [hhea] Asc/Desc, [OS/2] winAsc/winDesc
    - Adobe style metrics where TypoLinegap = hhea linegap = 0, TypoAsc - TypoDesc = UPM, internal leading in [hhea] Asc/Desc & [OS/2] winAsc/winDesc

### v0.5.4

- fix for font argument file path bug OSX/Linux/Win

### v0.5.3

- added [head] yMax metric to report
- added [head] yMin metric to report
- added [OS/2] (TypoAscender + TypoDescender + TypoLineGap) / UPM calculation to report
- added [OS/2] (winAsc + winDesc) / UPM calculation to report
- added [OS/2] (hhea Asc + Desc) / UPM calculation to report
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
