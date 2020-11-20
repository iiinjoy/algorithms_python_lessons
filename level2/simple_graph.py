#!/usr/bin/env python3


class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        vert = Vertex(v)
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                self.vertex[i] = vert
                break

    # здесь и далее, параметры v -- индекс вершины
    # в списке  vertex
    def RemoveVertex(self, v):
        if v >= self.max_vertex:
            return
        for v2 in range(self.max_vertex):
            if self.IsEdge(v, v2):
                self.RemoveEdge(v, v2)
        self.vertex[v] = None

    def IsEdge(self, v1, v2):
        # True если есть ребро между вершинами v1 и v2
        if v1 < self.max_vertex and v2 < self.max_vertex:
            return self.m_adjacency[v1][v2] == 1
        return False

    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        if v1 < self.max_vertex and v2 < self.max_vertex:
            self.m_adjacency[v1][v2] = 1
            self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        if v1 < self.max_vertex and v2 < self.max_vertex:
            self.m_adjacency[v1][v2] = 0
            self.m_adjacency[v2][v1] = 0

    def toValueList(self, vertex_list):
            L = []
            for v in vertex_list:
                L.append(v.Value)
            return L

    def DepthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        if self.vertex[VFrom] is None or self.vertex[VTo] is None:
            return []
        # 0. помечаем все узлы как непосещенные, очищаем стек
        for v in self.vertex:
            if v is not None:
                v.Hit = False
        path = []
        # 1. Выбираем текущую вершину X. Для начала работы это будет
        # исходная вершина
        x = VFrom
        while True:
            if not self.vertex[x].Hit:
                # 2. Фиксируем вершину X как посещённую
                self.vertex[x].Hit = True
                # 3. Помещаем вершину X в стек.
                path.append(x)
            # 4. Ищем среди смежных вершин вершины X целевую вершину Б.
            if self.IsEdge(x, VTo):
                path.append(VTo)
                break
            # Если целевой вершины среди смежных нету, то выбираем среди
            # смежных такую вершину, которая ещё не была посещена.
            # Если такая вершина найдена, делаем её текущей X и переходим к п.2.
            adj_fount = False
            for i in range(self.max_vertex):
                if self.IsEdge(x, i) and not self.vertex[i].Hit:
                    x = i
                    adj_fount = True
                    break
            if adj_fount:
                continue
            # 5. Если непосещённых смежных вершин более нету, удаляем из стека
            # верхний элемент
            path.pop()
            if len(path) == 0:
                # Если стек пуст, то прекращаем работу и информируем,
                # что путь не найден.
                return []
            else:
                # В противном случае делаем текущей вершиной X верхний элемент
                # стека, помечаем его как посещённый, и переходим к п.4
                x = path[-1]
                self.vertex[x].Hit = True
                continue

        vertex_path = []
        for i in path:
            vertex_path.append(self.vertex[i])
        return vertex_path

    def BreadthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        if self.vertex[VFrom] is None or self.vertex[VTo] is None:
            return []
        for v in self.vertex:
            if v is not None:
                v.Hit = False
        queue = []
        path = {}
        x = VFrom
        self.vertex[x].Hit = True
        path[x] = [x]
        while True:
            if self.IsEdge(x, VTo):
                p = path[x].copy()
                p.append(VTo)
                path[VTo] = p
                path.pop(x)
                break
            adj_found = False
            for i in range(self.max_vertex):
                if self.IsEdge(x, i) and not self.vertex[i].Hit:
                    adj_found = True
                    self.vertex[i].Hit = True
                    queue.append(i)
                    p = path[x].copy()
                    p.append(i)
                    path[i] = p
            if adj_found:
                path.pop(x)
            if len(queue) == 0:
                return []
            else:
                x = queue.pop(0)
        vertex_path = []
        for i in path[VTo]:
            vertex_path.append(self.vertex[i])
        return vertex_path

    def WeakVertices(self):
        # возвращает список узлов вне треугольников
        isWeak = [True] * self.max_vertex
        for v in range(self.max_vertex):
            if not isWeak[v]:
                continue
            adjs = []
            for i in range(self.max_vertex):
                if self.IsEdge(v, i):
                    adjs.append(i)
            for a in adjs:
                if isWeak[v]:
                    for b in adjs:
                        if self.IsEdge(a, b):
                            isWeak[v] = False
                            isWeak[a] = False
                            isWeak[b] = False
                            break
                else:
                    break
        weakvs = []
        for i in range(self.max_vertex):
            if isWeak[i]:
                weakvs.append(self.vertex[i])
        return weakvs
