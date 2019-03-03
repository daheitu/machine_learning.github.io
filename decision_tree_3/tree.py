from math import log

def calaShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts:
            labelCounts[currentLabel] = 1
        else:
            labelCounts[currentLabel] += 1
    shannonEnt = 0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


def createDataSet():
    dataSet = [[1, 1, "yes"],
            [1, 1, 'yes'],
            [1, 0, 'no'],
            [0, 1, 'no'],
            [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels

myData, labels = createDataSet()
print(calaShannonEnt(myData))


def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet


print(splitDataSet(myData, 0, 0))


def chooseBestFeatureToSplit(dataSet):
    numberFeatures = len(dataSet[0]) -1 
    baseEntropy = calaShannonEnt(dataSet)
    bestInfoGain = 0; bestFeature = -1
    for i in range(numberFeatures):
        print('current' +str(i))
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            print( subDataSet)
            prob = len(subDataSet)/float(len(dataSet))
            print(calaShannonEnt(subDataSet))
            newEntropy += prob * calaShannonEnt(subDataSet)
            infoGain = baseEntropy - newEntropy
            if infoGain > bestInfoGain:
                bestInfoGain = infoGain
                bestFeature = i
        print(infoGain)
    return bestFeature


print(chooseBestFeatureToSplit(myData))