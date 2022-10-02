import csv

with open('movies.csv') as f:
    r = csv.reader(f)
    data = list(r)
    all_movies = data[1:]
    headers = data[0]

headers.append("posters_link")
print(headers)

with open('final.csv','a+') as f:
    wr = csv.writer(f)
    wr.writerow(headers)

with open('movie_links.csv') as f:
    r = csv.reader(f)
    data = list(r)
    all_movie_links = data[1:]

print(len(all_movies))
print(len(all_movie_links))


for mitem in all_movies:
    poster_found = any(mitem[8] in m for m in all_movie_links)
    if poster_found:
        for m1 in all_movie_links:
            if mitem[8] == m1[0]:
                mitem.append(m1[1])
                if len(mitem) == 28:
                    with open('final.csv','a+') as f:
                        wr = csv.writer(f)
                        wr.writerow(mitem)
