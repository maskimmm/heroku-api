import math as m
import numpy as np
import json

# avgPVM:float = {
#     "Kurs" : 14284.75,
#     "PmaxCoeff" : -0.35,
#     "NOCT" : 44,
#     "Price" : 3696933.54,
#     "Wp" : 0.004990696,
#     "Weight" : 0.055452816
# }

# avgInverter:float = {
#     "Kurs" : 16293.95,
#     "Price" : 4423.78,
#     "Weight" : 0.004747294,
#     }

# print(type(avgInverter))
# print(avgInverter.keys()) # list key
# print(avgInverter["Price"]) # access key's value

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

    # sVI:float = [0, 0.431875863,0.653497657,0.627008728,0.432552214,0.531985251,0.628520241,0.656818742,0.516130328,0.524564597,0.390344796,0.574475265,0.557549993,0.658034062,0.641765028,0.595967765,0.498697268,0.757540308,0.555220492,0.664280617,0.478631463,0.56740776,0.578509138,0.50806733,0.660742918,0.647824455,0.786685244,0.518268693,0.453995539,0.526478472,0.414282308,0.593055926,0.465041059,0.549965033,0.593512149,0.816851847,0.752596744,0.607680625,0.725527453,0.593901315,0.487463242,0.462640395,0.422455195,0.465124578,0.581120655,0.401020354,0.462827225,0.591922519,0.392684195,0.462506631,0.585234445,0.479434677,0.555143283,0.545782261,0.507004067,0.487375333,0.581369534,0.580660398,0.579211692,0.562851816,0.687953577,0.452785635,0.599391732,0.47945302,0.455529926,0.505482386,0.622435867,0.492223467,0.581992772,0.581693539,0.626671242,0.631271127,0.577910156,0.410450655,0.620622174,0.714662932,0.81697317,0.759645575,0.617646099,0.747869533,0.737602833,0.793572741,0.707124128,0.600438399,0.627604631,0.817917509,0.888684006,0.517031754,0.571060237,0.550750679,0.803881886,0.715896904,0.62611939,0.580405286,0.525927758,0.631284828,0.701350162,0.424752512,0.816233604,0.543479999,0.905736371,0.883843012,0.732126537,0.895421822,0.717308454,0.859436632,0.673254328,0.78241463,0.524773483,0.582613677,0.501452848,0.914778303,0.918895152,0.883194456,0.922775217,0.881572422,0.772916795,0.766520483,0.962539042,0.536928524,0.691818702,0.802585174,0.80899343,0.923121376,0.676417228,0.949667851,0.729010246,0.946461678,0.986633932,0.965087052,0.669094355,0.784228882,0.590629831,0.937877501,1.002064852,0.874714105,0.907708113,0.990973716,0.951490681,0.48474163,0.781178952,0.823544695,0.402906968,0.66869264,0.594928851,0.969675845,0.874760427,0.76142182,0.816067847,0.261407091,0.811445716,0.829935213,0.49053084,0.426344663,0.509232714,0.926651186,1.060165782,1.047087246,0.89552973,0.75616614,0.997437621,0.922918875,1.051723361,0.990235769,1.036249126,1.017127614,0.665725123,0.773004488,0.993832341,1.017817444,1.043262944,1.019774788,0.721281302,0.863521517,1.043535668,1.026110868,1.008477219,0.912565789,1.037906851,1.010856358,0.966825017,1.031252373,1.04468906,1.042594787,1.049237445,1.066922543,1.047969349,0.786320119,0.403704989,1.034813464,0.978931985,0.90542633,1.034652123,0.984933949,0.950005659,0.971351974,0.823304285,0.515015354,0.946279752,1.086671476,1.022763866,0.906115107,1.043348736,0.946907324,1.057246077,1.026776618,1.016332402,0.990853869,0.992124243,1.032180256,1.056673888,0.853733376,1.064071438,0.991501756,0.998071137,0.986549934,0.886853053,0.694010329,0.88383303,0.880360296,0.753813788,0.934569351,0.95229449,0.836974125,0.67991929,1.032189677,0.874802261,0.78494654,0.941557621,0.986710321,0.996197397,0.990554287,1.004632962,0.890074997,1.009032804,1.003560508,0.964198669,0.994582653,1.015665263,0.996034434,0.993062759,0.760867192,0.93510699,0.95122927,0.952038157,0.919637941,0.732473351,0.905617329,0.944010216,0.920166741,0.932459014,0.919000074,0.922203619,0.850062319,0.908556163,0.901358336,0.91051608,0.862438064,0.902962443,0.83847136,0.911851526,0.933095623,0.873486804,0.898435553,0.847381086,0.9168877,0.826497858,0.925161038,0.898839398,0.900676198,0.780732871,0.874434073,0.923723303,0.89982469,0.806557354,0.8989459,0.85082961,0.886029814,0.845522322,0.811169823,0.839729539,0.779510482,0.779349852,0.577201402,0.49704378,0.887351151,0.848922854,0.887790509,0.876719349,0.863329619,0.856385115,0.682128237,0.472970431,0.242635139,0.595453964,0.614944313,0.836774535,0.751059637,0.822200027,0.881289518,0.707507793,0.661697788,0.824486101,0.705455283,0.490118735,0.460048579,0.640680246,0.592056747,0.663830018,0.565724317,0.719765887,0.811514805,0.787092831,0.795783004,0.809569591,0.827215759,0.637479225,0.557581605,0.701822842,0.806721911,0.730094132,0.816708563,0.81669322,0.82924053,0.799065591,0.628058173,0.795651383,0.646559367,0.660737102,0.582711801,0.681321604,0.316237282,0.378985331,0.421446856,0.527197003,0.277997795,0.686477099,0.519809179,0.420129318,0.628566705,0.42548391,0.48489074,0.448996034,0.546049568,0.153753914,0.484792513,0.470549551,0.315779972,0.570700619,0.526932048,0.4867896,0.383013587,0.431081744,0.452675868,0.446828398,0.686547475,0.534557827,0.64091421,0.776170726,0.630905442,0.47341185,0.485707663,0.450654054,0.569332753,0.510203289,0.297359382,0.563971783]
    sVI:float = [0,0.451931998,0.683839601,0.656114289,0.452626311,0.556667475,0.657673254,0.68727535,0.540055753,0.548872982,0.408427153,0.601077634,0.58335881,0.68848222,0.671448197,0.623520957,0.521743216,0.792532039,0.580854769,0.694935314,0.500707986,0.593565664,0.605164869,0.531464803,0.691154728,0.677624992,0.822852858,0.542082081,0.474843355,0.550640199,0.433283369,0.620239537,0.486343475,0.575141511,0.620664547,0.854197247,0.786981669,0.635425956,0.758630968,0.620980614,0.50967409,0.483705536,0.441677107,0.486273,0.607524403,0.419228018,0.483825967,0.618758904,0.410474593,0.483444944,0.611709302,0.501107319,0.58021967,0.570417432,0.529871789,0.50934125,0.607552062,0.606791295,0.605257726,0.588143048,0.718842748,0.473100344,0.626263691,0.500931576,0.475921291,0.528092657,0.650256362,0.51420729,0.607966208,0.60763398,0.654596333,0.659379972,0.6036236,0.428699459,0.648194603,0.746389575,0.853214716,0.793318976,0.645004695,0.780971914,0.770226778,0.814612071,0.738354315,0.626937557,0.65528271,0.853962682,0.92781983,0.539784592,0.596172934,0.574953246,0.839183581,0.747313038,0.653576857,0.605840647,0.5489601,0.658912553,0.732023764,0.443316803,0.851884618,0.567202394,0.94524545,0.922372481,0.764022045,0.934406979,0.748519522,0.896808985,0.70251286,0.816396721,0.547552121,0.607888163,0.523193904,0.954416908,0.958689702,0.92142164,0.962693648,0.919687812,0.806316549,0.799626411,1.004089444,0.560094555,0.721652544,0.837178572,0.843846081,0.962871812,0.705530675,0.990523318,0.760358634,0.987142661,1.029023111,1.006532779,0.697816624,0.817879742,0.615963292,0.978089437,1.045012398,0.912189506,0.946582901,1.033399476,0.992211997,0.505480328,0.814589202,0.858755713,0.420128137,0.697265587,0.620342583,1.011086226,0.912107394,0.793921527,0.850891368,0.272559289,0.846055881,0.865326303,0.511444308,0.444518017,0.530935202,0.966136264,1.105332497,1.091689844,0.933670933,0.78836743,1.039908185,0.962212004,1.096495722,1.032386691,1.08035508,1.060416626,0.694056714,0.805899984,1.036123594,1.061128118,1.087655593,1.063167661,0.751972955,0.900266228,1.087941464,1.069776721,1.051394643,0.951403734,1.082082155,1.053883678,1.007981759,1.075156052,1.089169637,1.086991506,1.093922841,1.112367506,1.092613748,0.819823438,0.420908896,1.07892011,1.020664823,0.944033358,1.078778661,1.026949419,0.990540574,1.012807744,0.858450479,0.537006705,0.986697241,1.133098439,1.066473157,0.944850881,1.087964972,0.987412405,1.10248588,1.070727453,1.059851248,1.033296814,1.034637079,1.076425995,1.101986853,0.890357989,1.109737597,1.034070778,1.040939975,1.028941825,0.924977392,0.723857757,0.921861153,0.918256185,0.786277336,0.97483613,0.993344499,0.873070516,0.709256715,1.076749153,0.91258639,0.818866984,0.982266886,1.029394197,1.03931457,1.033450281,1.048162321,0.928661964,1.052801266,1.047116134,1.006069792,1.037798102,1.059822456,1.039363618,1.036288329,0.794005727,0.975858963,0.99270919,0.993578955,0.959789972,0.764473718,0.945207066,0.985304658,0.960444069,0.973300847,0.959278683,0.962649213,0.887368659,0.948456178,0.94096881,0.950556007,0.900389519,0.94272431,0.875418727,0.952060146,0.974269568,0.912057317,0.938135518,0.884851406,0.957460173,0.863096499,0.966157802,0.938698216,0.940645085,0.815403987,0.913294293,0.964803612,0.939871141,0.842479009,0.939011365,0.888778166,0.925577171,0.883289195,0.847428741,0.877292498,0.814405207,0.814262902,0.603077584,0.519342753,0.92718965,0.887063904,0.927706927,0.916166704,0.902202763,0.894973562,0.712886988,0.494313182,0.253591921,0.622362461,0.642753479,0.874642366,0.78507264,0.859461095,0.921256583,0.739616232,0.691748192,0.861955343,0.737537187,0.512423058,0.480998697,0.669875813,0.61905461,0.694120834,0.591555504,0.752652072,0.848616909,0.823101322,0.832212013,0.846652802,0.865130577,0.666715341,0.58316875,0.734048125,0.843785283,0.763656112,0.854273194,0.854277805,0.867423127,0.835878207,0.657007498,0.832344157,0.676391203,0.69123772,0.609623214,0.712801391,0.330855139,0.396511133,0.440944268,0.551596411,0.290868826,0.718271967,0.54389309,0.439601347,0.657708588,0.445216321,0.507384618,0.469830333,0.571393664,0.160891832,0.507303481,0.492403433,0.330448443,0.597214759,0.551416177,0.509411234,0.400814458,0.451118287,0.473717445,0.467599096,0.718462257,0.55940738,0.670707464,0.812250267,0.660230935,0.495415212,0.50828046,0.471595459,0.595785606,0.533905297,0.311171199,0.590162398]
    def __init__(self, inputGMT: float, inputLat: float, inputLong: float, inputColTilt: float, inputAzimuthCol: float):
        
        #input data
        self.inputGMT = inputGMT
        self.ltm = inputGMT * 15
        self.inputLat = inputLat
        self.inputLong = inputLong
        self.inputColTilt = inputColTilt
        self.inputAzimuthCol = inputAzimuthCol

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

    # def pvOutputPerDay(self,day:float = 1, clockTime:float = 24):
    #     pvOutputPerDay = 0.0
    #     for iterate in range(clockTime):
    #         pvOutputPerDay = pvOutputPerDay + self.pvOutput(day=day, clockTime=iterate)
    #     return pvOutputPerDay

    def pvOutputYearly(self,day:float = 367):
        pvOutputYearly = 0.0
        for iterate in range(1, day):
            pvOutputYearly = pvOutputYearly + self.pvOutput(day=iterate)
        return pvOutputYearly

    def pvOutputDaily(self, day:float=367):
        __pvOutputYearly = self.pvOutputYearly(day=day)
        pvOutputDaily = __pvOutputYearly/366
        return pvOutputDaily


# nc = Calculation(inputGMT = 7, inputLat = -7.285499, inputLong = 112.79608, inputColTilt = 15, inputAzimuthCol = 180)

# print("Expected Energy Per Day: " + str(nc.expectedEnergyPerDay(day= 1)))
# print("Expected Energy Per Day After SVI: " + str(nc.expectedEnergyPerDaySVI(day= 1)))
# print("Expected Energy Daily: " + str(nc.getExpectedEnergyDaily()))
# print("Expected Energy Yearly After SVI: " + str(nc.getExpectedEnergySVIYearly(day= 367)))

# print("Expected PV Output: " + str(nc.pvOutput()))
# print("Expected PV Output Daily: " + str(nc.pvOutputDaily()))
# print("Expected PV Output Yearly After SVI: " + str(nc.pvOutputYearly()))

