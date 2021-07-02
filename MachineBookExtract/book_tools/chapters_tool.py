import re
import pandas as pd
from book_tools_main.book_analyser_local import book_analyser_local


class chapters_tool:

    def get_chapters_position(self, content):
        """Get chapters if is divided by chapter, number or roman"""
        lines = content.split('\n')

        # dictionary
        dict_chars_roman_dot = {}
        dict_chars_roman = {}
        dict_chars_chap_nr_dot = {}
        dict_chars_chap_ro_dot = {}

        # get founded lines
        for i in range(len(lines)):
            if i - 1 > 0:
                if lines[i - 1] == '':
                    # not collect blank lines and THE END.
                    if lines[i] == '':
                        continue
                    if 'THE END.' in lines[i]:
                        continue

                    # Check first word
                    # CHAPTER inside
                    if i + 1 < len(lines) and i + 2 < len(lines):
                        wordsNext = lines[i + 1].lstrip().split(' ')
                        wordsNextNext = lines[i + 2].lstrip().split(' ')
                        if 'chapter' in wordsNext[0].lower() or 'chapter' in wordsNextNext[0].lower():
                            continue
                    words = lines[i].lstrip().split(' ')

                    # Check first word
                    # CHAPTER and NUMBER and .
                    firstword = words[0]
                    s = ''
                    if firstword.lower() == 'chapter':
                        s = re.sub(r'[^a-zA-Z0-9]', '', words[1])
                        if not self.check_if_roman_numeral(s):
                            dict_chars_chap_nr_dot[int(s)] = i

                    # Check first word
                    # ROMAN NUMBER and .
                    s = ''
                    try:
                        s = re.sub(r'[^a-zA-Z0-9]', '', firstword)
                    except:
                        s = ''
                    lastwordot = ''
                    try:
                        lastwordot = s[-1]
                        # print(s)
                    except:
                        lastwordot = ''
                    if self.check_if_roman_numeral(s):
                        # print(lines[i], '|', s)
                        if dict_chars_chap_ro_dot.get(self.decimal_to_roman_str(s)) == None:
                            dict_chars_chap_ro_dot[int(self.decimal_to_roman_str(s))] = i

                    # Check last word
                    # ROMAN NUMBER and .
                    lastwordot = ''
                    try:
                        lastwordot = words[len(words) - 1]
                    except:
                        lastwordot = ''
                    if lastwordot != '' and lastwordot[-1] == '.':
                        lastword = lastwordot[0:len(lastwordot) - 1]
                        if self.check_if_roman_numeral(lastword):
                            if dict_chars_roman_dot.get(self.decimal_to_roman_str(lastword)) == None:
                                # print(lines[i], '|', lastwordot)
                                dict_chars_roman_dot[self.decimal_to_roman_str(lastword)] = i

                    # Check last word
                    # ROMAN NUMBER
                    lastwordot = ''
                    try:
                        lastwordot = words[len(lastwordot) - 1]
                    except:
                        lastwordot = ''
                    if lastwordot != '':

                        lastword = lastwordot
                        if self.check_if_roman_numeral(lastword):
                            if dict_chars_roman.get(self.decimal_to_roman_str(lastword)) == None:
                                # print(lines[i], '|', lastword)
                                dict_chars_roman[self.decimal_to_roman_str(lastword)] = i

        # Create List of chapters and positions
        # chapter Roman and .
        li_chap_chars_roman_dot = self.sort_and_order(dict_chars_roman_dot)
        count_roman_dot = len(li_chap_chars_roman_dot)

        # chapter Roman
        li_chap_chars_roman = self.sort_and_order(dict_chars_roman)
        count_roman = len(li_chap_chars_roman)

        # chapter Number Dot
        li_chap_chars_chapter_number_dot = self.sort_and_order(dict_chars_chap_nr_dot)
        count_chapter_number_dot = len(li_chap_chars_chapter_number_dot)

        # chapter Roman Dot
        li_chap_chars_chapter_roman_dot = self.sort_and_order(dict_chars_chap_ro_dot)
        count_chapter_roman_dot = len(li_chap_chars_chapter_roman_dot)

        # return the biggest list (appropriate amount of chapters)
        data_index = {
            'roman-dot': count_roman_dot,
            'roman': count_roman,
            'chapter-number': count_chapter_number_dot,
            'chapter-roman-dot': count_chapter_roman_dot
        }
        chap_val = max(data_index, key=data_index.get)

        data_lists = {
            'roman-dot': li_chap_chars_roman_dot,
            'roman': li_chap_chars_roman,
            'chapter-number': li_chap_chars_chapter_number_dot,
            'chapter-roman-dot': li_chap_chars_chapter_roman_dot
        }
        divide_numbers_list = data_lists[chap_val]

        # print(data_index)
        return lines, divide_numbers_list

    def get_fragments(self, divide_numbers_list, lines):
        """Get fragments from position of chars fragments"""
        try:
            if len(divide_numbers_list) > 0:
                divide_numbers_list[0] = int(divide_numbers_list[0] + 1)

            p = divide_numbers_list
            fragments = []
            j = 0
            chapter = ''

            for i in range(len(lines)):
                if i < p[j]:
                    continue
                if i >= p[j]:
                    if j + 1 < len(p) and i == p[j + 1]:
                        j += 1
                        fragments.append(chapter)
                        chapter = ''
                    else:
                        chapter += lines[i] + '\n'
                    if i + 1 >= len(lines):
                        fragments.append(chapter)
        except Exception as e:
            fragments = []
        return fragments

    def get_chapters_content(self, content):
        """Get list of fragments in book list of chars"""
        lines, chapters_pos_numbers = self.get_chapters_position(content)
        fragments = self.get_fragments(chapters_pos_numbers, lines)

        return fragments

    def sort_and_order(self, dicts):
        """Get the biggest value of list"""
        keys = sorted(dicts.items())
        count = 1
        positions_list = []

        for key in keys:
            if key[0] == count:
                positions_list.append(key[1])
                count += 1
            else:
                break

        return positions_list

    def get_local_statistics(self, fragments, present, past, adjs, characters):
        """Get local statistics for chapters"""
        words_amount_list = []
        char_amount_list = []
        sentences_amount_list = []
        sentences_avg_chars_list = []
        sentences_avg_words_list = []
        dialogues_amount_list = []
        dialogues_l_amount_list = []
        dialogues_s_amount_list = []
        total_vb_amount_list = []
        present_vb_amount_list = []
        past_vb_amount_list = []
        adj_vb_amount_list = []
        heroes_list = []
        df = pd.DataFrame()

        for i in range(len(fragments)):
            # update
            b_a_l = book_analyser_local(fragments[i])
            b_a_l.start_chapter(fragments[i], present, past, adjs, characters)

            words_amount_list.append(b_a_l.book_words_amount)
            char_amount_list.append(b_a_l.book_chars_amount)
            sentences_amount_list.append(b_a_l.book_sentences_amount)
            sentences_avg_chars_list.append(b_a_l.book_sentences_average_chars)
            sentences_avg_words_list.append(b_a_l.book_sentences_average_words)
            dialogues_amount_list.append(b_a_l.dialogues_amount)
            dialogues_l_amount_list.append(b_a_l.dialogues_long_a)
            dialogues_s_amount_list.append(b_a_l.dialogues_short_a)
            total_vb_amount_list.append(b_a_l.total_vb)
            present_vb_amount_list.append(b_a_l.present_vb)
            past_vb_amount_list.append(b_a_l.past_vb)
            adj_vb_amount_list.append(b_a_l.total_adj)
            heroes_list.append(b_a_l.characters)

        # set
        df['WordsAmount'] = words_amount_list
        df['CharsAmount'] = char_amount_list
        df['SentencesAmount'] = sentences_amount_list
        df['SentencesAvgChars'] = sentences_avg_chars_list
        df['SentencesAvgWords'] = sentences_avg_words_list
        df['DialoguesAmount'] = dialogues_amount_list
        df['DialoguesLongAmount'] = dialogues_l_amount_list
        df['DialoguesShortAmount'] = dialogues_s_amount_list
        df['VerbsAmount'] = total_vb_amount_list
        df['VerbsPresentAmount'] = present_vb_amount_list
        df['VerbsPastAmount'] = past_vb_amount_list
        df['AdjectivesAmount'] = adj_vb_amount_list
        df['Characters'] = heroes_list

        return df

    def check_if_roman_numeral(self, numeral):
        """Check if number is roman or not"""
        if not numeral.isupper():
            valid = False
            return valid
        validRomanNumerals = ["M", "D", "C", "L", "X", "V", "I", "(", ")"]
        valid = True
        for letters in numeral:
            if letters not in validRomanNumerals:
                # print("Sorry that is not a valid roman numeral")
                valid = False
                break
        return valid

    def decimal_to_roman(self, r):
        """Short roman numbers in string"""
        if r == 'I':
            return 1
        if r == 'V':
            return 5
        if r == 'X':
            return 10
        if r == 'L':
            return 50
        if r == 'C':
            return 100
        if r == 'D':
            return 500
        if r == 'M':
            return 1000
        return -1

    def decimal_to_roman_str(self, str):
        """Long roman numbers in string"""
        res = 0
        i = 0

        while i < len(str):
            s1 = self.decimal_to_roman(str[i])

            if i + 1 < len(str):
                s2 = self.decimal_to_roman(str[i + 1])

                if s1 >= s2:
                    res = res + s1
                    i = i + 1
                else:
                    res = res + s2 - s1
                    i = i + 2
            else:
                res = res + s1
                i = i + 1
        return res

    # ====================================================================

    # EXPERIMENT - AND VALUES

    def get_statisctis_location(self, doc):
        gpe = []  # countries, cities, states
        loc = []  # non gpe locations, mountain ranges, bodies of water
        for ent in doc.ents:
            if (ent.label_ == 'GPE'):
                gpe.append(ent.text)
            elif (ent.label_ == 'LOC'):
                loc.append(ent.text)

        gpe.extend(loc)
        gpe = list(set(gpe))

        for g in gpe:
            print(g)


    def get_statisctis_time(self, doc):
        gpe = []  # countries, cities, states
        loc = []  # non gpe locations, mountain ranges, bodies of water
        for ent in doc.ents:
            if (ent.label_ == 'DATE'):
                gpe.append(ent.text)

        gpe = list(set(gpe))
        del gpe[:30]
        for g in gpe:
            print(g)

    # ====================================================================
