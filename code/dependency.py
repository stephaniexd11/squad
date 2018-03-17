import spacy
from spacy.tokens import Doc

# WhitespaceTokenizer from
# https://spacy.io/usage/linguistic-features#tokenization
class WhitespaceTokenizer(object):
    def __init__(self, vocab):
        self.vocab = vocab

    def __call__(self, text):
        words = text.split(' ')
        # All tokens 'own' a subsequent space character in this tokenizer
        spaces = [True] * len(words)
        return Doc(self.vocab, words=words, spaces=spaces)


class DependencyParser(object):
    """Parses dependencies from text"""

    def __init__(self):
        self.nlp = spacy.load('en')
        self.nlp.tokenizer = WhitespaceTokenizer(self.nlp.vocab)

    def parse(self, text):
        return [token.dep for token in self.nlp(unicode(text.strip("\n")))]

PARSER = DependencyParser()