    @time
    @memory 
    def load():
        df = load.completed_orders()
        df = load.transform_price(df)
        df = load.transform_dates(df)
        df = load.create_sales(df)
        load.create_table(df)

