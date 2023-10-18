## to test
with open('/home/matt/eia_api_key.txt', 'r') as f:
  key = f.read().rstrip('\n')

AID = 'ELEC.GEN.ALL-AK-99.A'
getEIA(ID = AID, key = key)

QID = "ELEC.GEN.ALL-AK-99.Q"
getEIA(ID = QID, key = key)

MID = "ELEC.GEN.ALL-AK-99.M"
getEIA(ID = MID, key = key)

WID = "NG.RNGWHHD.W"
getEIA(ID = WID, key = key)

DID = "NG.RNGWHHD.D"
getEIA(ID = DID, key = key)

HID = "EBA.FMPP-ALL.D.H"
HID = "EBA.PACE-NWMT.ID.H"
getEIA(ID = HID, key = key)

HLID = "EBA.TVA-ALL.D.HL"
getEIA(ID = HLID, key = key)
