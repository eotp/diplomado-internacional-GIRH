def annotation(ax=None, date="2014-4"):
    import matplotlib.pyplot as plt
    if ax is None:
        fig, ax = plt.subplots()
    
    ax.axis("off")
    ax.annotate(xy=(0.01,0.95) ,s="Anomalía mensual de la precipitación en Perú\npara el período 1998 a 2017", size=18)
    ax.annotate(xy=(0.01,0.65) ,s=date, size=18)
    ax.annotate(xy=(0.01,0.15) ,s="Recursos:\n - Tropical Rainfall Measuring Mission (TRMM, TMPA/3B43)\n    Rainfall Estimate L3 1 month 0.25 degree x 0.25 degree V7", size=10)
    ax.annotate(xy=(0.01,0.05) ,s=" - Ocean Nino Index (ONI), NOAA", size=10)

annotation()