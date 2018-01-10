import web
import json
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from base import Session, engine, Base
from feature import Feature

urls = (
    '/index', 'index',
    '/requestSubmit','requestSubmit'
)
app = web.application(urls, globals(),autoreload=False)
render = web.template.render('templates/')
class index:
    def GET(self):
        return render.FeatureRequest()
class requestSubmit:
    def POST(self):
        # How to obtain the name key and then print the value?
        data = json.loads(web.data())
        #insertTable()
        print data[1]
        #new = Feature(data['title'], data['description'],data['client'],data['client_priority'],data['target_date'],data['product_area'])

  # value = data["name"]
        return "success"


    def insertTable():
    # generate database schema
        Base.metadata.create_all(engine)
    # create a new session
        session = Session()



if __name__ == "__main__":
    #app = web.application(urls, globals())
    app.run()
