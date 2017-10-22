def gen_fake_database(database_manager):
    fake_data = [
    [2, 1, 2, 3],
    [3, 1, 2, 3],
    [4, 1, 2, 3],
    [5, 4, 5, 6],
    [6, 5, 6, 7],
    [7, 6, 7, 8],
    [8, 9, 10, 11],
    [9, 9, 11, 12],
    [10, 12, 13, 14],
    ]
    for f in fake_data:
        for i in range(3):
            data = {"uid":str(f[0]), "ac_url":str(f[i + 1])}
            database_manager.push(data)
