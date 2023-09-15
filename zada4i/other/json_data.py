import json


def main():
    with open('data.json', 'r') as file:
        neighbors = json.load(file)
        if neighbors:
            neighbors.sort(key=lambda x: x['count'])
            min_value = neighbors[0]['count']
            print(*list(map(lambda dic: dic['date'], filter(lambda dic: dic['count'] == min_value, neighbors))),
                  sep='\n')
        else:
            print()


if __name__ == '__main__':
    main()
