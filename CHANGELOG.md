## Changelog

### v3.1.2

- adjust line length to < 90
- transition to GitHub Actions CI testing service
- update fonttools dependency to v4.14.0

### v3.1.1

- remove Py2 wheels

### v3.1.0

- add requirements.txt file with pinned dependency versions
- update all build dependencies to current release versions
- the fontTools dependency updates add support for Unicode 13
- convert PyPI documentation to repository README Markdown file
- add Py3.8 interpreter to CI testing

### v3.0.0

- added baseline to baseline distance calculations for hhea, typo, and win metrics to reports
- added fsSelection bit 7 `USE_TYPO_METRICS` bit flag setting to report
- standard output report formatting improvements for `report` subcommand
- removed Py3.5 interpreter testing, we will support for Py3.6+ only as of this release
- add support for automated source code coverage push to Codecov from Travis

### v2.0.0

- changed copyright notice from "Christopher Simpkins" to "Source Foundry Authors"
- eliminated Python 2 interpreter support
- updated shebang lines to `#!/usr/bin/env python3`
- black formatting for source files
- refactored Travis CI settings file
- modified Travis CI testing to Python 3.5 - 3.7
- refactored Appveyor CI settings file
- modified Appveyor CI testing to Python 3.5 - 3.7
-

### v1.0.1

- removed unused variables in commands module
- add docs/LICENSE.md to release archives and Python wheels
- remove Pipfile and Pipfile.lock from version control

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
