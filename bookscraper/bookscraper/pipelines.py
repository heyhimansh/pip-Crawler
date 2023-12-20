# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


#pipelines are basically used to modify the data ,clean the data in order to get the only useful information form it
# very usefull information 



class BookscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # strip all the whitespace 
        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name != 'description' :

                value = adapter.get(field_name)
                adapter[field_name] = value[0].strip()


        # categrory and product type conbert all in Lowercase letters
        cats = ['category' ,'type']
        for cat in cats :
            value =  adapter.get(cat)
            adapter[cat] = value.lower()

            # vlaue = adapter.get(cat).lower()
            # adapter.set(cat,vlaue)
        
        

        
        #Availability ::  to check the availabilty of product is available print the number
        available_str = adapter.get('stock')
        #In stock (10 available) given formate 
        split_arr = available_str.split('(')
        if len(split_arr) <2 :
            adapter['stock'] = 0
        else:
            available_arr = split_arr[1].split(' ')
            adapter['stock'] = int(available_arr[0])
            #In stock (10 available) given formate
        

        ##  Count number stars
        # "star-rating Two" 
        rating_str = adapter.get("stars")
        rat_arr = rating_str.split(' ')
        star_txt =  rat_arr[1].lower()
        if star_txt == "zero":
            adapter["stars"]=0
        elif star_txt == "one":
            adapter["stars"] =1 
        elif star_txt == "two":
            adapter["stars"] =2 
        elif star_txt == "three":
            adapter["stars"] =3 
        elif star_txt == "four":
            adapter["stars"] =4 
        elif star_txt == "five":
            adapter["stars"] = 5
        

        return item

