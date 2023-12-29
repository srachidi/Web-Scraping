import scrapy
from ..items import BooksScraperItem

class QuotesSpider(scrapy.Spider):
    name = "books"

    start_urls = [
        'http://example.com/books',  # Remplacez ceci par l'URL réelle que vous souhaitez scraper
    ]

    def parse(self, response):
        for book in response.css('div.book'):  # Remplacez 'div.book' par le sélecteur CSS approprié pour les livres
            item = BooksScraperItem()
            item['title'] = book.css('span.title::text').get()  # Remplacez 'span.title' par le sélecteur CSS approprié pour le titre du livre
            item['author'] = book.css('span.author::text').get()  # Remplacez 'span.author' par le sélecteur CSS approprié pour l'auteur du livre
            yield item

        # Si vous avez une pagination, vous pouvez la gérer ici
        # Par exemple, pour une pagination simple:
        # next_page = response.css('a.next_page::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
