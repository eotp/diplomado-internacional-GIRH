def final_plot(ds, min_max=["1997-10", "2018-3"]):
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec
    from matplotlib import rcParams
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['Arial']
    
    date = pd.to_datetime(ds.time.values).strftime("%Y-%m")
    
    plt.figure(figsize=(13, 7))
    G = gridspec.GridSpec(3, 4)
    ax0 = plt.subplot(G[0, :-2])
    ax1 = plt.subplot(G[1:3, :-2])
    ax2 = plt.subplot(G[:3, 2:],projection=ccrs.Orthographic(-70,-15))
    
    annotation(ax=ax0, date=date)
    plot_oni(oni, min_max=min_max, vline=date, ax=ax1)
    plot_map(ds, ax=ax2, title="Anomalía mensual ({})".format(date))    
    plt.tight_layout()