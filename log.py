# import psycopg2 to ccnnect to postgresql database
import psycopg2

# 1. What are the most popular three articles of all time?
query_One = '''select title, count as views
                from popular_view limit 3;'''

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

if __name__ == "__main__":
    # calls execute_query method to execute the query
    result = execute_query(query_One)
    print("The 3 most popular articles of all time are:\n")
    # calls article_query method to execute the query
    article_query(result)

