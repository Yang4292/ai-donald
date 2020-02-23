import scrapy
import io

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['https://www.rev.com/blog/transcripts/donald-trump-las-vegas-nevada-rally-transcript',
                    'https://www.rev.com/blog/transcripts/donald-trump-colorado-springs-co-rally-transcript',
                    'https://www.rev.com/blog/transcripts/donald-trump-phoenix-arizona-rally-transcript',
                    'https://www.rev.com/blog/transcripts/donald-trump-new-jersey-rally-speech-transcript-trump-holds-rally-in-wildwood-nj',
                    'https://www.rev.com/blog/transcripts/donald-trump-milwaukee-rally-transcript-trump-holds-rally-during-iowa-democratic-debate',
                    'https://www.rev.com/blog/transcripts/donald-trump-ohio-campaign-rally-transcript-transcript-of-toledo-ohio-rally',
                    'https://www.rev.com/blog/transcripts/donald-trump-michigan-rally-transcript-trump-holds-a-rally-in-battle-creek-during-impeachment',
                    'https://www.rev.com/blog/transcripts/donald-trump-hershey-pennsylvania-rally-transcript-december-10-2019',
                    'https://www.rev.com/blog/transcripts/donald-trump-kentucky-rally-speech-transcript-lexington-kentucky-rally',
                    'https://www.rev.com/blog/transcripts/donald-trump-mississippi-rally-speech-transcript-2019-rally-in-tupelo-mississippi',
                    'https://www.rev.com/blog/transcripts/donald-trump-dallas-rally-speech-transcript-october-17-2019',
                    'https://www.rev.com/blog/transcripts/donald-trump-minnesota-rally-speech-transcript-minneapolis-mn-rally-october-10-2019',
                    'https://www.rev.com/blog/transcripts/donald-trump-new-mexico-rally-transcript-full-speech-transcript',
                    'https://www.rev.com/blog/transcripts/donald-trump-north-carolina-rally-transcript-in-fayetteville-nc-september-9-2019',
                    'https://www.rev.com/blog/transcripts/donald-trump-new-hampshire-rally-transcript-august-15-2019',
                    'https://www.rev.com/blog/transcripts/donald-trump-ohio-rally-speech-transcript-full-transcript-of-august-1-2019-rally-in-cincinnati',
                    'https://www.rev.com/blog/transcripts/donald-trump-maga-event-speech-transcript-north-carolina-rally']

    def parse(self, response):
        file = io.open('speech.txt', mode='a', encoding='utf-8')
        SET_SELECTOR = '.fl-callout-text'
        speech = response.css(SET_SELECTOR)
        NAME_SELECTOR = 'p::text'
        
        for line in speech.css(NAME_SELECTOR):
            text = line.get()
            if(len(text) > 30):
                file.write(text + "\n")