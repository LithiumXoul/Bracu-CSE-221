def dist(pair_1, pair_2):
  x1 = pair_1[1]
  x2 = pair_2[1]
  y1= pair_1[2]
  y2 = pair_2[2]

  return  round(  ((((x1-x2) ** 2) + ((y1-y2) ** 2)) ** 0.5)  ,  6  )

def findClosestPair(pairsX, pairsY):
  if len(pairsX) == 2:
    return [  pairsX[0][0]  ,  pairsX[1][0]  ,  dist(pairsX[0], pairsX[1]) ]
  if len(pairsX) == 3:
    
    dist_1 = dist(pairsX[0], pairsX[1])
    dist_2 = dist(pairsX[1], pairsX[2])
    dist_3 = dist(pairsX[0], pairsX[2])

    if dist_1 <= dist_2 and dist_1 <= dist_3:
      return [  pairsX[0][0]  ,  pairsX[1][0]  ,  dist_1 ]

    elif dist_2 <= dist_1 and dist_2 <= dist_3:
      return [  pairsX[1][0]  ,  pairsX[2][0]  ,  dist_2 ]

    else:
      return [  pairsX[0][0]  ,  pairsX[2][0]  ,  dist_3 ]

  mid = len(pairsX) // 2
  mid_p = pairsX[mid]
  pairsY_l = []
  pairsY_r = []
  for pair in pairsY:
    if pair[1] < mid_p[1]:
      pairsY_l.append(pair)
    else:
      pairsY_r.append(pair)


  dl = findClosestPair(pairsX[:mid], pairsY_l)
  dr = findClosestPair(pairsX[mid:], pairsY_r)
  d = None

  if dl[2] < dr[2]: d = dl
  else: d = dr
    
  band_ps = []
  for pair in pairsY:
    if mid_p[1] - d[2] < pair[1] < mid_p[1] + d[2]:
      band_ps.append(pair)

  for i in range(len(band_ps)):
    for j in range(i + 1, min(i + 7, len(band_ps))):
      cd = dist(band_ps[i], band_ps[j])

      if cd < d[2]:
        d = [band_ps[i][0], band_ps[j][0], cd]

  return d

pairs = []
n = int(input())
for i in range(n):
  x,y = list(map(int, input().split()))
  pairs.append((i + 1, x, y))

pairsX = sorted(pairs, key = lambda pair: pair[1])
pairsY = sorted(pairs, key = lambda pair: pair[2])

res = findClosestPair(pairsX, pairsY)
res_str = ''
for meow in res:
  res_str += f'{meow} '
print(res_str[:-1])