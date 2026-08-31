def calculate_kpis(df):
    return {
        "On-Time Delivery Rate (%)": round(df.delivery_status.eq("On Time").mean()*100,2),
        "Average Delivery Time (hr)": round(df.delivery_time_hr.mean(),2),
        "Transportation Cost per Delivery": round(df.transport_cost.mean(),2),
        "Average Distance per Delivery (km)": round(df.distance_km.mean(),2),
        "Delivery Delay Rate (%)": round(df.delivery_status.eq("Delayed").mean()*100,2),
    }
