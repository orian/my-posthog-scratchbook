from clickhouse_connect import get_client

if __name__ == "__main__":
    print("Testing different clickhouse-connect query methods")
    print("Querying modes:")

    client = get_client(host="clickhouse", username="default", password="", database="default", secure=False,
                        verify=False)
    print("got client")

    queries = [
        {"q": "SELECT 1", "args": {}},
        {"q": "CREATE TABLE IF NOT EXISTS my_test_table(id int) ENGINE=MergeTree() PRIMARY KEY (id)", "args": {}},
        {"q": "INSERT INTO my_test_table(id) VALUES (1)", "args": {}},
        {"q": "DROP TABLE IF EXISTS my_test_table", "args": {}},
        {"q": "\nINSERT INTO person (id, created_at, team_id, properties, is_identified, _timestamp, _offset, is_deleted, version) SELECT '0194f9a3-3c0b-0000-7328-6a49ca570756', '2025-02-12 10:10:12.131347', 262, '{}', 0, '2025-02-12 10:10:12', 0, 0, 0\n", "args":{}},
    ]
    for query in queries:
        result = client.query(query=query["q"], parameters=query.get("args", None))
        print(result.summary)
