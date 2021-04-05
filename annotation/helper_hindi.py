import stanza
nlp_hi = stanza.Pipeline('hi')


def get_dependencies(doc, n):
    
    def getdeps(i):
        deps = []
        for head, rel, dep in doc.sentences[i].dependencies:
            deps.append((rel, dep.text))
        return deps

    return [getdeps(i) for i in range(n)]


def get_pos_tags(doc, n):

    def getpos(i):
        tokens = []
        for token in doc.sentences[i].words:
            tokens.append(token.upos)
        return tokens

    return [getpos(i) for i in range(n)]
