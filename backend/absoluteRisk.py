from constant import *
from form import *
from relativeRisk import *
import numpy as np
import math


def absoluteRisk(data: CheckedData):
    rrstar = relative_risk(data)
    One_AR_RR = np.full(70, np.nan)
    riskWork = 0
    cum_lambda = 0
    lambda1_temp = np.zeros((14, 5))
    lambda2_temp = np.zeros((14, 5))
    oneAR1 = Wrk_1_AR_all[data.race - 1][0]
    oneAR2 = Wrk_1_AR_all[data.race - 1][1]

    oneAR_RR1 = oneAR1 * rrstar.rr_star1
    oneAR_RR2 = oneAR2 * rrstar.rr_star2
    One_AR_RR[:30] = oneAR_RR1
    One_AR_RR[30:] = oneAR_RR2

    for i in range(14):
        lambda1_temp[i, :5] = Wrk_lambda1_all[data.race - 1, i]
        lambda2_temp[i, :5] = Wrk_lambda2_all[data.race - 1, i]

    lambda1 = np.ravel(lambda1_temp)
    lambda2 = np.ravel(lambda2_temp)

    for j in range(data.t1, data.t2):
        # h1*(t) * F(t) * r(t) + h2(t)
        lambdaj = lambda1[j] * One_AR_RR[j] + lambda2[j]

        PI_j = (
            (One_AR_RR[j] * lambda1[j] / lambdaj)
            * np.exp(-cum_lambda)
            * (1 - np.exp(-lambdaj))
        )
        riskWork += PI_j
        cum_lambda += lambdaj
        print(
            f"In the age {j + 20}, lambdaj = {lambdaj}, PI_j = {PI_j}, riskWork = {riskWork}, cumlambda = {cum_lambda}."
        )
    return riskWork


def absoluteRiskExact(data: CheckedData2):
    rrstar = relative_risk(data)
    print(rrstar.getData())
    One_AR_RR = np.full(70, np.nan)
    riskWork = 0
    cum_lambda = 0
    lambda1_temp = np.zeros((14, 5))
    lambda2_temp = np.zeros((14, 5))
    oneAR1 = Wrk_1_AR_all[data.race - 1][0]
    oneAR2 = Wrk_1_AR_all[data.race - 1][1]

    start_intervel = math.floor(data.t1) + 1
    end_intervel = math.ceil(data.t2) + 0
    num_intervel = math.ceil(data.t2) - math.floor(data.t1)

    oneAR_RR1 = oneAR1 * rrstar.rr_star1
    oneAR_RR2 = oneAR2 * rrstar.rr_star2
    One_AR_RR[:30] = oneAR_RR1
    One_AR_RR[30:] = oneAR_RR2

    for i in range(14):
        lambda1_temp[i, :5] = Wrk_lambda1_all[data.race - 1, i]
        lambda2_temp[i, :5] = Wrk_lambda2_all[data.race - 1, i]

    lambda1 = np.ravel(lambda1_temp)
    lambda2 = np.ravel(lambda2_temp)

    for j in range(1, num_intervel + 1):
        j_intervel = start_intervel + j - 1
        integral_length = 0
        if num_intervel > 1 and j > 1 and j < num_intervel:
            integral_length = 1
        if num_intervel > 1 and j == 1:
            integral_length = 1 - (data.t1 - math.floor(data.t1))
        if num_intervel > 1 and j == num_intervel:
            z1 = 1 if data.t2 > math.floor(data.t2) else 0
            z2 = 1 if data.t2 == math.floor(data.t2) else 0
            integral_length = (data.t2 - math.floor(data.t2)) * z1 + z2
        if num_intervel == 1:
            integral_length = data.t2 - data.t1

        lambdaj = lambda1[j_intervel] * One_AR_RR[j_intervel] + lambda2[j_intervel]
        PI_j = (
            (One_AR_RR[j_intervel] * lambda1[j_intervel] / lambdaj)
            * np.exp(-cum_lambda)
            * (1 - np.exp(-lambdaj * integral_length))
        )
        riskWork += PI_j
        cum_lambda += lambdaj * integral_length
        print(
            f"In the age {j_intervel + 20}, lambdaj = {lambdaj}, PI_j = {PI_j}, riskWork = {riskWork}, cumlambda = {cum_lambda}."
        )
    return riskWork * 100


def absoluteRiskWithoutT2(data: CheckedData):
    rrstar = relative_risk(data)
    One_AR_RR = np.full(70, np.nan)
    riskWork = 0
    cum_lambda = 0
    lambda1_temp = np.zeros((14, 5))
    lambda2_temp = np.zeros((14, 5))
    oneAR1 = Wrk_1_AR_all[data.race - 1][0]
    oneAR2 = Wrk_1_AR_all[data.race - 1][1]

    oneAR_RR1 = oneAR1 * rrstar.rr_star1
    oneAR_RR2 = oneAR2 * rrstar.rr_star2
    One_AR_RR[:30] = oneAR_RR1
    One_AR_RR[30:] = oneAR_RR2

    for i in range(14):
        lambda1_temp[i, :5] = Wrk_lambda1_all[data.race - 1, i]
        lambda2_temp[i, :5] = Wrk_lambda2_all[data.race - 1, i]

    lambda1 = np.ravel(lambda1_temp)
    lambda2 = np.ravel(lambda2_temp)

    results = {}

    for j in range(data.t1, 70):
        T = j + 21
        lambdaj = lambda1[j] * One_AR_RR[j] + lambda2[j]
        PI_j = (
            (One_AR_RR[j] * lambda1[j] / lambdaj)
            * np.exp(-cum_lambda)
            * (1 - np.exp(-lambdaj))
        )
        riskWork += PI_j
        cum_lambda += lambdaj
        results[T] = riskWork

    return results


def absoluteRiskAvg(data: CheckedData):
    One_AR_RR = np.ones(70)
    riskWork = 0
    cum_lambda = 0
    lambda1_temp = np.zeros((14, 5))
    lambda2_temp = np.zeros((14, 5))
    for i in range(14):
        lambda1_temp[i, :5] = Wrk_lambda1_all[data.race - 1, i]
        lambda2_temp[i, :5] = Wrk_lambda2_all[data.race - 1, i]

    if data.race == 1 or data.race == 4:
        lambda1_temp = Avg_lambda1
        lambda2_temp = Avg_lambda2

    lambda1 = np.ravel(lambda1_temp)
    lambda2 = np.ravel(lambda2_temp)

    for j in range(data.t1, data.t2):
        lambdaj = lambda1[j] * One_AR_RR[j] + lambda2[j]
        PI_j = (
            (One_AR_RR[j] * lambda1[j] / lambdaj)
            * np.exp(-cum_lambda)
            * (1 - np.exp(-lambdaj))
        )
        riskWork += PI_j
        cum_lambda += lambdaj
    return riskWork


def absoluteRiskAvgWithoutT2(data: CheckedData):
    One_AR_RR = np.ones(70)
    riskWork = 0
    cum_lambda = 0
    lambda1_temp = np.zeros((14, 5))
    lambda2_temp = np.zeros((14, 5))
    for i in range(14):
        lambda1_temp[i, :5] = Wrk_lambda1_all[data.race - 1, i]
        lambda2_temp[i, :5] = Wrk_lambda2_all[data.race - 1, i]

    if data.race == 1 or data.race == 4:
        lambda1_temp = Avg_lambda1
        lambda2_temp = Avg_lambda2

    lambda1 = np.ravel(lambda1_temp)
    lambda2 = np.ravel(lambda2_temp)

    results = {}

    for j in range(data.t1, 70):
        T = j + 21
        lambdaj = lambda1[j] * One_AR_RR[j] + lambda2[j]
        PI_j = (
            (One_AR_RR[j] * lambda1[j] / lambdaj)
            * np.exp(-cum_lambda)
            * (1 - np.exp(-lambdaj))
        )
        riskWork += PI_j
        cum_lambda += lambdaj
        results[T] = riskWork
    return results


def absoluteRiskVietnam(data: VietnamData):
    rrstar = relative_risk(data)
    One_AR_RR = np.zeros((14, 5))
    riskWork = 0
    cum_lambda = 0
    lambda1_temp = np.zeros((14, 5))
    lambda2_temp = np.zeros((14, 5))

    vietnam_lambda1 = [
        0.15,
        7.00,
        22.1,
        39.9,
        62.4,
        85.5,
        106.4,
        120.4,
        129.9,
        134.3,
        135.7,
        135.7,
        133.7,
        130.2,
    ]

    vietnam_lambda2 = [
        5.38,
        8.44,
        10.9,
        20.5,
        40.1,
        31.1,
        112.1,
        169.7,
        234.5,
        291.6,
        348.8,
        396.5,
        437.2,
        465.6,
    ]

    AR = [
        0.2649375,
        0.264935443,
        0.253614338,
        0.25962513,
        0.279475838,
        0.313479636,
        0.261615447,
        0.29965019,
        0.31028855,
        0.309270672,
        0.320638651,
        0.320638725,
        0.320638483,
        0.32063861,
    ]
    
    RR = [
        rrstar.rr_star1,
        rrstar.rr_star1,
        rrstar.rr_star1,
        rrstar.rr_star1,
        rrstar.rr_star1,
        rrstar.rr_star1,
        rrstar.rr_star2,
        rrstar.rr_star2,
        rrstar.rr_star2,
        rrstar.rr_star2,
        rrstar.rr_star2,
        rrstar.rr_star2,
        rrstar.rr_star2,
        rrstar.rr_star2,
    ]

    for i in range(14):
        vietnam_lambda1[i] = vietnam_lambda1[i] / 100000
        vietnam_lambda2[i] = vietnam_lambda2[i] / 100000
        One_AR_RR[i, :5] = AR[i] * RR[i]
        lambda1_temp[i, :5] = vietnam_lambda1[i]
        lambda2_temp[i, :5] = vietnam_lambda2[i]

    one_arrr = np.ravel(One_AR_RR)
    lambda1 = np.ravel(lambda1_temp)
    lambda2 = np.ravel(lambda2_temp)

    for j in range(data.t1, data.t2):
        lambdaj = lambda1[j] * one_arrr[j] + lambda2[j]

        PI_j = (
            (one_arrr[j] * lambda1[j] / lambdaj)
            * np.exp(-cum_lambda)
            * (1 - np.exp(-lambdaj))
        )
        riskWork += PI_j
        cum_lambda += lambdaj
        print(
            f"In the age {j + 20}, lambdaj = {lambdaj}, PI_j = {PI_j}, riskWork = {riskWork}, cumlambda = {cum_lambda}."
        )
    return riskWork
        
    
