from vetiver import VetiverModel
import vetiver
import pins


b = pins.board_folder('/var/folders/5w/dhznpltj14n3nxr4fybjj8_w0000gn/T/tmpup4ovlqy', allow_pickle_read=True)
v = VetiverModel.from_pin(b, 'cars', version = '20230216T141014Z-4db39')

vetiver_api = vetiver.VetiverAPI(v)
api = vetiver_api.app
