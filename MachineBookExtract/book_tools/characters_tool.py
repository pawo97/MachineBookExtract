import traceback

from book_tools.characters_person_rate import characters_person_rate


class characters_tool:

    def get_list_non_alpha_numeric(self, words):
        non_alpha_words = []
        for w in words:
            # blank
            if w != '':
                alphanumeric = ""
                for character in w:
                    if character.isalnum():
                        alphanumeric += character
                non_alpha_words.append(alphanumeric.lower())

        return list(dict.fromkeys(non_alpha_words))

    def get_second_word(self, li):
        li_second_word = []
        for i in li:
            if ' ' in i:
                j = i.split(' ')
                if len(j) >= 2:
                    li_second_word.append(j[1])
            else:
                li_second_word.append(i)

        return li_second_word

    def get_words_with_prefix(self, nouns):
        prefix_list = []
        for s in nouns:
            s_final = ''
            if (s.startswith('a ') or s.startswith('A ')) and s[2].isupper() and 'CHAPTER' not in s:
                s_final = s[2:]
                # print("LL", s[2:])
                prefix_list.append(s_final)
            elif (s.startswith('the ') or s.startswith('The ')) and s[4].isupper() and 'CHAPTER' not in s:
                s_final = s[4:]
                # print("LL", s[4:])
                prefix_list.append(s_final)

        return prefix_list

    def get_persons_no_duplicates(self, doc):
        persons = []
        for entity in doc.ents:
            if entity.label_ == 'PERSON':
                if entity.text[0].isupper():
                    persons.append(entity.text)

        return list(dict.fromkeys(persons))

    def get_last_word(self, persons):
        new_persons = []
        for i in persons:
            i = i.replace('\n', ' ')
            if ' ' in i:
                j = i.split(' ')
                if len(j) >= 2:
                    new_persons.append(j[len(j) - 1])
            else:
                new_persons.append(i)

        return new_persons

    def remove_dot_s(self, persons):
        new_persons = []

        for w in persons:
            if w.endswith("’s"):
                w = w[0:len(w) - 2]
            new_persons.append(w)

        return new_persons

    def check_spacy_tags(self, nlp, words_selected, persons):
        # Create rating list
        person_rates = []
        for p in persons:
            if p != 'the' and p != 'a' and len(p) > 1:
                # check spacy tag
                doc = nlp(p)

                if 'NN' == doc[0].tag_:
                    person = characters_person_rate()
                    person.rate = 0
                    person.word = p
                    person.tag = doc[0].tag_
                    person_rates.append(person)
                elif 'NNS' == doc[0].tag_:
                    person = characters_person_rate()
                    person.rate = 0
                    person.word = p[0:len(p) - 1]
                    person.tag = doc[0].tag_
                    person_rates.append(person)
                elif 'NNP' == doc[0].tag_:
                    person = characters_person_rate()
                    person.rate = 0
                    person.word = p
                    person.tag = doc[0].tag_
                    person_rates.append(person)

        # Count in words
        for w in words_selected:
            for p in person_rates:
                if p.word in w or p.word == w:
                    p.rate += 1

        person_rates.sort(key=lambda x: x.rate, reverse=True)
        person_rates = list(dict.fromkeys(person_rates))
        return person_rates

    def capital_letter_and_not_empty_str_list(self, persons):
        del persons[30:]

        # capital letter
        for i in range(len(persons)):
            persons[i] = persons[i].title()

        # delete empty strings
        final_person = []
        for i in range(len(persons)):
            if persons[i] != '' and len(persons[i]) > 2:
                final_person.append(persons[i])

        return final_person

    def sum_lists_rates(self, one, two, three):
        d = {}
        for i in one:
            d[i.lower()] = 0

        for i in two:
            if i not in d.keys():
                d[i.lower()] = 0
            else:
                d[i] += 1

        for i in three:
            if i not in d.keys():
                d[i.lower()] = 0
            else:
                d[i] += 1

        d = list(dict(sorted(d.items(), key=lambda item: item[1], reverse=True)).keys())
        return d

    def get_characters(self, words, doc, nlp):
        try:
            # Words in all book
            words_selected = self.get_list_non_alpha_numeric(words)

            # nouns + persons + big literal
            # get nouns
            # ==================================================================== GET BY TAGS
            nouns = [chunk.text for chunk in doc.noun_chunks]

            # starts with a, the
            a_the_lists = self.get_words_with_prefix(nouns)

            # second term of word ex. white rabbit
            second_words_list = self.get_second_word(a_the_lists)

            # delete non alphanumerical
            li_not_alpha = self.get_list_non_alpha_numeric(second_words_list)

            # delete duplicates
            li_not_alpha_duplicates = list(dict.fromkeys(li_not_alpha))

            # ==================================================================== GET BY WORDS
            # Get persons
            persons = self.get_persons_no_duplicates(doc)

            # Remove two words
            li_not_space = self.get_last_word(persons)

            # Remove 's
            li_dot_s = self.remove_dot_s(li_not_space)

            # Remove alphanumeric
            persons_result_list = self.get_list_non_alpha_numeric(li_dot_s)

            # ==================================================================== RATING PERSONS
            # Two list togheter without duplicates
            li_persons = list(dict.fromkeys(persons_result_list))

            # Create rating list
            li_person_rate = self.check_spacy_tags(nlp, words_selected, li_persons)

            del li_person_rate[30:]
            li_persons = []
            for p in li_person_rate:
                li_persons.append(str(p.word))

            # ==================================================================== SUM RESULTS

            persons_result_list = self.capital_letter_and_not_empty_str_list(persons_result_list)

            # sum and the biggest values from three lists
            d = self.sum_lists_rates(persons_result_list, li_persons, li_not_alpha_duplicates)

            # capitalize first letter
            final_list = self.capital_letter_and_not_empty_str_list(d)

        except Exception as e:
            print(traceback.format_exc())
            final_list = []

        return final_list
