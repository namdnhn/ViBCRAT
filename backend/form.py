from pydantic import BaseModel


class Form(BaseModel):
    t1: int
    t2: int
    nBiops: int
    hypPlas: int
    ageMen: int
    age1st: int
    nRela: int
    race: int
    
class Form2(BaseModel):
    t1: float
    t2: float
    nBiops: int
    hypPlas: int
    ageMen: int
    age1st: int
    nRela: int
    race: int
    
class KoreanForm(BaseModel):
    t1: float
    nRela: int
    ageMen: int
    menopause: int
    ageMenopause: int
    pregnancy: int
    age1st: int
    durationBreastFeeding: int
    bmi: float
    oralContraceptive: int
    exercise: int
    
class VietnamForm(BaseModel):
    t1: float
    breastDensity: float
    ageMen: int
    pregnancyNumber: int
    babyNumber: int
    hormoneTherapy: int
    

class CheckedData:
    def __init__(self, form: Form):
        self.t1 = form.t1 - 20
        self.t2 = form.t2 - 20
        self.race = form.race

        if form.nBiops == 99 or form.nBiops == 0:
            self.nBiops = 0
        elif form.nBiops == 1:
            self.nBiops = 1
        else:
            self.nBiops = 2

        if form.ageMen >= 14 or form.ageMen == 99:
            self.ageMen = 0
        elif form.ageMen >= 12:
            self.ageMen = 1
        elif form.race == 2:
            self.ageMen = 1
        else:
            self.ageMen = 2

        if form.age1st < 20 or form.age1st == 99 or form.race == 2:
            self.age1st = 0
        elif form.age1st < 25:
            self.age1st = 1
        elif form.age1st < 30:
            self.age1st = 2
        else:
            self.age1st = 3

        if form.nRela == 0 or form.nRela == 99:
            self.nRela = 0
        elif form.nRela == 1:
            self.nRela = 1
        else:
            if form.race >= 5 and form.race <= 10:
                self.nRela = 1
            else:
                self.nRela = 2

        if self.nBiops == 0:
            self.rHyp = 1.00
        else:
            if form.hypPlas == 0:
                self.rHyp = 0.93
            elif form.hypPlas == 1:
                self.rHyp = 1.82
            elif form.hypPlas == 99:
                self.rHyp = 1.00
            else:
                self.rHyp = 0

class CheckedData2:
    def __init__(self, form: Form2):
        self.t1 = form.t1 - 20
        self.t2 = form.t2 - 20
        self.race = form.race

        if form.nBiops == 99 or form.nBiops == 0:
            self.nBiops = 0
        elif form.nBiops == 1:
            self.nBiops = 1
        else:
            self.nBiops = 2

        if form.ageMen >= 14 or form.ageMen == 99:
            self.ageMen = 0
        elif form.ageMen >= 12:
            self.ageMen = 1
        elif form.race == 2:
            self.ageMen = 1
        else:
            self.ageMen = 2

        if form.age1st < 20 or form.age1st == 99 or form.race == 2:
            self.age1st = 0
        elif form.age1st < 25:
            self.age1st = 1
        elif form.age1st < 30:
            self.age1st = 2
        else:
            self.age1st = 3

        if form.nRela == 0 or form.nRela == 99:
            self.nRela = 0
        elif form.nRela == 1:
            self.nRela = 1
        else:
            if form.race >= 5 and form.race <= 10:
                self.nRela = 1
            else:
                self.nRela = 2

        if self.nBiops == 0:
            self.rHyp = 1.00
        else:
            if form.hypPlas == 0:
                self.rHyp = 0.93
            elif form.hypPlas == 1:
                self.rHyp = 1.82
            elif form.hypPlas == 99:
                self.rHyp = 1.00
            else:
                self.rHyp = 0
                
class KoreanData:
    def __init__(self, form: KoreanForm):
        self.t1 = form.t1 - 20
        self.nRela = form.nRela
        self.ageMen13 = 0
        self.ageMen1316 = 0
        if form.ageMen < 13:
            self.ageMen13 = 1
        elif form.ageMen < 17:
            self.ageMen1316 = 1
            
        self.menopause = form.menopause
        
        self.ageMenopause4549 = 0
        self.ageMenopause5054 = 0
        self.ageMenopause55 = 0
        if form.ageMenopause > 45 and form.ageMenopause < 50:
            self.ageMenopause4549 = 1
        elif form.ageMenopause > 50 and form.ageMenopause < 55:
            self.ageMenopause5054 = 1
        elif form.ageMenopause > 55:
            self.ageMenopause55 = 1
            
        self.pregnancy = form.pregnancy
        
        self.age1stNull = 0
        self.age1st2430 = 0
        self.age1st31 = 0
        if form.age1st == 0:
            self.age1stNull = 1
        elif form.age1st > 23 and form.age1st < 31:
            self.age1st2430 = 1
        elif form.age1st > 30:
            self.age1st31 = 1
            
        self.neverBreastFeeding = 0
        self.durationBreastFeeding06 = 0
        if form.durationBreastFeeding == 0:
            self.neverBreastFeeding = 1
        elif form.durationBreastFeeding < 7:
            self.durationBreastFeeding06 = 1
        
        self.bmi2530 = 0
        self.bmi30 = 0
        if form.bmi > 25 and form.bmi < 30:
            self.bmi2530 = 1
        elif form.bmi > 30:
            self.bmi30 = 1
            
        self.oralContraceptive = form.oralContraceptive
        self.exercise = form.exercise
        
class VietnamData:
    def __init__(self, form: VietnamForm):
        self.t1 = form.t1 - 20
        self.breastDensity = 0
        self.ageMen = 0
        self.pregnancy = 0
        self.babyNumber = 0
        self.hormoneTherapy = form.hormoneTherapy
        if form.breastDensity > 75:
            self.breastDensity = 1
        if form.ageMen < 14:
            self.ageMen = 1
        if form.pregnancyNumber < 3:
            self.pregnancy = 1
        if form.babyNumber < 2:
            self.babyNumber = 1