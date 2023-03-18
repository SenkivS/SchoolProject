
def qs2html(qs_list):
    s = '<table>'
    for record in qs_list:
        s += f'<tr><td>{record.name}</td><td>{record.surname}</td><td>{record.email}</td></tr>'
    s += '</table>'
    return s
