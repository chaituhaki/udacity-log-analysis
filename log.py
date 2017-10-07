# import psycopg2 to ccnnect to postgresql database
import psycopg2

# 1. What are the most popular three articles of all time?
query_One = '''select title, count as views
                from popular_view limit 3;'''

# 2. Who are the most popular article authors of all time?
query_Two = '''select name, sum(count) as views
              from popular_view group by name
              order by views desc;'''

# 3. On which days did more than 1% of requests lead to errors?
query_Three = "select * from error_view where error_percent>1;"

db_Name = "news"


# Execute the query by connecting to database
def execute_query(query):
    db = psycopg2.connect(database=db_Name)
    cur = db.cursor()
    cur.execute(query)
    # Saves the data that is fetched from database by cur.execute()
    result_Set = cur.fetchall()
    db.close()
    return result_Set

# print query 1 results
def article_query(result):
    for i in range(len(result)):
        title = result[i][0]
        view = result[i][1]
        print("%s---> %i views" % (title, view))

# print query 2 results
def author_query(result):
    for i in range(len(result)):
        title = result[i][0]
        view = result[i][1]
        print("%s---> %i views" % (title, view))

# print query 3 results
def error_query(result):
    for i in range(len(result)):
        title = result[i][0]
        view = result[i][1]
        print("%s---> %.2f errors" % (title, view))

if __name__ == "__main__":
    # calls execute_query method to execute the query
    result = execute_query(query_One)
    print("The 3 most popular articles of all time are:\n")
    # calls article_query method to execute the query
    article_query(result)
    print("\n")

    result = execute_query(query_Two)
    print("The list of popular authors of all time are:\n")
    author_query(result)
    print("\n")

    result = execute_query(query_Three)
    print("Days with more than 1% of request that lead to an error:\n")
    error_query(result)
