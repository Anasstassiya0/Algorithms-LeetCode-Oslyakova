class Solution:
    def twoSum(self, arr, target):
        map = {} #создаем хэш-таблицу

        for i in range(len(arr)): #получаем индекс и тек.значение 
            x = arr[i]
            need = target - x

            if need in map:
                return [map[need], i]

            map[x] = i #добавляем 