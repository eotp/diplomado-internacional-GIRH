def extract_timestep(ds):
    import re
    import datetime
    import numpy as np
    file_header = ds.attrs["FileHeader"]
    text = file_header.split(";")[5]
    match = re.search(r'\d{4}-\d{2}-\d{2}', text)
    date = datetime.datetime.strptime(match.group(), '%Y-%m-%d').date()
    return date