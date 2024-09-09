from index import RetailPriceProcessed, RetailPrices, Session

with Session() as db:
    result = db.query(RetailPriceProcessed).all()
    for row in result:
        print(row.total_price)