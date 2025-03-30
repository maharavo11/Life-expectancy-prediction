# Loading the data.
africa = pd.read_csv('https://raw.githubusercontent.com/MLGlobalHealth/StatML4PopHealth/refs/heads/main/data/africa_who_life_expectancy.csv')

# Data visualization.
# List and sort regions for consistent order
regions = sorted(africa['Region'].unique())

fig, axes = plt.subplots(nrows=1, ncols=len(regions), figsize=(20, 5), sharey=True)
fig.tight_layout(pad=4.0)

# Iterate through regions
for idx, reg in enumerate(regions):
    ax = axes[idx]
    region_df = africa[africa['Region'] == reg]
    countries = sorted(region_df['Country'].unique())

    # Plot each country's data
    for i, country in enumerate(countries):
        country_df = region_df[region_df['Country'] == country]
        colors = sns.color_palette("tab20", len(africa['Country'].unique()))
        ax.scatter(country_df['Year'], country_df['Life_expectancy'],
                   marker='.', label=country, color=colors[i % len(colors)])

    # Formatting
    ax.set_title(reg, fontsize=12, fontweight='bold')
    ax.set_xlabel('Year', fontsize=10)
    if idx == 0:
        ax.set_ylabel('Life Expectancy', fontsize=10)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.25), ncol=2, fontsize=8, frameon=False)
plt.subplots_adjust(bottom=0.2)
plt.show()
