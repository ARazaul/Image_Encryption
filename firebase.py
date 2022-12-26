import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

data={"name":"rajaul","age":22,"sex":"male"}
# Adddata
# ===================================================
# db.collection("INFO").add(data)
# db.collection("INFO2").document("Students").set(data)
# db.collection("INFO3").document().set(data)
# db.collection("INFO2").document("Students").set({"address":"KTM"},merge=True)
# db.collection("INFO2").document("Students").collection("child").document().set(data)

# ==========================================================

# ReadData
# ==============================================================
# r=db.collection("INFO2").document("Students").get()
# if r.exists:
#   print(r.to_dict())
# else:
#   print("no exists")

# =================================================================
# read alll docs
# docs=db.collection("INFO3").get()

# for i in docs:
#   print(i.to_dict())

# ====================================================================

# Quaring
# read alll docs
# docs=db.collection("INFO3").where("age","<",45).get()
# for i in docs:
#   print(i.to_dict())

# ======================================================================
# Update Data
# db.collection("INFO3").document("xhzciAr3zPRN96etLQNB").update({"hero":"anamol","age":21})
# db.collection("INFO3").document("xhzciAr3zPRN96etLQNB").update({"name":"anamol","age":21})
# db.collection("INFO3").document("xhzciAr3zPRN96etLQNB").update({"age":firestore.Increment(3)})
# =========================================================================
# Delete Data
# ==========================================================================
# db.collection("INFO4").document("Tess1").delete()
# db.collection("INFO3").document("xhzciAr3zPRN96etLQNB").update({"hero":firestore.DELETE_FIELD})
