import unicodecsv as csv

author_dict = {}

with open("pol_accounts.csv") as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        # print(row.keys())
        author_dict[row["id"]] = (None, [row["screen_name"], row["description"]])


# id;"screen_name";"description";
# "created_at";"location";"is_verified";
# "latest_following_count";"latest_followers_count";
# "latest_status_count";"array_agg"
# None
