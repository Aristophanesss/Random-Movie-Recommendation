# This file contains the movie list
import random

result_movie = {
    "moviename": "",
    "movietype": "",
    "movieyear": 0,
    "movielanguage": ""
}
typeflag = ''
yearflag = ''
languageflag = ''
type = ''
year = ''
language = ''
setrandome = True
choose_movie = [
    {
        "moviename": "The Shawshank Redemption",
        "movietype": "Action",
        "movieyear": 1994,
        "movielanguage": "English"
    },
    {
        "moviename": "Forrest Gump",
        "movietype": "Comedy",
        "movieyear": 1994,
        "movielanguage": "English"
    }, {
        "moviename": "The Dark Knight",
        "movietype": "Superhero",
        "movieyear": 2008,
        "movielanguage": "English"
    }, {
        "moviename": "The Godfather",
        "movietype": "Drama",
        "movieyear": 1972,
        "movielanguage": "English"
    }, {
        "moviename": "12 Angry Men",
        "movietype": "Drama",
        "movieyear": 1957,
        "movielanguage": "English"
    },
]


def setflag(flag):
    global setrandome
    setrandome = flag


def set_param(t, tf, y, yf, l, lf):
    global type, typeflag, year, yearflag, language, languageflag
    type = t
    typeflag = tf
    year = y
    yearflag = yf
    language = l
    languageflag = lf


def get_randommovie():
    global result_movie
    number = random.randint(0, len(choose_movie) - 1)
    result_movie = choose_movie[number]
    return result_movie


def get_prefer():
    global result_movie, year, yearflag, typeflag, type, language, languageflag
    print(yearflag, year, type, typeflag, language, languageflag)
    temp_list = []
    if yearflag == "year":
        if year == "before":
            f_t = True
        else:
            f_t = False
        if typeflag == "type":
            if languageflag == "language":
                for item in choose_movie:
                    if f_t:
                        ff = item["movieyear"] < 2000
                    else:
                        ff = item["movieyear"] > 2000
                    if item["movietype"] == type and ff and item["movielanguage"] == language:
                        temp_list.append(item)
            else:
                for item in choose_movie:
                    if f_t:
                        ff = item["movieyear"] < 2000
                    else:
                        ff = item["movieyear"] > 2000
                    if item["movietype"] == type and ff:
                        temp_list.append(item)
        else:
            if languageflag == "language":
                for item in choose_movie:
                    if f_t:
                        ff = item["movieyear"] < 2000
                    else:
                        ff = item["movieyear"] > 2000
                    if ff and item["movielanguage"] == language:
                        temp_list.append(item)
            else:
                for item in choose_movie:
                    if f_t:
                        ff = item["movieyear"] < 2000
                    else:
                        ff = item["movieyear"] > 2000
                    if ff:
                        temp_list.append(item)
    else:
        if typeflag == "type":
            if languageflag == "language":
                for item in choose_movie:
                    if item["movietype"] == type and item["movielanguage"] == language:
                        temp_list.append(item)
            else:
                for item in choose_movie:
                    if item["movietype"] == type:
                        temp_list.append(item)
        else:
            print("====================")
            if languageflag == "language":
                for item in choose_movie:
                    if item["movielanguage"] == language:
                        temp_list.append(item)
            else:
                temp_list = choose_movie
    number = random.randint(0, len(temp_list) - 1)
    result_movie = temp_list[number]
    return result_movie
