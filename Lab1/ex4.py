from matplotlib import pyplot

from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)

db = client.get_database()

post_connection = db["customers"]


# events = post_connection.find({"ref": "events"}).count()
events = post_connection.count_documents({"ref": "events"})
print(events)
# wom = post_connection.find({"ref": "wom"}).count()
wom = post_connection.count_documents({"ref": "wom"})
print(wom)
# ads = post_connection.find({"ref": "ads"}).count()
ads = post_connection.count_documents({"ref": "ads"})
print(ads)

ref_counts = [events, wom, ads]
ref_names = ["Events", "Wom", "Ads"]

pyplot.pie(ref_counts, labels=ref_names, autopct="%.1f%%",shadow = True, explode = [0, 0.1, 0])
pyplot.title("Percentage of references")
pyplot.axis("equal")

pyplot.show()
