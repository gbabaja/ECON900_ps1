from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

df = pd.DataFrame()

for one_file_name in glob.glob("html_files1/*.html"):
	print("parsing " + one_file_name)
	page_no = os.path.splitext(os.path.basename(one_file_name))[0].replace("boardgamegeek_page_no_","")
	f = open(one_file_name, "r")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()
	collection_table = soup.find("table", {"id": "collectionitems"})
	collection_tbody = collection_table.find("tbody")
	collection_rows = collection_tbody.find_all("tr", {"id": "row_"})
	for r in collection_rows:
		collection_rank = r.find("td", {"class": "collection_rank"}).find("a")['name']
		collection_name = r.find("td", {"class": "collection_objectname"}).find("div", {"style": "z-index:1000;"}).find("a").text
		collection_year = r.find("td", {"class": "collection_objectname"}).find("div", {"style": "z-index:1000;"}).find("span", {"class": "smallerfont dull"}).text
		collection_rating = r.find("td", {"class": "collection_bggrating"}).text 
		collection_avg_rating = r.find("td", {"class": "collection_bggrating"}).find_next_sibling("td", {"class": "collection_bggrating"}).text
		collection_num_voters = r.find("td", {"class": "collection_bggrating"}).find_next_sibling("td", {"class": "collection_bggrating"}).find_next_sibling("td", {"class": "collection_bggrating"}).text
		collection_list_price = r.find("td",{"class": "collection_shop"}).find("div", {"class": "aad"}).next_element.next_element.next_element.next_element
		collection_lowest_amazon_price=r.find("td",{"class": "collection_shop"}).find("div", {"class": "aad"}).findnext("div").select("div:nth-of-type(1)").select("div:nth-of-type(2)").find("a", {"class": "ulprice"}).find("span", {"class": "positive"}).text
		#find("div", recursive=False).select('div > div')[0].get_text(strip=True)
		#collection_lowest_amazon_price=r.find("td",{"class": "collection_shop"}).find("div", {"class": "aad"}).next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
		collection_new_amazon_price=r.find("td",{"class": "collection_shop"}).find("div", {"class": "aad"}).next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
		df = df.append({
			'page_no': page_no,
			'rank': collection_rank,
			'name': collection_name,
			'year': collection_year,
			'rating': collection_rating,
			'avg_rating': collection_avg_rating,
			'num_voters':collection_num_voters,
			'list_price': collection_list_price,
			'lowest_amazon_price': collection_lowest_amazon_price,
			'new_amazon_price':collection_lowest_amazon_price,
			}, ignore_index=True)

df.to_csv("parsed_files/boardgamegeek_dataset.csv")
