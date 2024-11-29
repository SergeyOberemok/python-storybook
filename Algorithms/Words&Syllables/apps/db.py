from utilities.databases import getData


def main():
    data = getData('select * from o2cxdb.o2cx_order')

    print(data)

if __name__ == '__main__':
    main()