def QueryResult(ConnectionString:str, Query:str, Flag:str, Params: tuple[str] | None = None):
    try:
        Cursor = ConnectionString.cursor(dictionary=True)
    except:
        return False
    try:
        match Flag:
            case 'single':
                if Params is None:
                    Cursor.execute(Query)
                else:
                    Cursor.execute(Query, Params)
                Single = Cursor.fetchone()
                return Single
            case 'multiple':
                if Params is None:
                    Cursor.execute(Query)
                else:
                    Cursor.execute(Query, Params)
                Multiple = Cursor.fetchall()
                return Multiple
            case 'create':
                Cursor.execute(Query, Params)
                Cursor.commit()
    except:
        return False
