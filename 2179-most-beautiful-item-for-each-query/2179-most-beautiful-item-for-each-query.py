class Solution(object):
    def maximumBeauty(self, items, queries):
        items.sort()
        result = [0]*len(queries)
        sorted_queries = sorted(enumerate(queries), key=lambda x:x[1])
        max_beauty = 0
        item_index = 0

        for idx, max_price in sorted_queries:
            while item_index < len(items) and items[item_index][0] <= max_price:
                max_beauty = max(max_beauty, items[item_index][1])
                item_index += 1
            result[idx] = max_beauty
        return result


            
        """
        :type items: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        