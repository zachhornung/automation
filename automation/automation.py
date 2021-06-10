import re

def remove_duplicates(arr, phone_numbers=False):
  filtered = []
  # seen_so_far = {}
  for i, item in enumerate(arr):
    add = True
    for j in range(i+1, len(arr)):
      if item == arr[j]:
        add = False
    if add:
      filtered.append(item)
    
  if phone_numbers:
    filtered = [re.sub('\W', '', item) for item in filtered]
    add_hyphen = [re.sub('(\d\d\d)(\d\d\d)(\d\d\d\d)', r'\1-\2-\3', item) for item in filtered]
    filtered = add_hyphen
  return filtered

def extract_baby_goats(path):
  with open(path) as f:
    data = f.read()
    
    email_pattern = re.compile('\S+@\S+')
    emails = re.findall(email_pattern, data)
    
    phone_pattern = re.compile('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})x?[0-9]*')
    phone_numbers = re.findall(phone_pattern, data)
  
  filtered_emails = remove_duplicates(emails)
  filtered_phone_numbers = remove_duplicates(phone_numbers, True)
  
  with open('automation/phone_numbers.txt', 'w') as f, open('automation/emails.txt', 'w') as g:
    for phone_number in filtered_phone_numbers:
      f.write(phone_number+'\n')
      
    for email in filtered_emails:
      g.write(email+'\n')
  

if __name__ == '__main__':
  extract_baby_goats('automation/assets/potential-contacts.txt')