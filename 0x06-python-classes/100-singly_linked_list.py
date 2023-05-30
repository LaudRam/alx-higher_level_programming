#!/usr/bin/python3

''' Singly linked list module '''


class Node():
    ''' Defines a node of a singly linked list'''

    def __init__(self, data, next_node=None):
        '''
            Initialises new node

            Args:
                data (int): data for the node
                next_node (Node): next node in list
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        ''' Retrieves data attribute '''
        return self.__data

    @data.setter
    def data(self, value):
        ''' Sets data attribute

            Raise:
                TypeError: if data is not an integer
        '''
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        ''' Retrieves next_node attribute
            Return: next node
        '''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        ''' Sets next_node attribute

            Raise:
                TypeError: if next_node is not a node object
        '''
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList():
    ''' Defines a singly linked list '''

    def __init__(self):
        ''' Initialises the singly linked list '''
        self.__head = None

    def sorted_insert(self, value):
        '''
            Inserts a new node into sorted list

            Args - value (Node): new node to insert
        '''
        node = Node(value)
        temp = self.__head

        if self.__head is None:
            self.__head = node
            return

        if node.data < temp.data:
            node.next_node = temp
            self.__head = node
            return

        while temp.next_node is not None:
            if temp.next_node.data < node.data:
                temp = temp.next_node
            else:
                node.next_node = temp.next_node
                temp.next_node = node
                return
        temp.next_node = node

    def __str__(self):
        ''' Makes list printable '''
        temp = self.__head

        if temp is None:
            return ("")
        while temp.next_node is not None and temp:
            print(temp.data)
            temp = temp.next_node
        return (str(temp.data))
