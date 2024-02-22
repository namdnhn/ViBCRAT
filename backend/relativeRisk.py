from constant import *
from form import *
import numpy as np


class RelativeRisk:
    def __init__(self, rr_star1, rr_star2, patternNumber):
        self.rr_star1 = rr_star1
        self.rr_star2 = rr_star2
        self.patternNumber = patternNumber

    def getData(self):
        return f"rrstar1: {self.rr_star1}, rrstar2: {self.rr_star2}, patternNumber: {self.patternNumber}"


def relative_risk(data: CheckedData) -> RelativeRisk:
    lp1 = (
        data.nBiops * Wrk_Beta_all[data.race - 1][0]
        + data.ageMen * Wrk_Beta_all[data.race - 1][1]
        + data.age1st * Wrk_Beta_all[data.race - 1][2]
        + data.nRela * Wrk_Beta_all[data.race - 1][3]
        + data.age1st * data.nRela * Wrk_Beta_all[data.race - 1][5]
        + np.log(data.rHyp)
    )

    lp2 = lp1 + data.nBiops * Wrk_Beta_all[data.race - 1][4]

    rr_star1 = np.exp(lp1)
    rr_star2 = np.exp(lp2)

    patternNumber = (
        data.nBiops * 3 * 3 * 4
        + data.ageMen * 3 * 4
        + data.age1st * 3
        + data.nRela * 1
        + 1
    )
    return RelativeRisk(
        rr_star1=rr_star1, rr_star2=rr_star2, patternNumber=patternNumber
    )


def relative_risk_korea(data: KoreanData):
    lp1 = (
        -1.2700 + 0.1136 * data.nRela
        + 0.6224 * data.ageMen13 + 0.3624 * data.ageMen1316
        + 0.5539 * data.menopause + 0.0763 * data.age1stNull
        + 0.1451 * data.age1st2430 + 0.2264 * data.age1st31
        + (-0.0722) * data.neverBreastFeeding + 0.2198 * data.durationBreastFeeding06
        + 0.2121 * data.oralContraceptive + 0.2878 * data.exercise
    )

    lp2 = (
        -0.6729
        + 0.6960 * data.nRela + 0.8755 * data.ageMen13
        + 0.4244 * data.ageMen1316 + 0.9154 * data.menopause
        + 0.2954 * data.ageMenopause4549 + 0.3048 * data.ageMenopause5054
        + 0.4794 * data.ageMenopause55 + 0.6287 * data.pregnancy
        + 0.1474 * data.bmi2530 + 0.8239 * data.bmi30
        + 0.4175 * data.oralContraceptive + 0.6115 * data.exercise
    )

    rr_star1 = np.exp(lp1)
    rr_star2 = np.exp(lp2)
    
    return RelativeRisk(
        rr_star1=rr_star1, rr_star2=rr_star2, patternNumber=0
    )
    
def relative_risk_vietnam(data: VietnamData):
    lp1 = (
        0.18232 * data.breastDensity + 0.83291 * data.ageMen
        + 0.95551 * data.pregnancy + 0.83291 * data.hormoneTherapy
    )
    
    lp2 = (
        0.64185 * data.breastDensity + 0.53063 * data.ageMen
        + 0.83291 * data.pregnancy + 0.40547 * data.babyNumber
    )
    
    rr_star1 = np.exp(lp1)
    rr_star2 = np.exp(lp2)
    
    return RelativeRisk(
        rr_star1=rr_star1, rr_star2=rr_star2, patternNumber=0
    )