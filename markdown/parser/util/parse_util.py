#!/usr/bin/env python
"""
Some functions about characters and strings.
"""


class ParseUtil(object):

    @staticmethod
    def get_heading_space_num(line, index=0):
        """
        Get the number of spaces from a given index.

        Args:
            line: The UTF-8 string.
            index: The start index.

        Returns:
            The number of spaces.
        """
        num = 0
        for c in line[index:]:
            if c == ' ':
                num += 1
            elif c == '\t':
                num += 4
            else:
                break
        return num

    @staticmethod
    def is_digit(char):
        return '0' <= char <= '9'

    @staticmethod
    def is_white_space(char):
        """
        A whitespace character is a space (U+0020), tab (U+0009), newline (U+000A),
        line tabulation (U+000B), form feed (U+000C), or carriage return (U+000D).

        Args:
            char: The single character.

        Returns:
            A boolean value.
        """
        return char in {' ', '\t', '\n', '\v', '\f', '\r'}

    @staticmethod
    def is_unicode_white_space(char):
        """
        A Unicode whitespace character is any code point in the Unicode Zs class,
        or a tab (U+0009), carriage return (U+000D), newline (U+000A), or form
        feed (U+000C).

        See Also:
            http://www.unicode.org/Public/UNIDATA/UnicodeData.txt

        Args:
            char: The single character.

        Returns:
            A boolean value.
        """
        return ParseUtil.is_white_space(char) or \
            char in {  # Unicode Zs class
                u'\u00A0', u'\u1680', u'\u2000', u'\u2001', u'\u2002',
                u'\u2003', u'\u2004', u'\u2005', u'\u2006', u'\u2007',
                u'\u2008', u'\u2009', u'\u200A', u'\u202F', u'\u205F',
                u'\u3000'
            }

    @staticmethod
    def is_ascii_punctuation(char):
        """
        An ASCII punctuation character is !, ", #, $, %, &, ', (, ), *, +, ,, -, .,
        /, :, ;, <, =, >, ?, @, [, \, ], ^, _, `, {, |, }, or ~.

        Args:
            char: The single character.

        Returns:
            A boolean value.
        """
        return char in {
            '!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
            '+', ',', '-', '.', '/', ':', ';', '<', '=', '>',
            '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',
            '}', '~'
        }

    @staticmethod
    def is_punctuation(char):
        """
        A punctuation character is an ASCII punctuation character or anything in the
        Unicode classes Pc, Pd, Pe, Pf, Pi, Po, or Ps.

        See Also:
            http://www.unicode.org/Public/UNIDATA/UnicodeData.txt

        Args:
            char: The single character.

        Returns:
            A boolean value.
        """
        return ParseUtil.is_ascii_punctuation(char) or \
            char in {
                # Unicode Pc class
                u'\u005F', u'\u203F', u'\u2040', u'\u2054', u'\uFE33',
                u'\uFE34', u'\uFE4D', u'\uFE4E', u'\uFE4F', u'\uFF3F',
                # Unicode Pd class
                u'\u002D', u'\u058A', u'\u05BE', u'\u1400', u'\u1806',
                u'\u2010', u'\u2011', u'\u2012', u'\u2013', u'\u2014',
                u'\u2015', u'\u2E17', u'\u2E1A', u'\u2E3A', u'\u2E3B',
                u'\u2E40', u'\u301C', u'\u3030', u'\u30A0', u'\uFE31',
                u'\uFE32', u'\uFE58', u'\uFE63', u'\uFF0D',
                # Unicode Pe class
                u'\u0029', u'\u005D', u'\u007D', u'\u0F3B', u'\u0F3D',
                u'\u169C', u'\u2046', u'\u207E', u'\u208E', u'\u2309',
                u'\u230B', u'\u232A', u'\u2769', u'\u276B', u'\u276D',
                u'\u276F', u'\u2771', u'\u2773', u'\u2775', u'\u27C6',
                u'\u27E7', u'\u27E9', u'\u27EB', u'\u27ED', u'\u27EF',
                u'\u2984', u'\u2986', u'\u2988', u'\u298A', u'\u298C',
                u'\u298E', u'\u2990', u'\u2992', u'\u2994', u'\u2996',
                u'\u2998', u'\u29D9', u'\u29DB', u'\u29FD', u'\u2E23',
                u'\u2E25', u'\u2E27', u'\u2E29', u'\u3009', u'\u300B',
                u'\u300D', u'\u300F', u'\u3011', u'\u3015', u'\u3017',
                u'\u3019', u'\u301B', u'\u301E', u'\u301F', u'\uFD3E',
                u'\uFE18', u'\uFE36', u'\uFE38', u'\uFE3A', u'\uFE3C',
                u'\uFE3E', u'\uFE40', u'\uFE42', u'\uFE44', u'\uFE48',
                u'\uFE5A', u'\uFE5C', u'\uFE5E', u'\uFF09', u'\uFF3D',
                u'\uFF5D', u'\uFF60', u'\uFF63',
                # Unicode Pf class
                u'\u00BB', u'\u2019', u'\u201D', u'\u203A', u'\u2E03',
                u'\u2E05', u'\u2E0A', u'\u2E0D', u'\u2E1D', u'\u2E21',
                # Unicode Pi class
                u'\u00AB', u'\u2018', u'\u201B', u'\u201C', u'\u201F',
                u'\u2039', u'\u2E02', u'\u2E04', u'\u2E09', u'\u2E0C',
                u'\u2E1C', u'\u2E20',
                # Unicode Po class
                u'\u0021', u'\u0022', u'\u0023', u'\u0025', u'\u0026',
                u'\u0027', u'\u002A', u'\u002C', u'\u002E', u'\u002F',
                u'\u003A', u'\u003B', u'\u003F', u'\u0040', u'\u005C',
                u'\u00A1', u'\u00A7', u'\u00B6', u'\u00B7', u'\u00BF',
                u'\u037E', u'\u0387', u'\u055A', u'\u055B', u'\u055C',
                u'\u055D', u'\u055E', u'\u055F', u'\u0589', u'\u05C0',
                u'\u05C3', u'\u05C6', u'\u05F3', u'\u05F4', u'\u0609',
                u'\u060A', u'\u060C', u'\u060D', u'\u061B', u'\u061E',
                u'\u061F', u'\u066A', u'\u066B', u'\u066C', u'\u066D',
                u'\u06D4', u'\u0700', u'\u0701', u'\u0702', u'\u0703',
                u'\u0704', u'\u0705', u'\u0706', u'\u0707', u'\u0708',
                u'\u0709', u'\u070A', u'\u070B', u'\u070C', u'\u070D',
                u'\u07F7', u'\u07F8', u'\u07F9', u'\u0830', u'\u0831',
                u'\u0832', u'\u0833', u'\u0834', u'\u0835', u'\u0836',
                u'\u0837', u'\u0838', u'\u0839', u'\u083A', u'\u083B',
                u'\u083C', u'\u083D', u'\u083E', u'\u085E', u'\u0964',
                u'\u0965', u'\u0970', u'\u0AF0', u'\u0DF4', u'\u0E4F',
                u'\u0E5A', u'\u0E5B', u'\u0F04', u'\u0F05', u'\u0F06',
                u'\u0F07', u'\u0F08', u'\u0F09', u'\u0F0A', u'\u0F0B',
                u'\u0F0C', u'\u0F0D', u'\u0F0E', u'\u0F0F', u'\u0F10',
                u'\u0F11', u'\u0F12', u'\u0F14', u'\u0F85', u'\u0FD0',
                u'\u0FD1', u'\u0FD2', u'\u0FD3', u'\u0FD4', u'\u0FD9',
                u'\u0FDA', u'\u104A', u'\u104B', u'\u104C', u'\u104D',
                u'\u104E', u'\u104F', u'\u10FB', u'\u1360', u'\u1361',
                u'\u1362', u'\u1363', u'\u1364', u'\u1365', u'\u1366',
                u'\u1367', u'\u1368', u'\u166D', u'\u166E', u'\u16EB',
                u'\u16EC', u'\u16ED', u'\u1735', u'\u1736', u'\u17D4',
                u'\u17D5', u'\u17D6', u'\u17D8', u'\u17D9', u'\u17DA',
                u'\u1800', u'\u1801', u'\u1802', u'\u1803', u'\u1804',
                u'\u1805', u'\u1807', u'\u1808', u'\u1809', u'\u180A',
                u'\u1944', u'\u1945', u'\u1A1E', u'\u1A1F', u'\u1AA0',
                u'\u1AA1', u'\u1AA2', u'\u1AA3', u'\u1AA4', u'\u1AA5',
                u'\u1AA6', u'\u1AA8', u'\u1AA9', u'\u1AAA', u'\u1AAB',
                u'\u1AAC', u'\u1AAD', u'\u1B5A', u'\u1B5B', u'\u1B5C',
                u'\u1B5D', u'\u1B5E', u'\u1B5F', u'\u1B60', u'\u1BFC',
                u'\u1BFD', u'\u1BFE', u'\u1BFF', u'\u1C3B', u'\u1C3C',
                u'\u1C3D', u'\u1C3E', u'\u1C3F', u'\u1C7E', u'\u1C7F',
                u'\u1CC0', u'\u1CC1', u'\u1CC2', u'\u1CC3', u'\u1CC4',
                u'\u1CC5', u'\u1CC6', u'\u1CC7', u'\u1CD3', u'\u2016',
                u'\u2017', u'\u2020', u'\u2021', u'\u2022', u'\u2023',
                u'\u2024', u'\u2025', u'\u2026', u'\u2027', u'\u2030',
                u'\u2031', u'\u2032', u'\u2033', u'\u2034', u'\u2035',
                u'\u2036', u'\u2037', u'\u2038', u'\u203B', u'\u203C',
                u'\u203D', u'\u203E', u'\u2041', u'\u2042', u'\u2043',
                u'\u2047', u'\u2048', u'\u2049', u'\u204A', u'\u204B',
                u'\u204C', u'\u204D', u'\u204E', u'\u204F', u'\u2050',
                u'\u2051', u'\u2053', u'\u2055', u'\u2056', u'\u2057',
                u'\u2058', u'\u2059', u'\u205A', u'\u205B', u'\u205C',
                u'\u205D', u'\u205E', u'\u2CF9', u'\u2CFA', u'\u2CFB',
                u'\u2CFC', u'\u2CFE', u'\u2CFF', u'\u2D70', u'\u2E00',
                u'\u2E01', u'\u2E06', u'\u2E07', u'\u2E08', u'\u2E0B',
                u'\u2E0E', u'\u2E0F', u'\u2E10', u'\u2E11', u'\u2E12',
                u'\u2E13', u'\u2E14', u'\u2E15', u'\u2E16', u'\u2E18',
                u'\u2E19', u'\u2E1B', u'\u2E1E', u'\u2E1F', u'\u2E2A',
                u'\u2E2B', u'\u2E2C', u'\u2E2D', u'\u2E2E', u'\u2E30',
                u'\u2E31', u'\u2E32', u'\u2E33', u'\u2E34', u'\u2E35',
                u'\u2E36', u'\u2E37', u'\u2E38', u'\u2E39', u'\u2E3C',
                u'\u2E3D', u'\u2E3E', u'\u2E3F', u'\u2E41', u'\u2E43',
                u'\u2E44', u'\u3001', u'\u3002', u'\u3003', u'\u303D',
                u'\u30FB', u'\uA4FE', u'\uA4FF', u'\uA60D', u'\uA60E',
                u'\uA60F', u'\uA673', u'\uA67E', u'\uA6F2', u'\uA6F3',
                u'\uA6F4', u'\uA6F5', u'\uA6F6', u'\uA6F7', u'\uA874',
                u'\uA875', u'\uA876', u'\uA877', u'\uA8CE', u'\uA8CF',
                u'\uA8F8', u'\uA8F9', u'\uA8FA', u'\uA8FC', u'\uA92E',
                u'\uA92F', u'\uA95F', u'\uA9C1', u'\uA9C2', u'\uA9C3',
                u'\uA9C4', u'\uA9C5', u'\uA9C6', u'\uA9C7', u'\uA9C8',
                u'\uA9C9', u'\uA9CA', u'\uA9CB', u'\uA9CC', u'\uA9CD',
                u'\uA9DE', u'\uA9DF', u'\uAA5C', u'\uAA5D', u'\uAA5E',
                u'\uAA5F', u'\uAADE', u'\uAADF', u'\uAAF0', u'\uAAF1',
                u'\uABEB', u'\uFE10', u'\uFE11', u'\uFE12', u'\uFE13',
                u'\uFE14', u'\uFE15', u'\uFE16', u'\uFE19', u'\uFE30',
                u'\uFE45', u'\uFE46', u'\uFE49', u'\uFE4A', u'\uFE4B',
                u'\uFE4C', u'\uFE50', u'\uFE51', u'\uFE52', u'\uFE54',
                u'\uFE55', u'\uFE56', u'\uFE57', u'\uFE5F', u'\uFE60',
                u'\uFE61', u'\uFE68', u'\uFE6A', u'\uFE6B', u'\uFF01',
                u'\uFF02', u'\uFF03', u'\uFF05', u'\uFF06', u'\uFF07',
                u'\uFF0A', u'\uFF0C', u'\uFF0E', u'\uFF0F', u'\uFF1A',
                u'\uFF1B', u'\uFF1F', u'\uFF20', u'\uFF3C', u'\uFF61',
                u'\uFF64', u'\uFF65', u'\U00010100', u'\U00010101', u'\U00010102',
                u'\U0001039F', u'\U000103D0', u'\U0001056F', u'\U00010857', u'\U0001091F',
                u'\U0001093F', u'\U00010A50', u'\U00010A51', u'\U00010A52', u'\U00010A53',
                u'\U00010A54', u'\U00010A55', u'\U00010A56', u'\U00010A57', u'\U00010A58',
                u'\U00010A7F', u'\U00010AF0', u'\U00010AF1', u'\U00010AF2', u'\U00010AF3',
                u'\U00010AF4', u'\U00010AF5', u'\U00010AF6', u'\U00010B39', u'\U00010B3A',
                u'\U00010B3B', u'\U00010B3C', u'\U00010B3D', u'\U00010B3E', u'\U00010B3F',
                u'\U00010B99', u'\U00010B9A', u'\U00010B9B', u'\U00010B9C', u'\U00011047',
                u'\U00011048', u'\U00011049', u'\U0001104A', u'\U0001104B', u'\U0001104C',
                u'\U0001104D', u'\U000110BB', u'\U000110BC', u'\U000110BE', u'\U000110BF',
                u'\U000110C0', u'\U000110C1', u'\U00011140', u'\U00011141', u'\U00011142',
                u'\U00011143', u'\U00011174', u'\U00011175', u'\U000111C5', u'\U000111C6',
                u'\U000111C7', u'\U000111C8', u'\U000111C9', u'\U000111CD', u'\U000111DB',
                u'\U000111DD', u'\U000111DE', u'\U000111DF', u'\U00011238', u'\U00011239',
                u'\U0001123A', u'\U0001123B', u'\U0001123C', u'\U0001123D', u'\U000112A9',
                u'\U0001144B', u'\U0001144C', u'\U0001144D', u'\U0001144E', u'\U0001144F',
                u'\U0001145B', u'\U0001145D', u'\U000114C6', u'\U000115C1', u'\U000115C2',
                u'\U000115C3', u'\U000115C4', u'\U000115C5', u'\U000115C6', u'\U000115C7',
                u'\U000115C8', u'\U000115C9', u'\U000115CA', u'\U000115CB', u'\U000115CC',
                u'\U000115CD', u'\U000115CE', u'\U000115CF', u'\U000115D0', u'\U000115D1',
                u'\U000115D2', u'\U000115D3', u'\U000115D4', u'\U000115D5', u'\U000115D6',
                u'\U000115D7', u'\U00011641', u'\U00011642', u'\U00011643', u'\U00011660',
                u'\U00011661', u'\U00011662', u'\U00011663', u'\U00011664', u'\U00011665',
                u'\U00011666', u'\U00011667', u'\U00011668', u'\U00011669', u'\U0001166A',
                u'\U0001166B', u'\U0001166C', u'\U0001173C', u'\U0001173D', u'\U0001173E',
                u'\U00011C41', u'\U00011C42', u'\U00011C43', u'\U00011C44', u'\U00011C45',
                u'\U00011C70', u'\U00011C71', u'\U00012470', u'\U00012471', u'\U00012472',
                u'\U00012473', u'\U00012474', u'\U00016A6E', u'\U00016A6F', u'\U00016AF5',
                u'\U00016B37', u'\U00016B38', u'\U00016B39', u'\U00016B3A', u'\U00016B3B',
                u'\U00016B44', u'\U0001BC9F', u'\U0001DA87', u'\U0001DA88', u'\U0001DA89',
                u'\U0001DA8A', u'\U0001DA8B', u'\U0001E95E', u'\U0001E95F',
                # Unicode Ps class
                u'\u0028', u'\u005B', u'\u007B', u'\u0F3A', u'\u0F3C',
                u'\u169B', u'\u201A', u'\u201E', u'\u2045', u'\u207D',
                u'\u208D', u'\u2308', u'\u230A', u'\u2329', u'\u2768',
                u'\u276A', u'\u276C', u'\u276E', u'\u2770', u'\u2772',
                u'\u2774', u'\u27C5', u'\u27E6', u'\u27E8', u'\u27EA',
                u'\u27EC', u'\u27EE', u'\u2983', u'\u2985', u'\u2987',
                u'\u2989', u'\u298B', u'\u298D', u'\u298F', u'\u2991',
                u'\u2993', u'\u2995', u'\u2997', u'\u29D8', u'\u29DA',
                u'\u29FC', u'\u2E22', u'\u2E24', u'\u2E26', u'\u2E28',
                u'\u2E42', u'\u3008', u'\u300A', u'\u300C', u'\u300E',
                u'\u3010', u'\u3014', u'\u3016', u'\u3018', u'\u301A',
                u'\u301D', u'\uFD3F', u'\uFE17', u'\uFE35', u'\uFE37',
                u'\uFE39', u'\uFE3B', u'\uFE3D', u'\uFE3F', u'\uFE41',
                u'\uFE43', u'\uFE47', u'\uFE59', u'\uFE5B', u'\uFE5D',
                u'\uFF08', u'\uFF3B', u'\uFF5B', u'\uFF5F', u'\uFF62',
            }
