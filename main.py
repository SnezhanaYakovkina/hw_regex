import csv, re
from pprint import pprint


def create_new_list(old_list):
  new_list = {}

  for contact in old_list:
    pattern = re.compile("\s{2,}|\s{1,}$")
    contact[0:3] = re.sub(pattern, '', ' '.join(contact[0:3])).split(' ')
    # Приведём номера телефонов к единому формату:
    phone_pattern = re.compile(r"(\+7|8)?\s?\(?(\d{3})\)?[-\s]?(\d{3})[\-]?(\d\d)[\-]?(\d\d)")
    new_phone_pattern = r"+7(\2)\3-\4-\5"
    add_phone_pattern = re.compile(r"\(?(доб\.\s\d{4})\)?")
    new_add_phone_pattern = r"\1"
    contact[5] = re.sub(phone_pattern, new_phone_pattern, contact[5])
    contact[5] = re.sub(add_phone_pattern, new_add_phone_pattern, contact[5])

    name = contact[0] + contact[1]
    if name not in new_list:
      new_list[name] = contact
    else:
      for i, data in enumerate(contact):
        if data != '':
          new_list[name][i] = data

  return list(new_list.values())


if __name__ == '__main__':
  with open("phonebook_raw.csv", encoding="UTF-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    pprint(contacts_list)

  with open("phonebook.csv", "w", encoding="UTF-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(create_new_list(contacts_list))


