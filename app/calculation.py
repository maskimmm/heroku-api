import math as m
import numpy as np

class Calculation:

    # Local Variable
    __koefisienPantul: float = 0.1
    __suhuRata: float = [0, 26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.4,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.2,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.3,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.9,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6,26.6]
    
    #Average Inverter
    __avgIKurs:float = 16293.95
    __avgIPrice:float = 4423.78
    __avgIWeight:float = 0.004747294

    # Average PVM
    __avgPKurs:float = 14284.75
    __avgPPmaxCoeff:float = - 0.0035
    __avgPNOCT:float = 44
    __avgPPrice:float = 3696933.54
    __avgPWp:float = 0.004990696
    __avgPWeight:float = 0.055452816

    # Analisa Ekonomi
    __iAnalisaEkonomi = 0.025
    __dAnalisaEkonomi = 0.0257

    sVI:float = [0,0.451931998,0.683839601,0.656114289,0.452626311,0.556667475,0.657673254,0.68727535,0.540055753,0.548872982,0.408427153,0.601077634,0.58335881,0.68848222,0.671448197,0.623520957,0.521743216,0.792532039,0.580854769,0.694935314,0.500707986,0.593565664,0.605164869,0.531464803,0.691154728,0.677624992,0.822852858,0.542082081,0.474843355,0.550640199,0.433283369,0.620239537,0.486343475,0.575141511,0.620664547,0.854197247,0.786981669,0.635425956,0.758630968,0.620980614,0.50967409,0.483705536,0.441677107,0.486273,0.607524403,0.419228018,0.483825967,0.618758904,0.410474593,0.483444944,0.611709302,0.501107319,0.58021967,0.570417432,0.529871789,0.50934125,0.607552062,0.606791295,0.605257726,0.588143048,0.718842748,0.473100344,0.626263691,0.500931576,0.475921291,0.528092657,0.650256362,0.51420729,0.607966208,0.60763398,0.654596333,0.659379972,0.6036236,0.428699459,0.648194603,0.746389575,0.853214716,0.793318976,0.645004695,0.780971914,0.770226778,0.814612071,0.738354315,0.626937557,0.65528271,0.853962682,0.92781983,0.539784592,0.596172934,0.574953246,0.839183581,0.747313038,0.653576857,0.605840647,0.5489601,0.658912553,0.732023764,0.443316803,0.851884618,0.567202394,0.94524545,0.922372481,0.764022045,0.934406979,0.748519522,0.896808985,0.70251286,0.816396721,0.547552121,0.607888163,0.523193904,0.954416908,0.958689702,0.92142164,0.962693648,0.919687812,0.806316549,0.799626411,1.004089444,0.560094555,0.721652544,0.837178572,0.843846081,0.962871812,0.705530675,0.990523318,0.760358634,0.987142661,1.029023111,1.006532779,0.697816624,0.817879742,0.615963292,0.978089437,1.045012398,0.912189506,0.946582901,1.033399476,0.992211997,0.505480328,0.814589202,0.858755713,0.420128137,0.697265587,0.620342583,1.011086226,0.912107394,0.793921527,0.850891368,0.272559289,0.846055881,0.865326303,0.511444308,0.444518017,0.530935202,0.966136264,1.105332497,1.091689844,0.933670933,0.78836743,1.039908185,0.962212004,1.096495722,1.032386691,1.08035508,1.060416626,0.694056714,0.805899984,1.036123594,1.061128118,1.087655593,1.063167661,0.751972955,0.900266228,1.087941464,1.069776721,1.051394643,0.951403734,1.082082155,1.053883678,1.007981759,1.075156052,1.089169637,1.086991506,1.093922841,1.112367506,1.092613748,0.819823438,0.420908896,1.07892011,1.020664823,0.944033358,1.078778661,1.026949419,0.990540574,1.012807744,0.858450479,0.537006705,0.986697241,1.133098439,1.066473157,0.944850881,1.087964972,0.987412405,1.10248588,1.070727453,1.059851248,1.033296814,1.034637079,1.076425995,1.101986853,0.890357989,1.109737597,1.034070778,1.040939975,1.028941825,0.924977392,0.723857757,0.921861153,0.918256185,0.786277336,0.97483613,0.993344499,0.873070516,0.709256715,1.076749153,0.91258639,0.818866984,0.982266886,1.029394197,1.03931457,1.033450281,1.048162321,0.928661964,1.052801266,1.047116134,1.006069792,1.037798102,1.059822456,1.039363618,1.036288329,0.794005727,0.975858963,0.99270919,0.993578955,0.959789972,0.764473718,0.945207066,0.985304658,0.960444069,0.973300847,0.959278683,0.962649213,0.887368659,0.948456178,0.94096881,0.950556007,0.900389519,0.94272431,0.875418727,0.952060146,0.974269568,0.912057317,0.938135518,0.884851406,0.957460173,0.863096499,0.966157802,0.938698216,0.940645085,0.815403987,0.913294293,0.964803612,0.939871141,0.842479009,0.939011365,0.888778166,0.925577171,0.883289195,0.847428741,0.877292498,0.814405207,0.814262902,0.603077584,0.519342753,0.92718965,0.887063904,0.927706927,0.916166704,0.902202763,0.894973562,0.712886988,0.494313182,0.253591921,0.622362461,0.642753479,0.874642366,0.78507264,0.859461095,0.921256583,0.739616232,0.691748192,0.861955343,0.737537187,0.512423058,0.480998697,0.669875813,0.61905461,0.694120834,0.591555504,0.752652072,0.848616909,0.823101322,0.832212013,0.846652802,0.865130577,0.666715341,0.58316875,0.734048125,0.843785283,0.763656112,0.854273194,0.854277805,0.867423127,0.835878207,0.657007498,0.832344157,0.676391203,0.69123772,0.609623214,0.712801391,0.330855139,0.396511133,0.440944268,0.551596411,0.290868826,0.718271967,0.54389309,0.439601347,0.657708588,0.445216321,0.507384618,0.469830333,0.571393664,0.160891832,0.507303481,0.492403433,0.330448443,0.597214759,0.551416177,0.509411234,0.400814458,0.451118287,0.473717445,0.467599096,0.718462257,0.55940738,0.670707464,0.812250267,0.660230935,0.495415212,0.50828046,0.471595459,0.595785606,0.533905297,0.311171199,0.590162398]
    def __init__(self, inputGMT: str, inputLat: str, inputLong: str, inputColTilt: str, inputAzimuthCol: str, inputRoofLength: str, inputRoofWidth: str, inputPLN: str):
        
        #input data
        self.inputGMT = float(inputGMT)
        self.ltm = float(inputGMT) * 15
        self.inputLat = float(inputLat)
        self.inputLong = float(inputLong)
        self.inputColTilt = float(inputColTilt)
        self.inputAzimuthCol = float(inputAzimuthCol)
        self.inputRoofLength = float(inputRoofLength)
        self.inputRoofWidth = float(inputRoofWidth)
        self.inputPLN = float(inputPLN)
        self.RoofArea = float(inputRoofWidth) * float(inputRoofLength)

    # B (Koefisien) // Col E
    def koefisien(self, day:float):
        __day = day
        vkoefisien = 360/365 * (__day - 81)
        # print("Koefisien: " + str(vkoefisien))
        return vkoefisien

    # E (Equation Of Time in Minute) // Col F
    def eOTMinute(self, day:float):
        __vkoefisien = self.koefisien(day= day)
        eOTMinute = (9.87 * m.sin(2 * __vkoefisien * m.pi/180)) - (7.53 * m.cos(__vkoefisien * m.pi/180)) - (1.5 * m.sin(__vkoefisien * m.pi/180))
        # print("Equation Of Time in Minute: " + str(eOTMinute))
        return eOTMinute

    # E (Equation Of Time in Hours) // Col G
    def eOTHours(self, day:float):
        __vEOTMinute = self.eOTMinute(day= day)
        eOTHour = __vEOTMinute/60
        # print("Equation of Time in Hours: " + str(eOTHour))
        return eOTHour

    # Time Correction (Minute) // Col H
    def timeCorrection(self, day:float):
        __vEOTMinute = self.eOTMinute(day= day)
        __vErr = self.ltm - self.inputLong
        timeCorrection = 4 * __vErr + __vEOTMinute
        # print("Time Correction: " + str(timeCorrection))
        return timeCorrection

    # Solar Time // Col I
    def solarTime(self, day:float, clockTime:float):
        __clockTime = clockTime
        __vTimeCorrection = self.timeCorrection(day= day)
        solarTime = __clockTime + (__vTimeCorrection/60)
        # print("Solar Time: " + str(solarTime))
        return solarTime

    # Hour Angle (H) // Col J
    def hourAngle(self, day:float, clockTime:float):
        __solarTime = self.solarTime(clockTime= clockTime, day= day)
        hourAngle = 15 * (12 - __solarTime)
        # print("Hour Angle: " + str(hourAngle))
        return hourAngle

    # Declination (Delta) // Col K
    def declination(self, day:float):
        __day = day
        declination = 23.45 * m.sin(360/365 * (__day - 81) * m.pi/180)
        # print("Declination: " + str(declination))
        return declination

    # Angle at Solar Noon (Beta N) // Col L
    def angleAtSolarNoon(self, day:float):
        __vLat = self.inputLat
        __vDeclination = self.declination(day= day)
        angleAtSolarNoon = 90 - __vLat + __vDeclination
        # print("Angle at Solar Noon: " + str(angleAtSolarNoon))
        return angleAtSolarNoon

    # Sin Beta // Col N
    def sinBeta(self, day:float, clockTime:float):
        __vLat = self.inputLat
        __declination = self.declination(day= day)
        __hourAngle = self.hourAngle(clockTime= clockTime, day= day)
        sinBeta = m.cos(__vLat * m.pi/180) * m.cos(__declination * m.pi/180) * m.cos(__hourAngle * m.pi/180) + m.sin(__vLat * m.pi/180) * m.sin(__declination * m.pi/180)
        # print("Sin Beta: " + str(sinBeta))
        return sinBeta

    # Altitude (Beta) // Col O
    def altitude(self, day:float, clockTime:float):
        __sinBeta = self.sinBeta(clockTime= clockTime, day= day)
        altitude = m.degrees(m.asin(__sinBeta))
        # print("Altitude: " + str(altitude))
        return altitude
    
    # Cos H // Col P
    def cosH(self, day:float, clockTime:float):
        __hourAngle = self.hourAngle(clockTime= clockTime, day= day)
        cosH = m.cos(__hourAngle * m.pi/180)
        # print("Cos H: " + str(cosH))
        return cosH
    
    # Tan D (Delta) // Col Q
    def tanD(self, day:float):
        __declination = self.declination(day= day)
        tanD = m.tan(__declination * m.pi/180)
        # print("Tan Delta: " + str(tanD))
        return tanD

    # Tan L (L) //Col R
    def tanL(self):
        __vLat = self.inputLat
        tanL = m.tan(__vLat * m.pi/180)
        # print("Tan L: " + str(tanL))
        return tanL

    # Tan D/L // Col S
    def tanDPL(self,day:float):
        __tanD = self.tanD(day= day)
        __tanL = self.tanL()
        if(__tanL == 0):
            tanDPL = np.Infinity
        else:
            tanDPL = __tanD/__tanL
        # print("Tan D / Tan L: " + str(tanDPL))
        return tanDPL

    # Sin Phi // Col T
    def sinPhi(self, day:float, clockTime:float):
        __declination = self.declination(day= day)
        __hourAngle = self.hourAngle(clockTime= clockTime, day= day)
        __altitude = self.altitude(clockTime= clockTime, day= day)
        sinPhi = m.cos(__declination * m.pi/180) * m.sin(__hourAngle * m.pi/180) / m.cos(__altitude * m.pi/180)
        # print("Sin Phi: " + str(sinPhi))
        return sinPhi

    # Arcsin Phi 1 // Col U
    def asinPhi1(self, day:float, clockTime:float):
        __sinPhi = self.sinPhi(clockTime= clockTime, day= day)
        asinPhi1 = m.degrees(m.asin(__sinPhi))
        # print("Arcsin Phi 1: " + str(asinPhi1))
        return asinPhi1

    # Arcsin Phi 2 // Col V
    def asinPhi2(self, day:float, clockTime:float):
        __asinPhi1 = self.asinPhi1(clockTime= clockTime, day= day)
        asinPhi2 = 180 - __asinPhi1
        # print("Arcsin Phi 2: "  + str(asinPhi2))
        return asinPhi2

    # Arcsin Phi 2 Correction // Col W
    def asinPhi2Correction(self, day:float, clockTime:float):
        __asinPhi2 = self.asinPhi2(clockTime= clockTime, day= day)
        if(__asinPhi2 > 180):
            asinPhi2Correction = -360 + __asinPhi2
        else:
            asinPhi2Correction = __asinPhi2
        # print("Arcsin Phi 2 Correction: " + str(asinPhi2Correction))
        return asinPhi2Correction
    
    # Condition X // Col X
    def conditionX(self, day:float, clockTime:float):
        __vLat = self.inputLat
        __cosH = self.cosH(clockTime= clockTime, day= day)
        __tanD = self.tanD(day= day)
        __tanL = self.tanL()
        if(__vLat > 0):
            if(__cosH >= __tanD/__tanL):
                conditionX = False
            else:
                conditionX = True
        else:
            if(__cosH >= __tanD/__tanL):
                conditionX = True
            else:
                conditionX = False
        # print("Condition X: " + str(conditionX))
        return conditionX
    
    # Azimuth NESW (N=0, E=90, S=180, W= -90) // Col Y
    def azimuthNESW(self, day:float, clockTime:float):
        __conditionX = self.conditionX(clockTime= clockTime, day= day)
        __asinPhi1 = self.asinPhi1(clockTime= clockTime, day= day)
        __asinphi2Correction = self.asinPhi2Correction(clockTime= clockTime, day= day)
        if(__conditionX == True):
            if(np.abs(__asinPhi1)< np.abs(__asinphi2Correction)):
                azimuthNESW = __asinPhi1
            else:
                azimuthNESW = __asinphi2Correction
        else:
            if(np.abs(__asinPhi1)<np.abs(__asinphi2Correction)):
                azimuthNESW = __asinphi2Correction
            else:
                azimuthNESW = __asinPhi1
        # print("Azimuth NESW: " + str(azimuthNESW))
        return azimuthNESW
    
    # Azimuth SENW (S=0, E=90, N=180, W= -90) // Col Z
    def azimuthSENW(self, day:float, clockTime:float):
        __azimuthNESW = self.azimuthNESW(clockTime= clockTime, day= day)
        if(__azimuthNESW > 0):
            azimuthSENW = 180 - __azimuthNESW
        else:
            azimuthSENW = - 180 - __azimuthNESW
        # print("Azimuth SENW: " + str(azimuthSENW))
        return azimuthSENW

    # Sunrise Hour Angle // Col AA
    def sunriseHourAngle(self, day:float):
        __vLat = self.inputLat
        __tanD = self.tanD(day= day)
        sunriseHourAngle = m.degrees(m.acos( - m.tan(__vLat * m.pi/180) * __tanD))
        # print("Sunrise HOur Angle: " + str(sunriseHourAngle))
        return sunriseHourAngle

    # Q // Col AB
    def qColAB(self, day:float):
        __vLat = self.inputLat
        __declination = self.declination(day= day)
        __sunrieHourAngle = self.sunriseHourAngle(day = day)
        qColAB = 3.467 / (m.cos(__vLat * m.pi/180) * m.cos(__declination * m.pi/180) * m.sin(__sunrieHourAngle * m.pi/180))
        # print("Q: " + str(qColAB))
        return qColAB

    # Cos Tetha // Col AC
    def cosT(self, day:float, clockTime:float):
        __altitude = self.altitude(clockTime= clockTime, day= day)
        __azimuthSENW = self.azimuthSENW(clockTime= clockTime, day= day)
        __azimuthCol = self.inputAzimuthCol
        __colTilt = self.inputColTilt
        __sinBeta = self.sinBeta(clockTime= clockTime, day= day)
        cosT = m.cos(__altitude * m.pi/180) * m.cos((__azimuthSENW - __azimuthCol) * m.pi/180) * m.sin(__colTilt * m.pi/180) + __sinBeta * m.cos(__colTilt * m.pi/180)
        # print("Cos Tetha: " + str(cosT))
        return cosT

    # Incidence Angle Between Sun & Collector Face (Tetha) // Col AD
    def incidenceAngle(self, day:float, clockTime:float):
        __cosT = self.cosT(clockTime= clockTime, day= day)
        incidenceAngle = m.degrees(m.acos(__cosT))
        # print("Incidence Angle Between Sun and Collector Face: " + str(incidenceAngle))
        return incidenceAngle

    # Io // Col AE
    def ioColAE(self, day:float):
        __day = day
        ioColAE = 1.377 * (1 + 0.034 * m.cos(360  * __day/365 * m.pi/180))
        # print("Io: " + str(ioColAE))
        return ioColAE

    # Air Mass Ratio // Col AF
    def airMassRatio(self, day:float, clockTime:float):
        __sinBeta = self.sinBeta(clockTime= clockTime, day= day)
        airMassRatio = 1/__sinBeta
        # print("Air Mass Ratio: " + str(airMassRatio))
        return airMassRatio

    # A // Col AG
    def aColAG(self, day:float):
        __day = day
        aColAG = 1160 + 75 * m.sin(360/365 * (__day - 275) * m.pi/180)
        # print("A: " + str(aColAG))
        return aColAG

    # K // Col AH
    def kColAH(self, day:float):
        __day = day
        kColAH = 0.174 + 0.035 * m.sin(360/365 * (__day - 100) * m.pi/180)
        # print("K: " + str(kColAH))
        return kColAH

    # Direct Irradiance (Ib) (kW/m^2) // Col AI
    def iB(self, day:float, clockTime:float):
        __altitude = self.altitude(clockTime= clockTime, day= day)
        __aColAG = self.aColAG(day= day)
        __kColAH = self.kColAH(day= day)
        __airMAssRatio = self.airMassRatio(clockTime= clockTime, day= day)
        if(__altitude < 0):
            iB:float = 0.0
        else:
            iB = __aColAG * m.exp(-__kColAH * __airMAssRatio)/1000
        # print("Direct Irradiance: " + str(iB))
        return iB

    # IB Horizontal (Ibh) // Col AJ
    def iBH(self, day:float, clockTime:float):
        __iB = self.iB(clockTime= clockTime, day= day)
        __SinBeta = self.sinBeta(clockTime= clockTime, day= day)
        iBH = __iB * __SinBeta
        # print("Ibh: " + str(iBH))
        return iBH

    # IBC // Col AK
    def iBC(self, day:float, clockTime:float):
        __cosT = self.cosT(clockTime= clockTime, day= day)
        __iB = self.iB(clockTime= clockTime, day= day)
        if(__cosT < 0):
            iBC:float = 0.0
        else:
            iBC = __iB * __cosT
        # print("Ibc: " + str(iBC))
        return iBC

    # C // Col AL
    def cColAL(self, day:float):
        __day = day
        cColAL = 0.095 + 0.04 * m.sin(360/365 * (__day - 100) * m.pi/180)
        # print("C: " + str(cColAL))
        return cColAL

    # Diffuse on Horizontal (Idh) // Col AM
    def iDH(self, day:float, clockTime:float):
        __cColAL = self.cColAL(day= day)
        __iB = self.iB(clockTime= clockTime, day= day)
        iDH = __cColAL * __iB
        # print("Diffuse on Horizontal: " + str(iDH))
        return iDH

    # Total Horizontal (Ih) // Col AN
    def iH(self, day:float, clockTime:float):
        __iDH = self.iDH(clockTime= clockTime, day= day)
        __iBH = self.iBH(clockTime= clockTime, day= day)
        iH = __iDH + __iBH
        # print("Total Horizontal (Ih): " + str(iH))
        return iH

    # Idc // COl AO
    def iDC(self, day:float, clockTime:float):
        __iDH = self.iDH(clockTime= clockTime, day= day)
        _colTilt = self.inputColTilt
        iDC = __iDH * (1 + m.cos(_colTilt * m.pi/180))/2
        # print("Idc: " + str(iDC))
        return iDC

    # Irc // Col AP
    def iRC(self, day:float, clockTime:float):
        __koefisienPantul = self.__koefisienPantul
        __iB = self.iB(clockTime= clockTime, day= day)
        __sinBeta = self.sinBeta(clockTime= clockTime, day= day)
        __cColAL = self.cColAL(day= day)
        __ColTilt = self.inputColTilt
        iRC = __koefisienPantul * __iB * (__sinBeta + __cColAL) * (1 - m.cos(__ColTilt * m.pi/180))/2
        # print("Irc: " + str(iRC))
        return iRC

    # Ic (kW/m^2) // Col AQ
    def iC(self, day:float, clockTime:float):
        __iRC = self.iRC(clockTime= clockTime, day= day)
        __iDC = self.iDC(clockTime= clockTime, day= day)
        __iBC = self.iBC(clockTime= clockTime, day= day)
        iC = __iRC + __iDC + __iBC
        # print("Ic: " + str(iC))
        return iC

    # Expected Energy (kWh/m^2/day) // Col AR
    def expectedEnergyPerDay(self, day:float=1, clockTime:float = 24):
        expectedEnergyPerDay = 0.0
        # __iC = self.iC(clockTime= iterate, day= day)
        for iterate in range(clockTime):
            expectedEnergyPerDay = expectedEnergyPerDay + self.iC(clockTime=iterate, day=day)
        # print("Expected Energy: " + str(expectedEnergy))
        return expectedEnergyPerDay

    # Expected Energy After Seasonal Variation Index // AT
    def expectedEnergyPerDaySVI(self, day:float=1, clockTime:float = 24):
        __expectedEnergyPerDay = self.expectedEnergyPerDay(clockTime= clockTime, day= day)
        __sVI:float = self.sVI[day]
        expectedEnergyPerDaySVI = __expectedEnergyPerDay * __sVI
        return expectedEnergyPerDaySVI

    def getExpectedEnergySVIYearly(self, day:float=367, clockTime:float = 24):
        # __expectedEnergyDailySVI = self.expectedEnergyDailySVI(clockTime=clockTime, day=day)
        getExpectedEnergySVIYearly:float = 0
        for iterate in range(1, day):
            getExpectedEnergySVIYearly += self.expectedEnergyPerDaySVI(clockTime=clockTime, day=iterate)
        return getExpectedEnergySVIYearly

    def getExpectedEnergyDaily(self, day:float = 367, clockTime:float = 24):
        __getExpectedEnergySVIYearly = self.getExpectedEnergySVIYearly(clockTime=clockTime, day=day)
        getExpectedEnergyDaily = __getExpectedEnergySVIYearly/366
        return getExpectedEnergyDaily

    # Tcell // Col AV
    def tCell(self, day:float):
        __suhurata:float = self.__suhuRata[day]
        __avgPNOCT = self.__avgPNOCT
        tCell = __suhurata + ((__avgPNOCT-20)/0.8)
        return tCell

    # pDc // Col AW
    def pDc (self, day:float):
        __tCell = self.tCell(day=day)
        __avgPPmaxCoeff = self.__avgPPmaxCoeff
        pDc = 1 + (__tCell-25) * (__avgPPmaxCoeff) * 1
        return pDc

    # pAc // Col AX
    def pAc(self, day:float):
        __pDc = self.pDc(day=day)
        pAc = __pDc * 0.965 * 0.99 * 0.997 * 0.991 * 0.995 * 0.97 * 0.959
        return pAc

    # PV Output/Generated Energy (kWh/kWp) // Col AY
    def pvOutput(self, day:float = 1):
        __expectedEnergyPerDaySVI = self.expectedEnergyPerDaySVI(day=day)
        __pAc = self.pAc(day=day)
        pvOutput = __pAc * __expectedEnergyPerDaySVI * 1
        return pvOutput


    def pvOutputYearly(self,day:float = 367):
        pvOutputYearly = 0.0
        for iterate in range(1, day):
            pvOutputYearly = pvOutputYearly + self.pvOutput(day=iterate)
        return pvOutputYearly

    def pvOutputDaily(self, day:float=367):
        __pvOutputYearly = self.pvOutputYearly(day=day)
        pvOutputDaily = __pvOutputYearly/366
        return pvOutputDaily


    # SIZING TAB

    # SIZING
    # Golongan PLN
    def golPLN (self):
        __pln = self.inputPLN
        # print(str(__pln))
        if(__pln > 0 and __pln <= 900):
            print("Golongan R-1 (900 VA)")
            golPLN = 1352.0
        elif(__pln > 900 and __pln <= 1300):
            print("Golongan R-1 (1300 VA)")
            golPLN = 1444.7
        elif(__pln > 1300 and __pln <= 2200):
            print("Golongan R-1 (2200 VA)")
            golPLN = 1444.7
        elif(__pln > 2200 and __pln <= 5500):
            print("Golongan R-2 (2200-5500 VA)")
            golPLN = 1444.7
        elif(__pln > 5500):
            print("Golongan R-3 (>5500 VA)")
            golPLN = 1444.7
        else:
            print("Golongan Tidak sesuai")
            golPLN = 0
        return golPLN

    # Kapasitas Terpasang (Temp) // B16
    def kTB16(self):
        __roofArea =self.RoofArea
        __avgPWp = self.__avgPWp
        kapasitas = __roofArea / __avgPWp
        return kapasitas

    # Kapasitas terpasang (Temp) // D16
    def kTD16(self):
        __kTB16 = self.kTB16()
        kTD16 = __kTB16 * (0.965 * 0.99 * 0.997 * 0.991 * 0.995 * 0.97 * 0.959)
        return kTD16

    # Kapasitas Terpasang (Temp) // F16
    def kTF16(self):
        __kTD16 = self.kTD16()
        kTF16 = __kTD16 / 0.85
        return kTF16

    # Inverter // B17
    def inverterB17(self):
        __PLN = self.inputPLN
        __kTF16 = self.kTF16()
        if (__kTF16 > __PLN):
            inverter = __PLN
        else:
            inverter = __kTF16
        return inverter

    # Inverter // D17
    def inverterD17(self):
        __inverterB17 = self.inverterB17()
        inverter = __inverterB17 * 0.85
        return inverter

    # Inverter // F17
    def inverterF17(self):
        __inverterD17 = self.inverterD17()
        inverter = __inverterD17 / (0.965 * 0.99 * 0.997 * 0.991 * 0.995 * 0.97 * 0.959)
        return inverter

    # Kapasitas Terpasang // B18
    def kapasitasTerpasangB18(self):
        return self.inverterF17()

    # Kapasitas Terpasang // D18
    def kapasitasTerpasangD18(self):
        kapasitas = self.kapasitasTerpasangB18() * (0.965 * 0.99 * 0.997 * 0.991 * 0.995 * 0.97 * 0.959)
        return kapasitas

    # Berat PV // B19
    def beratPV(self):
        __kTB18 = self.kapasitasTerpasangB18()
        __avgPWeight = self.__avgPWeight
        beratPV = __kTB18 * __avgPWeight
        return beratPV
    
    # Berat Inverter // B20
    def beratInverter(self):
        __inverterb17 = self.inverterB17()
        __avgIWeight = self.__avgIWeight
        beratInverter = __inverterb17 * __avgIWeight
        return beratInverter

    # HARGA INVESTASI
    # PV // B23
    def pvB23(self):
        __kTB18 = self.kapasitasTerpasangB18()
        __avgPPrice = self.__avgPPrice
        pvB23 = __kTB18 * __avgPPrice / 1000
        return pvB23
    
    # Inverter // B24
    def inverterB24(self):
        __inverterB17 = self.inverterB17()
        __avgIPrice = self.__avgIPrice
        inverterB24 = __inverterB17 * __avgIPrice
        return inverterB24

    # Shipping PV & inverter // B25
    def shippingPVInverterB25(self):
        __beratPV = self.beratPV()
        __beratInverter = self.beratInverter()
        __kurs = self.__avgPKurs
        shipping = (__beratPV + __beratInverter) * 1.05 * __kurs
        return shipping

    # Pajak // B26
    def pajakB26(self):
        __b23 = self.pvB23()
        __b24 = self.inverterB24()
        __b25 = self.shippingPVInverterB25()
        B26 = (__b23 + __b24 + __b25) * 0.175
        return B26
    
    # Mounting // B27
    def MountingB27(self):
        __roofLength = self.inputRoofLength
        __roofWidth = self.inputRoofWidth
        b27 = (__roofLength + __roofWidth) * 2 * 88000
        return b27

    # Total // B28
    def totalB28(self):
        __b23 = self.pvB23()
        __b24 = self.inverterB24()
        __b25 = self.shippingPVInverterB25()
        __b26 = self.pajakB26()
        __b27 = self.MountingB27()
        b28 = __b23 + __b24 + __b25 + __b26 + __b27
        return b28
    
    # Energi Terbangkitkan // B30
    def energiTerbangkitkanB30(self):
        __b18 = self.kapasitasTerpasangB18()
        __pvOutputYearly = self.pvOutputYearly()
        b30 = __b18 / 1000 * __pvOutputYearly
        return b30
    
    # Pendapatan Energi // B31
    def pendapatanEnergiB31(self):
        __biayaPLN = self.golPLN()
        __b30 = self.energiTerbangkitkanB30()
        b31 = __b30 * __biayaPLN * 0.65
        return b31

    # ANALISA EKONOMI TAB

    # OM Cost/Tahun // B5
    def oMCostB5(self):
        __d18 = self.kapasitasTerpasangD18()
        __avgPKurs = self.__avgPKurs
        b5 = (__d18 * 25 * __avgPKurs / 1000) * -1
        return b5
    
    # Simple Payback Period
    def simplePayback(self):
        __b3 = self.totalB28()
        __b4 = self.pendapatanEnergiB31()
        __b5 = self.oMCostB5()
        b6 = __b3 / (__b4 + __b5)
        return b6
    
    # Return of Investment (ROI)
    def rOI(self, year:float = 26):
        __d18 = self.kapasitasTerpasangD18()
        __avgPkurs = self.__avgPKurs
        __iAE = self.__iAnalisaEkonomi
        __dAE = self.__dAnalisaEkonomi
        __b28 = self.totalB28()
        __colF1 = self.pendapatanEnergiB31()
        newdict = {}
        for iterate in range(1, year):
            if(iterate == 1 ):
                __year = iterate
                __colF = __colF1
                __colG = (__d18 * 25 * __avgPkurs * (((1 + __iAE) / (1 + __dAE)) ** (__year + 1)) / 1000) * -1
                __colH = __colF + __colG
                __roi = (__colH - __b28) / __b28 
                newdict.update({__year:{'Tahun': __year, 'YearlyIncome': __colF, 'OMCost': __colG, 'IncomeYearN': __colH, 'ROI': __roi}})
            else:
                __year = iterate
                __colF = __colF1 * ((1 + __iAE)/(1+__dAE)) ** __year
                __colG = (__d18 * 25 * __avgPkurs * (((1 + __iAE) / (1 + __dAE)) ** (__year + 1)) / 1000) * -1
                for iterate in range(1, __year + 1):
                    if(iterate == 1):
                        ___year = iterate
                        ___colF = __colF1
                        ___colG = ((__d18 * 25 * __avgPkurs * (((1 + __iAE) / (1 + __dAE)) ** (___year + 1)) / 1000) * -1)
                        __colH = ___colF + ___colG
                    else:
                        ___year = iterate
                        ___colF += __colF
                        ___colG += ((__d18 * 25 * __avgPkurs * (((1 + __iAE) / (1 + __dAE)) ** (___year + 1)) / 1000) * -1)
                        __colH = ___colF + ___colG
                __roi = (__colH - __b28) / __b28
                newdict.update({__year:{'Tahun': __year, 'YearlyIncome': __colF, 'OMCost': __colG, 'IncomeYearN': __colH, 'ROI': __roi}})
        return newdict

    # net Present Value
    def netPresentValue(self, year:float = 26):
        __d18 = self.kapasitasTerpasangD18()
        __avgPkurs = self.__avgPKurs
        __iAE = self.__iAnalisaEkonomi
        __dAE = self.__dAnalisaEkonomi
        __b28 = self.totalB28()
        __colM1 = self.pendapatanEnergiB31()
        __colL = - __b28
        newdict = {}
        for iterate in range(1, year):
            if(iterate == 1 ):
                __year = iterate
                __colL = __colL
                __colM = __colM1
                __colN = (__d18 * 25 * __avgPkurs * (((1 + __iAE) / (1 + __dAE)) ** (__year + 1)) / 1000) * -1
                __colO = (__colM + __colN) * ((1 + __iAE) ** __year) / ((1 + __dAE) ** __year)
                __colP = __colL + __colO
                newdict.update({__year:{'Tahun': __year, 'CapitalCost':__colL, 'YearlyIncome': __colM, 'OMCost': __colN,
                'Rt': __colO, 'NPV': __colP}})
            else:
                __year = iterate
                __colL = __colL
                __colM = __colM1 * ((1 + __iAE)/(1+__dAE)) ** __year
                __colN = (__d18 * 25 * __avgPkurs * (((1 + __iAE) / (1 + __dAE)) ** (__year + 1)) / 1000) * -1
                __colO = (__colM + __colN) * ((1 + __iAE) ** __year) / ((1 + __dAE) ** __year)
                for iterate in range(1, __year + 1):
                    if(iterate == 1):
                        ___year = iterate
                        ___colM = __colM1
                        ___colN = ((__d18 * 25 * __avgPkurs * (((1 + __iAE) / (1 + __dAE)) ** (___year + 1)) / 1000) * -1)
                        ___colO = (___colM + ___colN) * ((1 + __iAE) ** ___year) / ((1 + __dAE) ** ___year)
                        __colP = __colL + ___colO
                    else:
                        ___year = iterate
                        ___colM = __colM
                        ___colN = ((__d18 * 25 * __avgPkurs * (((1 + __iAE) / (1 + __dAE)) ** (___year + 1)) / 1000) * -1)
                        ___colO += (___colM + ___colN) * ((1 + __iAE) ** ___year) / ((1 + __dAE) ** ___year)
                        __colP = __colL + ___colO
                newdict.update({__year:{'Tahun': __year, 'CapitalCost':__colL, 'YearlyIncome': __colM, 'OMCost': __colN,
                'Rt': __colO, 'NPV': __colP}})
        return newdict


