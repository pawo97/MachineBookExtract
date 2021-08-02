import traceback


class book_analyser_output():
    def __init__(self, book_analyser):
        self.b_a = book_analyser

    # ==================================================================================================================
    # Print tools
    # ==================================================================================================================
    def add_offset(self, value):
        final_str = value
        n = 7
        for i in range(n):
            if i > len(value):
                final_str += ' '

        return str(final_str)

    def add_offset_n(self, value, n):
        final_str = value
        for i in range(n):
            if i > len(value):
                final_str += ' '

        return str(final_str)

    # ==================================================================================================================
    # Print functions
    # ==================================================================================================================
    def get_basic_statistics_total(self):
        s0 = "|== Basic statistics ==========|" + "\n"
        s1 = "|CHARS AMOUNT         | " + self.add_offset(str(self.b_a.book_chars_amount)) + " |\n"
        s2 = "|WORDS AMOUNT         | " + self.add_offset(str(self.b_a.book_words_amount)) + " |\n"
        s3 = "|SENTENCES AMOUNT     | " + self.add_offset(str(self.b_a.book_sentences_amount)) + " |\n"
        s4 = "|AVG CHARS SENTENCES  | " + self.add_offset(str(self.b_a.book_sentences_average_chars)) + " |\n"
        s5 = "|AVG WORDS SENTENCES  | " + self.add_offset(str(self.b_a.book_sentences_average_words)) + " |\n"
        s6 = "|==============================|" + "\n"

        s_out = s0 + s1 + s2 + s3 + s4 + s5 + s6
        return s_out

    def get_time_statistics_total(self):
        s0 = "|== Tense statistics ==========|" + "\n"
        s1 = "|VERBS AMOUNT         | " + self.add_offset(str(self.b_a.total_vb)) + " |\n"
        s2 = "|PRESENT AMOUNT       | " + self.add_offset(str(self.b_a.present_vb)) + " |\n"
        s3 = "|PAST AMOUNT          | " + self.add_offset(str(self.b_a.past_vb)) + " |\n"
        s4 = "|PRESENT %            | " + self.add_offset(str(round(self.b_a.present_vb_p, 2))) + " |\n"
        s5 = "|PAST %               | " + self.add_offset(str(round(self.b_a.past_vb_p, 2))) + " |\n"
        s6 = "|==============================|" + "\n"

        s_out = s0 + s1 + s2 + s3 + s4 + s5 + s6
        return s_out

    def get_readability_total(self):
        s0 = "|== Readability statistics ====|" + "\n"
        s1 = "|FRE AMOUNT           | " + self.add_offset(str(self.b_a.fre)) + " |\n"
        s2 = "|FOG AMOUNT           | " + self.add_offset(str(self.b_a.fog)) + " |\n"
        s3 = "|SMOG AMOUNT          | " + self.add_offset(str(self.b_a.smog)) + " |\n"
        s4 = "|==============================|" + "\n"

        s_out = s0 + s1 + s2 + s3 + s4
        return s_out

    def get_adjectives_total(self):
        s0 = "|== Adjective statistics ======|" + "\n"
        s1 = "|ADJECTIVE AMOUNT     | " + self.add_offset(str(self.b_a.total_adj)) + " |\n"
        s2 = "|==============================|" + "\n"

        s_out = s0 + s1 + s2
        return s_out

    def get_dialogues_total(self):
        s0 = "|== Dialogues statistics ======|" + "\n"
        s1 = "|DIALOGUES AMOUNT     | " + self.add_offset(str(self.b_a.dialogues_amount)) + " |\n"
        s2 = "|DIALOGUES AVG CHARS  | " + self.add_offset(str(self.b_a.dialogues_average_chars)) + " |\n"
        s3 = "|DIALOGUES AVG WORDS  | " + self.add_offset(str(self.b_a.dialogues_average_words)) + " |\n"
        s4 = "|DIALOGUES LONG       | " + self.add_offset(str(self.b_a.dialogues_long_a)) + " |\n"
        s5 = "|DIALOGUES SHORT      | " + self.add_offset(str(self.b_a.dialogues_short_a)) + " |\n"
        s6 = "|DIALOGUES LONG %     | " + self.add_offset(str(self.b_a.dialogues_long_p)) + " |\n"
        s7 = "|DIALOGUES SHORT %    | " + self.add_offset(str(self.b_a.dialogues_short_p)) + " |\n"
        s8 = "|==============================|" + "\n"

        s_out = s0 + s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8
        return s_out

    def get_characters_total(self):
        s0 = "|== Characters ================|" + "\n"

        s_pom = ""
        for i in range(len(self.b_a.characters)):
            s_pom += "| " + self.add_offset_n(str(i + 1), 3) + " | " + self.add_offset_n(self.b_a.characters[i],
                                                                                         24) + " |\n"

        s8 = "|==============================|" + "\n"
        s_out = s0 + s_pom + s8

        return s_out

    def get_execution_time(self):
        s0 = "|== Analyse time ==============|" + "\n"
        s1 = "|EXECUTION TIME       | " + self.add_offset(str(self.b_a.analyse_time)) + " |\n"
        s2 = "|==============================|" + "\n"
        s_out = s0 + s1 + s2
        return s_out

    # =========================================================================================================================
    # Output print function
    # =========================================================================================================================
    def get_statistics_print(self):
        try:
            print("|== STATISTICS ================|")
            print(self.get_basic_statistics_total(), end='')
            print(self.get_time_statistics_total(), end='')
            print(self.get_readability_total(), end='')
            print(self.get_adjectives_total(), end='')
            print(self.get_dialogues_total(), end='')
            print(self.get_characters_total(), end='')
            print(self.get_execution_time(), end='')

        except Exception as e:
            print(traceback.format_exc())

    # ==================================================================================================================
    # Save functions
    # ==================================================================================================================
    def save_statistics_basic(self, name):
        try:
            text_file = open(r'output/' + str(name) + "_GLOBAL.txt", "w")
            s_out = self.get_basic_statistics_total() \
                    + self.get_time_statistics_total() \
                    + self.get_readability_total() \
                    + self.get_adjectives_total() \
                    + self.get_dialogues_total() \
                    + self.get_characters_total() \
                    + self.get_execution_time()

            text_file.write(s_out)
            text_file.close()
        except Exception as e:
            print(traceback.format_exc())

    def save_statistics_local(self, name, dat1):
        try:
            dat1.to_excel(r'output/' + str(name) + "_LOCAL.xlsx")
        except Exception as e:
            print(traceback.format_exc())
