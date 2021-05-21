import csv


def populateBankData(app, schema_editor):
    Bank = app.get_model('bank_app', 'Bank')
    with open('bank_app/db_script/data.csv') as bank_data:
        csv_reader = csv.reader(bank_data, delimiter=',')
        csv_reader.__next__()
        toCreateBankObjectList = []
        for row in csv_reader:
            toCreateBankObjectList.append(
                Bank(
                    ifsc=row[0],
                    bank_id=row[1],
                    branch=row[2],
                    address=row[3],
                    city=row[4],
                    district=row[5],
                    state=row[6],
                    bank_name=row[7]
                )
            )
        Bank.objects.bulk_create(toCreateBankObjectList)
