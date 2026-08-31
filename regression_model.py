from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
def train_model(df):
    cols=["distance_km","package_weight_kg","number_of_stops"]
    d=df.dropna(subset=cols+["delivery_time_hr"])
    Xtr,Xte,ytr,yte=train_test_split(d[cols],d.delivery_time_hr,test_size=.2,random_state=42)
    model=LinearRegression().fit(Xtr,ytr)
    pred=model.predict(Xte)
    return model, {"MAE":mean_absolute_error(yte,pred),"RMSE":mean_squared_error(yte,pred)**.5,"R2":r2_score(yte,pred)}
