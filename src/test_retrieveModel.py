
import ModelStore
from analysis_model import analysis_model
from report_model import report_model
import ModelSelection

model = analysis_model("../../model/astrollama-3-8b-chat_summary.i1-Q4_K_M.gguf") 
role = "Data Analyst for Astronomy"
inputText = "how far is the closest star from earth"

model = ModelStore.ModelStore()

model.saveModel(model, role)

model_ret, role_ret = model.retrieveModel()

model_ret = ModelSelection.ModelSelection()
rsp = model_ret.response(inputText)

print(rsp["choices"][0]["message"]["content"])
#print(rsp["choices"]["content"])
