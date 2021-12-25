import re
import plotly.graph_objects as go


def create_directory():
    d = {}

    for line in file:
        line_refactor = re.sub("[^a-zA-Z0-9:,]", "", line)
        if "YEAR" in line_refactor:
            year = line_refactor.split(":")[1]
            d[year] = {}
        elif "WEEK" in line_refactor:
            week = line_refactor.split(":")[1]
            d[year][week] = {}
        elif "DAY" in line_refactor:
            day = line_refactor.split(":")[1]
            d[year][week][day] = []
        else:
            d[year][week][day].append(line_refactor)
    return d


def global_products_most_purchased(d):
    products_purchased = {}

    for year in d:
        for week in d[year]:
            for day in d[year][week]:
                for products in d[year][week][day]:
                    for item in products.split(","):
                        if item in products_purchased:
                            products_purchased[item] += 1
                        else:
                            products_purchased[item] = 1
    create_list(products_purchased)


def clients_per_year(d):
    clients = {}

    for year in d:
        for week in d[year]:
            for day in d[year][week]:
                for products in d[year][week][day]:
                    if year in clients:
                        clients[year] += 1
                    else:
                        clients[year] = 1
    create_list(clients)


def create_list(d):
    axe_x = []
    axe_y = []
    for items in d:
        axe_y.append(d[items])
        axe_x.append(items)

    if "p" in axe_x:
        sort_bubble(axe_x, axe_y)
    else:
        create_chart(axe_x, axe_y)


def create_chart(axe_x, axe_y):
    fig = go.Figure([go.Bar(x=axe_x, y=axe_y)])
    fig.show()


def sort_bubble(list_1, list_2):
    length = len(list_1)
    for i in range(length):
        for j in range(0, length - i - 1):
            if int(list_1[j].split("p")[1]) > int(list_1[j + 1].split("p")[1]):
                list_1[j], list_1[j + 1] = list_1[j + 1], list_1[j]
                list_2[j], list_2[j + 1] = list_2[j + 1], list_2[j]

    create_chart(list_1, list_2)


file = open("transact_log.txt", "r")

directory = create_directory()
global_products_most_purchased(directory)
clients_per_year(directory)

test = ["p95"]
