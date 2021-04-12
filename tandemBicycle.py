class Solutions:
    def tandemBicycle(self,redShirtSpeeds, blueShirtSpeeds, fastest):
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort()
        sum = 0
        if fastest == True:
            for idx in range(len(redShirtSpeeds)):
                sum += max(redShirtSpeeds[idx],blueShirtSpeeds[len(blueShirtSpeeds)-idx-1])
        else:
            for idx in range(len(redShirtSpeeds)):
                sum += max(redShirtSpeeds[idx],blueShirtSpeeds[idx])
        return sum	


obj = Solutions()
print(obj.tandemBicycle([1,2,3,4],[6,7,8,9],True))
    

