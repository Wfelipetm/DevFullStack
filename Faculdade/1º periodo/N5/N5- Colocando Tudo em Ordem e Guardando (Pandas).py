from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd
from faker import Faker
from num2words import num2words
from wordcloud import WordCloud

fake = Faker('pt_BR')
Faker.seed(0)


def Name_Ponts(num):
    time_list = [fake.color_name() for x in range(4)]
    fake_news = [{'Name': fake.name(), 'Pontos': fake.pyint(1, 100), }
                 for x in range(num)]
    return fake_news


faker_News = pd.DataFrame(Name_Ponts(num=10))

faker_News.to_csv('workers.csv')
faker_News['Pontos'] = faker_News['Pontos'].apply(
    lambda x: str(x).replace(",", "."))
faker_News['Pontos'] = faker_News['Pontos'].astype('float64')
faker_News['Pontos']
faker_News.hist(column='Pontos', bins=10)
plt.show()

faker_News.to_csv('workers.csv')
nuvem = faker_News['Pontos'] = faker_News['Pontos'].apply(num2words, lang='pt')
word_could_dict = Counter(nuvem)
wordcloud = WordCloud(
    width=1000, height=500).generate_from_frequencies(word_could_dict)

plt.figure(figsize=(5, 5))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
plt.savefig('yourfile.png', bbox_inches='tight')
plt.close()
