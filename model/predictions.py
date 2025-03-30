# New data
new_data_dict = {
    'Adult_mortality': 263.6,
    'Alcohol_consumption': 3.0,
    'BMI': 23.8,
    'Diphtheria': 80.9,
    'Economy_status_Developed': 0.0,
    'Economy_status_Developing': 1.0,
    'GDP_per_capita': 2705,
    'Hepatitis_B': 81.5,
    'Incidents_HIV': 1.8,
    'Infant_deaths': 47.6,
    'Measles': 69.5,
    'Polio': 81.1,
    'Population_mln': 22.1,
    'Schooling': 5.3,
    'Thinness_five_nine_years': 6.6,
    'Thinness_ten_nineteen_years': 6.7,
    'Under_five_deaths': 68.8
}


# Extracting the model parameters.
theta0 = fit.stan_variable("theta_0")
theta1 = fit.stan_variable("theta_1")
theta2 = fit.stan_variable("theta_2")
theta3 = fit.stan_variable("theta_3")
theta4 = fit.stan_variable("theta_4")
sigma = fit.stan_variable("sigma")

# getting the new data.
infant_new = new_data_dict['Infant_deaths']
hiv_new = new_data_dict['Incidents_HIV']
gdp_new = new_data_dict['GDP_per_capita']
polio_new = new_data_dict['Polio']
mu = theta0 + theta1 * infant_new + theta2 * hiv_new + theta3 * gdp_new + theta4 * polio_new

# Prediction.
y_pred = np.array([
    np.random.normal(mean, std) for mean, std in zip(mu, sigma)
])

# Plotting the distribution of the prediction
fig, ax = plt.subplots(figsize=(8, 5))
sns.kdeplot(y_pred, fill=True, alpha=0.5, linewidth=2, ax=ax)
ax.set_xlabel("Predicted Y values", fontsize=10)
ax.set_ylabel("Density", fontsize=10)
ax.set_title("Posterior Predictive Distribution", fontsize=12, fontweight="bold")
ax.grid(True)
plt.show()
