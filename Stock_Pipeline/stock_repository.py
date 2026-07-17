from database import get_connection

def upsert_stock(name, category, quantity):
    
    with get_connection() as conn:
        if conn is None:
            return False
        
        with conn.cursor() as cursor:
           sql = """
                INSERT INTO stock(name,category,quantity)
                VALUES(%s,%s,%s)
                ON DUPLICATE KEY UPDATE
                    quantity=quantity+VALUES(quantity)
        """
           cursor.execute(sql, (name, category, quantity))
           conn.commit()

           return True
        
def get_all_stock():
    with get_connection() as conn:
        if conn is None:
            return []
        
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT name,category,quantity FROM stock ORDER BY name")
            results=cursor.fetchall()

            return results
        


