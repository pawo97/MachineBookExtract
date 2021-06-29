from book_tools.PersonRate import PersonRate


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

    def create_rating_dict(self):
        pass

    def count_words(self):
        pass

    def get_characters(self, words, doc, nlp):
        # Words in all book
        words_selected = self.get_list_non_alpha_numeric(words)

        print('compare words selected in book')
        print(words_selected)

        # nouns + persons + big literal
        # get nouns
        nouns = [chunk.text for chunk in doc.noun_chunks]

        # starts with a, the
        a_the_lists = self.get_words_with_prefix(nouns)

        # second term of word ex. white rabbit
        second_words_list = self.get_second_word(a_the_lists)

        # delete non alphanumerical
        liPrefixNonAlphaNumeric = self.get_list_non_alpha_numeric(second_words_list)

        # delete duplicates
        liPrefixNonAlphaNumeric = list(dict.fromkeys(liPrefixNonAlphaNumeric))

        # Get persons
        persons = self.get_persons_no_duplicates(doc)

        # Remove two words
        liCharPrefixNonSpace = self.get_last_word(persons)

        # Remove 's
        liRemoveDotS = self.remove_dot_s(liCharPrefixNonSpace)

        # Remove alphanumeric
        liCharNotAphaNumeric = self.get_list_non_alpha_numeric(liRemoveDotS)

        # Two list togheter without duplicates
        liPersons = liCharNotAphaNumeric  # + liPrefixNonAlphaNumeric
        liPersons = list(dict.fromkeys(liPersons))

        # Create rating list
        liRatingPersons = []
        for p in liPersons:
            if p != 'the' and p != 'a' and p.__len__() > 1:
                # check spacy tag
                doc = nlp(p)
                # print(p, doc[0].tag_, end=" | ")
                if 'NN' == doc[0].tag_:
                    person = PersonRate()
                    person.rate = 0
                    person.word = p
                    person.tag = doc[0].tag_
                    liRatingPersons.append(person)
                elif 'NNS' == doc[0].tag_:
                    person = PersonRate()
                    person.rate = 0
                    person.word = p[0:p.__len__() - 1]
                    person.tag = doc[0].tag_
                    liRatingPersons.append(person)

        # print(wordsSelected)
        # for p in liRatingPersons:
        #         print(str(p.word) + ' ' + str(p.rate), end=' ')

        # Count in words
        for w in words_selected:
            for p in liRatingPersons:
                if p.word in w or p.word == w:
                    p.rate += 1

        liRatingPersons.sort(key=lambda x: x.rate, reverse=True)
        liRatingPersons = list(dict.fromkeys(liRatingPersons))

        del liRatingPersons[30:]
        liPersons = []
        for p in liRatingPersons:
            # print(str(p.word) + ' ' + str(p.tag) + ' ' + str(p.rate))
            liPersons.append(str(p.word))

        del liCharNotAphaNumeric[30:]

        for i in range(len(liCharNotAphaNumeric)):
            liCharNotAphaNumeric[i] = liCharNotAphaNumeric[i].title()

        index = 0
        for i in range(len(liCharNotAphaNumeric)):
            if liCharNotAphaNumeric[i] == '':
                index = i

        if index != 0:
            del liCharNotAphaNumeric[index]
        return liCharNotAphaNumeric
