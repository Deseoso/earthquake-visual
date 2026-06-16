from data_fetch import get_earthquakes
from visualization import draw_map
from processing import prepare_data
from data_fetch import get_time


def start_map():
    time_data = get_time()
    features = get_earthquakes(time_data)
    eq_data = prepare_data(features)

    draw_map(eq_data, time_data)

if __name__ == "__main__":
    start_map()



