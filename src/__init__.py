import pandas as pd
import numpy as np
from cmdstanpy import CmdStanModel
import arviz as az

# Plotting
import matplotlib.pyplot as plt
import seaborn as sns

# Installing packages for stan.
!curl -O "https://raw.githubusercontent.com/MLGlobalHealth/StatML4PopHealth/main/practicals/resources/scripts/utilities.py"

from utilities import custom_install_cmdstan, test_cmdstan_installation

custom_install_cmdstan()
