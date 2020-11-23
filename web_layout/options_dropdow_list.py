options = [
    {"label": 'Country', "value": 'Country'},
    {"label": 'State', "value": 'State'},
    {"label": 'Work Active', "value": 'WorkActive'},
    {"label": 'Job Title', "value": 'JobTitle'},
    {"label": 'Gender', "value": 'gender'}
]


def select_options(country=True, state=True, work_active=True, job_title=True, gender=True):
    opt = []
    if country:
        opt.append({"label": 'Country', "value": 'Country'})
    if state:
        opt.append({"label": 'State', "value": 'State'})
    if work_active:
        opt.append({"label": 'Work Active', "value": 'WorkActive'})
    if job_title:
        opt.append({"label": 'Job Title', "value": 'JobTitle'})
    if gender:
        opt.append({"label": 'Gender', "value": 'gender'})

    if opt == [] or opt is None or len(opt) <= 0:
        return options

    return opt
