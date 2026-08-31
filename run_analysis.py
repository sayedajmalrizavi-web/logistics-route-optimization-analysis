from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from data_cleaning import load_and_clean
from kpi_analysis import calculate_kpis
from regression_model import train_model
from clustering import cluster_routes
df=load_and_clean(ROOT/"data/logistics_data_synthetic.csv")
print("KPI RESULTS")
for k,v in calculate_kpis(df).items(): print(f"{k}: {v}")
_,metrics=train_model(df)
print("\nREGRESSION")
for k,v in metrics.items(): print(f"{k}: {v:.4f}")
print("\nCLUSTERS")
print(cluster_routes(df).route_cluster.value_counts().sort_index())
