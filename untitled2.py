import glassdoor_scrapper as gs
import pandas as pd

path = "C:/Users/Rizky Rahman/Documents/data_science_project/ds_salary_project/chromedriver"

df = gs.get_jobs('data scientist', 15, False, path, 15)
