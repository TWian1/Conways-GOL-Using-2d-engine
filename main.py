#Dont touch
from engine.engine import ps, general, inpt, pixel, time, settings
import time
general.start()
# Type Code Here ↓↓↓↓↓


def Main():
  width = 30
  height = 30
  settings.screensize(width, height) #screen size


  setup(width, height)
  rungen(width, height)




def setup(width, height):
  x = 0
  y = 0
  onbefore = False
  if pixel.data.p(x, y) == "255 255 255":
    onbefore = True
  if onbefore:
    pixel.color(x, y, "255 0 0")
  else:
    pixel.color(x, y, "255 255 255")
  general.clearscreen()
  general.printbrd()
  place = False
  while True:
    print("wasd to move")
    print("press e to place")
    print("type done once you're done")
    print("after each command press enter.")
    k = inpt.text(">>> ")
    if k == "d" and x < width:
      if onbefore == False:
        pixel.color(x, y, "0 0 0")
      else:
        pixel.color(x, y, "255 255 255")
      x += 1
      if pixel.data.p(x, y) == "255 255 255":
        onbefore = True
      else:
        onbefore = False
      if onbefore:
        pixel.color(x, y, "255 0 0")
      else:
        pixel.color(x, y, "255 255 255")
      place = False
      general.clearscreen()
      general.printbrd()
    if k == "a" and x > 0:
      if onbefore == False:
        pixel.color(x, y, "0 0 0")
      else:
        pixel.color(x, y, "255 255 255")
      x -= 1
      if pixel.data.p(x, y) == "255 255 255":
        onbefore = True
      else:
        onbefore = False
      if onbefore:
        pixel.color(x, y, "255 0 0")
      else:
        pixel.color(x, y, "255 255 255")
      place = False
      general.clearscreen()
      general.printbrd()
    if k == "w" and y > 0:
      if onbefore == False:
        pixel.color(x, y, "0 0 0")
      else:
        pixel.color(x, y, "255 255 255")
      y -= 1
      if pixel.data.p(x, y) == "255 255 255":
        onbefore = True
      else:
        onbefore = False
      if onbefore:
        pixel.color(x, y, "255 0 0")
      else:
        pixel.color(x, y, "255 255 255")
      place = False
      general.clearscreen()
      general.printbrd()
    if k == "s" and y < height:
      if onbefore == False:
        pixel.color(x, y, "0 0 0")
      else:
        pixel.color(x, y, "255 255 255")
      y += 1
      if pixel.data.p(x, y) == "255 255 255":
        onbefore = True
      else:
        onbefore = False
      if onbefore:
        pixel.color(x, y, "255 0 0")
      else:
        pixel.color(x, y, "255 255 255")
      place = False
      general.clearscreen()
      general.printbrd()
    if k == "e":
      pixel.color(x, y, "255 0 0")
      place = True
      onbefore = True
      general.clearscreen()
      general.printbrd()
    if k == "done":
      if place == False and onbefore == False:
        pixel.color(x, y, "0 0 0")
      else:
        pixel.color(x, y, "255 255 255")
      return




def rungen(width, height, length = 999999999999999999999999999):
  livedcoords = []
  deadbound = []
  timedif = 0
  foundlive = False


  for i in range(length):
    general.clearscreen()
    general.printbrd()
    print("Surface Area: " + str(len(livedcoords)))
    print("Space Calculated: " + str(len(livedcoords) * 8))
    print("Last Generation Time: " + str(timedif))





    time1 = time.time()
    livedcoords = []
    x = -1
    y = 0
    if not(foundlive):
      for a in pixel.data.a():
        x += 1
        if x == width:
          y+=1
          x = 0
        if x == width - 1 or x == 0 or y == height - 1 or y == 0:
          continue
        if a == "255 255 255":
          livedcoords.append([x, y])
      livecoords = livedcoords



    livedcoords = livecoords
    deadbound = []


    for b in livedcoords:
      for a1 in range(3):
        for a2 in range(3):
          if a2 - 1 == 0 and a1 - 1 == 0:
            continue
          if pixel.data.p(b[0] + a1 - 1, b[1] + a2 - 1) == "0 0 0":
            if not([b[0] + a1 - 1, b[1] + a2 - 1] in deadbound):
              deadbound.append([b[0] + a1 - 1, b[1] + a2 - 1])

    for c in deadbound:
      livedcoords.append(c)
    livedcopy = []
    for k in livedcoords:
      if k[0] == 0 or k[0] == width - 1 or k[1] == 0 or k[1] == width - 1:
        continue
      livedcopy.append(k)
    livedcoords = livedcopy
    change = []
    delchange = []
    foundlive = True
    livecoords = []
    for e in livedcoords:
      x = e[0]
      y = e[1]
      bordercount = 0
      for a1 in range(3):
        for a2 in range(3):
          if a2 - 1 == 0 and a1 - 1 == 0:
            continue
          if pixel.data.p(x + a2 - 1, y + a1 - 1) == "255 255 255":
            bordercount += 1
      if bordercount == 3 and pixel.data.p(x, y) == "0 0 0":
        change.append([x, y])
        livecoords.append([x, y])
      elif pixel.data.p(x, y) == "255 255 255":
        if bordercount == 3 or bordercount == 2:
          livecoords.append([x, y])
          continue
        delchange.append([x, y])
    for c in change:
      pixel.color(c[0], c[1], "255 255 255")
    for d in delchange:
      pixel.color(d[0], d[1], "0 0 0")
    timedif = time.time() - time1

Main()