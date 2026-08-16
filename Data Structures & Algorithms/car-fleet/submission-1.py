class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        ata = []
        cars = sorted(zip(position, speed), reverse=True)
        for pos, spd in cars:
            at = (target - pos) / spd
            if not ata:
                ata.append(at)
                fleet += 1
            if ata[-1] < at:
                fleet += 1
                ata.append(at)
        return fleet

