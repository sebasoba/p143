with open("links.csv", "a+") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_links = data[1:]

for item in all:
    poster_found = any(item[0] in link_items in all_movie_links)
    if poster_found:
        for ink_item in all_links:
            if link_item[0] in all_links[0]:
                movie_item.append(movie_link_item[1])