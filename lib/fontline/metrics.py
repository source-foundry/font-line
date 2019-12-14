#!/usr/bin/env python3

from fontline.utilities import get_sha1


class MetricsObject:
    def __init__(self, tt, filepath):
        self.tt = tt
        self.filepath = filepath
        self.sha1 = get_sha1(self.filepath)
        # Version string
        self.version = ""
        for needle in tt["name"].names:
            if needle.nameID == 5:
                self.version = needle.toStr()
                break
        # Vertical metrics values as integers
        self.os2_typo_ascender = tt["OS/2"].sTypoAscender
        self.os2_typo_descender = tt["OS/2"].sTypoDescender
        self.os2_win_ascent = tt["OS/2"].usWinAscent
        self.os2_win_descent = tt["OS/2"].usWinDescent
        self.os2_typo_linegap = tt["OS/2"].sTypoLineGap
        try:
            self.os2_x_height = tt["OS/2"].sxHeight
        except AttributeError:
            self.os2_x_height = "---- (OS/2 table does not contain sxHeight record)"
        try:
            self.os2_cap_height = tt["OS/2"].sCapHeight
        except AttributeError:
            self.os2_cap_height = "---- (OS/2 table does not contain sCapHeight record)"
        self.hhea_ascent = tt["hhea"].ascent
        self.hhea_descent = tt["hhea"].descent
        self.hhea_linegap = tt["hhea"].lineGap
        self.ymax = tt["head"].yMax
        self.ymin = tt["head"].yMin
        self.units_per_em = tt["head"].unitsPerEm

        # Bit flag checks
        self.fsselection_bit7_mask = 1 << 7
        self.fsselection_bit7_set = (
            tt["OS/2"].fsSelection & self.fsselection_bit7_mask
        ) != 0

        # Calculated values
        self.os2_typo_total_height = self.os2_typo_ascender + abs(self.os2_typo_descender)
        self.os2_win_total_height = self.os2_win_ascent + self.os2_win_descent
        self.hhea_total_height = self.hhea_ascent + abs(self.hhea_descent)

        self.hhea_btb_distance = self.hhea_total_height + self.hhea_linegap
        self.typo_btb_distance = self.os2_typo_total_height + self.os2_typo_linegap
        self.win_external_leading = self.hhea_linegap - (
            (self.os2_win_ascent + self.os2_win_descent)
            - (self.hhea_ascent - self.hhea_descent)
        )
        if self.win_external_leading < 0:
            self.win_external_leading = 0
        self.win_btb_distance = (
            self.os2_win_ascent + self.os2_win_descent + self.win_external_leading
        )

        self.typo_to_upm = 1.0 * self.typo_btb_distance / self.units_per_em
        self.winascdesc_to_upm = 1.0 * self.win_btb_distance / self.units_per_em
        self.hheaascdesc_to_upm = 1.0 * self.hhea_btb_distance / self.units_per_em
