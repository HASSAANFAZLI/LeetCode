class Solution:
    def countTime(self, time: str) -> int:
        
        hr, mn = time.split(':')
        hr_poss = 1
        mn_poss = 1
        
        if hr == '??':
            hr_poss *= 24
        elif hr[0] == '?':
            if int(hr[1]) > 3:  # ?4
                hr_poss *= 2  # 0, 1
            else:
                hr_poss *= 3  # 0, 1, 2
        elif hr[1] == '?':
            if int(hr[0]) > 1:  # 2?
                hr_poss *= 4  # 0, 1, 2, 3
            else:
                hr_poss *= 10

        if mn == '??':
            mn_poss *= 60
        elif mn[0] == '?':
            mn_poss *= 6
        elif mn[1] == '?':
            mn_poss *= 10

        return hr_poss * mn_poss
