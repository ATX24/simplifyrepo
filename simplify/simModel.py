
import sumy
import nltk
nltk.download('punkt')
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import requests
from bs4 import BeautifulSoup

class simModel:
    def summarize(text, numSentences):
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LexRankSummarizer()
        summary = summarizer(parser.document, numSentences) # number of sentences
        final = ' '
        for sentence in summary:
            final = final + ' ' + str(sentence)
        return final

    def scrape(url):
        import requests
        res = requests.get(url)
        html_page = res.content
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(html_page, 'html.parser')
        text = soup.find_all(text=True)

        output = ''
        blacklist = [
            '[document]',
            'noscript',
            'header',
            'html',
            'meta',
            'head', 
            'input',
            'script',
            'style'
            # there may be more elements you don't want, such as "style", etc.
        ]

        for t in text:
            if t.parent.name not in blacklist:
                output += '{} '.format(t)

        return output

    def getSummaryURL(text, numSentences):
        url = text
        print(url)
        return simModel.summarize(simModel.scrape(text), numSentences)

    def getSummary(text, numSentences):
        return simModel.summarize(text, numSentences)


        

    
