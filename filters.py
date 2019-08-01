def getTimeSignature(track):
  return track.get('time_signature')

def getTempo(track):
  return track.get('tempo')

def waltzFilter(track):
  if(not track):
   return False
  timeSignature = getTimeSignature(track)
  tempo = getTempo(track) # Recommended 84-96 BPM

  return timeSignature == 3 and tempo > 80 and tempo < 120

def rumbaFilter(track):
  if (not track):
    return False
  timeSignature = getTimeSignature(track)
  tempo = getTempo(track) # Recommended 120-144 BPM

  return timeSignature == 4 and tempo > 110 and tempo < 144

def chaChaFilter(track):
  if(not track):
    return False

  timeSignature = getTimeSignature(track)
  tempo = getTempo(track) # Recommended 112-128 BPM
  return timeSignature == 4 and tempo > 110 and tempo < 130

def salsaFilter(track):
  if(not track):
    return False

  timeSignature = getTimeSignature(track)
  tempo = getTempo(track) # Recommended 150-250 BPM 
  return timeSignature == 4 and tempo > 150 and tempo < 250