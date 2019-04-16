import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn import svm
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder #to normalize the data to reduce possible bias
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn import metrics
import numpy as np

#load data using pandas:
df = pd.read_csv("final_dataset_gb.csv") #var. names: name rating avg_rating year rank page_no num_voters list_price ios_prices all_prices
print(df.head(10)) #print first 10 rows of the dataframe
print(df.info()) #this will print information about the dataset and variables
print(df.describe(include=[np.number])) #to describe numberic columns

#variables I will use for machine learning exercise: #X=rank, avg_rating,num_voters and y=rating
bins=(2, 6.5, 10)  #we are creating 2 categories (bad or good for example) and the cutoff point for a good game is 6.5.
group_names=['bad', 'good']
df['rating']=pd.cut(df['rating'], bins=bins, labels=group_names)
print(df['rating'].unique()) #this will show you the newly created categories, i.e. bad vs good

label_ratings=LabelEncoder()
df['rating'] = label_ratings.fit_transform(df['rating'])
print(df.head(10)) #to see what transformation happened to the data
print(df['rating'].value_counts()) #to see how many "bad games" and "good games" there are
plot=sns.countplot(df['rating'])
plt.savefig('myfig.png')


#define the dependent and independent variables
X=df[['avg_rating','rank','num_voters']]
y=df['rating']

#split data into train and test parts
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#normalize independent variables to reduce possibility of bias due to magnitude differences
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

print(X_train[:10]) #to see the changes

#Now, we will use SVM classifier to try to predict "good" and "bad" games given characteristics
clf=svm.SVC()
clf.fit(X_train, y_train)
pred_clf=clf.predict(X_test) #to see how well the model is performing by comparing test values vs. predictions

print(classification_report(y_test, pred_clf))
print(confusion_matrix(y_test, pred_clf))    #based on the results, this model predicts "bad" games much better than it can predict "good" games.


#finally, let's test if 2 clusters make sense
for i in range(5):
	n = i + 2
	kmeans_predictions = KMeans(n_clusters=n).fit_predict(df[['rating','avg_rating','rank','num_voters']])
	print("kmean "  + str(n) + " clusters")
	print(metrics.silhouette_score(df[['rating','avg_rating','rank','num_voters']], kmeans_predictions))

for i in range(5):
	n = i + 2
	gaussian_predictions = GaussianMixture(n_components=n).fit(df[['rating','avg_rating','rank','num_voters']]).predict(df[['rating','avg_rating','rank','num_voters']])
	print("gaussian "  + str(n) + " components")
	print(metrics.silhouette_score(df[['rating','avg_rating','rank','num_voters']], gaussian_predictions))


