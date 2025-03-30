data {
    int<lower=0> N;             // Number of observations
    vector[N] x1;               // Infant Deaths
    vector[N] x2;               // HIV Incidence
    vector[N] x3;               // GDP per capita
    vector[N] x4;               // Polio Immunization
    vector[N] y;                // Life Expectancy
}

parameters {
    real theta_0;               // Intercept
    real theta_1;               // Coefficient for Infant Deaths
    real theta_2;               // Coefficient for HIV Incidence
    real theta_3;               // Coefficient for GDP per capita
    real theta_4;               // Coefficient for Polio Immunization
    real<lower=0> sigma;        // Standard deviation
}

transformed parameters {
    vector[N] mu;               // Expected life expectancy for each observation
    mu = theta_0 + theta_1 * x1 + theta_2 * x2 + theta_3 * x3 + theta_4 * x4;
}

model {
    // Priors
    theta_0 ~ normal(70, 10);   // Prior for intercept
    theta_1 ~ normal(0, 5);     // Prior for Infant Deaths effect
    theta_2 ~ normal(0, 5);     // Prior for HIV Incidence effect
    theta_3 ~ normal(0, 5);     // Prior for GDP per capita effect
    theta_4 ~ normal(0, 5);     // Prior for Polio effect
    sigma ~ cauchy(0, 2);       // Prior for standard deviation

    // Likelihood
    y ~ normal(mu, sigma);
}

generated quantities {
    vector[N] y_rep;            // Posterior predictive values
    for (i in 1:N) {
        y_rep[i] = normal_rng(mu[i], sigma);  // Simulated life expectancy values
    }
}
