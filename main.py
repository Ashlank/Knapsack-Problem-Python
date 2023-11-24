# Knapsack Problem - Dynamic Algorithm

def printTable(table):
    for i in range(len(table)):
        print(table[i])

def printElementsAndMaxBenefit(arr, maxValue):
    print('\nEl maximo beneficio es',maxValue)
    print('Los elementos que generan este beneficio son:',arr)

def printElementsNotTakenAndBenefit(arr, value):
    print('\nLos elementos que no fueron tomados son:',arr)
    print('El beneficio que generan es',value)

def knapsackSolver(arr, maxCapability):
    n = len(arr)
    W = maxCapability

    # Creo la tabla y la inicializo a 0
    m = []
    for i in range(n+1):
        row = []
        for j in range(W+1):
            row.append(0)
        m.append(row)

    # Lleno la tabla con los beneficios correspondientes
    for i in range(1,n+1):
        for j in range(1,W+1):
            if arr[i-1][0] <= j:
                if arr[i-1][1] + m[i-1][j-arr[i-1][0]] > m[i-1][j]:
                    m[i][j] = arr[i-1][1] + m[i-1][j-arr[i-1][0]]
                else:
                    m[i][j] = m[i-1][j]
            else:
                m[i][j] = m[i-1][j]

    maxBenefit = m[n][W]
    printTable(m)

    # Obtengo los elementos que generan el beneficio máximo
    elementsIndex = []
    i = n
    j = W
    while i > 0 and j > 0:
        if m[i][j] != m[i-1][j]:
            elementsIndex.append(i-1)
            j -= arr[i-1][0]
        i -= 1

    maxBenefitElements = []
    for index in elementsIndex:
        maxBenefitElements.append(elements[index])

    # Obtengo los objetos que no entran en la solución óptima y su beneficio total
    elementsNotTaken = []
    notTakenValue = 0
    for i in range(len(elements)):
        if i not in elementsIndex:
            elementsNotTaken.append(elements[i])
            notTakenValue += elements[i][1]

    printElementsAndMaxBenefit(maxBenefitElements, maxBenefit)
    printElementsNotTakenAndBenefit(elementsNotTaken, notTakenValue)

elements = [(4, 5), (2, 3), (5, 6), (3, 4)]
maxCapability = 8

knapsackSolver(elements, maxCapability)




# Knapsack Problem - Heuristic Algorithm

def knapsackSolverHeuristic(arr, maxCapability):
    ratios = []

    # Creo los ratios beneficio/peso
    for element in arr:
        ratios.append(element[1]/element[0])

    # Ordeno en forma decreciente los elementos, según la lista de ratios
    newLength = len(arr)-1
    for i in range(newLength):
        for j in range(newLength):
            if ratios[j] < ratios[j+1]:
                ratios[j], ratios[j+1] = ratios[j+1], ratios[j]
                arr[j], arr[j+1] = arr[j+1], arr[j]
        newLength -= 1

    # Tomo elementos hasta que se supere la capacidad máxima
    maxBenefit = 0
    elementsTaken = []
    currentWeight = 0

    for elem in arr:
        if currentWeight + elem[0] <= maxCapability:
            currentWeight += elem[0]
            maxBenefit += elem[1]
            elementsTaken.append(elem)

    print('\nUno de los maximos beneficios es', maxBenefit)
    print('Los elementos que lo generan son', elementsTaken)


knapsackSolverHeuristic(elements, maxCapability)