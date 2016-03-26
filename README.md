## font-line

### About
font-line is a libre open source command line tool for font vertical metrics reporting and line spacing modifications.  It currently supports reporting and modifications of `.ttf` and `.otf` font builds.

### Contents

- [Install Guide](https://github.com/source-foundry/font-line#install)
- [Usage](https://github.com/source-foundry/font-line#usage)
	- [Vertical Metrics Reporting](https://github.com/source-foundry/font-line#vertical-metrics-reporting)
	- [Line Spacing Modifications](https://github.com/source-foundry/font-line#vertical-metrics-modifications)
- [Changelog](https://github.com/source-foundry/font-line/blob/master/CHANGELOG.md)
- [License](https://github.com/source-foundry/font-line/blob/master/docs/LICENSE)

### Install

font-line is built with Python and can be used on any system where the Python interpreter is installed. Use either of the following methods to install font-line on your system.

#### pip Install

The latest release version is available through the Python Package Index and can be installed with pip:

```
$ pip install font-line
```

#### Download Project Repository and Install

The current repository version (which may be ahead of the PyPI release) can be installed by [downloading the repository](https://github.com/source-foundry/font-line/archive/master.zip) or cloning it with git:

```
git clone https://github.com/source-foundry/font-line.git
```

Navigate to the top level repository directory and enter the following command:

```
$ python setup.py install
```

### Usage

font-line works via sub-commands to the `font-line` executable.  The following sub-commands are currently supported:

- `percent` - modify the line spacing of a font to a percent of the Ascender to Descender delta value
- `report` - report OpenType metrics values for a font

Usage of these sub-commands is described in detail below.

#### Vertical Metrics Reporting

The following OpenType vertical metrics values and calculated values derived from these data are displayed with the `report` sub-command:

- [OS/2] TypoAscender
- [OS/2] TypoDescender
- [OS/2] WinAscent
- [OS/2] WinDescent
- [OS/2] TypoLineGap
- [hhea] Ascent
- [hhea] Descent
- [hhea] lineGap
- [head] unitsPerEm

##### `report` Sub-Command Usage

Enter one or more font path arguments to the command:

```
$ font-line report [fontpath 1] <fontpath ...>
``` 

Here is an example of the report generated with `font-line report`:

```
=== Hack-Regular.ttf ===
Version 2.019; ttfautohint (v1.4.1) -l 4 -r 80 -G 350 -x 0 -H 181 -D latn -f latn -w G -W -t -X ""
SHA1: 3d5f3ccfa40406ad252b76a2219cb629df8e5ab3

[head] Units per Em: 	2048
[OS/2] TypoAscender: 	1556
[OS/2] TypoDescender: 	-492
[OS/2] WinAscent: 	1901
[OS/2] WinDescent: 	483
[hhea] Ascent: 		1901
[hhea] Descent: 	-483

[hhea] LineGap: 	0
[OS/2] TypoLineGap: 	410

--- Height Calculations by Table Values ---
[OS/2] TypoAscender to TypoDescender: 	2048
[OS/2] WinAscent to WinDescent: 	2384
[hhea] Ascent to Descent: 		2384

--- Delta Values ---
WinAscent to TypoAscender: 	345
Ascent to TypoAscender: 	345
WinDescent to TypoDescender: 	-9
Descent to TypoDescender: 	-9

--- Ratio of TypoLineGap to UPM ---
TypoLineGap / UPM: 	0.2
```

Unix/Linux/OS X users can write this report to a file with the `>` command line idiom:

```
$ font-line report TheFont.ttf > font-report.txt
```

#### Vertical Metrics Modifications

font-line currently supports automated line spacing modifications to a user-defined percentage of the TypoAscender to TypoDescender metric (often defined with the same value as the font units per em metric).  This delta value will be abbreviated as TA:TD below.

##### `percent` Sub-Command Usage

Enter the desired percentage of the TA:TD metric as the first argument to the command.  This should be formatted as an integer value.  Then enter one or more font paths to which you would like to apply your font metrics changes.

```
$ font-line percent [percent change] [fontpath 1] <fontpath ...>
```

A common default value used by typeface designers is 20%.  To modify a font on the path `TheFont.ttf` to 20% of the TA:TD metric, you would enter the following command:

```
$ font-line percent 20 TheFont.ttf
```

Increase or decrease the integer value to increase or decrease your line spacing accordingly.

The original font file is preserved in an unmodified version and the modified file write takes place on a new path defined as `[original filename]-linegap[percent].[ttf|otf]`.  The path to the file is reported to you in the standard output after the modification is completed.  font-line does not modify the glyph set or hints applied to the font.  See the Details section below for a description of the OpenType table modifications that occur when the application is used on a font file.

You can inspect the new vertical metrics in the new font file with the `report` subcommand (see Usage above).

##### Details of Font Metrics Changes with `percent` Sub-Command

The interpretation of the multiple vertical metric values is platform and application dependent.  This has led to [debate over the 'best' approach to font line spacing](https://grahamwideman.wikispaces.com/Font+Vertical+Metrics). The line spacing modification approach used in font-line is defined with a  slightly modified version of Karsten Lücke's approach that is described [here](http://www.kltf.de/downloads/FontMetrics-kltf.pdf).

*The following values are preserved from the original font design*:

- [OS/2] TypoAscender
- [OS/2] TypoDescender

We assume that the TypoAscender - TypoDescender delta value is equivalent to the UPM size, and therefore that the percent TA:TD value is equivalent to percent UPM when line spacing is defined.

*Changes to OpenType metrics values in the font are defined as*:

- [hhea] lineGap is always set to 0
- [OS/2] TypoLineGap = x% * TA:TD value
- [hhea] Ascent = [OS/2] TypoAscender + 0.5(modified TypoLineGap)
- [hhea] Descent = [OS/2] TypoDescender + 0.5(modified TypoLineGap)
- [OS/2] WinAscent = [OS/2] TypoAscender + 0.5(modified TypoLineGap)
- [OS/2] WinDescent = [OS/2] TypoDescender + 0.5(modified TypoLineGap)

Note that the internal leading modifications are split evenly across [hhea] Ascent & Descent values, and across [OS/2] WinAscent & WinDescent values.  We add half of the new [OS/2] TypoLineGap value to the original [OS/2] TypoAscender or TypoDescender in order to define these new metrics properties. 

These newly defined properties can lead to clipping of glyph components if not properly defined.  There are no tests in font-line to provide assurance that this does not occur. We assume that the user is versed in these issues before use of the application and leave this testing to the designer / user before the modified fonts are used in a production setting.

### Acknowledgments

font-line is built with the fantastic [fontTools](https://github.com/behdad/fonttools) Python library.


