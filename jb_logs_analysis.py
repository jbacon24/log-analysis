#!/usr/bin/env python3

import psycopg2
import csv

conn = psycopg2.connect("dbname=news")
pgcur = conn.cursor()

sql_articles = """
    select
        a.title,
        count(l.id)
    from articles a
    join log l on concat('/article/', a.slug) = l.path
    group by a.title
    order by 2 desc
    limit 3;"""
pgcur.execute(sql_articles)
article_results = pgcur.fetchall()
header = ("Articles_Sorted", "Views")

sql_authors = """
    select
        name,
        sum(views)
    from
        (select
            au.name,
            a.title,
            count(l.id) as views
        from articles a
        join log l on concat('/article/', a.slug) = l.path
        join authors au on au.id = a.author
        group by au.name, a.title) as a
    group by name
    order by 2 desc;"""
pgcur.execute(sql_authors)
authors_results = pgcur.fetchall()
header2 = ("Authors_Sorted", "Views")

sql_loaderrors = """
    select
        time,
        (error::decimal/total::decimal)*100 as percent
    from
        (select
            distinct time::date,
            count(*) filter (where status = '404 NOT FOUND') as error,
            count(*) as total
        from log group by 1) as a
        where ((error::decimal/total::decimal)*100) > 1.00;"""
pgcur.execute(sql_loaderrors)
loaderrors_results = pgcur.fetchall()
header3 = ("Date", "Percent")

with open('results.txt', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(header)
    for row in article_results:
        writer.writerow(row)
    writer.writerow([])
    writer.writerow(header2)
    for row in authors_results:
        writer.writerow(row)
    writer.writerow([])
    writer.writerow(header3)
    for row in loaderrors_results:
        writer.writerow(row)
    writer.writerow([])

conn.close()
