def parseEmail(file):
  nld = makeNameLookupDict()
  with open(file, "r") as f:
    lines = f.readlines()
    mid = lines[0][13:-3]
    date = lines[1][6:-2]
    fromEmail = lines[2][6:-2]
    try:
      fromName = nameLookup(fromEmail, nld)
    except:
      fromName = fromEmail
    toEmails = [n.replace("\n", "").replace("\r", "").replace(" ", "") for n in lines[3][3:].split(", ")]
    i = 4
    while lines[i][0] == '\t':
      potentials = [l.replace("\n", "").replace("\r", "").replace("\t", "") for l in lines[i].split(", ")]
      for p in potentials:
        if p != "":
	  toEmails.append(p)
      i += 1
    toNames = []
    for email in toEmails:
      try:
        name = nameLookup(email, nld)
      except:
        name = email
      toNames.append(name)
    subject = lines[i][8:-2]
    while lines[i][:4] != "X-Fi":
      i += 1
    while lines[i][:2] == "X-":
      i += 1
    i += 1
    endingsigs = ["----", "____", "****", "Original Message"]
    text = ""
    while i < len(lines) and all([e not in lines[i] for e in endingsigs]):
      text += lines[i]
      print i, len(lines), lines[i]
      i += 1
    print "Message id:", mid
    print "Date:", date
    print "From Email:", fromEmail
    print "fromName:", fromName
    print "To Emails:", toEmails
    print "To Names:", toNames
    print "Text:", text
    return(mid, date, fromEmail, fromName, toEmails, toNames, text)
 
NLFILE = "roles.txt"

def makeNameLookupDict(file=NLFILE):
  with open(file, "r") as f:
    lines = f.readlines()
  nld = {}
  for l in lines:
    try:
      spl = l.split()
      em = spl[0]+"@enron.com"
      nld[em] = {}
      nld[em]["name"] = spl[1] + " " + spl[2]
      nld[em]["job"] = spl[3]
    except:
      pass
  return nld

def nameLookup(email, nld = makeNameLookupDict(NLFILE)):
  return nld[email]["name"]
