import json
import Connectors
import Transformations
import AutoML
try:
    BostonHousingPriceRegression_DBFS = Connectors.DBFSConnector.fetch(
        [], {}, "5e8ee970a8429fe1b520ce68", spark, "{'url': '/Demo/BostonTrain.csv', 'file_type': 'Delimeted', 'dbfs_token': 'dapib3c8e0614707f7e6d2addea6ce7c33d0', 'dbfs_domain': 'westus.azuredatabricks.net', 'delimiter': ',', 'is_header': 'Use Header Line'}")

except Exception as ex:
    print(ex)
try:
    BostonHousingPriceRegression_AutoFE = Transformations.TransformationMain.run(["5e8ee970a8429fe1b520ce68"], {"5e8ee970a8429fe1b520ce68": BostonHousingPriceRegression_DBFS}, "5e8ee970a8429fe1b520ce69", spark, json.dumps({"FE": [{"transformationsData": {}, "feature": "CRIM", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "298", "mean": "3.39", "stddev": "8.74", "min": "0.00906", "max": "88.9762", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "ZN", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "298", "mean": "11.38", "stddev": "23.01", "min": "0.0", "max": "100.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "INDUS", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "298", "mean": "10.76", "stddev": "6.75", "min": "0.46", "max": "27.74", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "CHAS", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "298", "mean": "0.07", "stddev": "0.26", "min": "0.0", "max": "1.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "NOX", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "298", "mean": "0.55", "stddev": "0.12", "min": "0.385", "max": "0.871", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "RM", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "298", "mean": "6.28", "stddev": "0.7", "min": "3.561", "max": "8.725", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "AGE", "type": "real", "selected": "True", "replaceby": "mean", "stats": {
                                                                                 "count": "298", "mean": "68.2", "stddev": "28.55", "min": "2.9", "max": "100.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "DIS", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "298", "mean": "3.92", "stddev": "2.21", "min": "1.1691", "max": "12.1265", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "RAD", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "298", "mean": "9.17", "stddev": "8.51", "min": "1.0", "max": "24.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "TAX", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "298", "mean": "405.33", "stddev": "164.74", "min": "187.0", "max": "711.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "PTRATIO", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "298", "mean": "18.29", "stddev": "2.21", "min": "12.6", "max": "22.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "B", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "298", "mean": "355.86", "stddev": "92.47", "min": "0.32", "max": "396.9", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "LSTAT", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "298", "mean": "12.53", "stddev": "7.2", "min": "1.92", "max": "34.77", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "MEDV", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "298", "mean": "22.77", "stddev": "9.4", "min": "5.0", "max": "50.0", "missing": "0"}, "transformation": ""}]}))

except Exception as ex:
    print(ex)
try:
    AutoML.functionRegression(BostonHousingPriceRegression_AutoFE, [
                              "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"], "MEDV")

except Exception as ex:
    print(ex)
