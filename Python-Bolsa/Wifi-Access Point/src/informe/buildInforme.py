from pyexcel_ods import get_data
from pyexcel_ods import save_data
from io import StringIO

data = get_data("Informe.ods")
import json
print(json.dumps(data))
data.update({"Sheet1": [[1, 1], [2, 20], [3, 100], [4, 4], [5, 1]]})
save_data("Informe.ods", data)
