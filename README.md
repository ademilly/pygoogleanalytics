## PyGoogleAnalytics

Wrapper for Google Analytics API python calls

### Setup

First and foremost you need a google analytics api service account.
Details are available here see https://developers.google.com/analytics/devguides/reporting/core/v4/ for more details
Instructions are available here https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py

```
    $ pip install git+ssh://git@github.com/ademilly/pygoogleanalytics.git
```

### Usage

```python
import pygoogleanalytics

# Inputs for standard google analytics reporting api
api = pygoogleanalytics.APICaller(
    ['https://www.googleapis.com/auth/analytics.readonly'],
    ('https://analyticsreporting.googleapis.com/$discovery/rest'),
    PATH_TO_P12_SECRET_FILE,
    SERVICE_ACCOUNT_ADDRESS
)

# prepare a dimensionFilterClauses with a 'and' operator
request_filter = pygoogleanalytics.RequestFilter('and').add_filter(
    {
        "dimensionName": "some_dimension",
        "operator": "some_operation",
        "expressions": "some_expression"
    }
).add_filter(
    {
        "dimensionName": "some_dimension",
        "operator": "some_operation",
        "expressions": "some_expression"
    }
)

some_kpi = pygoogleanalytics.Requester(api).build_request().for_view(
    'some_view_id'
).between(
    'some_start_date', 'some_end_date'
).for_variables(
    ['var1', 'var2', ...]
).with_filter_clause(request_filter).run_request().get_value('metrics')

print some_kpi
```

output:
```
    ['some_value', ...]
```
