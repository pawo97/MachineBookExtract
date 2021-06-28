from book_tools.PersonRate import PersonRate


class characters_tool:

    def getCharactersInBook(self, content, doc, nlp):
        # Words in all book
        blank = ' '
        words = content.split(' ')
        # print('compare words in book')
        # print(words)
        wordsSelected = []

        for w in words:
            # blank
            if w != '':
                # Remove nonalphanumeric
                alphanumeric = ""
                for character in w:
                    if character.isalnum():
                        alphanumeric += character
                wordsSelected.append(alphanumeric.lower())

        # print('compare words selected in book')
        # print(wordsSelected)

        # Nouns + Persons + Big literal
        # Nouns
        liNouns = [chunk.text for chunk in doc.noun_chunks]
        # z duzej litery

        # zaczyna sie na a, the
        liPrefix = []
        for s in liNouns:
            sFinal = ''
            if (s.startswith('a ') or s.startswith('A ')) and s[2].isupper() and 'CHAPTER' not in s:
                sFinal = s[2:]
                # print("LL", s[2:])
                liPrefix.append(sFinal)
            elif (s.startswith('the ') or s.startswith('The ')) and s[4].isupper() and 'CHAPTER' not in s:
                sFinal = s[4:]
                # print("LL", s[4:])
                liPrefix.append(sFinal)

        # druga czesc wyrazu, gdyz nazwisko wazniejsze, albo white rabbit
        liPrefixNonSpace = []
        for i in liPrefix:
            if ' ' in i:
                j = i.split(' ')
                if j.__len__() >= 2:
                    liPrefixNonSpace.append(j[1])
            else:
                liPrefixNonSpace.append(i)

        # usuniecie alfanumerycznych znakow
        liPrefixNonAlphaNumeric = []
        for w in liPrefixNonSpace:
            # blank
            if w != '':
                # Remove nonalphanumeric
                alphanumeric = ""
                for character in w:
                    if character.isalnum():
                        alphanumeric += character
                liPrefixNonAlphaNumeric.append(alphanumeric.lower())

        # delete duplicates
        liPrefixNonAlphaNumeric = list(dict.fromkeys(liPrefixNonAlphaNumeric))
        # print(liPrefixNonAlphaNumeric)

        # Get persons
        liCharacters = []
        for entity in doc.ents:
            if entity.label_ == 'PERSON':
                if entity.text[0].isupper():
                    liCharacters.append(entity.text)

        # Get persons
        liCharNotDuplicates = list(dict.fromkeys(liCharacters))
        # print("PERSONS")
        # print(liCharNotDuplicates)

        # Remove two words
        liCharPrefixNonSpace = []
        for i in liCharNotDuplicates:
            i = i.replace('\n', ' ')
            if ' ' in i:
                j = i.split(' ')
                if j.__len__() >= 2:
                    liCharPrefixNonSpace.append(j[j.__len__() - 1])
            else:
                liCharPrefixNonSpace.append(i)

        # Remove 's
        liRemoveDotS = []
        # print(liCharPrefixNonSpace)
        for w in liCharPrefixNonSpace:
            # blank
            if w.endswith("’s"):
                w = w[0:w.__len__() - 2]
            liRemoveDotS.append(w)
        # print(liRemoveDotS)

        # Remove alphanumeric
        liCharNotAphaNumeric = []
        for w in liRemoveDotS:
            # blank
            if w != '':
                # Remove nonalphanumeric
                alphanumeric = ""
                for character in w:
                    if character.isalnum():
                        alphanumeric += character
                liCharNotAphaNumeric.append(alphanumeric.lower())

        # Remove duplicates
        liCharNotAphaNumeric = list(dict.fromkeys(liCharNotAphaNumeric))
        # print(liCharNotAphaNumeric)

        # Two list togheter without duplicates
        liPersons = liCharNotAphaNumeric #+ liPrefixNonAlphaNumeric
        liPersons = list(dict.fromkeys(liPersons))
        # print(liPersons)
        # Delete verbs, adverbs, adjective
        # print("Verbs:", [token.lemma_ for token in self.doc if token.pos_ == "VERB"])

        # Create rating list
        # print(liPersons)
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
        for w in wordsSelected:
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