import pandas as pd
from index import RetailPrices, Session

# Create a session and add data to the database
with Session() as db:
    data = pd.read_csv("data/retail_price.csv")
    for index, row in data.iterrows():
        retail_prices = RetailPrices(
           product_id = row.iloc[0],
        product_category_name = row.iloc[1],
        month_year = row.iloc[2],
        qty = row.iloc[3],
        total_price = row.iloc[4],
        freight_price = row.iloc[5],
        unit_price = row.iloc[6],
        product_name_length = row.iloc[7], 
        product_description_length = row.iloc[8], 
        product_photos_qty = row.iloc[9],
        product_weight_g = row.iloc[10],
        product_score = row.iloc[11],
        customers = row.iloc[12],
        weekday = row.iloc[13],
        weekend = row.iloc[14],
        holiday = row.iloc[15],
        month = row.iloc[16],
        year = row.iloc[17],
        s = row.iloc[18],
        volume = row.iloc[19],
        comp_1 = row.iloc[20],
        ps1 = row.iloc[21],
        fp1 = row.iloc[22],
        comp_2 = row.iloc[23],
        ps2 = row.iloc[24],
        fp2 = row.iloc[25],
        comp_3 = row.iloc[26],
        ps3 = row.iloc[27],
        fp3 = row.iloc[28],
        lag_price = row.iloc[29],
        )
        db.add(retail_prices)
        db.commit()  # Make sure to commit the transaction
