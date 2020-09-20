Ebmin = 0
Ebmax = 100

PVmin = 0
PVmax = 1.111

Dmin = 2
Dmax = 340

n_bins = 10

c = 20
p = 15
learning_rate = 10e-1
eps = 0.5
discount_factor = 0.99
num_days = 365

initial_state = (PVmin, Ebmax, 2.5)
initial_action = 1 # (charging, discharging)

demand_csv_path = 'Data/demand.csv'
data_csv_path = 'Data/solar.csv'
final_csv_path = 'Data/final_csv.csv'

q_table_path = 'weights/power system agent q learning.npy'
cum_cost_path = 'weights/power_system_agent.png'
Egrid_path = 'weights/E grid effiency.png'
data_columns = ['Month','Day','Hour','PV_component','Demand']