# Choose data from 2008
data = df_2008.drop(columns = ['Economy_status_Developed', 'Economy_status_Developing',
                               'Region', 'Year', 'Country'])

# Loading the model.
model_fit = CmdStanModel(stan_file='maharavo_model.stan')

# Building the stan data.
infant = df_2008['Infant_deaths'].values
hiv = df_2008['Incidents_HIV'].values
gdp = df_2008['GDP_per_capita'].values
polio = df_2008['Polio'].values
stan_data = {
    'N': len(df_2008),
    'x1': infant,
    'x2': hiv,
    'x3': gdp,
    'x4': polio,
    'y': df_2008['Life_expectancy'].values
}

# Fitting the model to the data.
fit = model_fit.sample(
    data=stan_data,
    chains=4,
    iter_warmup=500,
    iter_sampling=1000,
    adapt_delta=0.95,
    seed=0)
