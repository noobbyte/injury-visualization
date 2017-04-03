import injuries

reports = injuries.get_reports = True

states = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

def getStateData(state):
    ans = {}
    for report in reports:
        if state = report['address']['state']:
            try:
                ans[report['address']['division']] += 1
            except:
                ans[report['address']['divison']] = 1
    return [{'label': key, 'count': ans[key]} for key in ans.keys()]