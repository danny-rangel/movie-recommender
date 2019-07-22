from collections import defaultdict
import csv

"""
    This function is used to parse the original data files and
    extract only the ratings that are higher than 3 and adding
    the movie id to the data for easier usage later on
"""


def transform_data(filename, output_filename):
    original_file = open(filename, "r")
    new_file = open(output_filename, "w")
    movie_id = None

    for line in original_file:
        if line.strip()[-1] == ":":
            movie_id = line.strip()[:-1]
        else:
            rating = line.split(",")[1]
            if int(rating) > 3:
                new_file.write(movie_id + "," + line)


"""
    This function is used to parse the transformed data and
    group the movies by the user id
"""


def group_movies_by_viewer(filename, output_filename):
    original_file = open(filename, "r")
    new_file = open(output_filename, "w")
    new_file_writer = csv.writer(new_file, delimiter=",")

    user_hash_table = defaultdict(list)

    for line in original_file:
        user_id = line.split(",")[1]
        movie_id = line.split(",")[0]
        user_hash_table[user_id].append(movie_id)

    for _, value in user_hash_table.items():
        new_string_list = []
        # new_string_list.append(key) removed because we don't care about user id?
        for movie in value:
            new_string_list.append(str(movie))

        new_file_writer.writerow(new_string_list)


def count_columns(filename):
    file = open(filename, "r")

    max = 0
    for line in file:
        length = len(line.split(","))
        if length > max:
            max = length

    return max
