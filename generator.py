# Author: Espen Olsen
# Version 1.0
# For Atea Python-workshop

import os
import jinja2

TEMPLATE_FILENAME = 'kurstemplate.j2'
DATA_FILENAME = 'data.txt'

def get_data(row):

		# Henter data fra txt filen

	data_fields = {
		field_name: field_value
		for field_name, field_value in row.items()
	}

## ---------------------------------------------------------------------------
## Setter opp Jinja2 og henter template
## ---------------------------------------------------------------------------

env = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.getcwd()),
	trim_blocks=True, lstrip_blocks=True)

template = env.get_template(TEMPLATE_FILENAME)

## ---------------------------------------------------------------------------
## Leser CSV og fyller inn data for hver linje
## ---------------------------------------------------------------------------
