from data_fetch import get_earthquakes
from visualization import draw_map
from processing import prepare_data

features = get_earthquakes()
eq_data = prepare_data(features)


if __name__ == "__main__":
    draw_map(eq_data)



