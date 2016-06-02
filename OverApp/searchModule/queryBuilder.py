from OverApp import models
from django.template import RequestContext

def associateSentiment(webquery):
    splitArr=webquery.split(" ")
    processedArr=splitArr[splitArr.index("in"):]
    facilities=models.HotelInfo.objects.all().values('HotelServices')
    servArr=splitArr[splitArr.index("with"):]

    return processedArr,servArr
