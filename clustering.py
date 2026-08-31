from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
def cluster_routes(df,n_clusters=3):
    cols=["distance_km","delivery_time_hr","transport_cost"]
    d=df[cols].dropna().copy()
    X=StandardScaler().fit_transform(d)
    d["route_cluster"]=KMeans(n_clusters=n_clusters,random_state=42,n_init=10).fit_predict(X)
    return d
