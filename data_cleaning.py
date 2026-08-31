import pandas as pd
def load_and_clean(path):
    df=pd.read_csv(path).drop_duplicates().copy()
    df["package_weight_kg"]=df["package_weight_kg"].fillna(df["package_weight_kg"].median())
    df["traffic_level"]=df["traffic_level"].fillna(df["traffic_level"].mode()[0])
    df["delivery_delay_hr"]=(df["delivery_time_hr"]-df["expected_time_hr"]).round(2)
    df["cost_per_km"]=df["transport_cost"]/df["distance_km"]
    return df
