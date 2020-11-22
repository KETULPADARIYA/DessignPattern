import matplotlib
import pandas as pd
from scipy.stats import pearsonr, ttest_rel
import seaborn as sns
import matplotlib.pyplot as plt

res = ['1', '25.65', '19.0146', '2', '17.52', '13.56', '3', '23.35', '18.128', '4', '19.23', '16.11', '5', '11.28',
       '8.94', '6', '18.69', '13.9338', '7', '10.66', '9.55']

existing_times = [float(i) for i in res[1::3]]
proposed_times = [float(i) for i in res[2::3]]


def get_data_frame(_a, _b):
    res = []
    n = 0
    for r, e in zip(_a, _b):
        res.append({
            "workstation_n": n,
            "standard time of existing process".replace(" ", "_"): r,
            "standard time of proposed process".replace(" ", "_"): e
        })
        n += 1

    return pd.DataFrame(res).set_index("workstation_n")


def print_in_required_format(a: str, b):
    if isinstance(b, int):
        print(f"{a:31}{b}")
    elif isinstance(b, float):
        print(f"{a:31}{b:.7f}")
    else:
        raise NotImplementedError


data_set = get_data_frame(existing_times, proposed_times)
print(data_set.describe())
person_coef = pearsonr(data_set["standard_time_of_existing_process"].values,
                       data_set["standard_time_of_proposed_process"].values)[0]
print_in_required_format('person correlation',person_coef)
print_in_required_format("degree of freedom",6)

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

matplotlib.rc('font', **font)

t_statistics = ttest_rel(existing_times,proposed_times)
print("\n \t----- paired t-test  ------")
print_in_required_format("p-value",t_statistics.pvalue)
print_in_required_format("statistic",t_statistics.statistic)

# print(data_set.corr())

plt.figure(figsize=(19,17))
data_set.plot(marker=".",figsize=(19,17),markersize=14)


plt.savefig("raj1.jpg")
plt.close()


plt.figure(figsize=(19,17))

data_set.boxplot()
plt.savefig("raj2.jpg")
