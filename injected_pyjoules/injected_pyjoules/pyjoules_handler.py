from pyJoules.energy_handler.energy_recorder.csv_handler import CSVHandler
import atexit

handler = CSVHandler('result.csv')
atexit.register(CSVHandler.save_data, handler)
