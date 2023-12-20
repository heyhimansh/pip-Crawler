############################################################################################
########################################    PART 6

import scrapy
# import the bBookItem class
from bookscraper.items import BookItem

class BookspiderSpider(scrapy.Spider):

    # name of spider we craeted
    name = "bookspider"

    # domain we select for scrap
    allowed_domains = ["books.toscrape.com"]
    #Actual URL
    start_urls = ["https://books.toscrape.com"]

    # this is  the function that exectues when the spider gets some response to procces 

    # count =0 
       
    def parse(self, response):
        # initially we want all the books
        books = response.css("article.product_pod")
       

        for book in books :
            # here we collect the url of the particular book 
           rel_url = book.css("h3 a").attrib["href"]

           # now call the parse_book_page that goes to the book url and collect the all the useful fn 
           # by calling another fn
           yield response.follow(rel_url ,callback=self.parse_book_page )

        # to go to the nest page
        nxt_pg = response.css("li.next a").attrib['href'] 

        if nxt_pg is not None:   # there may be no next page
            yield response.follow(nxt_pg, callback=self.parse)


    def parse_book_page(self, response):
        # here we can access all the details about the book individually

        # now it collects all the details of table row (tr)
        tb_row = response.css("table tr")

        # Increment the count for each item
        # self.count += 1

        #
        book_item = BookItem()

        # this  fn helps in getting these infromation
        
        book_item["url"] = response.url ,
        book_item["title"]=response.css(".product_main h1::text").get(),
        book_item[ "category"] =response.xpath("/html/body/div/div/ul/li[3]/a/text()").get(),
        book_item["type"] =tb_row[1].css("td::text").get(),
        book_item["price"]=response.css("p.price_color::text").get(),
        book_item["stock"] =tb_row[5].css("td::text").get(),
        book_item["price_excl_tax"] =tb_row[2].css("td::text").get(),
        book_item["price_incl_tax"]=tb_row[3].css("td::text").get(),
        book_item["stars"] =response.css("p.star-rating").attrib['class'],
        book_item["description"] =response.xpath("/html/body/div/div/div[2]/div[2]/article/p/text()").get(),
        
        yield book_item
        




        



############################################################################################
########################################    PART 5
# import scrapy


# class BookspiderSpider(scrapy.Spider):

#     # name of spider we craeted
#     name = "bookspider"

#     # domain we select for scrap
#     allowed_domains = ["books.toscrape.com"]
#     #Actual URL
#     start_urls = ["https://books.toscrape.com"]

#     # this is  the function that exectues when the spider gets some response to procces 

#     count =0 
       
#     def parse(self, response):
#         # initially we want all the books
#         books = response.css("article.product_pod")
       

#         for book in books :
#             # here we collect the url of the particular book 
#            rel_url = book.css("h3 a").attrib["href"]

#            # now call the parse_book_page that goes to the book url and collect the all the useful fn 
#            # by calling another fn
#            yield response.follow(rel_url ,self.parse_book_page )

#         # to go to the nest page
#         nxt_pg = response.css("li.next a").attrib['href'] 

#         if nxt_pg is not None:   # there may be no next page
#             yield response.follow(nxt_pg, self.parse)


#     def parse_book_page(self, response):
#         # here we can access all the details about the book individually

#         # now it collects all the details of table row (tr)
#         tb_row = response.css("table tr")

#         # Increment the count for each item
#         self.count += 1

#         # this  fn helps in getting these infromation
#         yield{
#             "id" : self.count,
#             "url" : response.url ,
#             "title":response.css(".product_main h1::text").get(),
#             "category" : response.xpath("/html/body/div/div/ul/li[3]/a/text()").get(),
#             "type" : tb_row[1].css("td::text").get(),
#             "price":response.css("p.price_color::text").get(),
#             "stock":"In Stock" if "In stock" in tb_row[5].css("td::text") else "out",
#             "price_excl_tax" :tb_row[2].css("td::text").get(),
#             "price_incl_tax" :tb_row[3].css("td::text").get(),
#             "stars" :response.css("p.star-rating").attrib['class'],
#             "description" : response.xpath("/html/body/div/div/div[2]/div[2]/article/p/text()").get(),
#         }


        