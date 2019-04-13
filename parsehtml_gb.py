from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

df = pd.DataFrame()


for one_file_name in glob.glob("html_files/*.html"):
	print("parsing " + one_file_name)
	page_no = os.path.splitext(os.path.basename(one_file_name))[0].replace("boardgamegeek_page_no_","")
	f = open(one_file_name, "r")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()
	collection_table = soup.find("table", {"id": "collectionitems"})
	collection_tbody = collection_table.find("tbody")
	collection_rows = collection_tbody.find_all("tr", {"id": "row_"})
	for r in collection_rows:
		c_rank=r.find("td", {"class": "collection_rank"})
		if c_rank is None:
			continue
		else:
			c_rank2 = c_rank.find("a")
			if c_rank2 is None:
				continue
			else:
				collection_rank=c_rank2['name']

		collection_name = r.find("td", {"class": "collection_objectname"}).find("div", {"style": "z-index:1000;"}).find("a").text
		
		c_year=r.find("td", {"class": "collection_objectname"}).find("div", {"style": "z-index:1000;"}).find("span", {"class": "smallerfont dull"})
		if c_year is None:
			continue
		else:
			collection_year =c_year.text

		c_rating=r.find("td", {"class": "collection_bggrating"})
		if c_rating is None:
			continue
		else:
			collection_rating = c_rating.text 
			collection_avg_rating = c_rating.find_next_sibling("td", {"class": "collection_bggrating"}).text
			collection_num_voters = c_rating.find_next_sibling("td", {"class": "collection_bggrating"}).find_next_sibling("td", {"class": "collection_bggrating"}).text
		
		pr_list=r.find("td",{"class": "collection_shop"}).find("div", {"class": "aad"})
		if pr_list is None:
			continue
		else:
			collection_list_price = pr_list.next_element.next_element.next_element.next_element

		pr_all=r.find("td",{"class": "collection_shop"}).find("div", {"class": "aad"})
		if pr_all is None:
			continue
		else:
			collection_all_prices = pr_all.find_next("div").text

		pr_ios=r.find("td",{"class": "collection_shop"}).find_next("div")
		if pr_ios is None:
			continue
		else:
			collection_ios_prices = pr_ios.find_next("div").find_next("div").find_next("div").find_next("div").text

		#collection_ios_prices = r.find("td",{"class": "collection_shop"}).find_next("div").find_next("div").find_next("div").find_next("div").find_next("div").text
		df = df.append({
			'page_no': page_no,
			'rank': collection_rank,
			'name': collection_name,
			'year': collection_year,
			'rating': collection_rating,
			'avg_rating': collection_avg_rating,
			'num_voters':collection_num_voters,
			'list_price': collection_list_price,
			'all_prices':collection_all_prices,
			'ios_prices':collection_ios_prices,
			}, ignore_index=True)

df.to_csv("parsed_files/boardgamegeek_dataset.csv")

#Examine scraped data
print(df.info())
df.head(10)
