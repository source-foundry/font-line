font-line |Build Status| |Build status| |codecov.io|
----------------------------------------------------

Source Repository: `https://github.com/source-foundry/font-line <https://github.com/source-foundry/font-line>`__

Issue Tracker and Reporting: `https://github.com/source-foundry/font-line/issues <https://github.com/source-foundry/font-line/issues>`__

License: MIT


About
~~~~~

font-line is a libre, open source command line tool for OpenType
vertical metrics reporting and command line based font line spacing
modifications. It currently supports ``.ttf`` and ``.otf`` font builds.

Contents
~~~~~~~~

-  `Install
   Guide <https://github.com/source-foundry/font-line#install>`__
-  `Usage <https://github.com/source-foundry/font-line#usage>`__

   -  `Vertical Metrics
      Reporting <https://github.com/source-foundry/font-line#vertical-metrics-reporting>`__
   -  `Line Spacing
      Modifications <https://github.com/source-foundry/font-line#vertical-metrics-modifications>`__

-  `Changelog <https://github.com/source-foundry/font-line/blob/master/CHANGELOG.md>`__
-  `License <https://github.com/source-foundry/font-line/blob/master/docs/LICENSE>`__

Quickstart
~~~~~~~~~~

-  Install: ``$ pip install font-line``
-  Metrics Report: ``$ font-line report [font path]``
-  Modify line spacing: ``$font-line percent [integer %] [font path]``

Install
~~~~~~~

font-line is built with Python and can be used on systems with Python
2.7+ and Python 3.3+ interpreters, including current releases of pypy
and pypy3. You can verify your installed Python version on the command
line with the command:

::

    $ python --version

Use either of the following methods to install font-line on your system.

pip Install
^^^^^^^^^^^

The latest font-line release is available through the Python Package
Index and can be installed with pip:

::

    $ pip install font-line

To upgrade to a new version of font-line after a pip install, use the
command ``pip install --upgrade font-line``.

Download Project Repository and Install
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The current repository version (which may be ahead of the PyPI release)
can be installed by `downloading the
repository <https://github.com/source-foundry/font-line/archive/master.zip>`__
or cloning it with git:

::

    git clone https://github.com/source-foundry/font-line.git

Navigate to the top level repository directory and enter the following
command:

::

    $ python setup.py install

Follow the same instructions to upgrade to a new version of the
application if you elect to install with this approach.

Usage
~~~~~

font-line works via sub-commands to the ``font-line`` command line
executable. The following sub-commands are available:

-  ``percent`` - modify the line spacing of a font to a percent of the
   Ascender to Descender distance
-  ``report`` - report OpenType metrics values for a font

Usage of these sub-commands is described in detail below.

Vertical Metrics Reporting
^^^^^^^^^^^^^^^^^^^^^^^^^^

The following OpenType vertical metrics values and calculated values
derived from these data are displayed with the ``report`` sub-command:

-  [OS/2] TypoAscender
-  [OS/2] TypoDescender
-  [OS/2] WinAscent
-  [OS/2] WinDescent
-  [OS/2] TypoLineGap
-  [hhea] Ascent
-  [hhea] Descent
-  [hhea] lineGap
-  [head] unitsPerEm
-  [head] yMax
-  [head] yMin

``report`` Sub-Command Usage
''''''''''''''''''''''''''''

Enter one or more font path arguments to the command:

::

    $ font-line report [fontpath 1] <fontpath ...>

Here is an example of the report generated with the Hack typeface file
``Hack-Regular.ttf`` using the command:

::

    $ font-line report Hack-Regular.ttf

Example Font Vertical Metrics Report
''''''''''''''''''''''''''''''''''''

::

    === Hack-Regular.ttf ===
    Version 2.020;DEV-03192016;
    SHA1: 638f033cc1b6a21597359278bee62cf7e96557ff

    --- Metrics ---
    [head] Units per Em:    2048
    [head] yMax:            2001
    [head] yMin:            -573
    [OS/2] TypoAscender:    1556
    [OS/2] TypoDescender:   -492
    [OS/2] WinAscent:       1901
    [OS/2] WinDescent:       483
    [hhea] Ascent:          1901
    [hhea] Descent:         -483

    [hhea] LineGap:           0
    [OS/2] TypoLineGap:     410

    --- Height Calculations by Table Values ---
    [OS/2] TypoAscender to TypoDescender:   2048
    [OS/2] WinAscent to WinDescent:         2384
    [hhea] Ascent to Descent:               2384

    --- Delta Values ---
    WinAscent to TypoAscender:      345
    Ascent to TypoAscender:         345
    WinDescent to TypoDescender:     -9
    Descent to TypoDescender:        -9

    --- Ratios ---
    (Typo Asc + Desc + Linegap) / UPM:  1.2
    (winAsc + winDesc) / UPM:           1.16
    (hhea Asc + Desc) / UPM:            1.16

The report includes the font version string, a SHA-1 hash digest of the
font file, and OpenType table metrics that are associated with line
spacing in the font.

Unix/Linux/OS X users can write this report to a file with the ``>``
command line idiom:

::

    $ font-line report TheFont.ttf > font-report.txt

You can modify ``font-report.txt`` to the file path of your choice.

Vertical Metrics Modifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

font-line supports automated line spacing modifications to a
user-defined percentage of the units per em metric. This value will be
abbreviated as UPM below.

``percent`` Sub-Command Usage
'''''''''''''''''''''''''''''

Enter the desired percentage of the UPM as the first argument to the
command. This should be *entered as an integer value*. Then enter one or
more font paths to which you would like to apply your font metrics
changes.

::

    $ font-line percent [percent change] [fontpath 1] <fontpath ...>

A common default value used by typeface designers is 20% UPM. To modify
a font on the path ``TheFont.ttf`` to 20% of the UPM metric, you would
enter the following command:

::

    $ font-line percent 20 TheFont.ttf

Increase or decrease the integer value to increase or decrease your line
spacing accordingly.

The original font file is preserved in an unmodified version and the
modified file write takes place on a new path defined as
``[original filename]-linegap[percent].[ttf|otf]``. The path to the file
is reported to you in the standard output after the modification is
completed. font-line does not modify the glyph set or hints applied to
the font. See the Details section below for a description of the
OpenType table modifications that occur when the application is used on
a font file.

You can inspect the vertical metrics in the new font file with the
``report`` sub-command (see Usage above).

Details of Font Metrics Changes with ``percent`` Sub-Command
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

The interpretation and display of these multiple vertical metrics values
is platform and application dependent. `There is no broadly accepted
"best"
approach <https://github.com/source-foundry/font-line/issues/2>`__. As
such, font-line attempts to preserve the original metrics design in the
font when modifications are made with the ``percent`` sub-command.

font-line currently supports three commonly used vertical metrics
approaches.

**Vertical Metrics Approach 1**:

Where metrics are defined as:

-  [OS/2] TypoLinegap = 0
-  [hhea] linegap = 0
-  [OS/2] TypoAscender = [OS/2] winAscent = [hhea] Ascent
-  [OS/2] TypoDescender = [OS/2] winDescent = [hhea] Descent

font-line calculates a delta value for the total expected height based
upon the % UPM value defined on the command line. The difference between
this value and the observed number of units that span the [OS/2]
winAscent to winDescent values is divided by half and then added to (for
increased line spacing) or subtracted from (for decreased line spacing)
each of the three sets of Ascender/Descender values in the font. The
[OS/2] TypoLinegap and [hhea] linegap values are not modified.

**Vertical Metrics Approach 2**

Where metrics are defined as:

-  [OS/2] TypoLinegap = 0
-  [hhea] linegap = 0
-  [OS/2] TypoAscender + TypoDescender = UPM
-  [OS/2] winAscent = [hhea] Ascent
-  [OS/2] winDescent = [hhea] Descent

font-line calculates a delta value for the total expected height based
upon the % UPM value defined on the command line. The difference between
this value and the observed number of units that span the [OS/2]
winAscent to winDescent values is divided by half and then added to (for
increased line spacing) or subtracted from (for decreased line spacing)
the [OS/2] winAsc/winDesc and [hhea] Asc/Desc values. The [OS/2]
TypoAsc/TypoDesc values are not modified and maintain a definition of
size = UPM value. The [OS/2] TypoLinegap and [hhea] linegap values are
not modified.

**Vertical Metrics Approach 3**

Where metrics are defined as:

-  [OS/2] TypoAscender + TypoDescender = UPM
-  [OS/2] TypoLinegap is set to leading value
-  [hhea] linegap = 0
-  [OS/2] winAscent = [hhea] Ascent
-  [OS/2] winDescent = [hhea] Descent

*Changes to the metrics values in the font are defined as*:

-  [OS/2] TypoLineGap = x% \* UPM value
-  [hhea] Ascent = [OS/2] TypoAscender + 0.5(modified TypoLineGap)
-  [hhea] Descent = [OS/2] TypoDescender + 0.5(modified TypoLineGap)
-  [OS/2] WinAscent = [OS/2] TypoAscender + 0.5(modified TypoLineGap)
-  [OS/2] WinDescent = [OS/2] TypoDescender + 0.5(modified TypoLineGap)

Note that the internal leading modifications are split evenly across
[hhea] Ascent & Descent values, and across [OS/2] WinAscent & WinDescent
values. We add half of the new [OS/2] TypoLineGap value to the original
[OS/2] TypoAscender or TypoDescender in order to define these new
metrics properties. The [hhea] linegap value is always defined as zero.

Important
^^^^^^^^^

The newly defined vertical metrics values can lead to clipping of glyph
components if not properly defined. There are no tests in font-line to
provide assurance that this does not occur. We assume that the user is
versed in these issues before use of the application and leave this
testing to the designer / user before the modified fonts are used in a
production setting.

Issue Reporting
~~~~~~~~~~~~~~~

Please `submit a new issue
report <https://github.com/source-foundry/font-line/issues/new>`__ on
the project repository.

Acknowledgments
~~~~~~~~~~~~~~~

font-line is built with the fantastic
`fontTools <https://github.com/behdad/fonttools>`__ Python library.

.. |Build Status| image:: https://travis-ci.org/source-foundry/font-line.svg?branch=master
   :target: https://travis-ci.org/source-foundry/font-line
.. |Build status| image:: https://ci.appveyor.com/api/projects/status/2s4725o5mxh2298c/branch/master?svg=true
   :target: https://ci.appveyor.com/project/chrissimpkins/font-line/branch/master
.. |codecov.io| image:: https://codecov.io/github/source-foundry/font-line/coverage.svg?branch=master
   :target: https://codecov.io/github/source-foundry/font-line?branch=master
