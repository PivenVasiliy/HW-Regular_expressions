import re
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    pattern1 = re.compile("(\+7|8)(\s?)(\(495\)|495)(\s|\-?)(\d{3})(\-?)(\d{2})(\-?)(\d{2})")
    pattern2 = re.compile("(\(?)(доб.)(\s)(\d{4})(\)?)")

    phone_list = []
    for contact in contacts_list:
        if len(contact[0].split()) == 3:
            contact[2] = (contact[0].split())[2]
            contact[1] = (contact[0].split())[1]
            contact[0] = (contact[0].split())[0]
        elif len(contact[0].split()) == 2:
            contact[1] = (contact[0].split())[1]
            contact[0] = (contact[0].split())[0]
        else:
            if len(contact[1].split()) == 2:
                contact[2] = (contact[1].split())[1]
                contact[1] = (contact[1].split())[0]
        phone_list.append(contact)
    i=1
    for abonent in phone_list:
        current_lastname = abonent[0]
        for abonent_1 in phone_list[i:len(phone_list)]:
            if current_lastname == abonent_1[0]:
                j=0
                for element_of_abonent_1 in abonent_1[0:7]:
                    if len(element_of_abonent_1) == 0:
                        abonent_1[j] = abonent[j]
                    j = j+1
                phone_list.remove(abonent)
        i = i+1

    result = pattern1.findall(str(phone_list))
    result2 = pattern2.findall(str(phone_list))
    final_string_1 = pattern1.sub(r'+7(495)\5-\7-\9',str(phone_list))
    final_string_2 = pattern2.sub(r'доб.\4',str(final_string_1))

    list_for_recording = final_string_2.split('[')
    for element in list_for_recording:
        print()

    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=' ')
        datawriter.writerows(list_for_recording)
