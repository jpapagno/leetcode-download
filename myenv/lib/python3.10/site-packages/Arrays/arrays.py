import sys, os

class Arrays:
    #This will not work with tuples... I think
    #sometimes we dont get... arrays...
    def __init__(self, _array):
        self._array = _array
    
    def save_array(self, _path, _mode="w"):
        #save the array that was passed through
        _file = open(_path, _mode)
        for line in self._array:
            _file.write(str(line) + "\n")
        _file.flush()
        _file.close()
    
    def convert_stored_to_array(self, _path, _objects_type="int"):
        _file = open(_path, "r")
        _data = []
        #Get the stored data that is an integer
        for line in _file.readlines():
            if(_objects_type.lower() == "int"):
                #pass the data inside as integer
                _data.append(int(line.replace('\n', '')))
            elif(_objects_type.lower() == "str"):
                #pass the data inside as string
                _data.append(str(line.replace('\n', '')))
            elif(_objects_type.lower() == "float" or _objects_type.lower() == "double"):
                #pass the data inside as float
                _data.append(float(line.replace('\n', '')))
            elif(_objects_type.lower() == "tuple"):
                #pass the data inside as tuple
                _data.append(tuple(line.replace('\n', '')))
        #close the file being read
        _file.close()
        return _data
