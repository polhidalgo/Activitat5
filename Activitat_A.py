import pandas as pd
import matplotlib.pyplot as plt


file_path = 'df_covid19_countries.csv'
df = pd.read_csv(file_path)

selected_countries = df['location'].unique()[:10]
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df_2021 = df[(df['year'] == 2021) & (df['location'].isin(selected_countries))]

def casos_totals_per_mes(df):
    casos_per_mes = df.groupby(['location', 'month'])['total_cases'].max().unstack()
    print("Casos totals per mes per país (2021):")
    print(casos_per_mes)
    return casos_per_mes

def morts_totals_per_mes(df):
    morts_per_mes = df.groupby(['location', 'month'])['total_deaths'].max().unstack()
    print("Morts totals per mes per país (2021):")
    print(morts_per_mes)
    return morts_per_mes

def taxa_reproduccio_per_mes(df):
    reproduccio_per_mes = df.groupby(['location', 'month'])['reproduction_rate'].mean().unstack()
    print("Taxa de reproducció per mes per país (2021):")
    print(reproduccio_per_mes)
    return reproduccio_per_mes

def main():
    casos_per_mes = casos_totals_per_mes(df_2021)
    morts_per_mes = morts_totals_per_mes(df_2021)
    reproduccio_per_mes = taxa_reproduccio_per_mes(df_2021)

    plt.figure(figsize=(12, 6))
    for country in casos_per_mes.index:
        plt.plot(casos_per_mes.columns, casos_per_mes.loc[country], label=country)
    plt.title("Casos totals per mes per país (2021)")
    plt.xlabel("Mes")
    plt.ylabel("Casos Totals")
    plt.legend()
    plt.show()

    plt.figure(figsize=(12, 6))
    for country in morts_per_mes.index:
        plt.plot(morts_per_mes.columns, morts_per_mes.loc[country], label=country)
    plt.title("Morts totals per mes per país (2021)")
    plt.xlabel("Mes")
    plt.ylabel("Morts Totals")
    plt.legend()
    plt.show()

    plt.figure(figsize=(12, 6))
    for country in reproduccio_per_mes.index:
        plt.plot(reproduccio_per_mes.columns, reproduccio_per_mes.loc[country], label=country)
    plt.title("Taxa de reproducció per mes per país (2021)")
    plt.xlabel("Mes")
    plt.ylabel("Taxa de Reproducció")
    plt.legend()
    plt.show()
main()
