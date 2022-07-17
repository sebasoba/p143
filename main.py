header.append("poster_lint")

with open("final.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)

npm i react-native-elements@1.2.7